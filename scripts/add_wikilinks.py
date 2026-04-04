#!/usr/bin/env python3
"""Add wikilinks between related answer files based on concept mentions."""

import os
import re

ANSWERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'Answers')

# Concept-to-file index: maps search terms to (file_path, display_text)
# Key = lowercase search term, Value = (path_without_extension, display_text)
CONCEPT_INDEX = {
    # Molecular Biology fundamentals
    'apoptosis': ('Answers/General/Apoptosis', 'apoptosis'),
    'apoptotic': ('Answers/General/Apoptosis', 'apoptosis'),
    'programmed cell death': ('Answers/General/Apoptosis', 'programmed cell death'),
    'autophagy': ('Answers/General/Autophagy in Head and Neck Cancer', 'autophagy'),
    'autophagic': ('Answers/General/Autophagy in Head and Neck Cancer', 'autophagy'),
    'cell cycle': ('Answers/General/Cell Cycle and Cancer', 'cell cycle'),
    'cyclin-dependent kinase': ('Answers/General/Cell Cycle and Cancer', 'cyclin-dependent kinases'),
    'tumour suppressor gene': ('Answers/General/Tumour Suppressor Genes', 'tumour suppressor genes'),
    'tumor suppressor gene': ('Answers/General/Tumour Suppressor Genes', 'tumour suppressor genes'),
    'telomerase': ('Answers/General/Telomerase and Cancer', 'telomerase'),
    'telomere': ('Answers/General/Telomerase and Cancer', 'telomerase'),
    'pi3k': ('Answers/General/PI3-Kinase Pathway', 'PI3K pathway'),
    'pi3-kinase': ('Answers/General/PI3-Kinase Pathway', 'PI3-kinase pathway'),
    'pi3k/akt': ('Answers/General/PI3-Kinase Pathway', 'PI3K/AKT pathway'),
    'mtor': ('Answers/General/PI3-Kinase Pathway', 'PI3K/mTOR pathway'),
    'tumour angiogenesis': ('Answers/General/Tumour Angiogenesis', 'tumour angiogenesis'),
    'angiogenesis': ('Answers/General/Tumour Angiogenesis', 'angiogenesis'),
    'vegf': ('Answers/General/Tumour Angiogenesis', 'VEGF'),
    'epigenetic': ('Answers/General/Epigenetics in Oncogenesis', 'epigenetics'),
    'dna methylation': ('Answers/General/Epigenetics in Oncogenesis', 'DNA methylation'),
    'histone modification': ('Answers/General/Epigenetics in Oncogenesis', 'histone modifications'),
    'microrna': ('Answers/General/MicroRNAs in Oral Cancer', 'microRNAs'),
    'mirna': ('Answers/General/MicroRNAs in Oral Cancer', 'miRNA'),
    'mir-21': ('Answers/General/MicroRNAs in Oral Cancer', 'miR-21'),

    # Epidemiology and carcinogenesis
    'field cancerization': ('Answers/Oral Cavity/Field Cancerization', 'field cancerization'),
    'field cancerisation': ('Answers/Oral Cavity/Field Cancerization', 'field cancerization'),
    'field change': ('Answers/Oral Cavity/Field Cancerization', 'field cancerization'),
    'tobacco carcinogenesis': ('Answers/General/Tobacco Carcinogenesis', 'tobacco carcinogenesis'),
    'viral carcinogenesis': ('Answers/General/Viral Carcinogenesis', 'viral carcinogenesis'),
    'human papillomavirus': ('Answers/General/HPV in Oral and Oropharyngeal Cancer', 'HPV'),
    'hpv-positive': ('Answers/General/HPV in Oral and Oropharyngeal Cancer', 'HPV-positive'),
    'hpv-16': ('Answers/General/HPV in Oral and Oropharyngeal Cancer', 'HPV-16'),
    'ebv': ('Answers/General/EBV Testing in Head and Neck Cancer', 'EBV'),
    'epstein-barr': ('Answers/General/EBV Testing in Head and Neck Cancer', 'Epstein-Barr virus'),
    'genetic susceptibility': ('Answers/General/Genetic Susceptibility to Oral Cancer', 'genetic susceptibility'),

    # Diagnostics
    'narrow band imaging': ('Answers/General/Narrow Band Imaging', 'narrow band imaging'),
    'nbi': ('Answers/General/Narrow Band Imaging', 'NBI'),
    'pet-ct': ('Answers/General/PET-CT in Head and Neck Cancer', 'PET-CT'),
    'pet/ct': ('Answers/General/PET-CT in Head and Neck Cancer', 'PET/CT'),
    'diffusion weighted': ('Answers/General/Diffusion Weighted MRI', 'diffusion-weighted MRI'),
    'dwi': ('Answers/General/Diffusion Weighted MRI', 'DWI'),
    'fluorescence-guided': ('Answers/Oral Cavity/Surgical Margins and Fluorescence-Guided Surgery', 'fluorescence-guided surgery'),
    'frozen section': ('Answers/General/Frozen Section in Surgical Margins', 'frozen section'),
    'fish': ('Answers/General/FISH in Head and Neck Cancer', 'FISH'),
    'pcr': ('Answers/General/PCR and Microarray Analysis', 'PCR'),
    'microarray': ('Answers/General/PCR and Microarray Analysis', 'microarray'),
    'next generation sequencing': ('Answers/General/Next Generation Sequencing in HNC', 'next-generation sequencing'),
    'ngs': ('Answers/General/Next Generation Sequencing in HNC', 'NGS'),
    'photodynamic therapy': ('Answers/General/Photodynamic Therapy', 'photodynamic therapy'),
    'pdt': ('Answers/General/Photodynamic Therapy', 'PDT'),
    'salivary biomarker': ('Answers/Oral Cavity/Salivary Biomarkers in Oral Cancer', 'salivary biomarkers'),
    'oral microbiome': ('Answers/Oral Cavity/Oral Microbiome and Cancer', 'oral microbiome'),

    # Pathology and staging
    'perineural invasion': ('Answers/General/Perineural Invasion', 'perineural invasion'),
    'pni': ('Answers/General/Perineural Invasion', 'PNI'),
    'extranodal extension': ('Answers/General/Extranodal Extension', 'extranodal extension'),
    'extracapsular spread': ('Answers/General/Extranodal Extension', 'extranodal extension'),
    'ene': ('Answers/General/Extranodal Extension', 'ENE'),
    'depth of invasion': ('Answers/Oral Cavity/Depth of Invasion in Oral Cancer', 'depth of invasion'),
    'doi': ('Answers/Oral Cavity/Depth of Invasion in Oral Cancer', 'DOI'),
    'isolated tumour cell': ('Answers/General/Isolated Tumour Cells', 'isolated tumour cells'),
    'itc': ('Answers/General/Isolated Tumour Cells', 'ITCs'),
    'histological grading': ('Answers/General/Histological Grading of SCC', 'histological grading'),
    'histological risk assessment': ('Answers/Oral Cavity/Histological Risk Assessment in Oral Cancer', 'histological risk assessment'),
    'brandwein-gensler': ('Answers/Oral Cavity/Histological Risk Assessment in Oral Cancer', 'Brandwein-Gensler risk model'),
    'basaloid squamous': ('Answers/Oral Cavity/Basaloid Squamous Cell Carcinoma', 'basaloid SCC'),
    'ajcc 8th': ('Answers/Oral Cavity/AJCC 8th Edition Oral Cavity Staging', 'AJCC 8th edition staging'),
    'ajcc staging': ('Answers/Oral Cavity/AJCC 8th Edition Oral Cavity Staging', 'AJCC staging'),

    # Surgical concepts
    'sentinel node biopsy': ('Answers/Oral Cavity/Sentinel Node Biopsy in Oral Cancer', 'sentinel node biopsy'),
    'sentinel lymph node': ('Answers/Oral Cavity/Sentinel Node Biopsy in Oral Cancer', 'sentinel lymph node biopsy'),
    'snb': ('Answers/Oral Cavity/Sentinel Node Biopsy in Oral Cancer', 'SNB'),
    'elective neck dissection': ('Answers/Oral Cavity/Node Negative Neck in Oral Cancer', 'elective neck dissection'),
    'node-negative neck': ('Answers/Oral Cavity/Node Negative Neck in Oral Cancer', 'node-negative neck'),
    'clinically n0': ('Answers/Oral Cavity/Node Negative Neck in Oral Cancer', 'clinically N0 neck'),
    'marginal mandibulectomy': ('Answers/Oral Cavity/Marginal Mandibulectomy', 'marginal mandibulectomy'),
    'segmental mandibulectomy': ('Answers/Oral Cavity/Types of Mandibulectomy', 'segmental mandibulectomy'),
    'types of mandibulectomy': ('Answers/Oral Cavity/Types of Mandibulectomy', 'types of mandibulectomy'),
    'mandibulotomy': ('Answers/Oral Cavity/Access Mandibulotomy', 'access mandibulotomy'),
    'access osteotomy': ('Answers/Oral Cavity/Access Mandibulotomy', 'access mandibulotomy'),
    'surgical margin': ('Answers/General/Surgical Margins in Head and Neck Cancer', 'surgical margins'),
    'floor of mouth': ('Answers/Oral Cavity/Floor of Mouth Carcinoma', 'floor of mouth carcinoma'),

    # Reconstruction
    'tongue reconstruction': ('Answers/Oral Cavity/Tongue Reconstruction Algorithm', 'tongue reconstruction'),
    'obturator': ('Answers/Oral Cavity/Obturator vs Flap Reconstruction', 'obturator reconstruction'),
    '3d model': ('Answers/Oral Cavity/3D Models in Mandibular Reconstruction', '3D models'),
    'virtual surgical planning': ('Answers/Oral Cavity/3D Models in Mandibular Reconstruction', 'virtual surgical planning'),
    'vsp': ('Answers/Oral Cavity/3D Models in Mandibular Reconstruction', 'VSP'),
    'regional flap': ('Answers/Oral Cavity/Regional Flaps in Oral Reconstruction', 'regional flaps'),
    'pectoralis major': ('Answers/Oral Cavity/Regional Flaps in Oral Reconstruction', 'pectoralis major flap'),
    'pmmf': ('Answers/Oral Cavity/Regional Flaps in Oral Reconstruction', 'PMMF'),
    'submental flap': ('Answers/Oral Cavity/Regional Flaps in Oral Reconstruction', 'submental flap'),
    'dental implant': ('Answers/Oral Cavity/Dental Implants after Mandibular Reconstruction', 'dental implants'),
    'osseointegrat': ('Answers/General/Osseointegrated Implants', 'osseointegrated implants'),
    'masseteric nerve': ('Answers/General/Masseteric Nerve Transfer', 'masseteric nerve transfer'),

    # Premalignant
    'leukoplakia': ('Answers/Oral Cavity/Oral Leukoplakia Management', 'leukoplakia'),
    'oral leukoplakia': ('Answers/Oral Cavity/Oral Leukoplakia Management', 'oral leukoplakia'),
    'erythroplakia': ('Answers/Oral Cavity/Oral Leukoplakia Management', 'erythroplakia'),
    'lichen planus': ('Answers/Oral Cavity/Oral Lichen Planus', 'oral lichen planus'),
    'olp': ('Answers/Oral Cavity/Oral Lichen Planus', 'OLP'),
    'submucous fibrosis': ('Answers/Oral Cavity/Oral Submucous Fibrosis', 'oral submucous fibrosis'),
    'osmf': ('Answers/Oral Cavity/Oral Submucous Fibrosis', 'OSMF'),
    'chemoprevention': ('Answers/Oral Cavity/Chemoprevention in Oral Cancer', 'chemoprevention'),
    'oral cancer screening': ('Answers/Oral Cavity/Oral Cancer Screening', 'oral cancer screening'),
    'melanoma': ('Answers/Oral Cavity/Melanoma of the Oral Cavity', 'oral melanoma'),
    'ameloblastoma': ('Answers/Oral Cavity/Ameloblastoma of Mandible', 'ameloblastoma'),
    'minor salivary gland': ('Answers/Oral Cavity/Minor Salivary Gland Tumours of the Oral Cavity', 'minor salivary gland tumours'),

    # Radiotherapy and complications
    'osteoradionecrosis': ('Answers/Oral Cavity/Osteoradionecrosis of the Mandible', 'osteoradionecrosis'),
    'orn': ('Answers/Oral Cavity/Osteoradionecrosis of the Mandible', 'ORN'),
    'adjuvant radiation': ('Answers/Oral Cavity/Adjuvant Radiation Therapy in Oral Cancer', 'adjuvant radiation'),
    'adjuvant rt': ('Answers/Oral Cavity/Adjuvant Radiation Therapy in Oral Cancer', 'adjuvant RT'),
    'hyperbaric oxygen': ('Answers/General/Hyperbaric Oxygen Therapy', 'hyperbaric oxygen therapy'),
    'hbo': ('Answers/General/Hyperbaric Oxygen Therapy', 'HBO'),
    'xerostomia': ('Answers/General/Xerostomia Management', 'xerostomia'),
    'trismus': ('Answers/General/Trismus Prevention', 'trismus'),
    'lymphedema': ('Answers/General/Post-treatment Lymphedema', 'lymphedema'),
    'lymphoedema': ('Answers/General/Post-treatment Lymphedema', 'lymphoedema'),

    # Rehabilitation and supportive care
    'swallowing': ('Answers/General/Swallowing Assessment in Head and Neck Cancer', 'swallowing assessment'),
    'dysphagia': ('Answers/General/Swallowing Assessment in Head and Neck Cancer', 'dysphagia'),
    'speech rehabilitation': ('Answers/General/Speech Rehabilitation after Laryngectomy', 'speech rehabilitation'),
    'tracheoesophageal puncture': ('Answers/General/Speech Rehabilitation after Laryngectomy', 'TEP'),
    'quality of life': ('Answers/General/Quality of Life in Head and Neck Cancer', 'quality of life'),
    'nutritional assessment': ('Answers/General/Nutritional Assessment and PEG Feeding', 'nutritional assessment'),
    'peg feeding': ('Answers/General/Nutritional Assessment and PEG Feeding', 'PEG feeding'),
    'chyle leak': ('Answers/General/Chyle Leak Management', 'chyle leak'),
    'nicotine replacement': ('Answers/General/Nicotine Replacement Therapy', 'nicotine replacement therapy'),

    # Evidence-based
    'non-inferiority': ('Answers/General/Non-Inferiority Clinical Trials', 'non-inferiority trials'),
    'recist': ('Answers/General/RECIST Criteria', 'RECIST criteria'),
    'performance scale': ('Answers/General/Performance Scales and RECIST', 'performance scales'),
    'who performance': ('Answers/General/WHO Performance Scale', 'WHO performance scale'),
    'balloon occlusion': ('Answers/General/Balloon Occlusion Test', 'balloon occlusion test'),
    'paraneoplastic': ('Answers/General/Paraneoplastic Syndrome', 'paraneoplastic syndrome'),
    'monoclonal antibod': ('Answers/General/Monoclonal Antibodies in Head and Neck Cancer', 'monoclonal antibodies'),
    'cetuximab': ('Answers/General/Monoclonal Antibodies in Head and Neck Cancer', 'cetuximab'),
    'neoadjuvant chemotherapy': ('Answers/Oral Cavity/Neoadjuvant Chemotherapy in Oral Cancer', 'neoadjuvant chemotherapy'),

    # Anatomy
    'infratemporal fossa': ('Answers/Oral Cavity/Infratemporal Fossa Spread', 'infratemporal fossa'),
    'masticator space': ('Answers/Oral Cavity/Masticator Space', 'masticator space'),
    'pterygopalatine fossa': ('Answers/Oral Cavity/Pterygopalatine Fossa', 'pterygopalatine fossa'),
    'referred otalgia': ('Answers/Oral Cavity/Referred Otalgia in Oral Cancer', 'referred otalgia'),

    # Specific cancers
    'jaw osteosarcoma': ('Answers/Oral Cavity/Jaw Osteosarcoma', 'jaw osteosarcoma'),
    'osteosarcoma of the jaw': ('Answers/Oral Cavity/Jaw Osteosarcoma', 'jaw osteosarcoma'),
}

