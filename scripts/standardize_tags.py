#!/usr/bin/env python3
"""Standardize tags across all answer files to a canonical taxonomy."""

import os
import re

ANSWERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'Answers')

# Map folder names to Tier 1 tags
FOLDER_TO_TIER1 = {
    'General': 'General',
    'Oral Cavity': 'Oral-Cavity',
    'Oropharynx': 'Oropharynx',
    'Larynx': 'Larynx',
    'Neck': 'Neck',
    'Hypopharynx': 'Hypopharynx',
    'Skull Base': 'Skull-Base',
    'Salivary Gland': 'Salivary-Gland',
    'Radiotherapy and Chemotherapy': 'Radiotherapy',
    'Reconstruction': 'Reconstruction',
    'Research Methodology': 'Evidence-Based',
    'Thyroid': 'Thyroid',
}

# Canonical Tier 2 tags
TIER2_TAGS = {
    'Molecular-Biology', 'Pathology', 'Surgery', 'Oncology', 'Reconstruction',
    'Radiotherapy', 'Systemic-Therapy', 'Diagnostics', 'Evidence-Based',
    'Rehabilitation', 'Staging', 'Complications', 'Epidemiology', 'Premalignant',
    'Supportive-Care', 'Anatomy',
}

# Map every existing tag to its canonical form
TAG_MAP = {
    # Tier 1 normalization
    'general': 'General',
    'General': 'General',
    'Oral-Cavity': 'Oral-Cavity',
    'oral-cavity': 'Oral-Cavity',
    'Oropharynx': 'Oropharynx',
    'oropharynx': 'Oropharynx',
    'Larynx': 'Larynx',
    'larynx': 'Larynx',
    'Neck': 'Neck',
    'neck': 'Neck',
    'Hypopharynx': 'Hypopharynx',
    'Skull-Base': 'Skull-Base',
    'skull-base': 'Skull-Base',
    'Salivary-Gland': 'Salivary-Gland',
    'salivary': 'Salivary-Gland',
    'Nasopharynx': 'Nasopharynx',
    'nasopharynx': 'Nasopharynx',
    'Paranasal-Sinuses': 'Paranasal-Sinuses',
    'sinonasal': 'Paranasal-Sinuses',

    # Molecular-Biology merges
    'molecular-biology': 'Molecular-Biology',
    'Molecular-Biology': 'Molecular-Biology',
    'cell-biology': 'Molecular-Biology',
    'basic-science': 'Molecular-Biology',
    'Basic-Science': 'Molecular-Biology',
    'genomics': 'Molecular-Biology',
    'Cytogenetics': 'Molecular-Biology',
    'FISH': 'Molecular-Biology',
    'Proteomics': 'Molecular-Biology',
    'EGFR': 'Molecular-Biology',
    'Biomarkers': 'Molecular-Biology',

    # Pathology merges
    'Pathology': 'Pathology',
    'pathology': 'Pathology',
    'Histology': 'Pathology',
    'Prognostic-Factors': 'Pathology',
    'Micrometastasis': 'Pathology',
    'Lymph-Node-Metastasis': 'Pathology',

    # Surgery merges
    'surgery': 'Surgery',
    'Surgical-Technique': 'Surgery',
    'Surgical-Oncology': 'Surgery',
    'Transoral-Surgery': 'Surgery',
    'Maxillectomy': 'Surgery',
    'Neck-Dissection': 'Surgery',
    'Neck-Management': 'Surgery',
    'Margins': 'Surgery',
    'Sentinel-Node': 'Surgery',
    'Free-Flaps': 'Reconstruction',
    'Adjuvant-Therapy': 'Surgery',
    'Neoadjuvant': 'Surgery',
    'Mandible': 'Surgery',

    # Oncology
    'oncology': 'Oncology',
    'Rare-Tumours': 'Oncology',
    'Oncologic-Emergencies': 'Oncology',
    'Carotid-Blowout': 'Oncology',

    # Reconstruction
    'Reconstruction': 'Reconstruction',
    'reconstruction': 'Reconstruction',
    'Prosthetics': 'Reconstruction',
    'Dental-Oncology': 'Reconstruction',

    # Radiotherapy
    'Radiotherapy': 'Radiotherapy',
    'radiotherapy': 'Radiotherapy',
    'radiation': 'Radiotherapy',
    'Mucositis': 'Radiotherapy',
    'Photobiomodulation': 'Radiotherapy',

    # Systemic-Therapy
    'Chemotherapy': 'Systemic-Therapy',
    'chemotherapy': 'Systemic-Therapy',
    'Targeted-Therapy': 'Systemic-Therapy',
    'targeted-therapy': 'Systemic-Therapy',
    'Immunotherapy': 'Systemic-Therapy',
    'immunotherapy': 'Systemic-Therapy',
    'Pharmacology': 'Systemic-Therapy',

    # Diagnostics
    'diagnostics': 'Diagnostics',
    'Diagnostics': 'Diagnostics',
    'Radiology': 'Diagnostics',
    'radiology': 'Diagnostics',
    'Imaging': 'Diagnostics',
    'imaging': 'Diagnostics',
    'PET-CT': 'Diagnostics',
    'diagnosis': 'Diagnostics',
    'Technology': 'Diagnostics',
    'Laser': 'Diagnostics',
    'Clinical-Assessment': 'Diagnostics',
    'Surveillance': 'Diagnostics',
    'Response-Assessment': 'Diagnostics',
    'interventional-radiology': 'Diagnostics',

    # Evidence-Based
    'Evidence-Based': 'Evidence-Based',
    'evidence-based-medicine': 'Evidence-Based',
    'Clinical-Trials': 'Evidence-Based',
    'clinical-trials': 'Evidence-Based',
    'Research-Methodology': 'Evidence-Based',
    'research-methodology': 'Evidence-Based',
    'AJCC': 'Staging',

    # Rehabilitation
    'Rehabilitation': 'Rehabilitation',
    'rehabilitation': 'Rehabilitation',
    'Swallowing': 'Rehabilitation',
    'Functional-Outcomes': 'Rehabilitation',

    # Staging
    'Staging': 'Staging',
    'staging': 'Staging',

    # Complications
    'Complications': 'Complications',
    'complications': 'Complications',
    'perioperative': 'Complications',
    'electrolyte': 'Complications',
    'vascular': 'Complications',
    'Airway-Management': 'Complications',
    'airway': 'Complications',
    'facial-nerve': 'Complications',

    # Epidemiology
    'epidemiology': 'Epidemiology',
    'Carcinogenesis': 'Epidemiology',
    'Viral-Carcinogenesis': 'Epidemiology',
    'Virology': 'Epidemiology',
    'tobacco': 'Epidemiology',
    'aetiology': 'Epidemiology',
    'HIV-AIDS': 'Epidemiology',
    'Kaposi-Sarcoma': 'Epidemiology',
    'Immunosuppression': 'Epidemiology',
    'Smoking-Cessation': 'Epidemiology',

    # Premalignant
    'Premalignant': 'Premalignant',
    'Mucosal-Disease': 'Premalignant',
    'Chemoprevention': 'Premalignant',
    'Prevention': 'Premalignant',
    'prevention': 'Premalignant',
    'Screening': 'Premalignant',
    'Public-Health': 'Premalignant',
    'Lips': 'Premalignant',

    # Supportive-Care
    'Supportive-Care': 'Supportive-Care',
    'Palliative-Care': 'Supportive-Care',
    'palliative-care': 'Supportive-Care',
    'survivorship': 'Supportive-Care',
    'Quality-of-Life': 'Supportive-Care',
    'quality-of-life': 'Supportive-Care',
    'End-of-Life': 'Supportive-Care',

    # Anatomy
    'Anatomy': 'Anatomy',

    # Misc that map to broader categories
    'treatment': 'Oncology',
    'treatment-planning': 'Oncology',
    'multidisciplinary': 'Oncology',
}

