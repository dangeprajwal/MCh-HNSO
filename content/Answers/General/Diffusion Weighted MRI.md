---
tags:
  - General
  - Diagnostics
---

# Diffusion Weighted MRI in Head and Neck Cancer

> [!question] Questions Covered
> - Diffusion weighted MRI (AMRITA 2020)

**Source:** Montgomery - Principles and Practice of HN Surgery, Chapter 3 (Imaging); Scott-Brown's Otorhinolaryngology Volume 3, Chapter 5 (Neck — Imaging of Metastatic Nodes), Chapter 7 (Sinonasal Cancer), Chapter 10 (Salivary Gland Tumours); Harrison - Head and Neck Cancer: A Multidisciplinary Approach, Chapter 4 (Diagnostic Imaging), Chapter 14 (Neck); Stell and Maran's Textbook of Head and Neck Surgery, Chapter 5 (Imaging of Neck Nodes), Chapter 15 (Larynx — Post-Treatment Surveillance), Chapter 32 (Hypopharynx)

> [!cite] Landmark Articles
> Diffusion-weighted MRI (DW-MRI) is a functional imaging technique that measures the random Brownian motion of water molecules within tissues. The foundational physics was described by Le Bihan et al. (1986), who introduced the intravoxel incoherent motion (IVIM) model and the concept of the apparent diffusion coefficient (ADC) — work that underpins all modern clinical DWI applications. Sumi et al. (2003) published the first significant study applying DW-MRI to cervical lymph node assessment in head and neck cancer, demonstrating that ADC values could discriminate metastatic from benign nodes. Vandecaveye et al. (2007) then showed that DW-MRI could differentiate post-treatment changes from recurrent tumour with 94.6% accuracy — a finding of immense clinical importance referenced in Montgomery's Chapter 3. Kim et al. (2009) established DW-MRI as a biomarker for predicting and detecting early treatment response in HNSCC during chemoradiation. Thoeny et al. (2012) published the definitive review of DW-MRI applications in the head and neck in *Radiology*, synthesizing the evidence for tissue characterization, nodal staging, treatment monitoring, and recurrence detection.
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Le Bihan D — MR imaging of intravoxel incoherent motions: application to diffusion and perfusion in neurologic disorders | Radiology | 1986 | [10.1148/radiology.161.2.3763909](https://doi.org/10.1148/radiology.161.2.3763909) |
> | Sumi M — Discrimination of metastatic cervical lymph nodes with diffusion-weighted MR imaging in patients with head and neck cancer | AJNR | 2003 | PMID: 13679283 |
> | Vandecaveye V — Detection of head and neck SCC with diffusion-weighted MRI after (chemo)radiotherapy | Int J Radiat Oncol Biol Phys | 2007 | [10.1016/j.ijrobp.2006.09.020](https://doi.org/10.1016/j.ijrobp.2006.09.020) |
> | Kim S — Diffusion-weighted MRI for predicting and detecting early response to chemoradiation therapy of HNSCC | Clin Cancer Res | 2009 | [10.1158/1078-0432.CCR-08-1287](https://doi.org/10.1158/1078-0432.CCR-08-1287) |
> | Thoeny HC — Diffusion-weighted MR imaging in the head and neck | Radiology | 2012 | [10.1148/radiol.11101821](https://doi.org/10.1148/radiol.11101821) |

---

## Introduction

Diffusion-weighted MRI (DW-MRI) is a functional imaging technique that measures the microscopic mobility of water molecules within biological tissues. Unlike conventional anatomical MRI (T1, T2, contrast-enhanced), which depicts morphological features, DW-MRI provides information about tissue cellularity, membrane integrity, and microstructural organization at the molecular level.

As described in Harrison's Chapter 4, emerging technologies in biologic neuroimaging — including DW-MRI — utilize biologic behaviour patterns such as tumour cellularity and perfusion to depict additional imaging dimensions beyond anatomy. Montgomery's Chapter 3 specifically highlights DW-MRI's role in detecting recurrence after chemoradiotherapy, noting that the technique can differentiate post-treatment inflammation from recurrent malignancy with a very high accuracy of 96%.

In head and neck oncology, DW-MRI has four principal applications: **(1) tissue characterization** — differentiating benign from malignant lesions, **(2) lymph node assessment** — identifying metastatic cervical nodes, **(3) treatment response monitoring** — predicting and detecting response to chemoradiation, and **(4) recurrence detection** — distinguishing tumour recurrence from post-treatment changes.

---

## Part A: Physics and Technical Principles

### The Basis of Diffusion-Weighted Imaging

DW-MRI exploits the random Brownian motion (diffusion) of water molecules in biological tissues. In 1986, Le Bihan et al. introduced the intravoxel incoherent motion (IVIM) model, showing that in a single voxel, signal attenuation is caused by both true molecular diffusion and microcirculation (perfusion) in the capillary network.

The key physical principles are:

1. **Free water** — in a glass of pure water, molecules diffuse freely and equally in all directions (isotropic diffusion)
2. **Restricted diffusion** — in biological tissues, cell membranes, intracellular organelles, and macromolecules restrict the movement of water molecules
3. **Hypercellular tissues** (e.g., malignant tumours) have more cell membranes per unit volume → **more restriction** → **lower ADC values**
4. **Hypocellular tissues** (e.g., oedema, necrosis, post-treatment fibrosis) have fewer barriers → **less restriction** → **higher ADC values**

### The b-Value and ADC Calculation

DW-MRI sequences apply extra **motion-probing gradients** (diffusion gradients) to a T2-weighted spin-echo sequence. The **b-value** (measured in s/mm²) describes the strength and duration of these gradients:

| b-Value | Effect | Clinical Use |
|---------|--------|-------------|
| **b = 0** | No diffusion weighting; essentially a T2-weighted image | Reference image |
| **Low b** (50-100) | Sensitive to perfusion effects (IVIM) | Perfusion assessment |
| **High b** (800-1000) | Sensitive to true diffusion; suppresses perfusion signal | Tumour detection |

The **apparent diffusion coefficient (ADC)** is calculated from images acquired at two or more b-values:

- ADC = ln(S₀/S₁) / (b₁ - b₀), where S₀ and S₁ are signal intensities at the two b-values
- ADC is displayed as a parametric **ADC map** — a quantitative image where each pixel represents the local diffusion coefficient
- ADC is measured in units of **× 10⁻³ mm²/s**

### Signal Interpretation

| DWI Signal | ADC Map | Interpretation | Example |
|-----------|---------|---------------|---------|
| High (bright) | Low (dark) | Restricted diffusion | Malignant tumour, abscess, lymphoma |
| Low (dark) | High (bright) | Free diffusion | Oedema, necrosis, cyst |
| High (bright) | High (bright) | T2 shine-through | Fluid with long T2 (not true restriction) |

**T2 shine-through** is an important pitfall: the underlying T2-weighted signal can cause high signal on DWI even without restricted diffusion — always correlate DWI with the ADC map to confirm true restriction.

---

## Part B: Clinical Applications in Head and Neck Cancer

### 1. Tissue Characterization — Benign vs Malignant

Malignant tumours have high cellularity, which restricts water diffusion and produces **low ADC values**. Benign lesions, inflammatory tissue, and cysts generally have higher ADC values.

Typical ADC values in the head and neck:

| Tissue Type | ADC (× 10⁻³ mm²/s) |
|------------|---------------------|
| Malignant tumour (SCC) | 0.8-1.2 |
| Lymphoma | 0.6-0.8 |
| Benign tumour (pleomorphic adenoma) | 1.5-2.0 |
| Cyst/necrosis | 2.0-3.0 |
| Normal tissue | 1.2-1.5 |

Scott-Brown's Chapter 10 specifically states that diffusion-weighted MRI (DW-MRI) is considered to have **superior diagnostic efficacy in identifying malignancy** in parotid tumours based on a specific diffusion pattern. However, there is substantial overlap in ADC values between benign and malignant parotid tumours, limiting specificity for this particular application.

### 2. Cervical Lymph Node Assessment

Stell and Maran's Chapter 5 describes that DW-MRI allows visualization of molecular diffusion and perfusion via microcirculation of blood in the capillary network and may improve detection of metastatic nodes in the neck. Cancer metastases to regional lymph nodes may be associated with alteration in both water diffusion and microcirculation within the node, and calculation of the ADC can be used as an adjunct tool to help discriminate metastatic neck nodes.

Key findings from the literature:

- **Metastatic nodes** show **lower ADC** values than benign reactive nodes (due to higher cellularity from tumour deposits)
- With a threshold ADC of **0.94 × 10⁻³ mm²/s**, sensitivity of 84%, specificity of 94%, and accuracy of 91% can be achieved
- Stell and Maran's further notes that studies have shown a significant difference in ADC values for nodes involved by **metastatic SCC**, **metastatic NPC**, and **lymphoma** — the ADC value for lymphoma and NPC being less than that for SCC, potentially allowing differentiation between causes of malignant lymphadenopathy
- **Limitation:** Necrotic metastatic nodes may show paradoxically **higher** ADC values due to loss of membrane integrity in necrotic areas

Harrison's Chapter 14 corroborates: diffusion-weighted MR sequences are being used more to differentiate benign from malignant neck nodes, with low ADC within a node suggesting the presence of tumour. Nodes responding to radiation therapy show an increasing ADC value.

### 3. Treatment Response Prediction and Monitoring

This is arguably the most important clinical application of DW-MRI in HNSCC. Montgomery's Chapter 3 describes the work of Vandecaveye et al., who showed that DW-MRI can be applied to head and neck cancer patients with clinical suspicion of recurrence, with the ADC having a very high accuracy of 96% for differentiating recurrence from post-radiotherapy change.

**Pre-treatment ADC as a predictor:**
- Tumours with **low pre-treatment ADC** (high cellularity) tend to respond **better** to chemoradiation
- Tumours with **high pre-treatment ADC** may contain areas of micronecrosis and hypoxia that are resistant to treatment

**Early ADC changes during treatment:**
- Kim et al. (2009) demonstrated that a **significant increase in ADC within 1 week** of starting chemoradiation predicted complete response (AUC 0.88, sensitivity 86%, specificity 83%)
- Complete responders showed significantly higher ADC increase than partial responders by the first week
- This allows early identification of non-responders who may benefit from treatment modification

**The biological basis:**
- Treatment-induced cell death → loss of membrane integrity → increased water mobility → ADC increase
- Non-responding tumours maintain their cellularity → ADC remains low
- ADC changes precede morphological (size) changes by weeks, enabling earlier response assessment

### 4. Post-Treatment Recurrence Detection

Distinguishing tumour recurrence from post-treatment changes (oedema, fibrosis, inflammation, necrosis) is one of the most challenging problems in head and neck imaging. As Stell and Maran's Chapter 15 notes, differentiation between inflammatory changes and recurrent tumour remains a significant problem after chemoradiation for laryngeal cancer.

DW-MRI addresses this by exploiting the fundamental difference in cellularity:

| Finding | ADC Value | Interpretation |
|---------|-----------|---------------|
| **Recurrent tumour** | Low (~1.17 × 10⁻³ mm²/s) | High cellularity → restricted diffusion |
| **Post-treatment change** | High (~2.07 × 10⁻³ mm²/s) | Oedema/fibrosis → free diffusion |
| **Necrosis** | Very high (>2.0) | Loss of membrane integrity |

Stell and Maran's notes that recurrent tumour tends to have a low ADC in comparison to necrosis, which exhibits a high ADC secondary to the loss of membrane integrity. Thus, a combination of imaging modalities may be useful in guiding further biopsies.

---

## Part C: DW-MRI by Head and Neck Subsite

### Sinonasal Cancer
Scott-Brown's Chapter 7 notes that T2 and diffusion-weighted sequences are useful in distinguishing between retained secretions, tumour, or mucosal thickening in sinonasal malignancy — a common diagnostic dilemma where conventional MRI alone may be insufficient.

### Salivary Gland Tumours
Scott-Brown's Chapter 10 describes DW-MRI as having superior diagnostic efficacy in identifying malignancy based on a specific diffusion pattern. DW-MRI is of value for the characterization of [[Answers/Oral Cavity/Minor Salivary Gland Tumours of the Oral Cavity|minor salivary gland tumours]] tumours and parotid masses. However, Warthin's tumours may show low ADC values mimicking malignancy.

### Larynx and Hypopharynx
Stell and Maran's Chapter 32 lists DW-MRI among newer imaging modalities that should be employed more widely in difficult cases of hypopharyngeal cancer, particularly for post-treatment assessment. For laryngeal cancer, DW-MRI aids in distinguishing post-chemoradiation changes from recurrence.

### Cervical Lymph Nodes
As detailed in Part B, DW-MRI provides functional information complementary to morphological criteria (size, shape, enhancement pattern) for nodal assessment.

---

## Part D: Advantages, Limitations, and Future Directions

### Advantages

1. **No ionizing radiation** — safe for repeated monitoring
2. **No contrast agent required** — valuable in patients with renal impairment
3. **Short acquisition time** — can be added to standard MRI protocols (2-5 minutes)
4. **Quantitative** — ADC values provide objective, reproducible measurements
5. **Functional information** — complements anatomical imaging
6. **Early response detection** — ADC changes precede morphological changes

### Limitations

1. **Susceptibility artefacts** — air-tissue interfaces in the head and neck (paranasal sinuses, skull base, dental amalgam) cause signal distortion
2. **Motion artefacts** — [[Answers/General/Swallowing Assessment in Head and Neck Cancer|swallowing assessment]], breathing, and vascular pulsation degrade image quality
3. **Spatial resolution** — lower than conventional MRI
4. **ADC overlap** — some benign lesions (Warthin's tumour, abscess) show low ADC values, and some malignant lesions with extensive necrosis show high values
5. **Lack of standardization** — different scanners, b-values, and measurement techniques limit comparability across institutions
6. **T2 shine-through** — can mimic restricted diffusion if ADC maps are not consulted

### Future Directions

- **IVIM modelling** — separating true diffusion from perfusion using multi-b-value acquisition
- **Diffusion kurtosis imaging (DKI)** — non-Gaussian diffusion models providing additional tissue microstructure information
- **Integration with PET/MRI** — combining metabolic (FDG) and diffusion information
- **Radiomics** — extracting quantitative features from ADC maps for prognostic modelling
- **Standardized protocols** — multicentre trials to establish validated ADC thresholds

---

> [!abstract] Key Points
> 1. DW-MRI measures the random Brownian motion of water molecules — restricted diffusion (low ADC) indicates high cellularity, as seen in malignant tumours
> 2. The apparent diffusion coefficient (ADC) is the key quantitative parameter — measured in × 10⁻³ mm²/s from images at different b-values
> 3. Le Bihan et al. (1986) introduced the IVIM model and ADC concept — the foundation of all clinical DWI
> 4. Four main applications in HNC: tissue characterization, nodal assessment, treatment response monitoring, and recurrence detection
> 5. Metastatic lymph nodes show lower ADC than benign nodes — threshold of 0.94 × 10⁻³ mm²/s gives 91% accuracy
> 6. Pre-treatment low ADC predicts better response to chemoradiation; ADC increase within 1 week of treatment predicts complete response (AUC 0.88)
> 7. DW-MRI differentiates recurrence (low ADC ~1.17) from post-treatment change (high ADC ~2.07) with accuracy up to 96%
> 8. T2 shine-through is a major pitfall — always correlate DWI with the ADC map to confirm true restriction
> 9. DW-MRI has superior diagnostic efficacy for identifying malignancy in parotid tumours based on diffusion patterns
> 10. Limitations include susceptibility artefacts at air-tissue interfaces, ADC value overlap, and lack of standardization across centres

> [!tip] Clinical Pearls
> - The key equation for exams: **high cellularity = restricted diffusion = HIGH signal on DWI = LOW ADC** — this is the hallmark of malignant tumours
> - Always look at both DWI and the ADC map together — DWI alone can be misleading due to T2 shine-through
> - Lymphoma has the LOWEST ADC values among head and neck malignancies (even lower than SCC) — if you see very restricted diffusion in a neck node, think lymphoma
> - The most clinically impactful application is post-treatment surveillance: conventional CT/MRI cannot reliably distinguish recurrence from fibrosis/oedema, but DW-MRI can with >90% accuracy
> - DW-MRI does NOT require gadolinium contrast — making it invaluable in patients with renal failure or gadolinium allergy
> - For the AMRITA exam: know the physics (b-value, ADC calculation), the four applications, and the key ADC values for malignant vs benign tissue

---
END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/General/index|General Topics]]
>
> **Related Notes:**
> - [[Answers/General/Molecular Markers and Proteomics|Molecular Markers and Proteomics]] — related topic
> - [[Answers/General/PCR and Microarray Analysis|PCR and Microarray Analysis]] — related topic
> - [[Answers/General/Paraneoplastic Syndrome|Paraneoplastic Syndrome]] — related topic
> - [[Answers/Oral Cavity/Imaging in Oral Cancer|Imaging in Oral Cancer]] — related topic
>
> **See Also:**
> - [[Answers/General/Apoptosis|Apoptosis]] — related topic
> - [[Answers/General/Autophagy in Head and Neck Cancer|Autophagy in Head and Neck Cancer]] — related topic
