#!/usr/bin/env python3
"""
MCh-HNSO Vault → Printer-Ready PDF
====================================
Converts all answer markdown files to a single A4 PDF.

Formatting:
  - Times New Roman 12 pt throughout
  - Justified body text, 1.5 line spacing
  - Bold Times New Roman for all headings and subheadings
  - Each note starts on a new page
  - Page numbers centred at the foot of every page
  - Index (note name + page number) prepended with Roman-numeral pages

Usage:
  python3 mch_to_pdf.py
"""

import os, re, math, io
from fpdf import FPDF
from fpdf.enums import WrapMode
from PyPDF2 import PdfMerger, PdfReader

# ─────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────
VAULT_ANSWERS = "/Users/prajwaldange/MCh-HNSO/content/Answers"
OUTPUT_DIR    = "/Users/prajwaldange/Downloads/Scott Brown Textbooks/PDF_Papers"
OUTPUT_FILE   = os.path.join(OUTPUT_DIR, "MCh_HNSO_Complete_Answers.pdf")

# Section display order
SECTION_ORDER = [
    "General",
    "Oral Cavity",
    "Oropharynx",
    "Hypopharynx",
    "Larynx",
    "Thyroid",
    "Neck",
    "Salivary Gland",
    "Skull Base",
    "Radiotherapy and Chemotherapy",
    "Reconstruction",
    "Research Methodology",
]

# ─────────────────────────────────────────────────────────────
# PAGE / FONT CONSTANTS
# ─────────────────────────────────────────────────────────────
PW, PH   = 210, 297          # A4 mm
ML, MR   = 25, 25            # left / right margins
MT, MB   = 25, 20            # top / bottom margins
UW       = PW - ML - MR      # usable width = 160 mm

TNR_REG  = "/Library/Fonts/Microsoft/Times New Roman.ttf"
TNR_BOLD = "/Library/Fonts/Microsoft/Times New Roman Bold.ttf"
TNR_ITAL = "/Library/Fonts/Microsoft/Times New Roman Italic.ttf"
TNR_BOLI = "/Library/Fonts/Microsoft/Times New Roman Bold Italic.ttf"

FS      = 12                           # body font size (pt)
LH      = FS * 0.352778 * 1.5         # body line height (mm) ≈ 6.35
LH_SM   = 10 * 0.352778 * 1.5         # smaller line height for tables/index


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def clean_md(text: str) -> str:
    """Strip Markdown / Obsidian formatting for plain PDF text."""
    if not text:
        return ""
    t = str(text)
    # Wikilinks with display text  [[Path|Display]]
    t = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', t)
    # Plain wikilinks  [[Path]]
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)
    # Standard links  [text](url)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    # Bold-italic  ***text***
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', t)
    # Bold  **text**
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    # Italic  *text*
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    # Code  `text`
    t = re.sub(r'`(.+?)`', r'\1', t)
    # HTML entities
    t = (t.replace('&mdash;', '—').replace('&ndash;', '–')
          .replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
          .replace('&nbsp;', ' ').replace('&#x27;', "'"))
    # HTML tags
    t = re.sub(r'<[^>]+>', '', t)
    # Escaped pipes (used in markdown tables inside callouts)
    t = t.replace(r'\|', '|')
    # Subscript / superscript Unicode → plain ASCII
    SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
    SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺', '0123456789-+')
    t = t.translate(SUB).translate(SUP)
    # Other missing glyphs
    t = t.replace('∝', 'proportional to').replace('\ufffd', '?')
    t = t.replace('\u2212', '-')   # minus sign → hyphen
    t = t.replace('\u00d7', 'x')   # multiplication sign
    t = t.replace('\u03b1', 'alpha').replace('\u03b2', 'beta')
    t = t.replace('\u03b3', 'gamma').replace('\u03b4', 'delta')
    t = t.replace('\u03bc', 'mu').replace('\u03c3', 'sigma')
    return t.strip()


