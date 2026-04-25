---
tags:
  - General
  - Molecular-Biology
---

# Next Generation Sequencing in Head and Neck Cancers

> [!question] Questions Covered
> - What is the role of Next Gen Sequencing in Head Neck Cancers? (PGI 2021)

**Source:** Scott-Brown's Otorhinolaryngology Volume 3, Chapter 6 (Molecular Biology of Head and Neck Cancer); Harrison - Head and Neck Cancer: A Multidisciplinary Approach, Chapter 7 (Molecular Biology), Chapter 12 ([[Answers/Oral Cavity/Chemoprevention in Oral Cancer|chemoprevention]])

> [!cite] Landmark Articles
> Next-generation sequencing (NGS) has revolutionized our understanding of head and neck squamous cell carcinoma (HNSCC) at the molecular level. In 2011, two simultaneous publications in *Science* provided the first comprehensive exome-level view of HNSCC: Agrawal et al. (2011) sequenced 32 HNSCC tumours and identified inactivating mutations in NOTCH1 — a novel finding implicating loss of squamous differentiation control. Stransky et al. (2011) sequenced 74 tumour-normal pairs and confirmed NOTCH1 as one of the most commonly mutated genes, along with novel mutations in genes regulating squamous differentiation (IRF6, TP63). Both studies are referenced in Harrison's Chapter 7. The landmark TCGA study (Cancer Genome Atlas Network, 2015) then provided the definitive genomic landscape of HNSCC based on 279 tumours — identifying four molecular subtypes, confirming distinct HPV+ and HPV- genomic profiles, and revealing novel therapeutic targets. Leemans et al. (2018) published the comprehensive review translating these genomic findings into clinical relevance for head and neck oncologists. India et al. (2020) extended NGS findings to the Indian subcontinent, revealing unique genomic alterations in betel-associated oral cancers.
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Agrawal N — Exome sequencing of HNSCC reveals inactivating mutations in NOTCH1 | Science | 2011 | [10.1126/science.1206923](https://doi.org/10.1126/science.1206923) |
> | Stransky N — The mutational landscape of head and neck squamous cell carcinoma | Science | 2011 | [10.1126/science.1208130](https://doi.org/10.1126/science.1208130) |
> | Cancer Genome Atlas Network — Comprehensive genomic characterization of head and neck squamous cell carcinomas | Nature | 2015 | [10.1038/nature14129](https://doi.org/10.1038/nature14129) |
> | Leemans CR — The biology and management of head and neck cancer | Nature | 2018 | [10.1038/s41586-019-1689-y](https://doi.org/10.1038/s41586-019-1689-y) |
> | Leemans CR — Biology of head and neck cancer: key targets and therapies | N Engl J Med | 2011 | [10.1038/nrc2982](https://doi.org/10.1038/nrc2982) |

---

## Introduction

As Scott-Brown's Chapter 6 states, our understanding of head and neck cancer has been **revolutionized by so-called next-generation sequencing of whole genomes and exomes**. These technologies enable a high depth of sequence coverage, which is particularly important for studies of cancer since the tumour biopsy may contain a mixture of normal and tumour tissues, and moreover, due to the heterogeneity of cancers, there may be many clones with some common and some distinct mutations.

Harrison's Chapter 7 notes that for the first time, **comprehensive exome sequencing data are available to catalogue** the genetic changes in HNSCC, with the full impact of these alterations on tumorigenesis, prognosis, and therapeutics yet to be realized.

---

## Part A: NGS Technology

### What is Next-Generation Sequencing?

NGS (also called high-throughput or second-generation sequencing) refers to technologies that allow massively parallel sequencing of millions of DNA fragments simultaneously. This contrasts with traditional Sanger sequencing, which sequences one fragment at a time.

Scott-Brown's Chapter 6 explains: the two most commonly used technologies, **Illumina/Solexa** and **SOLiD**, have been used to generate enormous quantities of data. Both approaches enable a high depth of sequence coverage.

### Types of NGS Approaches

| Approach | What It Sequences | Scale | Cost | Clinical Application |
|----------|------------------|-------|------|---------------------|
| **Whole genome sequencing (WGS)** | Entire genome (~3 billion base pairs) | Comprehensive | Highest | Research; structural variants, non-coding mutations |
| **Whole exome sequencing (WES)** | All protein-coding regions (~1-2% of genome, ~20,000 genes) | Broad | Moderate | Research and clinical; identifies most actionable mutations |
| **Targeted panel sequencing** | Selected cancer-related genes (50-500 genes) | Focused | Lowest | Clinical; FDA-approved panels (FoundationOne, MSK-IMPACT) |
| **RNA-Seq** | mRNA transcriptome | Expression profiling | Moderate | Gene expression, fusion genes, HPV status |

Scott-Brown's notes that in addition to high depth of coverage sequence analysis, it is now possible to examine the **transcriptome** (the mRNA products of the genes being actively transcribed) in greater detail and more quantitatively using **RNA-Seq**. The application of **RNAscope** is beginning to impact on the analysis of fixed tissue biopsy sections, particularly for detection of HPV gene expression.

### Key Concepts

| Term | Definition |
|------|-----------|
| **Somatic mutation** | Mutation acquired during life in tumour cells (not inherited) |
| **Germline mutation** | Inherited mutation present in all cells |
| **Mutational burden** | Total number of somatic mutations per megabase of DNA |
| **Driver mutation** | Mutation that confers growth advantage and drives cancer |
| **Passenger mutation** | Mutation that does not contribute to cancer development |
| **Actionable mutation** | Mutation for which a targeted therapy exists |
| **Copy number alteration (CNA)** | Amplification or deletion of DNA segments |
| **Tumour mutational burden (TMB)** | Biomarker for immunotherapy response |

---

## Part B: Genomic Landscape of HNSCC

### The TCGA Study (Cancer Genome Atlas Network, 2015)

The definitive genomic characterization of HNSCC profiled **279 tumours** using multiple platforms (WES, RNA-Seq, [[Answers/General/Epigenetics in Oncogenesis|DNA methylation]], copy number, protein expression). Scott-Brown's Chapter 6 specifically references the TCGA consortium as providing the most extensive recent studies of the head and neck cancer genome.

### Most Frequently Mutated Genes in HNSCC

| Gene | Frequency | Function | HPV Status |
|------|-----------|----------|-----------|
| **TP53** | 72% (HPV-), <5% (HPV+) | Tumour suppressor; cell cycle/[[Answers/General/Apoptosis|apoptosis]] | HPV- predominantly |
| **CDKN2A (p16)** | 58% (inactivation in HPV-) | Cell cycle inhibitor; CDK4/6 inhibition | HPV- (silenced); HPV+ (overexpressed as surrogate marker) |
| **PIK3CA** | 21% overall (56% HPV+) | [[Answers/General/PI3-Kinase Pathway|PI3K pathway]] catalytic subunit; growth signalling | Both; especially HPV+ |
| **NOTCH1** | 17% | Squamous differentiation | HPV- predominantly |
| **FAT1** | 12% | Wnt pathway regulation | HPV- |
| **CASP8** | 8% | Apoptosis (caspase-8) | HPV- (oral cavity subgroup) |
| **HRAS** | 6% | RAS/MAPK signalling | HPV- (oral cavity) |
| **NSD1** | 10% | Histone methyltransferase | HPV- (novel TCGA finding) |
| **TRAF3** | 22% (HPV+) | NF-κB regulation | HPV+ |

Scott-Brown's Chapter 6 confirms: these studies have confirmed the findings of many older studies that had correctly identified that the **most commonly mutated gene in head and neck cancers was the TP53 tumour suppressor**. In addition, however, these studies identified several genes as harbouring mutations in head and neck cancers that had not been identified by earlier studies.

### [[Answers/General/HPV in Oral and Oropharyngeal Cancer|HPV-positive]] vs HPV-Negative: Two Distinct Genomic Diseases

Scott-Brown's Chapter 6 emphasizes that examining the pathways affected by mutations, there are **two clearly different patterns of genetic alterations** depending on whether the disease has been promoted by HPV or not.

| Feature | HPV-Negative | HPV-Positive |
|---------|-------------|-------------|
| **Key driver** | TP53 mutation + carcinogen exposure | HPV E6/E7 viral oncoproteins |
| **TP53** | Near-universal loss-of-function mutations | Wild-type (degraded by E6) |
| **CDKN2A** | Frequent deletion/methylation | Intact (p16 overexpressed) |
| **PIK3CA** | Amplification (3q26) | Helical domain mutations |
| **Novel genes** | NSD1, FAT1, CASP8, HRAS | TRAF3, E2F1 amplification |
| **Copy number alterations** | Frequent (high CNA burden) | Fewer CNAs |
| **Mutational signature** | Smoking-related (C>A transversions) | APOBEC-related (C>T/G) |
| **TMB** | Moderate-high | Variable |
| **Prognosis** | Poorer | Favourable |

### Four Molecular Subtypes (TCGA mRNA Expression Profiling)

| Subtype | Characteristics | Enriched Mutations |
|---------|-----------------|-------------------|
| **Classical** | High EGFR/SOX2 expression; heavy smokers | TP53, CDKN2A, 3q amplification |
| **Basal** | Resembles basal cells; aggressive | TP53, CASP8, HRAS |
| **Mesenchymal** | EMT signature; immune infiltration | Variable |
| **Atypical** | HPV-related; best prognosis | PIK3CA, TRAF3 |

---

## Part C: Clinical Applications of NGS in HNC

### 1. Diagnostic Applications

| Application | NGS Role | Clinical Impact |
|------------|---------|----------------|
| **HPV status determination** | RNA-Seq for viral transcript detection | Staging ([[Answers/Oral Cavity/AJCC 8th Edition Oral Cavity Staging|AJCC 8th edition staging]] edition separates HPV+ oropharynx) |
| **Tumour of unknown primary** | Gene expression profiling + mutational signature | Identifies site of origin when conventional methods fail |
| **Histological subtyping** | Characteristic mutational profiles | Distinguishes SCC subtypes, adenoid cystic, NUT carcinoma |
| **Hereditary cancer screening** | Germline sequencing (BRCA, TP53, etc.) | Identifies familial cancer syndromes (Li-Fraumeni, Fanconi anaemia) |

### 2. Prognostic Applications

- **TP53 mutation type:** Disruptive TP53 mutations (truncating/hotspot) carry worse prognosis than non-disruptive mutations
- **HPV genomic integration** patterns detected by WGS may predict outcomes
- **Tumour mutational burden (TMB):** High TMB associated with better immunotherapy response
- **Molecular subtype classification** may guide prognosis beyond TNM staging

### 3. Therapeutic Applications (Precision Medicine)

Harrison's Chapter 12 references a "precision medicine" approach using molecular analyses to guide treatment selection.

| Genomic Target | Frequency in HNSCC | Targeted Therapy | Status |
|---------------|-------------------|-----------------|--------|
| **EGFR overexpression** | >90% | [[Answers/General/Monoclonal Antibodies in Head and Neck Cancer|cetuximab]], afatinib | FDA-approved (cetuximab) |
| **PIK3CA mutation/amplification** | 21% overall | Alpelisib, copanlisib | Clinical trials |
| **FGFR amplification** | 10-15% | Erdafitinib, futibatinib | Clinical trials |
| **CDKN2A loss / CDK amplification** | >50% | Palbociclib, ribociclib | Clinical trials |
| **NOTCH1 loss** | 17% | Gamma-secretase inhibitors | Early trials |
| **HRAS mutation** | 6% (oral cavity) | Tipifarnib (farnesyltransferase inhibitor) | Phase II positive results |
| **High TMB / MSI-H** | ~5% | Pembrolizumab | FDA-approved (tumour-agnostic) |
| **PD-L1 expression** | Variable | Pembrolizumab, nivolumab | FDA-approved |
| **NSD1 mutation** | 10% | Epigenetic modulators | Preclinical |

Scott-Brown's Chapter 6 notes the use of the TCGA consortium data to identify alterations in **EGFR, FGFR, PIK3CA, and [[Answers/General/Cell Cycle and Cancer|cyclin-dependent kinases]]** as candidate targets for therapeutic intervention in most HNSCCs.

### 4. Liquid Biopsy and ctDNA

- Circulating tumour DNA (ctDNA) can be detected using NGS panels
- Applications: minimal residual disease detection, treatment response monitoring, early recurrence detection
- Particularly valuable in post-treatment surveillance of HNSCC

---

## Part D: Epigenomics and Beyond

Scott-Brown's Chapter 6 discusses the role of **epigenetic alterations** identified through NGS-based methods:

- The TCGA network found mutations in histone methyltransferases (NSD1, KMT2D/MLL2) in a significant proportion of HNSCCs
- DNA methylation profiling reveals distinct patterns in HPV+ vs HPV- tumours
- Promoter hypermethylation of TSGs (CDKN2A, DAPK, MGMT) is common
- Epigenetic modifications contribute to **50-60% of all head and neck cancers** through altered gene regulation

---

## Part E: Challenges and Future Directions

### Current Challenges

1. **Tumour heterogeneity:** Intratumoral genomic heterogeneity means a single biopsy may not represent the entire tumour
2. **Actionability gap:** Only a minority of mutations have approved targeted therapies
3. **Cost and access:** NGS remains expensive and unavailable in many centres
4. **Bioinformatics:** Enormous data volumes require specialized computational analysis
5. **Turnaround time:** Clinical decision-making may not wait for sequencing results
6. **Variants of uncertain significance (VUS):** Many identified variants have no known clinical significance

### Future Directions

- **Single-cell sequencing:** Resolves intratumoral heterogeneity at individual cell level
- **Spatial transcriptomics:** Maps gene expression to tissue architecture
- **Multi-omic integration:** Combining genomics, epigenomics, transcriptomics, and proteomics
- **AI-driven analysis:** Machine learning for variant interpretation and treatment prediction
- **Clinical trial matching:** NGS-guided enrolment in biomarker-selected trials (basket/umbrella trials)

---

> [!abstract] Key Points
> 1. NGS (next-generation sequencing) enables massively parallel sequencing of millions of DNA fragments — WGS, WES, targeted panels, and RNA-Seq
> 2. The TCGA study (2015) is the landmark: 279 HNSCC tumours profiled → identified 4 molecular subtypes (classical, basal, mesenchymal, atypical) and confirmed HPV+/HPV- as distinct genomic diseases
> 3. TP53 is the most commonly mutated gene in HPV-negative HNSCC (72%); NOTCH1 (17%) was a novel discovery by NGS (Agrawal et al., 2011)
> 4. HPV+ tumours: PIK3CA helical domain mutations, TRAF3 loss, E2F1 amplification; HPV- tumours: TP53, CDKN2A loss, high copy number alterations
> 5. Therapeutic targets identified by NGS: PIK3CA, FGFR, CDK4/6, HRAS, NSD1, high TMB (for immunotherapy)
> 6. Tipifarnib for HRAS-mutant oral cavity SCC and pembrolizumab for high-TMB/MSI-H tumours are NGS-guided therapies entering clinical practice
> 7. Liquid biopsy (ctDNA) using NGS panels enables minimal residual disease detection and treatment monitoring
> 8. Epigenomic alterations (NSD1, KMT2D mutations; promoter methylation) contribute to 50-60% of HNSCCs
> 9. Key limitations: tumour heterogeneity, actionability gap, cost, and bioinformatics requirements
> 10. The two 2011 *Science* papers (Agrawal; Stransky) and the 2015 TCGA *Nature* paper form the foundational genomic literature for HNSCC

> [!tip] Clinical Pearls
> - For the PGI exam, know the THREE landmark NGS papers: Agrawal 2011, Stransky 2011, TCGA 2015 — and their key findings (NOTCH1, squamous differentiation genes, 4 subtypes)
> - The most clinically relevant NGS application TODAY is **HPV testing** and **PD-L1/TMB** for immunotherapy selection — these are already routine
> - HPV+ and HPV- HNSCC are **molecularly distinct diseases** — this is perhaps the single most important insight from NGS
> - The oral cavity HRAS/CASP8/NOTCH1 subgroup with low CNA burden has the best prognosis — a clinically relevant molecular subtype
> - Targeted panel sequencing (FoundationOne, MSK-IMPACT) is the most practical clinical NGS approach — it covers actionable genes at lower cost than WES/WGS
> - Scott-Brown's key quote for exams: "our understanding of head and neck cancer has been revolutionized by so-called next-generation sequencing"

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/General/index|General Topics]]
>
> **Related Notes:**
> - [[Answers/General/Apoptosis|Apoptosis]] — related topic
> - [[Answers/General/Cell Cycle and Cancer|Cell Cycle and Cancer]] — related topic
> - [[Answers/General/Epigenetics in Oncogenesis|Epigenetics in Oncogenesis]] — related topic
> - [[Answers/General/Molecular Markers and Proteomics|Molecular Markers and Proteomics]] — related topic
>
> **See Also:**
> - [[Answers/General/PI3-Kinase Pathway|PI3-Kinase Pathway]] — related topic
> - [[Answers/General/Autophagy in Head and Neck Cancer|Autophagy in Head and Neck Cancer]] — related topic
