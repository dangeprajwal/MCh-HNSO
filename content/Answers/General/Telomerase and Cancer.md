---
tags:
  - General
  - Molecular-Biology
  - Oncology
---

# Telomerase and Cancer

> [!question] Questions Covered
> - Write briefly on Telomerase and cancer (TMH 2018)

**Source:** Scott-Brown's Otorhinolaryngology Volume 3, Chapter 6 (Introducing Molecular Biology of HNC), Chapter 30 (Principles of Non-Surgical Treatment); Harrison - Head and Neck Cancer: A Multidisciplinary Approach, Chapter 10 ([[Answers/Oral Cavity/Chemoprevention in Oral Cancer|chemoprevention]]); Montgomery - Principles and Practice of HN Surgery, Chapter 2 (Molecular Biology), Chapter 39 (Investigational Drugs)

> [!cite] Landmark Articles
> Telomerase was discovered in 1985 by Greider and Blackburn in Tetrahymena extracts — work that contributed to the 2009 Nobel Prize in Physiology or Medicine. Kim et al. (1994) subsequently demonstrated that telomerase is reactivated in 90% of human cancers but absent in normal somatic tissues, establishing telomerase as a near-universal cancer biomarker. Patel et al. (2002) specifically demonstrated the clinical usefulness of telomerase activation and telomere length in head and neck cancer, showing activity in 78-82% of HNSCC. Vinagre et al. (2013) identified recurrent TERT promoter mutations across multiple cancer types, providing the genetic basis for telomerase reactivation. Hanahan and Weinberg (2000) identified "limitless replicative potential" — achieved through telomerase reactivation — as one of the six hallmarks of cancer.
>
> | No. | Article | Authors | Journal, Year | DOI | Key Finding |
> |-----|---------|---------|---------------|-----|-------------|
> | 1 | Identification of a specific telomere terminal transferase activity in Tetrahymena extracts | Greider CW, Blackburn EH | Cell, 1985 | [10.1016/0092-8674(85)90170-9](https://doi.org/10.1016/0092-8674(85)90170-9) | Discovery of telomerase — Nobel Prize 2009 |
> | 2 | Specific association of human telomerase activity with immortal cells and cancer | Kim NW, Piatyszek MA, Prowse KR et al. | Science, 1994 | [10.1126/science.7605428](https://doi.org/10.1126/science.7605428) | Telomerase active in 90% of cancers, absent in normal somatic tissues |
> | 3 | Clinical usefulness of telomerase activation and telomere length in head and neck cancer | Patel MM, Parekh LJ, Jha FP et al. | Head Neck, 2002 | [10.1002/hed.10169](https://doi.org/10.1002/hed.10169) | Telomerase active in 78-82% of HNSCC; higher telomere length associated with poor survival |
> | 4 | Frequency of TERT promoter mutations in human cancers | Vinagre J, Almeida A, Pópulo H et al. | Nat Commun, 2013 | [10.1038/ncomms3185](https://doi.org/10.1038/ncomms3185) | Identified recurrent TERT promoter mutations (C228T, C250T) across multiple cancer types |
> | 5 | The hallmarks of cancer | Hanahan D, Weinberg RA | Cell, 2000 | [10.1016/s0092-8674(00)81683-9](https://doi.org/10.1016/s0092-8674(00)81683-9) | Limitless replicative potential (telomerase reactivation) identified as a hallmark of cancer |

---

## Introduction

Normal somatic cells can complete a finite number of cell divisions — the **Hayflick limit** (typically 50-70 divisions) — before they permanently arrest their growth in a process of replicative senescence. As described in Scott-Brown's Chapter 30, this process occurs because cells cannot fully replicate the telomeric terminal portions of chromosomes at each cell division. Over time, telomeres shorten progressively, effectively behaving like molecular clocks that count down a normal cell's lifespan. When telomeres become critically short, they trigger [[Answers/General/Cell Cycle and Cancer|cell cycle]] arrest or [[Answers/General/Apoptosis|apoptosis]] through p53 and RB-dependent pathways — a critical tumour-suppressive mechanism.

In contrast, stem cells and malignant cells achieve immortality by maintaining the length of their telomeres. In most tumours, this involves upregulation of cellular **telomerase**, but in 10-15% of cases a different mechanism called **alternative lengthening of the telomeres (ALT)** is responsible (Scott-Brown's Chapter 30).

Montgomery's Chapter 39 describes telomerase as a potential selective anticancer target: tumours such as squamous cell carcinoma of the head and neck require telomerase to maintain telomere function, and inhibition of the enzyme can lead to apoptosis. Furthermore, because most tumour cells have very short telomeres, they are more likely to succumb to telomerase inhibition than normal cells.

---

## Part A: Telomere Biology

### Structure of Telomeres

Telomeres are specialized nucleoprotein structures at the ends of linear eukaryotic chromosomes. In humans, they consist of:
- **Tandem repeats** of the hexanucleotide sequence **TTAGGG**, extending 5-15 kilobases in length
- A 3' single-stranded G-rich overhang (150-200 nucleotides) that loops back and invades the double-stranded telomeric DNA, forming a protective **T-loop**
- The **shelterin complex** — a six-protein complex (TRF1, TRF2, POT1, TIN2, TPP1, RAP1) that caps and protects telomere ends

### Functions of Telomeres

1. **Chromosome protection:** Telomeres prevent chromosome ends from being recognized as DNA double-strand breaks, which would trigger inappropriate DNA damage responses, end-to-end fusions, and genomic instability
2. **End-replication problem:** Due to the requirement for an RNA primer in DNA replication, the lagging strand cannot be fully replicated to the very end of the chromosome — resulting in loss of 50-200 bp of telomeric DNA with each cell division
3. **Replicative clock:** Progressive telomere shortening limits the number of cell divisions, acting as an intrinsic tumour-suppressive mechanism

### The End-Replication Problem

DNA polymerase requires an RNA primer and synthesizes DNA only in the 5'→3' direction. When the terminal RNA primer is removed from the lagging strand, the resulting gap cannot be filled, leading to progressive shortening of the chromosome with each replication cycle. When telomeres shorten to a critical length (~4-6 kb), the shelterin complex can no longer form a stable protective cap, exposing chromosome ends and triggering:
- **Replicative senescence:** p53 and RB-mediated permanent cell cycle arrest
- **Crisis:** If senescence checkpoints are bypassed (e.g., by p53 mutation), continued telomere attrition leads to chromosomal end-to-end fusions, breakage-fusion-bridge cycles, massive genomic instability, and cell death

---

## Part B: Telomerase — Structure and Function

### Discovery

Telomerase was discovered in 1985 by Carol Greider and Elizabeth Blackburn in extracts from the ciliate Tetrahymena. They identified a novel activity that added tandem TTGGGG repeats to telomeric DNA sequences. This work, along with the contributions of Jack Szostak, was recognized with the **2009 Nobel Prize in Physiology or Medicine**.

### Structure

Telomerase is a specialized **ribonucleoprotein reverse transcriptase** composed of:
- **hTERT (human telomerase reverse transcriptase):** The catalytic protein subunit with reverse transcriptase activity — this is the rate-limiting component whose expression is tightly regulated
- **hTR/TERC (human telomerase RNA component):** Contains a template sequence (3'-CAAUCCCAAUC-5') complementary to the telomeric repeat, which serves as the template for telomere elongation
- **Dyskerin and associated proteins:** Required for hTR stability and telomerase complex assembly

### Mechanism of Action

1. hTR template region binds to the 3' single-stranded telomeric overhang
2. hTERT reverse transcribes the RNA template, extending the G-rich strand by one repeat (TTAGGG)
3. Translocation: telomerase repositions along the newly extended DNA
4. Repeat addition: the cycle repeats, progressively elongating the telomere
5. The complementary C-rich strand is subsequently synthesized by conventional DNA polymerase/primase

### Regulation of Telomerase Expression

hTERT transcription is the primary regulatory step. In normal somatic cells, the hTERT promoter is silenced by:
- Methylation of CpG islands
- Histone deacetylation
- Repression by transcription factors (e.g., WT1, MZF-2)

In cancer cells, hTERT is reactivated through:
- **TERT promoter mutations** (C228T, C250T) — create de novo ETS transcription factor binding sites, increasing TERT transcription
- **MYC activation** — MYC directly activates TERT transcription (Scott-Brown's Chapter 6 notes that MYC has effects on TERT, a gene implicated in immortalization of cancer cells)
- **HPV E6 oncoprotein** — degrades the NFX1 repressor of hTERT, resulting in loss of repression and consequent reduction in telomere erosion, thereby contributing to cellular immortality (Scott-Brown's Chapter 13)
- [[Answers/General/Epigenetics in Oncogenesis|epigenetics]] remodelling of the TERT promoter region

---

## Part C: Telomerase in Head and Neck Cancer

### Prevalence

As described in Montgomery's Chapter 2, telomerase is a reverse transcriptase enzyme that extends telomeric repeats and is involved in cellular immortality. Like EGFR, it is overexpressed in HNSCCs and also seems to predict advanced disease. Telomerase activity increases with late-stage carcinoma and is present at lower levels in all earlier stages. The finding of increased telomerase activity in histologically normal tissue suggests that the enzyme may be useful as a molecular marker of disease and may play a role in the molecular assessment of tumour margins.

Harrison's Chapter 10 provides specific data: using a telomerase rapid amplification protocol (TRAP) assay, Patel et al. identified telomerase activation in **78-82% of HNSCC**, **55-85% of premalignant lesions**, and **39-53% of adjacent normal-appearing tissue**. A higher telomere length was associated with poor survival. Reactivation of telomerase appears to be an early molecular alteration. Interestingly, telomerase activity in peripheral blood mononuclear cells was correlated with higher T and N stages and was an independent predictor of survival.

### TERT Promoter Mutations

Vinagre et al. (2013) identified two recurrent hotspot mutations in the TERT promoter:
- **C228T** (−124 bp from ATG start site)
- **C250T** (−146 bp from ATG start site)

Both mutations create de novo binding sites for ETS family transcription factors (GABPA/GABPB), leading to 2-4 fold increased TERT promoter activity. These mutations are found across multiple cancer types and have particular significance in:
- **Thyroid cancer:** 11% of PTC, 17% of FTC, 40-43% of ATC/PDTC — associated with aggressive behaviour, especially when co-occurring with BRAF V600E
- **HNSCC:** TERT C228T has been identified as a prognostic biomarker — associated with increased risk of tumour recurrence and death

### Role in HPV-Driven HNSCC

Scott-Brown's Chapter 13 describes a specific mechanism by which HPV contributes to telomerase activation: the E6 oncoprotein, in association with E6AP, degrades NFX1 — a transcriptional repressor of hTERT. This results in loss of hTERT repression and consequent reduction in telomere erosion, thereby contributing to the development of cellular immortality. This is one of the key mechanisms by which HPV drives the immortalization of infected keratinocytes.

---

## Part D: Telomerase as a Therapeutic Target

Montgomery's Chapter 39 describes the rationale: telomeres are tandem repeats of DNA associated with specific proteins that cap eukaryotic chromosomes and maintain the integrity of chromosome ends. Tumours require telomerase to maintain telomere function; inhibition of the enzyme can lead to apoptosis. Because most tumour cells have very short telomeres, they are more likely to succumb to telomerase inhibition than normal cells. The telomere is also involved in the repair of DNA double-strand breaks, and telomere dysfunction provokes radiosensitivity.

### Therapeutic Strategies

| Strategy | Mechanism | Example |
|----------|-----------|---------|
| Direct enzyme inhibition | Nucleoside analogues that inhibit hTERT | Imetelstat (GRN163L) — oligonucleotide complementary to hTR template |
| Immunotherapy | Telomerase peptide vaccines — hTERT is a tumour-associated antigen | GV1001, GRNVAC1 |
| G-quadruplex stabilizers | Small molecules that stabilize G-quadruplex structures in telomeric DNA, blocking telomerase access | Telomestatin, BRACO-19 |
| Gene therapy | Antisense to hTR or dominant-negative hTERT | Experimental |
| Oncolytic viruses | Telomerase promoter-driven viral replication — selective for telomerase-positive tumour cells | Telomelysin (OBP-301) |

### Telomerase as a Diagnostic Biomarker

The near-universal reactivation of telomerase in cancer (90% of all cancers, 78-82% of HNSCC) and its absence in normal somatic tissues makes it an attractive:
- **Diagnostic marker:** Detection of telomerase in brushings, fine needle aspirates, or [[Answers/General/Surgical Margins in Head and Neck Cancer|surgical margins]]
- **Margin assessment tool:** Montgomery notes telomerase may play a role in the molecular assessment of tumour margins — telomerase-positive histologically normal tissue at margins may indicate [[Answers/Oral Cavity/Field Cancerization|field cancerization]]
- **Prognostic marker:** Higher telomere length and TERT promoter mutations correlate with aggressive disease and poor survival

---

## Part E: Alternative Lengthening of Telomeres (ALT)

As noted in Scott-Brown's Chapter 30, 10-15% of tumours maintain telomere length through ALT — a telomerase-independent mechanism based on homologous recombination between telomeric sequences. ALT is characterized by:
- Heterogeneous telomere lengths (very long and very short)
- ALT-associated promyelocytic leukaemia (PML) bodies (APBs)
- Extrachromosomal telomeric DNA (C-circles)

ALT is more common in tumours of mesenchymal origin (sarcomas, gliomas) and is rare in epithelial cancers including HNSCC. However, its existence means that telomerase inhibition alone may not be sufficient to prevent all cancer cell immortalization.

---

> [!abstract] Key Points
> 1. Telomeres are TTAGGG repeat sequences that cap chromosome ends — they shorten by 50-200 bp with each cell division (end-replication problem)
> 2. When telomeres become critically short, cells undergo replicative senescence (p53/RB-mediated) or crisis — this is a fundamental tumour-suppressive mechanism
> 3. Telomerase is a ribonucleoprotein reverse transcriptase (hTERT + hTR) that extends telomeres — discovered by Greider and Blackburn (Nobel Prize 2009)
> 4. Telomerase is reactivated in 90% of human cancers but absent in normal somatic tissues (Kim et al., 1994) — making it a near-universal cancer marker
> 5. In HNSCC, telomerase is active in 78-82% of tumours and 55-85% of premalignant lesions — it is an early molecular alteration
> 6. TERT promoter mutations (C228T, C250T) create ETS binding sites that increase TERT transcription — important in thyroid cancer and HNSCC prognosis
> 7. HPV E6 activates telomerase by degrading NFX1 repressor of hTERT — a key mechanism of HPV-driven immortalization
> 8. MYC directly activates TERT transcription — linking oncogene activation with replicative immortality
> 9. Tumour cells have very short telomeres despite active telomerase — making them more vulnerable to telomerase inhibition than normal cells
> 10. The Hayflick limit (50-70 divisions) is the replicative ceiling for normal somatic cells — telomerase reactivation bypasses this limit

> [!tip] Clinical Pearls
> - Telomerase activity in histologically normal tissue at surgical margins may indicate field cancerization — a potential molecular margin assessment tool
> - In thyroid cancer, co-existing BRAF V600E + TERT promoter mutation identifies the most aggressive phenotype with the highest recurrence — always test for both
> - Imetelstat (GRN163L) is the most advanced telomerase inhibitor in clinical trials — it works by binding the hTR template region and blocking telomere extension
> - Telomerase-based immunotherapy exploits the fact that hTERT peptides are presented on tumour cell MHC — making telomerase both a therapeutic target and a vaccine antigen
> - The ALT pathway (10-15% of cancers) provides a telomerase-independent escape mechanism — this is why telomerase inhibition alone may not cure all cancers
> - Remember the timeline: Greider & Blackburn (1985) → Kim et al. (1994) → Hallmarks (2000) → TERT promoter mutations (2013) → Nobel Prize was in 2009

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/General/index|General Topics]]
>
> **Related Notes:**
> - [[Answers/General/Apoptosis|Apoptosis]] — cellular immortalisation and death pathways
> - [[Answers/General/Cell Cycle and Cancer|Cell Cycle and Cancer]] — immortalisation and proliferation
> - [[Answers/General/Epigenetics in Oncogenesis|Epigenetics in Oncogenesis]] — related topic
> - [[Answers/General/Viral Carcinogenesis|Viral Carcinogenesis]] — related topic
>
> **See Also:**
> - [[Answers/Oral Cavity/Field Cancerization|Field Cancerization]] — telomerase activation in premalignant fields
> - [[Answers/General/Autophagy in Head and Neck Cancer|Autophagy in Head and Neck Cancer]] — related topic