# Abbreviations that need word-boundary matching (short terms)
SHORT_TERMS = {'nbi', 'snb', 'pni', 'ene', 'doi', 'hbo', 'orn', 'olp', 'pdt',
               'ebv', 'dwi', 'ngs', 'vsp', 'itc', 'pcr', 'osmf', 'pmmf', 'fish'}


def get_file_identity(filepath):
    """Return the Answers/Category/Name path for a file."""
    # e.g. /path/to/content/Answers/General/Apoptosis.md -> Answers/General/Apoptosis
    parts = filepath.replace('\\', '/').split('/')
    try:
        idx = parts.index('Answers')
        return '/'.join(parts[idx:]).replace('.md', '')
    except ValueError:
        return None


def already_linked(content, target_path):
    """Check if content already contains a wikilink to the target."""
    return f'[[{target_path}' in content


def add_wikilinks_to_file(filepath):
    """Add wikilinks to a single file. Returns (changes_made, links_added)."""
    with open(filepath) as f:
        content = f.read()

    file_identity = get_file_identity(filepath)
    if not file_identity:
        return 0, []

    # Split frontmatter and body
    m = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if not m:
        return 0, []

    frontmatter = m.group(1)
    body = content[len(frontmatter):]

    linked_targets = set()
    links_added = []

    # Sort concepts by length (longest first) to avoid partial matches
    sorted_concepts = sorted(CONCEPT_INDEX.keys(), key=len, reverse=True)

    for concept in sorted_concepts:
        target_path, display = CONCEPT_INDEX[concept]

        # Don't link to self
        if target_path == file_identity:
            continue

        # Don't add duplicate links to same target
        if target_path in linked_targets:
            continue

        # Check if already linked
        if already_linked(body, target_path):
            linked_targets.add(target_path)
            continue

        # Build regex pattern
        if concept.lower() in SHORT_TERMS:
            # Short abbreviations: require word boundaries, case-sensitive
            pattern = r'(?<!\[)(?<!\|)\b(' + re.escape(concept.upper()) + r')\b(?!\])'
            replacement_text = concept.upper()
        else:
            # Normal terms: case-insensitive, word boundaries
            pattern = r'(?<!\[)(?<!\|)\b(' + re.escape(concept) + r'(?:s|es|ed|ing)?)\b(?!\])'
            replacement_text = None  # Will use matched text

        # Only match in body (not in callout headers, frontmatter, or existing links)
        # Find first match
        match = re.search(pattern, body, re.IGNORECASE if concept.lower() not in SHORT_TERMS else 0)
        if match:
            original = match.group(1)
            wikilink = f'[[{target_path}|{display}]]'

            # Replace only the first occurrence
            body = body[:match.start()] + wikilink + body[match.end():]
            linked_targets.add(target_path)
            links_added.append(f'{original} → {display}')

    if links_added:
        new_content = frontmatter + body
        with open(filepath, 'w') as f:
            f.write(new_content)

    return len(links_added), links_added


def main():
    total_links = 0
    files_changed = 0
    total_files = 0

    for folder_name in sorted(os.listdir(ANSWERS_DIR)):
        folder_path = os.path.join(ANSWERS_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        for fname in sorted(os.listdir(folder_path)):
            if not fname.endswith('.md') or fname == 'index.md':
                continue
            filepath = os.path.join(folder_path, fname)
            total_files += 1
            count, links = add_wikilinks_to_file(filepath)
            if count > 0:
                files_changed += 1
                total_links += count
                print(f"  ✓ {folder_name}/{fname}: +{count} links")
                for link in links:
                    print(f"      {link}")

    print(f"\nDone: {total_links} links added across {files_changed}/{total_files} files")


if __name__ == '__main__':
    main()
