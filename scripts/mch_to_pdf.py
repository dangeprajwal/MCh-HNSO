#!/usr/local/bin/python3
"""
MCh-HNSO Vault -> Printer-Ready PDF  (v3)
==========================================
- All 25 sections, 264 answer files
- Times New Roman 12 pt, A4, justified body text
- PDF bookmarks (outline panel) for every section and every note
- Clickable dot-leader index  --  click any title to jump to the page
- Roman-numeral footer on index pages, Arabic on content pages
- Word-wrap in table cells (no mid-word breaks)
- Accurate row-height estimation (1-line rows never double-spaced)

Usage:
  /usr/local/bin/python3 mch_to_pdf.py
"""

import os, re, math, io
from fpdf import FPDF
from fpdf.enums import WrapMode
from PyPDF2 import PdfReader          # only used in Pass 1 to count pages

# ─────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────
VAULT_ANSWERS = "/Users/prajwaldange/MCh-HNSO/content/Answers"
OUTPUT_DIR    = "/Users/prajwaldange/Downloads/Scott Brown Textbooks/PDF_Papers"
OUTPUT_FILE   = os.path.join(OUTPUT_DIR, "MCh_HNSO_Complete_Answers.pdf")

SECTION_ORDER = [
    "General",
    "Oral Cavity",
    "Oropharynx",
    "Hypopharynx",
    "Larynx",
    "Nasopharynx",
    "Nose and Paranasal Sinuses",
    "Neck",
    "Skull Base",
    "Thyroid",
    "Parathyroid",
    "Salivary Gland",
    "Ear and Temporal Bone",
    "Eye and Orbit",
    "Plastic Surgery",
    "Radiotherapy and Chemotherapy",
    "Robotic Surgery",
    "HPV",
    "Anatomy",
    "Statistics",
    "Trials",
    "Radiology and Nuclear Medicine",
    "Malignancy of Unknown Origin",
    "Soft Tissue Malignancy",
    "Cutaneous Malignancy",
    "Reconstruction",
    "Research Methodology",
]

# ─────────────────────────────────────────────────────────────
# PAGE / FONT CONSTANTS
# ─────────────────────────────────────────────────────────────
PW, PH = 210, 297           # A4 mm
ML, MR = 25, 25
MT, MB = 25, 20
UW     = PW - ML - MR       # 160 mm

TNR_REG  = "/Library/Fonts/Microsoft/Times New Roman.ttf"
TNR_BOLD = "/Library/Fonts/Microsoft/Times New Roman Bold.ttf"
TNR_ITAL = "/Library/Fonts/Microsoft/Times New Roman Italic.ttf"
TNR_BOLI = "/Library/Fonts/Microsoft/Times New Roman Bold Italic.ttf"

FS   = 12
LH   = FS * 0.352778 * 1.5     # ~6.35 mm


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def clean_md(text: str) -> str:
    if not text:
        return ""
    t = str(text)

    # ── Wikilinks ──────────────────────────────────────────────
    t = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', t)
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)

    # ── Standard markdown links [text](url) ───────────────────
    # Fix: allow parentheses inside URLs (e.g. DOIs like ...S0092-8674(00)81683-9)
    # Key: use [^()]* (exclude BOTH parens from base) so inner paren-pairs
    # are handled explicitly by (?:\([^()]*\)[^()]*)*
    t = re.sub(r'\[([^\]]+)\]\([^()]*(?:\([^()]*\)[^()]*)*\)', r'\1', t)

    # ── Inline markup ─────────────────────────────────────────
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    t = re.sub(r'`(.+?)`', r'\1', t)

    # ── HTML entities ─────────────────────────────────────────
    t = (t.replace('&mdash;', '--').replace('&ndash;', '-')
          .replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
          .replace('&nbsp;', ' ').replace('&#x27;', "'"))
    t = re.sub(r'<[^>]+>', '', t)

    # ── Escaped table pipes ───────────────────────────────────
    t = t.replace(r'\|', '|')

    # ── Unicode: typographic dashes FIRST (before latin-1 encoding) ──
    t = t.replace('—', '--')   # em dash  —  ->  --
    t = t.replace('–', '-')    # en dash  –  ->  -
    t = t.replace('’', "'")    # right single quote '
    t = t.replace('‘', "'")    # left  single quote '
    t = t.replace('“', '"')    # left  double quote "
    t = t.replace('”', '"')    # right double quote "
    t = t.replace('…', '...')  # ellipsis …

    # ── Other math / special Unicode ──────────────────────────
    t = t.replace('−', '-')    # minus sign
    t = t.replace('×', 'x')    # multiplication ×
    t = t.replace('≥', '>=').replace('≤', '<=')
    t = t.replace('→', '->').replace('←', '<-')
    t = t.replace('≠', '!=').replace('±', '+/-')
    t = t.replace('°', ' deg')
    t = t.replace('∝', 'proportional to')
    # Greek letters
    for uc, asc in [('α','alpha'),('β','beta'),('γ','gamma'),
                    ('δ','delta'),('μ','mu'),('σ','sigma'),
                    ('ε','epsilon'),('τ','tau'),('ρ','rho'),
                    ('θ','theta'),('λ','lambda')]:
        t = t.replace(uc, asc)

    # ── Final: strip anything still not Latin-1 ───────────────
    t = t.encode('latin-1', errors='replace').decode('latin-1')
    return t.strip()


