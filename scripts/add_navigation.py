#!/usr/bin/env python3
"""Add collapsible compass navigation callouts to all answer files."""

import os
import re
from collections import defaultdict

ANSWERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'Answers')

# Folder display names for parent links
FOLDER_NAMES = {
    'General': 'General Topics',
    'Oral Cavity': 'Oral Cavity',
}


def get_file_info(filepath):
    """Extract file identity, tags, and outbound wikilinks."""
    with open(filepath) as f:
        content = f.read()

    folder = os.path.basename(os.path.dirname(filepath))
    name = os.path.splitext(os.path.basename(filepath))[0]
    identity = f'Answers/{folder}/{name}'

    # Extract tags
    tags = set()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            line = line.strip()
            if line.startswith('- ') and len(line) < 40:
                tags.add(line[2:].strip())

    # Extract outbound wikilinks
    links = set()
    for link_match in re.finditer(r'\[\[(Answers/[^\]|]+)', content):
        target = link_match.group(1)
        if target != identity:
            links.add(target)

    return {
        'identity': identity,
        'folder': folder,
        'name': name,
        'tags': tags,
        'links': links,
        'filepath': filepath,
        'content': content,
    }


def compute_relatedness(file_a, file_b):
    """Score how related two files are (higher = more related)."""
    score = 0

    # Shared tags (Tier 2 only, excluding folder tags)
    folder_tags = {'General', 'Oral-Cavity', 'Oropharynx', 'Larynx', 'Neck',
                   'Hypopharynx', 'Skull-Base', 'Salivary-Gland'}
    shared_tags = (file_a['tags'] - folder_tags) & (file_b['tags'] - folder_tags)
    score += len(shared_tags) * 3

    # Mutual linking (A links to B AND B links to A)
    a_links_b = file_b['identity'] in file_a['links']
    b_links_a = file_a['identity'] in file_b['links']
    if a_links_b and b_links_a:
        score += 5
    elif a_links_b or b_links_a:
        score += 2

    # Same folder bonus
    if file_a['folder'] == file_b['folder']:
        score += 1

    return score


