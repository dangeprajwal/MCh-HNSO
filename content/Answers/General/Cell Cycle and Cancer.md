---
tags:
  - general
  - molecular-biology
  - oncology
  - basic-science
---

# Cell Cycle and Cancer

> [!question] Questions Covered
> - Apoptosis (AMRITA 2018)
> - Discuss briefly on cell cycle and cancer (TMH 2018)
> - Write briefly on Cell Cycle (TMH 2020)

**Source:** Scott-Brown's Otorhinolaryngology Volume 3, Chapter 6 (Molecular Biology of Head and Neck Cancer); Harrison - Head and Neck Cancer: A Multidisciplinary Approach

> [!cite] Landmark Articles
> The understanding of cell cycle deregulation in cancer was revolutionized by Hanahan and Weinberg's seminal 2000 paper defining six hallmarks of cancer — cited over 14,000 times — which framed cell cycle dysregulation within the broader context of self-sufficiency in growth signals, insensitivity to anti-growth signals, and evasion of apoptosis. Vermeulen et al. (2003) authored the definitive review of cell cycle regulation, deregulation, and therapeutic targets in cancer. Suh et al. (2014) applied this framework specifically to head and neck cancer, detailing how TP53, CDKN2A, CCND1, and HPV oncoproteins E6/E7 disrupt cell cycle control. The Cancer Genome Atlas (TCGA) Network's 2015 comprehensive genomic analysis of HNSCC identified mutations in cell cycle regulators in the majority of tumours. Alsahafi et al. (2019) provided an updated molecular biology review of HNSCC, integrating the latest understanding of cell cycle and apoptosis pathways.
>
> | No. | Article | Authors | Journal, Year | DOI | Key Finding |
> |-----|---------|---------|---------------|-----|-------------|
> | 1 | The hallmarks of cancer | Hanahan D, Weinberg RA | Cell, 2000 | [10.1016/S0092-8674(00)81683-9](https://doi.org/10.1016/S0092-8674(00)81683-9) | Defined 6 hallmarks including cell cycle deregulation, apoptosis evasion; >14,000 citations |
> | 2 | The cell cycle: regulation, deregulation and therapeutic targets in cancer | Vermeulen K, Van Bockstaele DR, Berneman ZN | Cell Prolif, 2003 | [10.1046/j.1365-2184.2003.00266.x](https://doi.org/10.1046/j.1365-2184.2003.00266.x) | Comprehensive review of CDK-cyclin regulation, checkpoints, and cancer deregulation |
> | 3 | Clinical update on cancer: molecular oncology of head and neck cancer | Suh Y, Amelio I, Guerrero Urbano T, Tavassoli M | Cell Death Dis, 2014 | [10.1038/cddis.2013.548](https://doi.org/10.1038/cddis.2013.548) | HNC-specific review of TP53, p16, Cyclin D1, HPV E6/E7 in cell cycle disruption |
> | 4 | Comprehensive genomic characterization of head and neck squamous cell carcinomas | The Cancer Genome Atlas Network | Nature, 2015 | [10.1038/nature14129](https://doi.org/10.1038/nature14129) | TCGA analysis of 279 HNSCC; cell cycle regulators mutated in majority of tumours |
> | 5 | Clinical update on head and neck cancer: molecular biology and ongoing challenges | Alsahafi E, Begg K, Amelio I et al. | Cell Death Dis, 2019 | [10.1038/s41419-019-1769-9](https://doi.org/10.1038/s41419-019-1769-9) | Updated molecular review; HPV E6 degrades p53, E7 inactivates Rb; p16 as surrogate marker |

---

## Introduction

The cell cycle is the highly ordered and tightly regulated series of events through which a cell duplicates its DNA, segregates its chromosomes, and divides into two genetically identical daughter cells. In normal adult tissues, the vast majority of cells are quiescent — they have exited the active cell cycle and reside in a resting state known as G0. Entry into the cell cycle from G0 requires specific mitogenic signals (growth factors binding to their receptors), and progression through the cycle is governed by a series of molecular checkpoints that ensure each phase is completed accurately before the next one begins. These checkpoints function as a quality control system: if DNA damage is detected, the cell cycle is halted to allow repair; if the damage is irreparable, the cell is eliminated through apoptosis (programmed cell death).

Deregulation of the cell cycle is one of the fundamental hallmarks of cancer, as defined in the seminal framework by Hanahan and Weinberg (2000). Cancer cells acquire the ability to proliferate autonomously (self-sufficiency in growth signals), ignore signals that would normally halt proliferation (insensitivity to anti-growth signals), and resist programmed cell death (evading apoptosis) — all of which involve disruption of cell cycle regulatory mechanisms. In head and neck squamous cell carcinoma (HNSCC), the most frequently mutated genes — TP53 (mutated in 60-80% of HPV-negative tumours), CDKN2A/p16 (inactivated in 50-60%), CCND1/Cyclin D1 (amplified in 30-40%), and PIK3CA (mutated in 20-30%) — all have direct and well-characterized roles in cell cycle regulation. Understanding the normal cell cycle and how it becomes deregulated in cancer is essential for comprehending cancer biology, the mechanism of action of chemotherapy and radiotherapy (both of which target dividing cells), and the rationale for emerging targeted therapies such as CDK4/6 inhibitors.

---

## Part A: Normal Cell Cycle Phases

The cell cycle consists of four sequential phases:

| Phase | Duration | Key Events |
|-------|----------|------------|
| G1 (Gap 1) | Variable (hours to days) | Cell growth; preparation for DNA synthesis; major checkpoint (Restriction Point) |
| S (Synthesis) | 6-8 hours | DNA replication |
| G2 (Gap 2) | 2-5 hours | Preparation for mitosis; DNA damage checkpoint |
| M (Mitosis) | ~1 hour | Chromosome separation and cell division |

Cells can also exit the cycle into **G0** — a quiescent state. Most normal adult cells are in G0. Mitogenic signals are required to re-enter G1.

---

## Part B: Regulation by Cyclins and CDKs

The cell cycle is regulated by the coordinated action of **cyclins** and **cyclin-dependent kinases (CDKs)**. Cyclins are regulatory subunits whose levels oscillate during the cycle; CDKs are catalytic kinases that are only active when bound to their cyclin partner.

### Cyclin-CDK Complexes Drive Cell Cycle Progression

| Phase Transition | Cyclin-CDK Complex | Function |
|-----------------|-------------------|----------|
| G1 entry | Cyclin D / CDK4 or CDK6 | Phosphorylates Rb; responds to mitogens |
| G1→S transition | Cyclin E / CDK2 | Completes Rb phosphorylation; commits to S phase |
| S phase | Cyclin A / CDK2 | DNA replication initiation and progression |
| G2→M transition | Cyclin A / CDC2 (CDK1) | Prepares for mitosis |
| Mitosis | Cyclin B / CDC2 (CDK1) | Drives mitotic entry |

### The Rb Pathway — Central Gatekeeper

The **retinoblastoma protein (Rb)** is the key gatekeeper of the G1-S transition:

1. In the absence of mitogenic signals, Rb is **under-phosphorylated** and bound to **E2F transcription factor**, rendering E2F inactive
2. Mitogens activate **Cyclin D/CDK4/6** complexes that **phosphorylate Rb**
3. Phosphorylated Rb releases E2F, which activates expression of genes needed for S-phase entry (DNA polymerases, Cyclin E, thymidylate synthase)
4. Cyclin E/CDK2 completes Rb phosphorylation, committing the cell to S phase
5. After mitosis, Rb is **de-phosphorylated** by phosphatases — resetting the cycle

---

## Part C: Cell Cycle Checkpoints

Checkpoints are quality-control mechanisms that halt cell cycle progression if errors are detected:

### G1-S Checkpoint (Restriction Point)
- Governed by **p53** and **p16/Rb** pathways
- DNA damage activates p53 → upregulates **p21 (CDKN1A)** → inhibits Cyclin E/CDK2 → G1 arrest
- Anti-proliferative signals activate **p16 (CDKN2A)** → inhibits Cyclin D/CDK4/6 → prevents Rb phosphorylation

### Intra-S Checkpoint
- Monitors ongoing DNA replication
- ATR kinase pathway halts replication forks if damage detected

### G2-M Checkpoint
- Ensures DNA replication is complete and error-free before mitosis
- ATM/ATR → CHK1/CHK2 → p53 activation → cell cycle arrest or apoptosis

### Spindle Assembly Checkpoint (SAC)
- Ensures all chromosomes are properly attached to mitotic spindle before anaphase

---

## Part D: CDK Inhibitors (CKIs)

Two families of endogenous CDK inhibitors provide negative regulation:

| Family | Members | Targets | Function |
|--------|---------|---------|----------|
| INK4 family | p16 (CDKN2A), p15, p18, p19 | CDK4, CDK6 | Block Cyclin D/CDK4/6; prevent Rb phosphorylation |
| CIP/KIP family | p21 (CDKN1A), p27 (CDKN1B), p57 | CDK2, CDK4, CDK6 | Broad CDK inhibition; p21 is the effector of p53 |

---

## Part E: Cell Cycle Deregulation in Head and Neck Cancer

### Most Frequently Mutated Cell Cycle Genes in HNSCC

| Gene | Protein | Frequency | Mechanism | Effect |
|------|---------|-----------|-----------|--------|
| TP53 | p53 | 60-80% (HPV−) | Missense mutation | Loss of G1 arrest and apoptosis; genome instability |
| CDKN2A | p16 | 50-60% (HPV−) | Deletion, mutation, or hypermethylation | Loss of CDK4/6 inhibition; uncontrolled G1→S |
| CCND1 | Cyclin D1 | 30-40% | Amplification | Constitutive Rb phosphorylation; accelerated G1→S |
| PIK3CA | PI3K p110α | 20-30% | Activating mutation | Promotes cell survival and proliferation |
| RB1 | Rb | ~5% (HPV−) | Mutation/deletion | Loss of E2F regulation |

### HPV-Mediated Cell Cycle Disruption

In HPV-positive HNSCC (primarily oropharyngeal), viral oncoproteins directly hijack cell cycle control:

- **E7 oncoprotein** binds and inactivates Rb → releases E2F → forces S-phase entry
- **E6 oncoprotein** binds p53 via E6AP → promotes p53 degradation via ubiquitin pathway → loss of G1 checkpoint and apoptosis
- Result: **p16 accumulates** (because Rb is inactivated, there is no negative feedback on p16 expression) → p16 serves as a surrogate marker of HPV infection
- HPV+ tumours have fewer total mutations than HPV− tumours but different mutational profiles

---

## Part F: Apoptosis

Apoptosis (programmed cell death) is the cell's self-destruction mechanism activated when DNA damage is irreparable or when abnormal proliferation signals are detected.

### Two Main Pathways

**Intrinsic (Mitochondrial) Pathway:**
- Triggered by DNA damage, hypoxia, loss of growth factor signaling
- Pro-apoptotic BCL-2 family members (BAX, BAK) permeabilize the mitochondrial outer membrane
- Release of cytochrome c → activates caspase-9 → activates executioner caspases (3, 6, 7)
- **p53 is the master regulator** — upregulates BAX and PUMA, downregulates BCL-2

**Extrinsic (Death Receptor) Pathway:**
- Triggered by death ligands (FasL, TNF, TRAIL) binding to death receptors (Fas, TNFR, DR4/5)
- Activates caspase-8 → activates executioner caspases
- Important in immune-mediated tumour surveillance

### Evasion of Apoptosis in HNSCC
- TP53 mutation (60-80%) → loss of BAX upregulation
- BCL-2 overexpression → blocks mitochondrial apoptosis
- Survivin overexpression → inhibits caspases
- EGFR/PI3K/AKT pathway activation → promotes survival signaling

---

> [!abstract] Key Points
> 1. The cell cycle has four phases (G1, S, G2, M) regulated by cyclin-CDK complexes
> 2. Rb is the central gatekeeper of G1→S; its phosphorylation by Cyclin D/CDK4/6 releases E2F to activate S-phase genes
> 3. p53 is the "guardian of the genome" — activates p21 for G1 arrest or BAX for apoptosis
> 4. p16 (CDKN2A) inhibits CDK4/6 → prevents Rb phosphorylation → the most frequently inactivated gene in HPV− HNSCC
> 5. TP53 is mutated in 60-80% of HPV-negative HNSCC — the single most common genetic alteration
> 6. Cyclin D1 amplification (30-40%) drives constitutive Rb phosphorylation and uncontrolled proliferation
> 7. HPV E7 inactivates Rb, E6 degrades p53 — together they bypass both major cell cycle checkpoints
> 8. p16 overexpression in HPV+ tumours is a surrogate marker (feedback from Rb inactivation)
> 9. Apoptosis has two pathways: intrinsic (mitochondrial, p53-regulated) and extrinsic (death receptor)
> 10. The hallmarks of cancer (Hanahan & Weinberg 2000) provide the framework for understanding cell cycle deregulation

> [!tip] Clinical Pearls
> - p16 immunohistochemistry is used clinically as a surrogate marker for HPV status — but remember p16 overexpression results from Rb inactivation, not directly from HPV
> - TP53 mutation patterns differ between HPV+ (wild-type p53 degraded by E6) and HPV− (missense mutations) — this explains the different biology and prognosis
> - CDK4/6 inhibitors (palbociclib, ribociclib) are FDA-approved for breast cancer and under investigation in HNSCC
> - Understanding cell cycle biology is essential for interpreting the mechanism of action of radiotherapy (DNA damage → checkpoint activation → apoptosis) and chemotherapy (S-phase cytotoxics)
> - HPV+ HNSCC has fewer total mutations but intact p53 → explains better response to chemoradiation and better prognosis
> - Cyclin D1 amplification can be detected by FISH — it may serve as a prognostic biomarker in HNSCC

---
END OF ANSWER
