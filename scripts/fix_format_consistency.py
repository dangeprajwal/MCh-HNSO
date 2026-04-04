#!/usr/bin/env python3
"""Fix format inconsistencies: question callout headings and landmark table formats."""

import os
import re

ANSWERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'Answers')

STANDARD_QUESTION_HEADING = 'Questions Covered'


def fix_question_heading(content, filename):
    """Ensure [!question] heading is 'Questions Covered'."""
    # Match [!question] followed by anything that's NOT "Questions Covered"
    pattern = r'(\[!question\])\s+(?!Questions Covered)(.+)'
    m = re.search(pattern, content)
    if m:
        old_heading = m.group(2).strip()
        content = content[:m.start()] + '[!question] Questions Covered' + content[m.end():]
        return content, old_heading
    return content, None


def convert_6col_to_4col(content, filename):
    """Convert 6-column landmark tables to 4-column format.

    Old format: | No. | Article | Authors | Journal, Year | DOI | Key Finding |
    OR:         | #   | Title   | Authors | Journal, Year | DOI | Key Finding |
    New format: | Study | Journal | Year | DOI |
    """
    # Find the cite callout section
    cite_match = re.search(r'(> \[!cite\] Landmark Articles\n(?:>.*\n)*)', content)
    if not cite_match:
        return content, False

    cite_block = cite_match.group(1)

    # Check if it's already in 4-column format
    if '| Study |' in cite_block:
        return content, False

    # Check if it has a 6-column table
    # Pattern: | No. | or | # |
    if not (re.search(r'> \| (?:No\.|#)', cite_block)):
        return content, False

    # Parse the table rows (skip header and separator)
    lines = cite_block.split('\n')
    new_lines = []
    table_started = False
    header_replaced = False

    for line in lines:
        # Skip empty lines at end
        if not line.strip():
            new_lines.append(line)
            continue

        # Check if this is a table header line
        if not header_replaced and re.match(r'> \| (?:No\.|#)\s*\|', line):
            new_lines.append('> | Study | Journal | Year | DOI |')
            header_replaced = True
            table_started = True
            continue

        # Check if this is a separator line
        if table_started and re.match(r'> \|[-| ]+\|', line):
            new_lines.append('> |---|---|---|---|')
            continue

        # Check if this is a data row (starts with > | number or > | Author)
        if table_started and re.match(r'> \|', line):
            cells = [c.strip() for c in line.split('|')]
            # Remove empty first/last from split
            cells = [c for c in cells if c and c != '>']

            if len(cells) >= 5:
                # Old format: No, Article, Authors, Journal+Year, DOI, Key Finding
                # Extract what we need
                article = cells[1].strip() if len(cells) > 1 else ''
                authors = cells[2].strip() if len(cells) > 2 else ''
                journal_year = cells[3].strip() if len(cells) > 3 else ''
                doi = cells[4].strip() if len(cells) > 4 else ''

                # Parse journal and year from "Journal, Year" or "Journal Year"
                jy_match = re.match(r'(.+?),?\s*(\d{4})', journal_year)
                if jy_match:
                    journal = jy_match.group(1).strip().rstrip(',')
                    year = jy_match.group(2)
                else:
                    journal = journal_year
                    year = ''

                # Build study name from authors + article
                # If authors is like "First Author et al." use that
                # Combined: "Author — Article Title"
                if authors and article:
                    # Shorten: take first author surname
                    author_short = authors.split(' et al')[0].split(',')[0].strip()
                    study = f'{author_short} — {article}'
                elif article:
                    study = article
                else:
                    study = authors

                # Truncate study if too long
                if len(study) > 60:
                    study = study[:57] + '...'

                new_lines.append(f'> | {study} | {journal} | {year} | {doi} |')
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_cite = '\n'.join(new_lines)
    content = content[:cite_match.start()] + new_cite + content[cite_match.end():]
    return content, True


def main():
    q_fixed = 0
    t_fixed = 0
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
                content = f.read()

            original = content

            # Fix question heading
            content, old_q = fix_question_heading(content, fname)
            if old_q:
                q_fixed += 1
                print(f'  Q: {folder_name}/{fname}: "{old_q}" → "Questions Covered"')

            # Fix table format
            content, did_fix_table = convert_6col_to_4col(content, fname)
            if did_fix_table:
                t_fixed += 1
                print(f'  T: {folder_name}/{fname}: 6-col → 4-col table')

            if content != original:
                with open(filepath, 'w') as f:
                    f.write(content)

    print(f'\nDone: {q_fixed} question headings fixed, {t_fixed} tables converted ({total} files)')


if __name__ == '__main__':
    main()