def get_connection_phrase(file_a_name, file_b_name):
    """Generate a brief connection phrase based on file names."""
    # Use a curated map for common connections
    PHRASES = {
        # Molecular biology cluster
        ('Apoptosis', 'Cell Cycle and Cancer'): 'checkpoint regulation and apoptotic triggers',
        ('Apoptosis', 'Tumour Suppressor Genes'): 'p53-mediated apoptosis',
        ('Apoptosis', 'PI3-Kinase Pathway'): 'AKT survival signalling vs apoptosis',
        ('Apoptosis', 'Autophagy in Head and Neck Cancer'): 'alternative programmed cell death',
        ('Apoptosis', 'Telomerase and Cancer'): 'cellular immortalisation and death pathways',
        ('Cell Cycle and Cancer', 'Tumour Suppressor Genes'): 'Rb/p53 checkpoint control',
        ('Cell Cycle and Cancer', 'PI3-Kinase Pathway'): 'growth factor signalling and proliferation',
        ('Cell Cycle and Cancer', 'Epigenetics in Oncogenesis'): 'epigenetic silencing of cell cycle regulators',
        ('Tumour Suppressor Genes', 'PI3-Kinase Pathway'): 'PTEN as PI3K pathway regulator',
        ('Tumour Suppressor Genes', 'Epigenetics in Oncogenesis'): 'promoter methylation silencing TSGs',
        ('Tumour Suppressor Genes', 'Field Cancerization'): 'clonal expansion of p53-mutant fields',
        ('Tumour Angiogenesis', 'PI3-Kinase Pathway'): 'VEGF regulation via PI3K/AKT',
        ('Tumour Angiogenesis', 'Monoclonal Antibodies in Head and Neck Cancer'): 'bevacizumab anti-VEGF therapy',
        ('Telomerase and Cancer', 'Cell Cycle and Cancer'): 'immortalisation and proliferation',
        ('Telomerase and Cancer', 'Field Cancerization'): 'telomerase activation in premalignant fields',
        ('MicroRNAs in Oral Cancer', 'Epigenetics in Oncogenesis'): 'miRNA as epigenetic regulators',
        ('MicroRNAs in Oral Cancer', 'Salivary Biomarkers in Oral Cancer'): 'salivary miRNA as diagnostic markers',
        ('Genetic Susceptibility to Oral Cancer', 'Tobacco Carcinogenesis'): 'CYP/GST polymorphisms and carcinogen metabolism',
        ('HPV in Oral and Oropharyngeal Cancer', 'Viral Carcinogenesis'): 'E6/E7 oncoproteins and viral oncogenesis',
        ('HPV in Oral and Oropharyngeal Cancer', 'Non-Inferiority Clinical Trials'): 'De-ESCALaTE and RTOG 1016 trial design',

        # Epidemiology cluster
        ('Tobacco Carcinogenesis', 'Field Cancerization'): 'tobacco-induced field changes',
        ('Tobacco Carcinogenesis', 'Epidemiology of HNC in India'): 'smokeless tobacco and Indian epidemiology',
        ('Tobacco Carcinogenesis', 'Oral Submucous Fibrosis'): 'areca nut carcinogenesis',
        ('Epidemiology of HNC in India', 'Oral Submucous Fibrosis'): 'betel quid and OSMF prevalence',
        ('Epidemiology of HNC in India', 'Oral Cancer Screening'): 'population screening in high-prevalence regions',
        ('Viral Carcinogenesis', 'EBV Testing in Head and Neck Cancer'): 'EBV latent infection and NPC',

        # Premalignant cluster
        ('Field Cancerization', 'Chemoprevention in Oral Cancer'): 'targeting premalignant fields',
        ('Field Cancerization', 'Oral Leukoplakia Management'): 'leukoplakia as field change marker',
        ('Field Cancerization', 'Surgical Margins in Head and Neck Cancer'): 'molecularly altered margins',
        ('Oral Leukoplakia Management', 'Oral Lichen Planus'): 'premalignant mucosal conditions',
        ('Oral Leukoplakia Management', 'Oral Submucous Fibrosis'): 'potentially malignant disorders',
        ('Oral Leukoplakia Management', 'Chemoprevention in Oral Cancer'): 'chemoprevention of leukoplakia progression',
        ('Oral Lichen Planus', 'Lichen Planus and Oral Cancer'): 'malignant transformation risk',
        ('Oral Submucous Fibrosis', 'Oral Leukoplakia Management'): 'potentially malignant disorders',
        ('Oral Cancer Screening', 'Salivary Biomarkers in Oral Cancer'): 'screening biomarker development',

        # Surgery cluster
        ('Surgical Margins in Head and Neck Cancer', 'Frozen Section in Surgical Margins'): 'intraoperative margin assessment',
        ('Surgical Margins in Head and Neck Cancer', 'Surgical Margins and Fluorescence-Guided Surgery'): 'margin assessment techniques',
        ('Surgical Margins in Head and Neck Cancer', 'Adjuvant Radiation Therapy in Oral Cancer'): 'positive margins and adjuvant RT indication',
        ('Depth of Invasion in Oral Cancer', 'AJCC 8th Edition Oral Cavity Staging'): 'DOI-based T-staging',
        ('Depth of Invasion in Oral Cancer', 'Node Negative Neck in Oral Cancer'): 'DOI threshold for elective neck dissection',
        ('Depth of Invasion in Oral Cancer', 'Sentinel Node Biopsy in Oral Cancer'): 'DOI-guided nodal management',
        ('Node Negative Neck in Oral Cancer', 'Sentinel Node Biopsy in Oral Cancer'): 'alternatives for N0 neck management',
        ('Extranodal Extension', 'Adjuvant Radiation Therapy in Oral Cancer'): 'ENE as indication for adjuvant chemoRT',
        ('Extranodal Extension', 'Perineural Invasion'): 'adverse pathological features',
        ('Perineural Invasion', 'Adjuvant Radiation Therapy in Oral Cancer'): 'PNI as adjuvant RT indication',
        ('Perineural Invasion', 'Histological Risk Assessment in Oral Cancer'): 'PNI in risk stratification',

        # Mandible cluster
        ('Marginal Mandibulectomy', 'Types of Mandibulectomy'): 'mandibulectomy classification',
        ('Marginal Mandibulectomy', 'Imaging in Oral Cancer'): 'mandibular invasion assessment',
        ('Types of Mandibulectomy', '3D Models in Mandibular Reconstruction'): 'VSP-guided mandibular reconstruction',
        ('Types of Mandibulectomy', 'Dental Implants after Mandibular Reconstruction'): 'implant rehabilitation after mandibulectomy',
        ('Ameloblastoma of Mandible', 'Types of Mandibulectomy'): 'mandibulectomy for odontogenic tumours',
        ('Ameloblastoma of Mandible', 'Jaw Osteosarcoma'): 'mandibular tumour management',
        ('Access Mandibulotomy', 'Infratemporal Fossa Spread'): 'surgical access for deep tumours',
        ('Floor of Mouth Carcinoma', 'Marginal Mandibulectomy'): 'mandible management in FOM cancer',

        # Reconstruction cluster
        ('Tongue Reconstruction Algorithm', 'Regional Flaps in Oral Reconstruction'): 'flap options for tongue defects',
        ('Regional Flaps in Oral Reconstruction', 'Obturator vs Flap Reconstruction'): 'reconstruction options comparison',
        ('Dental Implants after Mandibular Reconstruction', 'Osseointegrated Implants'): 'implant rehabilitation principles',
        ('Dental Implants after Mandibular Reconstruction', '3D Models in Mandibular Reconstruction'): 'VSP for implant-guided reconstruction',

        # Rehabilitation cluster
        ('Swallowing Assessment in Head and Neck Cancer', 'Swallowing Assessment and Rehabilitation'): 'swallowing evaluation and therapy',
        ('Swallowing Assessment in Head and Neck Cancer', 'Quality of Life in Head and Neck Cancer'): 'functional outcomes measurement',
        ('Quality of Life in Head and Neck Cancer', 'Speech Rehabilitation after Laryngectomy'): 'rehabilitation and QoL outcomes',
        ('Xerostomia Management', 'Osteoradionecrosis of the Mandible'): 'late radiation complications',
        ('Xerostomia Management', 'Trismus Prevention'): 'post-RT functional rehabilitation',
        ('Trismus Prevention', 'Osteoradionecrosis of the Mandible'): 'radiation-induced mandibular complications',
        ('Hyperbaric Oxygen Therapy', 'Osteoradionecrosis of the Mandible'): 'HBO for ORN management',
        ('Infrared Therapy in Head and Neck Cancer', 'Xerostomia Management'): 'photobiomodulation for xerostomia',

        # Complications cluster
        ('Chyle Leak Management', 'Postoperative Fever Day 3'): 'postoperative complications',
        ('Postoperative Anuria', 'Postoperative Hyponatremia'): 'perioperative fluid/electrolyte issues',
        ('Postoperative Hyponatremia', 'Paraneoplastic Syndrome'): 'SIADH differential diagnosis',
        ('Oncologic Emergencies and End of Life', 'Cancer Pain Management'): 'palliative and emergency management',

        # Diagnostics cluster
        ('PET-CT in Head and Neck Cancer', 'Diffusion Weighted MRI'): 'advanced imaging modalities',
        ('PET-CT in Head and Neck Cancer', 'Imaging in Oral Cancer'): 'staging and surveillance imaging',
        ('Narrow Band Imaging', 'Photodynamic Therapy'): 'optical diagnostic and therapeutic techniques',
        ('FISH in Head and Neck Cancer', 'PCR and Microarray Analysis'): 'molecular diagnostic techniques',
        ('PCR and Microarray Analysis', 'Next Generation Sequencing in HNC'): 'genomic profiling methods',
        ('Molecular Markers and Proteomics', 'Proteomics and Molecular Markers'): 'molecular biomarker discovery',

        # Anatomy cluster
        ('Infratemporal Fossa Spread', 'Masticator Space'): 'deep space tumour extension',
        ('Infratemporal Fossa Spread', 'Pterygopalatine Fossa'): 'skull base anatomy and spread pathways',
        ('Masticator Space', 'Pterygopalatine Fossa'): 'parasellar space anatomy',
        ('Referred Otalgia in Oral Cancer', 'Floor of Mouth Carcinoma'): 'cranial nerve involvement patterns',

        # Evidence-based cluster
        ('Non-Inferiority Clinical Trials', 'Phase III Clinical Trials'): 'clinical trial design principles',
        ('Performance Scales and RECIST', 'RECIST Criteria'): 'response evaluation criteria',
        ('Performance Scales and RECIST', 'WHO Performance Scale'): 'performance status assessment',

        # Treatment cluster
        ('Monoclonal Antibodies in Head and Neck Cancer', 'Neoadjuvant Chemotherapy in Oral Cancer'): 'systemic therapy approaches',
        ('Adjuvant Radiation Therapy in Oral Cancer', 'Osteoradionecrosis of the Mandible'): 'radiation benefits vs late complications',
    }

    # Check both orderings
    key1 = (file_a_name, file_b_name)
    key2 = (file_b_name, file_a_name)
    if key1 in PHRASES:
        return PHRASES[key1]
    if key2 in PHRASES:
        return PHRASES[key2]

    # Generic fallback based on shared characteristics
    return 'related topic'