def to_roman(n: int) -> str:
    vals = [(1000,'m'),(900,'cm'),(500,'d'),(400,'cd'),
            (100,'c'),(90,'xc'),(50,'l'),(40,'xl'),
            (10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')]
    r = ''
    for v, s in vals:
        while n >= v:
            r += s; n -= v
    return r


# ─────────────────────────────────────────────────────────────
# PDF CLASS
# ─────────────────────────────────────────────────────────────
class MchPDF(FPDF):
    """
    roman_cutoff: pages 1..roman_cutoff get Roman numeral footers.
                  Pages above get Arabic footers equal to the PDF page number.
                  Set to 0 for all-Arabic (used in Pass 1 measurement).
    """

    def __init__(self, roman_cutoff: int = 0):
        super().__init__('P', 'mm', 'A4')
        self.set_margins(ML, MT, MR)
        self.set_auto_page_break(True, MB)
        self._roman_cutoff = roman_cutoff
        self.add_font('TNR', '',   TNR_REG)
        self.add_font('TNR', 'B',  TNR_BOLD)
        self.add_font('TNR', 'I',  TNR_ITAL)
        self.add_font('TNR', 'BI', TNR_BOLI)

    def footer(self):
        pg = self.page_no()
        if self._roman_cutoff > 0 and pg <= self._roman_cutoff:
            label = to_roman(pg)
        else:
            label = str(pg)
        self.set_y(-15)
        self.set_font('TNR', '', 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 8, label, align='C')
        self.set_text_color(0, 0, 0)

    # ── headings ──────────────────────────────────────────────
    def write_h1(self, text):
        self.ln(LH * 0.3)
        self.set_font('TNR', 'B', FS)
        self.multi_cell(UW, LH, clean_md(text), align='C',
                        new_x='LMARGIN', new_y='NEXT')
        self.ln(LH * 0.5)
        y = self.get_y()
        self.line(ML, y, PW - MR, y)
        self.ln(LH * 0.5)

    def write_h2(self, text):
        self.ln(LH * 0.5)
        self.set_font('TNR', 'B', FS)
        self.multi_cell(UW, LH, clean_md(text), align='L',
                        new_x='LMARGIN', new_y='NEXT')
        self.ln(LH * 0.15)

    def write_h3(self, text):
        self.ln(LH * 0.3)
        self.set_font('TNR', 'B', FS)
        self.multi_cell(UW, LH, clean_md(text), align='L',
                        new_x='LMARGIN', new_y='NEXT')

    def write_h4(self, text):
        self.ln(LH * 0.2)
        self.set_font('TNR', 'BI', FS)
        self.multi_cell(UW, LH, clean_md(text), align='L',
                        new_x='LMARGIN', new_y='NEXT')

    def write_body(self, text):
        self.set_font('TNR', '', FS)
        cleaned = clean_md(text)
        if cleaned:
            self.multi_cell(UW, LH, cleaned, align='J',
                            new_x='LMARGIN', new_y='NEXT')
            self.ln(LH * 0.2)

    def write_bullet(self, text, level=0):
        self.set_font('TNR', '', FS)
        indent = level * 6
        bw = 5
        cw = UW - indent - bw
        x0 = ML + indent
        y0 = self.get_y()
        self.set_xy(x0, y0)
        self.cell(bw, LH, chr(8226))
        self.set_xy(x0 + bw, y0)
        self.multi_cell(cw, LH, clean_md(text), align='J',
                        new_x='LMARGIN', new_y='NEXT')

    def write_numbered(self, n, text):
        self.set_font('TNR', '', FS)
        nw = 8
        y0 = self.get_y()
        self.set_xy(ML, y0)
        self.cell(nw, LH, f"{n}.")
        self.set_xy(ML + nw, y0)
        self.multi_cell(UW - nw, LH, clean_md(text), align='J',
                        new_x='LMARGIN', new_y='NEXT')

    def write_hrule(self):
        self.ln(LH * 0.5)
        y = self.get_y()
        self.line(ML, y, PW - MR, y)
        self.ln(LH * 0.5)

    def write_callout_header(self, ctype, title):
        self.ln(LH * 0.4)
        y = self.get_y()
        self.line(ML, y, ML + 2, y)
        self.set_font('TNR', 'BI', FS)
        label = title if title else ctype.title()
        self.set_x(ML + 4)
        self.multi_cell(UW - 4, LH, label, align='L',
                        new_x='LMARGIN', new_y='NEXT')

    # ── section divider page ──────────────────────────────────
    def write_section_page(self, name):
        mid = PH / 2
        self.set_y(mid - 18)
        self.write_hrule()
        self.set_font('TNR', 'B', 14)
        self.cell(UW, LH, name, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(LH * 0.5)
        self.set_font('TNR', 'I', 10)
        self.cell(UW, LH * 0.8,
                  'MCh Head and Neck Surgery & Oncology -- Examination Answers',
                  align='C', new_x='LMARGIN', new_y='NEXT')
        self.write_hrule()

    # ── tables ────────────────────────────────────────────────
    def write_table(self, headers, rows, small=False):
        """
        Render a Markdown table with:
          • Vertically centred text in every cell (border drawn via rect(),
            text rendered separately at the centred y-position)
          • WORD wrap (CHAR fallback for long unbreakable tokens like DOIs)
          • Consistent row heights driven by the tallest cell
          • Reduced line height (1.45x) for compact appearance
        """
        fsize  = 9 if small else 10
        cell_h = fsize * 0.352778 * 1.45   # 1.45× for tighter, more uniform rows
        n_cols = max(len(headers), max((len(r) for r in rows), default=0))
        if n_cols == 0:
            return

        widths = self._calc_col_widths(headers, rows, n_cols, fsize)

        def _draw_row(cells, y0, row_h, is_header=False):
            """Draw one full row: borders first, then vertically centred text."""
            for i in range(n_cols):
                x    = ML + sum(widths[:i])
                w    = widths[i]
                text = clean_md(cells[i]) if i < len(cells) else ''
                bold = is_header
                align = 'C' if is_header else 'L'

                # ── 1. Draw full-height cell border (+ fill for header) ──
                self.set_draw_color(0, 0, 0)
                self.set_line_width(0.2)
                if is_header:
                    self.set_fill_color(230, 230, 230)
                    self.rect(x, y0, w, row_h, style='FD')
                else:
                    self.rect(x, y0, w, row_h, style='D')

                # ── 2. Compute vertical offset for centering ─────────────
                n_lines  = self._cell_lines(text, w, fsize, cell_h)
                text_h   = cell_h * n_lines
                v_off    = max(0.0, (row_h - text_h) / 2.0)

                # ── 3. Render text without border at centred y position ──
                self.set_font('TNR', 'B' if bold else '', fsize)
                self.set_xy(x, y0 + v_off)
                if text:
                    try:
                        self.multi_cell(w, cell_h, text,
                                        border=0, align=align,
                                        wrapmode=WrapMode.WORD,
                                        new_x='LMARGIN', new_y='NEXT')
                    except Exception:
                        try:
                            self.multi_cell(w, cell_h, text,
                                            border=0, align=align,
                                            wrapmode=WrapMode.CHAR,
                                            new_x='LMARGIN', new_y='NEXT')
                        except Exception:
                            t = text
                            while t and self.get_string_width(t) > w - 3:
                                t = t[:-1]
                            self.set_xy(x + 1, y0 + v_off)
                            self.cell(w - 1, cell_h, t, border=0, align=align)

            # Move cursor to next row
            self.set_xy(ML, y0 + row_h)

        # ── Header row ────────────────────────────────────────────
        if headers:
            y0    = self.get_y()
            row_h = self._row_h(headers, widths, fsize, cell_h)
            if y0 + row_h > PH - MB - 5:
                self.add_page(); y0 = self.get_y()
            _draw_row(headers, y0, row_h, is_header=True)

        # ── Data rows ─────────────────────────────────────────────
        for row in rows:
            while len(row) < n_cols:
                row.append('')
            y0    = self.get_y()
            row_h = self._row_h(row[:n_cols], widths, fsize, cell_h)
            if y0 + row_h > PH - MB - 5:
                self.add_page(); y0 = self.get_y()
            _draw_row(row[:n_cols], y0, row_h, is_header=False)

        self.ln(LH * 0.5)

    def _calc_col_widths(self, headers, rows, n, fsize):
        """
        Three-tier column-width algorithm.

        Tier 1  NARROW  nat <= 22 mm  e.g. Year, short %, stage numbers
                         -> exact natural width, never scaled
        Tier 2  MEDIUM  22 < nat <= 42 mm  e.g. Journal names, short labels
                         -> exact natural width, never scaled
                         (ensures "Nat Rev Cancer", "Laryngoscope" etc. fit)
        Tier 3  WIDE    nat >  42 mm  e.g. Study/Title, DOI, long description
                         -> share remaining budget with per-column cap;
                            scaled proportionally when over budget

        This guarantees that medium-length content (journal names) is never
        squeezed below its natural width, while long columns absorb the scaling.
        """
        self.set_font('TNR', '', fsize)
        NARROW_MAX = 22.0    # ≤ this → Tier 1
        MEDIUM_MAX = 42.0    # ≤ this → Tier 2
        MIN_WIDE   = 20.0    # absolute floor for Tier 3 columns
        PAD        = 6.0     # padding added to string_width

        # ── Measure natural (single-line) widths ─────────────
        nat = [0.0] * n
        for row in ([headers] if headers else []) + list(rows):
            for i, c in enumerate(row[:n]):
                w = self.get_string_width(clean_md(str(c))) + PAD
                if w > nat[i]:
                    nat[i] = w

        # ── Classify columns ──────────────────────────────────
        narrow_idx = [i for i in range(n) if nat[i] <= NARROW_MAX]
        medium_idx = [i for i in range(n) if NARROW_MAX < nat[i] <= MEDIUM_MAX]
        wide_idx   = [i for i in range(n) if nat[i] > MEDIUM_MAX]

        # Tier 1 + 2: exact natural widths
        widths = list(nat)

        # Tier 3: allocate remaining budget
        fixed_total = sum(nat[i] for i in narrow_idx + medium_idx)
        budget      = UW - fixed_total

        if wide_idx:
            # Cap at fair_share * 1.2 — prevents Study/title column from
            # monopolising space and gives DOI column enough width (~50 mm)
            # to fit most DOI strings without wrapping.
            cap = (budget / len(wide_idx)) * 1.2
            for i in wide_idx:
                widths[i] = max(MIN_WIDE, min(nat[i], cap))

            # Scale down proportionally if over budget
            total = sum(widths)
            if total > UW + 0.01:
                over  = total - UW
                wtot  = sum(widths[i] for i in wide_idx)
                if wtot > 0:
                    for i in wide_idx:
                        widths[i] = max(MIN_WIDE,
                                        widths[i] - (widths[i] / wtot) * over)

            # Distribute any surplus to wide columns
            total = sum(widths)
            if total < UW - 0.01:
                extra = (UW - total) / len(wide_idx)
                for i in wide_idx:
                    widths[i] += extra
        else:
            # No wide columns: scale medium columns proportionally
            total = sum(widths)
            if total > UW + 0.01:
                over = total - UW
                mtot = sum(widths[i] for i in medium_idx) if medium_idx else 1
                for i in medium_idx:
                    widths[i] = max(MIN_WIDE,
                                    widths[i] - (widths[i] / mtot) * over)

        # ── Float safety: absorb rounding into last wide/medium/narrow col ──
        fix_pool = wide_idx or medium_idx or list(range(n))
        fix_idx  = fix_pool[-1]
        diff = UW - sum(widths)
        widths[fix_idx] = max(MIN_WIDE, widths[fix_idx] + diff)

        return widths

    def _cell_lines(self, text, col_w, fsize, cell_h):
        """
        Return the predicted line count for a single cell.
        Uses the same conservative word-wrap simulation as _row_h
        (avail × 0.93) so the vertical-centering offset matches the
        actual rendered height.
        """
        if not text:
            return 1
        self.set_font('TNR', '', fsize)
        cm    = (fsize * 0.352778) / 6
        avail = (col_w - 2 * cm) * 0.93
        if avail <= 0:
            return 1
        sp_w  = self.get_string_width(' ')
        words = text.split()
        lines = 1
        line_w = 0.0
        for word in words:
            ww = self.get_string_width(word)
            if ww > avail:
                if line_w > 0:
                    lines += 1; line_w = 0
                lines += max(0, int(ww / avail))
                line_w = ww % avail if avail > 0 else 0
            elif line_w == 0:
                line_w = ww
            elif line_w + sp_w + ww <= avail:
                line_w += sp_w + ww
            else:
                lines += 1; line_w = ww
        return lines

    def _row_h(self, cells, widths, fsize, cell_h):
        """
        Estimate table row height using a conservative word-wrap simulation.

        Root cause of overflow bug: get_string_width() has tiny floating-point
        differences vs. fpdf2's internal layout engine, causing borderline words
        to be predicted as fitting on the current line when fpdf2 actually wraps
        them to the next line. Fix: shrink the simulated available width by 7%
        so borderline wrap decisions always predict wrapping.

        Single-line rows are unaffected (their text has plenty of headroom);
        multi-line rows may get +1 extra line of height at most, preventing
        the next row from overlapping.

        Returns cell_h * max_lines + 1.2 mm flat bottom padding per row.
        """
        self.set_font('TNR', '', fsize)
        max_lines = 1
        sp_w = self.get_string_width(' ')
        cm   = (fsize * 0.352778) / 6

        for i, c in enumerate(cells):
            if i >= len(widths) or widths[i] <= 2:
                continue
            text = clean_md(str(c))
            if not text:
                continue

            # ── conservative available width (7% narrower than actual) ──
            raw_avail = widths[i] - 2 * cm
            avail     = raw_avail * 0.93   # <-- key fix: catch borderline wraps
            if avail <= 0:
                continue

            words  = text.split()
            lines  = 1
            line_w = 0.0
            for word in words:
                ww = self.get_string_width(word)
                if ww > avail:
                    # Word longer than column: will char-wrap
                    if line_w > 0:
                        lines += 1; line_w = 0
                    lines += max(0, int(ww / avail))
                    line_w = ww % avail if avail > 0 else 0
                elif line_w == 0:
                    line_w = ww
                elif line_w + sp_w + ww <= avail:
                    line_w += sp_w + ww
                else:
                    lines += 1; line_w = ww

            if lines > max_lines:
                max_lines = lines

        return cell_h * max_lines + 0.6   # 0.6 mm flat padding — keeps rows tight


# ─────────────────────────────────────────────────────────────
# MARKDOWN PARSER  (unchanged from v2)
# ─────────────────────────────────────────────────────────────
def parse_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        raw = f.read()
    if raw.startswith('---'):
        end = raw.find('\n---', 3)
        if end != -1:
            raw = raw[end + 4:].lstrip('\n')

    lines = raw.split('\n')
    elems = []
    i = 0
    while i < len(lines):
        line    = lines[i]
        stripped = line.strip()

        m = re.match(r'^>\s*\[!(\w+)\][-+]?\s*(.*)', stripped)
        if m:
            ctype, ctitle = m.group(1).lower(), m.group(2).strip()
            cl = []
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith('>') or s == '>':
                    cl.append(s); i += 1
                else:
                    break
            if ctype == 'compass':
                continue
            elems.append(('callout_start', ctype, ctitle))
            elems += _parse_callout_body(cl)
            elems.append(('callout_end',))
            continue

        if stripped.startswith('>') and not stripped.startswith('> [!'):
            t = stripped[1:].strip()
            if t:
                elems.append(('body', t))
            i += 1; continue

        hm = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if hm:
            level = len(hm.group(1))
            tag   = ('h1','h2','h3','h4','h4','h4')[min(level-1, 5)]
            elems.append((tag, hm.group(2).strip()))
            i += 1; continue

        if re.match(r'^[-*_]{3,}$', stripped) and stripped:
            elems.append(('hrule',)); i += 1; continue

        if stripped.startswith('|') and '|' in stripped[1:]:
            tl = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                tl.append(lines[i].strip()); i += 1
            if len(tl) >= 2:
                hdr  = _parse_table_row(tl[0])
                rows = [_parse_table_row(r) for r in tl[2:]
                        if not re.match(r'^\|[-| :]+\|$', r)]
                elems.append(('table', hdr, [r for r in rows if r]))
            continue

        nm = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if nm:
            elems.append(('numbered', int(nm.group(1)), nm.group(2)))
            i += 1; continue

        bm = re.match(r'^(\s*)[*\-+]\s+(.*)', line)
        if bm:
            indent = len(bm.group(1)) // 2
            elems.append(('bullet', bm.group(2), indent))
            i += 1; continue

        if not stripped:
            i += 1; continue

        para = [stripped]; i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith('#') or nxt.startswith('|')
                    or nxt.startswith('>')
                    or re.match(r'^[-*_]{3,}$', nxt)
                    or re.match(r'^\d+\.\s+', nxt)
                    or re.match(r'^[*\-+]\s+', nxt)):
                break
            para.append(nxt); i += 1
        elems.append(('body', ' '.join(para)))

    return elems


def _parse_callout_body(callout_lines):
    stripped = []
    for cl in callout_lines:
        if cl.startswith('> '):
            stripped.append(cl[2:])
        elif cl == '>':
            stripped.append('')
        else:
            stripped.append(cl.lstrip('> '))

    elems = []
    i = 0
    while i < len(stripped):
        s = stripped[i].strip()
        if not s:
            i += 1; continue

        if s.startswith('|') and '|' in s[1:]:
            tl = []
            while i < len(stripped) and stripped[i].strip().startswith('|'):
                tl.append(stripped[i].strip()); i += 1
            if len(tl) >= 2:
                hdr  = _parse_table_row(tl[0])
                rows = [_parse_table_row(r) for r in tl[2:]
                        if not re.match(r'^\|[-| :]+\|$', r)]
                elems.append(('table', hdr, [r for r in rows if r]))
            continue

        hm = re.match(r'^(#{1,4})\s+(.*)', s)
        if hm:
            tag = ('h2','h3','h4','h4')[min(len(hm.group(1))-1, 3)]
            elems.append((tag, hm.group(2).strip()))
            i += 1; continue

        nm = re.match(r'^(\d+)\.\s+(.*)', s)
        if nm:
            elems.append(('numbered', int(nm.group(1)), nm.group(2)))
            i += 1; continue

        bm = re.match(r'^[*\-+]\s+(.*)', s)
        if bm:
            elems.append(('bullet', bm.group(1), 0))
            i += 1; continue

        elems.append(('body', s)); i += 1
    return elems


def _parse_table_row(line):
    line = line.strip()
    if line.startswith('|'): line = line[1:]
    if line.endswith('|'):   line = line[:-1]
    return [c.strip() for c in line.split('|')]


# ─────────────────────────────────────────────────────────────
# RENDER A SINGLE FILE
# ─────────────────────────────────────────────────────────────
def render_file(path, pdf):
    in_cite = False
    for elem in parse_file(path):
        t = elem[0]
        if t == 'callout_start':
            in_cite = (elem[1] == 'cite')
            if elem[1] != 'cite':
                pdf.write_callout_header(elem[1], elem[2])
        elif t == 'callout_end':
            in_cite = False; pdf.ln(LH * 0.3)
        elif t == 'h1':     pdf.write_h1(elem[1])
        elif t == 'h2':     pdf.write_h2(elem[1])
        elif t == 'h3':     pdf.write_h3(elem[1])
        elif t == 'h4':     pdf.write_h4(elem[1])
        elif t == 'body':   pdf.write_body(elem[1])
        elif t == 'bullet': pdf.write_bullet(elem[1], level=elem[2] if len(elem)>2 else 0)
        elif t == 'numbered': pdf.write_numbered(elem[1], elem[2])
        elif t == 'hrule':  pdf.write_hrule()
        elif t == 'table':  pdf.write_table(elem[1], elem[2], small=in_cite)


# ─────────────────────────────────────────────────────────────
# COLLECT FILES
# ─────────────────────────────────────────────────────────────
def collect_files():
    result = []
    for section in SECTION_ORDER:
        folder = os.path.join(VAULT_ANSWERS, section)
        if not os.path.isdir(folder):
            continue
        files = sorted(
            f for f in (os.path.join(folder, n) for n in os.listdir(folder))
            if f.endswith('.md') and not os.path.basename(f).lower().startswith('index')
        )
        if files:
            result.append((section, files))
    return result


# ─────────────────────────────────────────────────────────────
# PASS 1  —  measure raw page count (content only, no index)
# ─────────────────────────────────────────────────────────────
def measure_content_pages(files_by_section):
    """Render content to a temp PDF and return raw page count + entry list."""
    pdf     = MchPDF(roman_cutoff=0)
    entries = []
    for section, files in files_by_section:
        pdf.add_page()                           # section divider
        for filepath in files:
            pdf.add_page()
            entries.append((os.path.basename(filepath).replace('.md',''),
                            section,
                            pdf.page_no()))      # raw page in this temp PDF
            try:
                render_file(filepath, pdf)
            except Exception as e:
                print(f"    WARN: {os.path.basename(filepath)}: {e}")
    buf = io.BytesIO()
    pdf.output(buf)
    n_pages = PdfReader(buf).pages.__len__()
    return n_pages, entries   # entries have raw page numbers (1-indexed in content-only PDF)


# ─────────────────────────────────────────────────────────────
# PASS 2  —  build complete PDF in one document
#            index (Roman) + content (Arabic)
#            bookmarks for sections and notes
#            clickable index entries
# ─────────────────────────────────────────────────────────────
def build_complete_pdf(files_by_section, n_index_pages, entries_raw):
    """
    entries_raw: [(title, section, raw_content_page), ...]
    In the final merged doc, a raw content page r becomes PDF page (n_index_pages + r).
    """
    # Build lookup: (title, section) -> final PDF page number
    final_page = {
        (title, section): n_index_pages + raw
        for title, section, raw in entries_raw
    }

    pdf = MchPDF(roman_cutoff=n_index_pages)

    # ── TITLE PAGE (page 1 = 'i') ─────────────────────────────
    pdf.add_page()
    pdf.set_y(PH / 2 - 40)
    pdf.write_hrule()
    pdf.set_font('TNR', 'B', 16)
    pdf.cell(UW, LH * 1.2, 'MCh Head and Neck Surgery & Oncology',
             align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(LH * 0.4)
    pdf.set_font('TNR', 'B', 13)
    pdf.cell(UW, LH, 'Examination Answers -- Complete Collection',
             align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(LH * 0.8)
    pdf.set_font('TNR', '', 11)
    total_notes    = len(entries_raw)
    total_sections = len(set(s for _, s, _ in entries_raw))
    total_pages    = n_index_pages + entries_raw[-1][2]
    pdf.cell(UW, LH * 0.9,
             f'{total_notes} notes  |  {total_sections} sections  |  {total_pages} pages',
             align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.write_hrule()

    # ── INDEX PAGES ───────────────────────────────────────────
    # We need one index page to start; more will be added automatically.
    pdf.add_page()
    pdf.set_font('TNR', 'B', 13)
    pdf.cell(UW, LH, 'INDEX', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(LH * 0.5)
    pdf.write_hrule()
    pdf.ln(LH * 0.2)

    idx_lh = 10 * 0.352778 * 1.4    # compact line height

    # Create all link IDs now; set destinations after content is rendered.
    link_ids = {}   # (title, section) -> link_id

    current_section = None
    for title, section, _ in entries_raw:
        link_id = pdf.add_link()
        link_ids[(title, section)] = link_id

        if section != current_section:
            current_section = section
            if pdf.get_y() + idx_lh * 2 > PH - MB - 5:
                pdf.add_page()
            pdf.ln(idx_lh * 0.4)
            pdf.set_font('TNR', 'B', 10)
            pdf.cell(UW, idx_lh, section.upper(),
                     new_x='LMARGIN', new_y='NEXT')
            y = pdf.get_y()
            pdf.line(ML, y, ML + 40, y)
            pdf.ln(idx_lh * 0.2)

        if pdf.get_y() + idx_lh > PH - MB - 5:
            pdf.add_page()

        pdf.set_font('TNR', '', 10)
        page_num  = final_page.get((title, section), 0)
        pg_str    = str(page_num)
        pg_w      = pdf.get_string_width(pg_str) + 2
        title_w   = pdf.get_string_width(title)
        avail     = UW - pg_w - title_w - 4
        dot_w     = pdf.get_string_width('.')
        n_dots    = max(3, int(avail / dot_w)) if dot_w > 0 else 3
        dot_str   = ' ' + '.' * n_dots + ' '

        y0 = pdf.get_y()
        pdf.set_xy(ML, y0)
        # Clickable title cell
        pdf.cell(UW - pg_w, idx_lh, title + dot_str,
                 align='L', link=link_id)
        pdf.set_x(PW - MR - pg_w)
        pdf.cell(pg_w, idx_lh, pg_str,
                 align='R', link=link_id,
                 new_x='LMARGIN', new_y='NEXT')

    # Verify we are still within n_index_pages
    if pdf.page_no() > n_index_pages:
        print(f"  NOTE: Index grew to {pdf.page_no()} pages (expected {n_index_pages}). "
              f"Re-run script once to recalibrate.")

    # ── CONTENT  ──────────────────────────────────────────────
    for section, files in files_by_section:
        # Section divider page — top-level PDF bookmark
        pdf.add_page()
        pdf.start_section(section, level=0)
        pdf.write_section_page(section)

        for filepath in files:
            pdf.add_page()
            title = os.path.basename(filepath).replace('.md', '')

            # Second-level bookmark for this note
            pdf.start_section(title, level=1)

            # Register the link destination at the top of this page
            key = (title, section)
            if key in link_ids:
                pdf.set_link(link_ids[key], page=pdf.page_no())

            try:
                render_file(filepath, pdf)
            except Exception as e:
                print(f"    WARN: {os.path.basename(filepath)}: {e}")
                pdf.set_font('TNR', 'I', 10)
                pdf.multi_cell(UW, LH, f"[Rendering error: {e}]")

    buf = io.BytesIO()
    pdf.output(buf)
    return buf.getvalue()


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("MCh-HNSO -> PDF  (v3: bookmarks + clickable index + word-wrap tables)")
    print("=" * 70)

    files_by_section = collect_files()
    total_notes = sum(len(f) for _, f in files_by_section)
    print(f"Found {total_notes} notes across {len(files_by_section)} sections:")
    for sec, fs in files_by_section:
        print(f"  {sec}: {len(fs)}")
    print()

    # ── Pass 1: measure ───────────────────────────────────────
    print("Pass 1: measuring content layout...")
    n_content_pages, entries_raw = measure_content_pages(files_by_section)
    print(f"  Content: {n_content_pages} raw pages, {total_notes} notes")

    # Estimate index size: title page + ~1 index page per 40 entries
    est_index = 2 + math.ceil(total_notes / 35)
    print(f"  Estimated index pages: {est_index}")

    # ── Pass 2: build final PDF ───────────────────────────────
    print(f"\nPass 2: building complete PDF (index pages = {est_index})...")
    final_bytes = build_complete_pdf(files_by_section, est_index, entries_raw)

    with open(OUTPUT_FILE, 'wb') as f:
        f.write(final_bytes)

    # Verify final page count
    actual_pages = len(PdfReader(io.BytesIO(final_bytes)).pages)
    size_mb = len(final_bytes) / (1024 * 1024)

    print()
    print("=" * 70)
    print(f"Saved: {OUTPUT_FILE}")
    print(f"  Index   : {est_index} pages  (i ... {to_roman(est_index)})")
    print(f"  Content : {actual_pages - est_index} pages")
    print(f"  Total   : {actual_pages} pages")
    print(f"  Size    : {size_mb:.1f} MB")
    print(f"  Notes   : {total_notes}")
    print(f"  Bookmarks: YES  |  Clickable index: YES  |  Word-wrap tables: YES")
    print("=" * 70)

    # ── Check if index overflowed and re-run is needed ────────
    reader   = PdfReader(io.BytesIO(final_bytes))
    idx_text = ''.join(reader.pages[p].extract_text() or ''
                       for p in range(min(est_index, actual_pages)))
    # The first content section name should NOT appear in the index pages
    first_section = files_by_section[0][0].upper()
    if first_section in idx_text and 'MCh Head and Neck' not in idx_text[:100]:
        print(f"\n  WARNING: Index may have overflowed {est_index} pages.")
        print("  Increase est_index in main() and re-run if content bleeds into index.")


if __name__ == '__main__':
    main()