def to_roman(n: int) -> str:
    """Convert integer to lowercase Roman numeral."""
    vals = [(1000,'m'),(900,'cm'),(500,'d'),(400,'cd'),
            (100,'c'),(90,'xc'),(50,'l'),(40,'xl'),
            (10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')]
    r = ''
    for v, s in vals:
        while n >= v:
            r += s
            n -= v
    return r


# ─────────────────────────────────────────────────────────────
# PDF CLASS
# ─────────────────────────────────────────────────────────────
class MchPDF(FPDF):
    """
    Custom FPDF subclass with MCh-HNSO formatting.
    page_offset: number of index pages prepended — added to every footer.
    roman_footer: if True, render footer as Roman numerals (for index PDF).
    """

    def __init__(self, page_offset: int = 0, roman_footer: bool = False):
        super().__init__('P', 'mm', 'A4')
        self.set_margins(ML, MT, MR)
        self.set_auto_page_break(True, MB)
        self._page_offset  = page_offset
        self._roman_footer = roman_footer
        self.add_font('TNR', '',   TNR_REG)
        self.add_font('TNR', 'B',  TNR_BOLD)
        self.add_font('TNR', 'I',  TNR_ITAL)
        self.add_font('TNR', 'BI', TNR_BOLI)

    # ── footer ──────────────────────────────────────────────
    def footer(self):
        self.set_y(-15)
        self.set_font('TNR', '', 9)
        self.set_text_color(80, 80, 80)
        if self._roman_footer:
            pg = to_roman(self.page_no())
        else:
            pg = str(self.page_no() + self._page_offset)
        self.cell(0, 8, pg, align='C')
        self.set_text_color(0, 0, 0)

    # ── headings ────────────────────────────────────────────
    def write_h1(self, text: str):
        """Note title: 12 pt bold, centred."""
        self.ln(LH * 0.3)
        self.set_font('TNR', 'B', FS)
        self.multi_cell(UW, LH, clean_md(text), align='C',
                        new_x='LMARGIN', new_y='NEXT')
        self.ln(LH * 0.5)
        # underline rule
        y = self.get_y()
        self.line(ML, y, PW - MR, y)
        self.ln(LH * 0.5)

    def write_h2(self, text: str):
        """Section heading: 12 pt bold, left."""
        self.ln(LH * 0.5)
        self.set_font('TNR', 'B', FS)
        self.multi_cell(UW, LH, clean_md(text), align='L',
                        new_x='LMARGIN', new_y='NEXT')
        self.ln(LH * 0.15)

    def write_h3(self, text: str):
        """Sub-heading: 12 pt bold, left."""
        self.ln(LH * 0.3)
        self.set_font('TNR', 'B', FS)
        self.multi_cell(UW, LH, clean_md(text), align='L',
                        new_x='LMARGIN', new_y='NEXT')

    def write_h4(self, text: str):
        """Sub-sub-heading: 12 pt bold-italic, left."""
        self.ln(LH * 0.2)
        self.set_font('TNR', 'BI', FS)
        self.multi_cell(UW, LH, clean_md(text), align='L',
                        new_x='LMARGIN', new_y='NEXT')

    # ── body text ───────────────────────────────────────────
    def write_body(self, text: str):
        """Body paragraph: 12 pt, justified, 1.5 spacing."""
        self.set_font('TNR', '', FS)
        cleaned = clean_md(text)
        if cleaned:
            self.multi_cell(UW, LH, cleaned, align='J',
                            new_x='LMARGIN', new_y='NEXT')
            self.ln(LH * 0.2)

    # ── lists ───────────────────────────────────────────────
    def write_bullet(self, text: str, level: int = 0):
        """Bullet point, optionally indented."""
        self.set_font('TNR', '', FS)
        indent = level * 6
        bw     = 5
        cw     = UW - indent - bw
        x0     = ML + indent
        y0     = self.get_y()
        self.set_xy(x0, y0)
        self.cell(bw, LH, chr(8226))          # •
        self.set_xy(x0 + bw, y0)
        self.multi_cell(cw, LH, clean_md(text), align='J',
                        new_x='LMARGIN', new_y='NEXT')

    def write_numbered(self, n: int, text: str):
        """Numbered list item."""
        self.set_font('TNR', '', FS)
        nw  = 8
        cw  = UW - nw
        y0  = self.get_y()
        self.set_xy(ML, y0)
        self.cell(nw, LH, f"{n}.")
        self.set_xy(ML + nw, y0)
        self.multi_cell(cw, LH, clean_md(text), align='J',
                        new_x='LMARGIN', new_y='NEXT')

    # ── rules ───────────────────────────────────────────────
    def write_hrule(self):
        self.ln(LH * 0.5)
        y = self.get_y()
        self.line(ML, y, PW - MR, y)
        self.ln(LH * 0.5)

    # ── callout blocks ──────────────────────────────────────
    def write_callout_header(self, ctype: str, title: str):
        """Render a callout box header (thin rule + italic label)."""
        self.ln(LH * 0.4)
        y = self.get_y()
        self.line(ML, y, ML + 2, y)   # short left bar
        self.set_font('TNR', 'BI', FS)
        label = title if title else ctype.title()
        self.set_x(ML + 4)
        self.multi_cell(UW - 4, LH, label, align='L',
                        new_x='LMARGIN', new_y='NEXT')

    # ── tables ──────────────────────────────────────────────
    def write_table(self, headers: list, rows: list, small: bool = False):
        """Render a Markdown table. Columns auto-sized to fit usable width."""
        fsize  = 9 if small else 10
        cell_h = fsize * 0.352778 * 1.5
        n_cols = max(len(headers), max((len(r) for r in rows), default=0))
        if n_cols == 0:
            return

        widths = self._calc_col_widths(headers, rows, n_cols, fsize)

        def render_cell(text, w, y0, bold=False, centre=False, fill=False):
            """Render one table cell with fallback if too narrow."""
            self.set_font('TNR', 'B' if bold else '', fsize)
            if fill:
                self.set_fill_color(220, 220, 220)
            align = 'C' if centre else 'L'
            try:
                self.multi_cell(w, cell_h, text,
                                border=1, align=align, fill=fill,
                                wrapmode=WrapMode.CHAR,
                                new_x='RIGHT', new_y='TOP')
            except Exception:
                # Last-resort: truncate to single line
                t = text
                while t and self.get_string_width(t) > w - 3:
                    t = t[:-1]
                self.cell(w, cell_h, t, border=1, align=align, fill=fill)
                self.set_xy(self.get_x(), y0)   # stay on same row

        # ── Header row ──────────────────────────────────────
        if headers:
            y0    = self.get_y()
            max_h = self._row_h(headers, widths, fsize, cell_h, char_wrap=True)
            for i, h in enumerate(headers[:n_cols]):
                self.set_xy(ML + sum(widths[:i]), y0)
                render_cell(clean_md(h), widths[i], y0, bold=True, centre=True, fill=True)
            self.set_y(y0 + max_h)

        # ── Data rows ────────────────────────────────────────
        self.set_font('TNR', '', fsize)
        for row in rows:
            while len(row) < n_cols:
                row.append('')
            y0    = self.get_y()
            max_h = self._row_h(row[:n_cols], widths, fsize, cell_h, char_wrap=True)
            if y0 + max_h > PH - MB - 5:
                self.add_page()
                y0 = self.get_y()
            for i, cell in enumerate(row[:n_cols]):
                self.set_xy(ML + sum(widths[:i]), y0)
                render_cell(clean_md(cell), widths[i], y0)
            self.set_y(y0 + max_h)

        self.ln(LH * 0.5)

    def _calc_col_widths(self, headers, rows, n, fsize):
        """
        Compute column widths that sum to exactly UW.

        Strategy:
        • Measure the true natural width of each column's widest cell.
        • Cap ONLY the single widest column (Study titles etc.) at 42 % of UW.
          All other columns keep their natural widths so Journal/DOI etc. are
          never starved.
        • If total still > UW, scale all columns down proportionally while
          respecting a per-column minimum (dynamic: UW / n * 0.55, min 10 mm).
        • If total < UW, distribute surplus evenly.
        """
        self.set_font('TNR', '', fsize)
        MIN_COL = max(10.0, UW / n * 0.55)    # dynamic minimum per column
        MAX_COL = UW * 0.42                    # cap for the dominant column

        # ── Step 1: measure natural widths ──────────────────
        mx = [0.0] * n
        for row in ([headers] if headers else []) + list(rows):
            for i, c in enumerate(row[:n]):
                w = self.get_string_width(clean_md(str(c))) + 6
                if w > mx[i]:
                    mx[i] = w

        # ── Step 2: cap only the largest column ─────────────
        big_idx = mx.index(max(mx))
        mx[big_idx] = min(mx[big_idx], MAX_COL)

        # ── Step 3: enforce per-column minimums ─────────────
        mx = [max(w, MIN_COL) for w in mx]

        total = sum(mx)

        # ── Step 4: scale down if over budget ───────────────
        if total > UW + 0.01:
            scale  = UW / total
            scaled = [w * scale for w in mx]
            # re-enforce minimums after scaling
            for i in range(n):
                if scaled[i] < MIN_COL:
                    scaled[i] = MIN_COL
            # if minimums push us back over, reduce non-min columns
            over2 = sum(scaled) - UW
            if over2 > 0.01:
                free = [i for i in range(n) if scaled[i] > MIN_COL + 0.01]
                if free:
                    per = over2 / len(free)
                    for i in free:
                        scaled[i] = max(scaled[i] - per, MIN_COL)
            mx = scaled

        # ── Step 5: distribute surplus evenly ───────────────
        total = sum(mx)
        if total < UW - 0.01:
            extra = (UW - total) / n
            mx = [w + extra for w in mx]

        # ── Float safety ─────────────────────────────────────
        diff = UW - sum(mx)
        mx[-1] = max(mx[-1] + diff, MIN_COL)

        return mx

    def _row_h(self, cells, widths, fsize, cell_h, char_wrap=False):
        """Estimate the rendered height of a table row (in mm).
        Uses character-level wrapping model when char_wrap=True."""
        self.set_font('TNR', '', fsize)
        max_lines = 1
        c_margin  = (fsize * 0.352778) / 6     # fpdf2 default cell margin
        for i, c in enumerate(cells):
            if i >= len(widths) or widths[i] <= 2:
                continue
            text  = clean_md(str(c))
            avail = widths[i] - 2 * c_margin   # actual render width inside borders
            if avail <= 0:
                continue
            full_w = self.get_string_width(text)
            # Estimate lines (char wrap = break anywhere)
            lines  = max(1, math.ceil(full_w / avail))
            if lines > max_lines:
                max_lines = lines
        return cell_h * max_lines

    # ── section separator page ──────────────────────────────
    def write_section_page(self, name: str):
        """Full-page centred section divider."""
        self.add_page()
        mid = PH / 2
        self.set_y(mid - 18)
        self.write_hrule()
        self.set_font('TNR', 'B', 14)
        self.cell(UW, LH, name, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(LH * 0.5)
        self.set_font('TNR', 'I', 10)
        self.cell(UW, LH * 0.8, 'MCh Head and Neck Surgery & Oncology — Examination Answers',
                  align='C', new_x='LMARGIN', new_y='NEXT')
        self.write_hrule()


# ─────────────────────────────────────────────────────────────
# MARKDOWN PARSER
# ─────────────────────────────────────────────────────────────
def parse_file(path: str) -> list:
    """
    Parse a markdown file into a list of elements.
    Element types:
      ('h1', text), ('h2', text), ('h3', text), ('h4', text),
      ('body', text), ('bullet', text, level),
      ('numbered', n, text), ('hrule',),
      ('callout_start', ctype, title), ('callout_end',),
      ('table', headers, rows)
    Compass callout elements are excluded.
    """
    with open(path, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Strip YAML frontmatter
    if raw.startswith('---'):
        end = raw.find('\n---', 3)
        if end != -1:
            raw = raw[end + 4:].lstrip('\n')

    lines  = raw.split('\n')
    elems  = []
    i      = 0
    skip_compass = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Callout block start ──────────────────────────────
        m = re.match(r'^>\s*\[!(\w+)\][-+]?\s*(.*)', stripped)
        if m:
            ctype = m.group(1).lower()
            ctitle = m.group(2).strip()

            # Collect all lines belonging to this callout
            callout_lines = []
            i += 1
            while i < len(lines):
                cl = lines[i]
                cl_stripped = cl.strip()
                # Callout continues while lines start with '>'
                if cl_stripped.startswith('>') or cl_stripped == '>':
                    callout_lines.append(cl_stripped)
                    i += 1
                else:
                    break

            # Skip compass callouts entirely
            if ctype == 'compass':
                continue

            # Emit callout header
            elems.append(('callout_start', ctype, ctitle))

            # Parse callout body
            elems += _parse_callout_body(callout_lines)

            elems.append(('callout_end',))
            continue

        # ── Standalone > line (stray callout content) ────────
        if stripped.startswith('>') and not stripped.startswith('> [!'):
            text = stripped[1:].strip()
            if text:
                elems.append(('body', text))
            i += 1
            continue

        # ── Heading ──────────────────────────────────────────
        hm = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if hm:
            level = len(hm.group(1))
            text  = hm.group(2).strip()
            tag   = ('h1','h2','h3','h4','h4','h4')[min(level-1, 5)]
            elems.append((tag, text))
            i += 1
            continue

        # ── Horizontal rule ───────────────────────────────────
        if re.match(r'^[-*_]{3,}$', stripped) and stripped:
            elems.append(('hrule',))
            i += 1
            continue

        # ── Table ─────────────────────────────────────────────
        if stripped.startswith('|') and '|' in stripped[1:]:
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            if len(table_lines) >= 2:
                headers = _parse_table_row(table_lines[0])
                rows    = []
                for tl in table_lines[2:]:          # skip separator
                    if re.match(r'^\|[-| :]+\|$', tl):
                        continue
                    row = _parse_table_row(tl)
                    if row:
                        rows.append(row)
                elems.append(('table', headers, rows))
            continue

        # ── Numbered list ─────────────────────────────────────
        nm = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if nm:
            elems.append(('numbered', int(nm.group(1)), nm.group(2)))
            i += 1
            continue

        # ── Bullet list ───────────────────────────────────────
        bm = re.match(r'^(\s*)[*\-+]\s+(.*)', line)
        if bm:
            indent = len(bm.group(1)) // 2
            elems.append(('bullet', bm.group(2), indent))
            i += 1
            continue

        # ── Empty line ────────────────────────────────────────
        if not stripped:
            i += 1
            continue

        # ── Regular paragraph ─────────────────────────────────
        para = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt
                    or nxt.startswith('#')
                    or nxt.startswith('|')
                    or nxt.startswith('>')
                    or re.match(r'^[-*_]{3,}$', nxt)
                    or re.match(r'^\d+\.\s+', nxt)
                    or re.match(r'^[*\-+]\s+', nxt)):
                break
            para.append(nxt)
            i += 1
        elems.append(('body', ' '.join(para)))

    return elems


def _parse_callout_body(callout_lines: list) -> list:
    """Parse lines inside a callout block (all start with '>')."""
    # Strip the leading '> ' prefix
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
        line = stripped[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        # Table inside callout
        if s.startswith('|') and '|' in s[1:]:
            table_lines = []
            while i < len(stripped) and stripped[i].strip().startswith('|'):
                table_lines.append(stripped[i].strip())
                i += 1
            if len(table_lines) >= 2:
                headers = _parse_table_row(table_lines[0])
                rows    = []
                for tl in table_lines[2:]:
                    if re.match(r'^\|[-| :]+\|$', tl):
                        continue
                    row = _parse_table_row(tl)
                    if row:
                        rows.append(row)
                elems.append(('table', headers, rows))
            continue

        # Heading inside callout
        hm = re.match(r'^(#{1,4})\s+(.*)', s)
        if hm:
            level = len(hm.group(1))
            tag = ('h2','h3','h4','h4')[min(level-1, 3)]
            elems.append((tag, hm.group(2).strip()))
            i += 1
            continue

        # Numbered
        nm = re.match(r'^(\d+)\.\s+(.*)', s)
        if nm:
            elems.append(('numbered', int(nm.group(1)), nm.group(2)))
            i += 1
            continue

        # Bullet
        bm = re.match(r'^[*\-+]\s+(.*)', s)
        if bm:
            elems.append(('bullet', bm.group(1), 0))
            i += 1
            continue

        # Paragraph
        elems.append(('body', s))
        i += 1

    return elems


def _parse_table_row(line: str) -> list:
    """Parse a markdown table row into a list of cell strings."""
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    cells = [c.strip() for c in line.split('|')]
    return cells


# ─────────────────────────────────────────────────────────────
# RENDER A SINGLE FILE
# ─────────────────────────────────────────────────────────────
def render_file(path: str, pdf: MchPDF):
    """Render a single answer file into the PDF (on the current page)."""
    in_cite_callout = False   # landmark articles — use small table

    for elem in parse_file(path):
        etype = elem[0]

        if etype == 'callout_start':
            ctype  = elem[1]
            ctitle = elem[2]
            in_cite_callout = (ctype == 'cite')
            # Don't print header for cite callout — just render its table
            if ctype != 'cite':
                pdf.write_callout_header(ctype, ctitle)

        elif etype == 'callout_end':
            in_cite_callout = False
            pdf.ln(LH * 0.3)

        elif etype == 'h1':
            pdf.write_h1(elem[1])
        elif etype == 'h2':
            pdf.write_h2(elem[1])
        elif etype == 'h3':
            pdf.write_h3(elem[1])
        elif etype == 'h4':
            pdf.write_h4(elem[1])

        elif etype == 'body':
            pdf.write_body(elem[1])

        elif etype == 'bullet':
            pdf.write_bullet(elem[1], level=elem[2] if len(elem) > 2 else 0)

        elif etype == 'numbered':
            pdf.write_numbered(elem[1], elem[2])

        elif etype == 'hrule':
            pdf.write_hrule()

        elif etype == 'table':
            pdf.write_table(elem[1], elem[2], small=in_cite_callout)


# ─────────────────────────────────────────────────────────────
# COLLECT FILES
# ─────────────────────────────────────────────────────────────
def collect_files() -> list:
    """
    Returns list of (section_name, [filepath, ...]) in SECTION_ORDER.
    Only sections with ≥1 answer file are included.
    """
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
# BUILD CONTENT PDF
# ─────────────────────────────────────────────────────────────
def build_content_pdf(files_by_section: list, page_offset: int = 0) -> tuple:
    """
    Render all answer files into a PDF.
    Returns (pdf_bytes, entries) where entries = [(title, section, page_num), ...]
    page_num is the number shown in the footer (= raw page + page_offset).
    """
    pdf     = MchPDF(page_offset=page_offset)
    entries = []   # (title, section, actual_page)

    for section, files in files_by_section:
        # Section divider page
        pdf.write_section_page(section)

        for filepath in files:
            pdf.add_page()
            actual_pg = pdf.page_no() + page_offset
            title     = os.path.basename(filepath).replace('.md', '')
            entries.append((title, section, actual_pg))
            try:
                render_file(filepath, pdf)
            except Exception as exc:
                print(f"    ⚠  Error in {os.path.basename(filepath)}: {exc}")
                pdf.set_font('TNR', 'I', 10)
                pdf.multi_cell(UW, LH, f"[Rendering error: {exc}]", align='L')

    buf = io.BytesIO()
    pdf.output(buf)
    return buf.getvalue(), entries


# ─────────────────────────────────────────────────────────────
# BUILD INDEX PDF
# ─────────────────────────────────────────────────────────────
def build_index_pdf(entries: list) -> bytes:
    """
    Build the index PDF with Roman-numeral page numbers.
    entries = [(title, section, page_num), ...]
    """
    pdf = MchPDF(roman_footer=True)
    pdf.add_page()

    # ── Title page ──────────────────────────────────────────
    pdf.set_y(PH / 2 - 35)
    pdf.write_hrule()
    pdf.set_font('TNR', 'B', 14)
    pdf.cell(UW, LH, 'MCh Head and Neck Surgery & Oncology', align='C',
             new_x='LMARGIN', new_y='NEXT')
    pdf.ln(LH * 0.3)
    pdf.set_font('TNR', 'B', 12)
    pdf.cell(UW, LH, 'Examination Answers — Complete Collection', align='C',
             new_x='LMARGIN', new_y='NEXT')
    pdf.ln(LH * 0.6)
    pdf.set_font('TNR', '', 10)
    n_notes    = len(entries)
    n_sections = len(set(e[1] for e in entries))
    pdf.cell(UW, LH * 0.8, f'{n_notes} notes across {n_sections} sections',
             align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.write_hrule()

    # ── Index pages ─────────────────────────────────────────
    pdf.add_page()

    pdf.set_font('TNR', 'B', 12)
    pdf.cell(UW, LH, 'INDEX', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(LH * 0.5)
    pdf.write_hrule()
    pdf.ln(LH * 0.3)

    current_section = None
    idx_lh = 10 * 0.352778 * 1.4   # compact line height for index

    for title, section, page in entries:
        # Section header in index
        if section != current_section:
            current_section = section
            if pdf.get_y() + idx_lh * 2 > PH - MB - 5:
                pdf.add_page()
            pdf.ln(idx_lh * 0.5)
            pdf.set_font('TNR', 'B', 10)
            pdf.cell(UW, idx_lh, section.upper(), new_x='LMARGIN', new_y='NEXT')
            # thin underline
            y = pdf.get_y()
            pdf.line(ML, y, ML + 40, y)
            pdf.ln(idx_lh * 0.3)

        # Entry line with dot leader
        if pdf.get_y() + idx_lh > PH - MB - 5:
            pdf.add_page()

        pdf.set_font('TNR', '', 10)
        page_str  = str(page)
        pg_w      = pdf.get_string_width(page_str) + 2
        title_w   = pdf.get_string_width(title)
        avail_w   = UW - pg_w - title_w - 4
        dot_w     = pdf.get_string_width('.')
        n_dots    = max(3, int(avail_w / dot_w)) if dot_w > 0 else 3
        dot_str   = ' ' + ('.' * n_dots) + ' '

        y0 = pdf.get_y()
        pdf.set_xy(ML, y0)
        pdf.cell(UW - pg_w, idx_lh, title + dot_str, align='L')
        pdf.set_x(PW - MR - pg_w)
        pdf.cell(pg_w, idx_lh, page_str, align='R',
                 new_x='LMARGIN', new_y='NEXT')

    buf = io.BytesIO()
    pdf.output(buf)
    return buf.getvalue()


# ─────────────────────────────────────────────────────────────
# COUNT PAGES IN A PDF BYTES OBJECT
# ─────────────────────────────────────────────────────────────
def count_pdf_pages(pdf_bytes: bytes) -> int:
    reader = PdfReader(io.BytesIO(pdf_bytes))
    return len(reader.pages)


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("MCh-HNSO → PDF Converter")
    print("=" * 50)

    # Step 1: Collect files
    files_by_section = collect_files()
    total_notes = sum(len(f) for _, f in files_by_section)
    print(f"Found {total_notes} answer files across {len(files_by_section)} sections")
    for sec, files in files_by_section:
        print(f"  {sec}: {len(files)} files")
    print()

    # Step 2: Pass 1 — render content to get raw page numbers
    print("Pass 1: measuring page layout...")
    _, entries_raw = build_content_pdf(files_by_section, page_offset=0)
    print(f"  Content spans {entries_raw[-1][2]} raw pages")

    # Step 3: Render index (with placeholder numbers) to count index pages
    print("Measuring index size...")
    index_bytes_temp = build_index_pdf(entries_raw)
    n_index_pages    = count_pdf_pages(index_bytes_temp)
    print(f"  Index = {n_index_pages} pages (Roman-numeral front matter)")

    # Step 4: Pass 2 — render content with correct page offset
    print(f"Pass 2: rendering content with page offset +{n_index_pages}...")
    content_bytes, entries_final = build_content_pdf(
        files_by_section, page_offset=n_index_pages
    )
    last_page = entries_final[-1][2]
    print(f"  Content pages: {n_index_pages + 1} – {last_page}")

    # Step 5: Build final index with correct page numbers
    print("Building final index...")
    # entries_final already has page_num = raw_page + n_index_pages
    index_bytes_final = build_index_pdf(entries_final)

    # Step 6: Merge index + content
    print("Merging index + content...")
    merger = PdfMerger()
    merger.append(io.BytesIO(index_bytes_final))
    merger.append(io.BytesIO(content_bytes))

    with open(OUTPUT_FILE, 'wb') as f:
        merger.write(f)

    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print()
    print("=" * 50)
    print(f"✓  Saved: {OUTPUT_FILE}")
    print(f"   Index: {n_index_pages} pages (Roman numerals)")
    print(f"   Content: {last_page - n_index_pages} pages")
    print(f"   Total: {last_page} pages")
    print(f"   File size: {size_mb:.1f} MB")
    print(f"   Notes: {total_notes}")
    print("=" * 50)


if __name__ == '__main__':
    main()