def build_navigation(all_files):
    """Build navigation callouts for all files."""
    results = {}

    for file_info in all_files:
        identity = file_info['identity']
        name = file_info['name']
        folder = file_info['folder']

        # Score all other files
        scored = []
        for other in all_files:
            if other['identity'] == identity:
                continue
            score = compute_relatedness(file_info, other)
            if score > 0:
                scored.append((score, other))

        # Sort by score descending, then by name
        scored.sort(key=lambda x: (-x[0], x[1]['name']))

        # Take top 4 as Related Notes
        related = scored[:4]
        # Take next 1-2 as See Also
        see_also = scored[4:6] if len(scored) > 4 else []

        # Build callout
        parent_name = FOLDER_NAMES.get(folder, folder)
        lines = [
            f'> [!compass]- Navigate',
            f'> **Parent:** [[Answers/{folder}/index|{parent_name}]]',
            f'>',
        ]

        if related:
            lines.append('> **Related Notes:**')
            for score, other in related:
                phrase = get_connection_phrase(name, other['name'])
                lines.append(f"> - [[{other['identity']}|{other['name']}]] — {phrase}")

        if see_also:
            lines.append('>')
            lines.append('> **See Also:**')
            for score, other in see_also:
                phrase = get_connection_phrase(name, other['name'])
                lines.append(f"> - [[{other['identity']}|{other['name']}]] — {phrase}")

        results[identity] = '\n'.join(lines)

    return results


