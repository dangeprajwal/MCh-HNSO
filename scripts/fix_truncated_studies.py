#!/usr/bin/env python3
"""Fix truncated study names in 4-column landmark tables.

Recovers original article titles from git history (pre-conversion commit)
and rebuilds the 4-column tables with full study names.
"""

import os
import re
import subprocess

ANSWERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'Answers')
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
PRE_COMMIT = '8c5b508'


def get_original(rel_path):
    """Get file content from pre-conversion commit."""
    try:
        r = subprocess.run(
            ['git', 'show', f'{PRE_COMMIT}:{rel_path}'],
            capture_output=True, text=True, cwd=REPO_ROOT, timeout=5
        )
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def parse_6col(content):
    """Extract rows from a 6-column landmark table."""
    m = re.search(r'> \[!cite\] Landmark Articles\n((?:>.*\n)*)', content)
    if not m:
        return None
    block = m.group(0)
    if not re.search(r'> \| (?:No\.|#)', block):
        return None

    rows = []
    in_table = False
    for line in block.split('\n'):
        if re.match(r'> \| (?:No\.|#)\s*\|', line):
            in_table = True
            continue
        if in_table and re.match(r'> \|[-| ]+\|', line):
            continue
        if in_table and re.match(r'> \|', line):
            raw = line.lstrip('> ')
            cells = [c.strip() for c in raw.split('|')]
            cells = [c for c in cells if c]
            if len(cells) >= 5:
                rows.append({
                    'article': cells[1].strip(),
                    'authors': cells[2].strip(),
                    'jy': cells[3].strip(),
                    'doi': cells[4].strip(),
                })
    return rows if rows else None


def build_4col(rows):
    """Build 4-column table lines from parsed rows."""
    lines = ['> | Study | Journal | Year | DOI |', '> |---|---|---|---|']
    for row in rows:
        author = row['authors'].split(' et al')[0].split(',')[0].strip()
        article = row['article']
        study = f'{author} — {article}' if author and article else (article or author)

        jy_match = re.match(r'(.+?),?\s*(\d{4})', row['jy'])
        if jy_match:
            journal = jy_match.group(1).strip().rstrip(',')
            year = jy_match.group(2)
        else:
            journal = row['jy']
            year = ''

        lines.append(f'> | {study} | {journal} | {year} | {row["doi"]} |')
    return '\n'.join(lines)


def main():
    fixed = 0
    total = 0

    for folder_name in sorted(os.listdir(ANSWERS_DIR)):
        folder_path = os.path.join(ANSWERS_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        for fname in sorted(os.listdir(folder_path)):
            if not fname.endswith('.md') or fname == 'index.md':
                continue

            filepath = os.path.join(folder_path, fname)
            total += 1

            with open(filepath) as f:
                current = f.read()

            # Only fix files with truncated entries in cite block
            cite_match = re.search(r'(> \[!cite\] Landmark Articles\n(?:>.*\n)*)', current)
            if not cite_match:
                continue
            if '... |' not in cite_match.group(1):
                continue

            # Get original from git
            rel_path = os.path.relpath(filepath, REPO_ROOT)
            original = get_original(rel_path)
            if not original:
                print(f'  SKIP (no git history): {folder_name}/{fname}')
                continue

            rows = parse_6col(original)
            if not rows:
                print(f'  SKIP (no 6-col table): {folder_name}/{fname}')
                continue

            # Build new table
            new_table = build_4col(rows)

            # Replace the old 4-col table within the cite block
            cite_block = cite_match.group(1)
            # Find where the table starts (| Study |) in the cite block
            table_start = cite_block.find('> | Study |')
            if table_start == -1:
                print(f'  SKIP (no 4-col header): {folder_name}/{fname}')
                continue

            # Everything before the table in cite block
            pre_table = cite_block[:table_start]
            # Replace
            new_cite = pre_table + new_table + '\n'
            current = current[:cite_match.start()] + new_cite + current[cite_match.end():]

            with open(filepath, 'w') as f:
                f.write(current)

            fixed += 1
            print(f'  Fixed: {folder_name}/{fname}')

    print(f'\nDone: {fixed}/{total} files fixed')


if __name__ == '__main__':
    main()