TIER1_TAGS = set(FOLDER_TO_TIER1.values())


def get_tier1_for_folder(folder_name):
    return FOLDER_TO_TIER1.get(folder_name, 'General')


def standardize_file(filepath, folder_name):
    with open(filepath) as f:
        content = f.read()

    # Parse frontmatter
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return False, "no frontmatter"

    fm = m.group(1)
    rest = content[m.end():]

    # Extract existing tags
    old_tags = []
    for line in fm.split('\n'):
        stripped = line.strip()
        if stripped.startswith('- ') and not stripped.startswith('- **') and not stripped.startswith('- [['):
            tag = stripped[2:].strip()
            if len(tag) < 30 and not any(c in tag for c in '()|>=<*'):
                old_tags.append(tag)

    if not old_tags:
        return False, "no tags found"

    # Map to canonical tags
    new_tags = set()
    unmapped = []
    for tag in old_tags:
        if tag in TAG_MAP:
            new_tags.add(TAG_MAP[tag])
        else:
            unmapped.append(tag)

    # Ensure correct Tier 1 tag
    expected_tier1 = get_tier1_for_folder(folder_name)
    # Remove any wrong Tier 1 tags
    new_tags -= TIER1_TAGS
    new_tags.add(expected_tier1)

    # Separate into Tier 1 and Tier 2
    tier1 = [t for t in new_tags if t in TIER1_TAGS]
    tier2 = sorted([t for t in new_tags if t in TIER2_TAGS])

    # Ensure at least 1 Tier 2 tag
    if not tier2:
        tier2 = ['Oncology']

    # Cap at 3 Tier 2 tags (keep the most specific ones)
    if len(tier2) > 3:
        tier2 = tier2[:3]

    # Build new frontmatter
    tag_lines = '\n'.join(f'  - {t}' for t in tier1 + tier2)
    new_fm = f'tags:\n{tag_lines}'

    # Reconstruct file
    new_content = f'---\n{new_fm}\n---{rest}'

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True, f"{old_tags} → {tier1 + tier2}"

    return False, "no change"


def main():
    changed = 0
    total = 0
    for folder_name in os.listdir(ANSWERS_DIR):
        folder_path = os.path.join(ANSWERS_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        for fname in sorted(os.listdir(folder_path)):
            if not fname.endswith('.md') or fname == 'index.md':
                continue
            filepath = os.path.join(folder_path, fname)
            total += 1
            did_change, info = standardize_file(filepath, folder_name)
            if did_change:
                changed += 1
                print(f"  ✓ {folder_name}/{fname}: {info}")
            # else:
            #     print(f"  - {folder_name}/{fname}: {info}")

    print(f"\nDone: {changed}/{total} files updated")


if __name__ == '__main__':
    main()