def append_callout(filepath, callout_text):
    """Append navigation callout to the end of a file."""
    with open(filepath) as f:
        content = f.read()

    # Remove any existing compass callout
    content = re.sub(r'\n*> \[!compass\][-+]? Navigate\n(?:>.*\n)*', '', content)

    # Ensure file ends with newline, then add callout
    content = content.rstrip('\n') + '\n\n' + callout_text + '\n'

    with open(filepath, 'w') as f:
        f.write(content)


def main():
    # Collect all file info
    all_files = []
    for folder_name in sorted(os.listdir(ANSWERS_DIR)):
        folder_path = os.path.join(ANSWERS_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        for fname in sorted(os.listdir(folder_path)):
            if not fname.endswith('.md') or fname == 'index.md':
                continue
            filepath = os.path.join(folder_path, fname)
            all_files.append(get_file_info(filepath))

    print(f"Analysed {len(all_files)} files")

    # Build navigation
    nav = build_navigation(all_files)

    # Apply
    for file_info in all_files:
        identity = file_info['identity']
        callout = nav[identity]
        append_callout(file_info['filepath'], callout)
        related_count = callout.count('[[Answers/')
        print(f"  ✓ {file_info['folder']}/{file_info['name']}: {related_count} nav links")

    print(f"\nDone: navigation callouts added to {len(all_files)} files")


if __name__ == '__main__':
    main()
