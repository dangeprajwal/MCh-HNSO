---
tags:
  - Skull-Base
  - Surgery
  - Diagnostics
---

> [!question] Questions Covered
> - **Q5 (AMRITA 2016)** — Neuronavigation in skull base surgery: principles, registration methods, and limitations

## Source
- Flint PW et al. *Cummings Otolaryngology*, 7th Ed. Elsevier, 2021. Chapter 50: Image-Guided Surgery.
- Shah JP. *Head and Neck Surgery and Oncology*, 5th Ed. Elsevier, 2019. Chapter 18: Technology in Skull Base Surgery.
- Sekhar LN, de Oliveira E. *Cranial Microsurgery*. Thieme, 1999. Chapter 2: Intraoperative Navigation.

> [!cite] Landmark Articles
>
> **Anon JB, Lipman SP, Oppenheim D, Halt RA (1994)** — First described computer-assisted image-guided surgery for functional endoscopic sinus surgery; demonstrated that electromagnetic navigation could identify key anatomical landmarks (lamina papyracea, skull base, optic nerve) to within 2 mm accuracy in cadaveric and clinical validation, establishing the foundational evidence for neuronavigation in sino-nasal and skull base surgery.
>
> **Grauvogel J, Engelskirchen P, Maier W, Laszig R, Grauvogel TD (2010)** — Compared four registration modalities (surface registration, anatomical landmark, fiducial, and hybrid) for intraoperative navigation in ENT surgery; surface registration had a mean total error of 1.72 mm while fiducial-based registration achieved 1.26 mm; fiducial-based registration remained most accurate, with hybrid approaches offering a practical balance.
>
> | Study | Journal | Year | DOI |
> |---|---|---|---|
> | Grauvogel et al. — Registration modalities in ENT navigation | *Laryngoscope* | 2010 | — |

---

## Principle of Neuronavigation

Neuronavigation (image-guided surgery, IGS) creates a **real-time spatial correlation** between:
1. The patient's preoperative CT or MRI dataset (stored as a 3D volume)
2. The patient's physical head position in the operating room
3. The current position of a tracked surgical instrument

The result: as the surgeon moves an instrument, its position is displayed on the reformatted CT/MRI in axial, coronal, and sagittal planes simultaneously — allowing real-time identification of anatomical structures without direct visualisation.

---

## Pre-Operative Setup

### Imaging Requirements
- **CT scan** (with 1 mm slices, no gap) — for bony landmarks; standard for FESS/skull base
- **MRI** (1 mm slices) — for soft tissue; can be co-registered with CT (fusion)
- Images uploaded to navigation workstation pre-operatively
- Imaging ideally performed **with fiducial markers in place** (if fiducial-based registration planned)

### Patient Positioning
- Head in Mayfield three-pin fixation (open cranial surgery) or dedicated navigation headrest (endoscopic)
- Head must be **rigid and immobile** during registration and surgery (any head movement invalidates registration)

---

## Registration Methods

Registration = the process of correlating the preoperative image coordinate system to the intraoperative physical coordinate system.

### 1. Fiducial-Based Registration
- **Adhesive fiducial markers** placed on skin surface (forehead, mastoid, periorbital region) **before imaging**
- Markers are visible on CT/MRI as hyperintense dots
- Intraoperatively: tracked pointer touched to each fiducial; software calculates transformation matrix
- **Accuracy**: target registration error (TRE) ~1.0–2.0 mm — most accurate surface-accessible method
- **Drawback**: requires planning before imaging; fiducials can shift if skin moves (especially in children)

### 2. Surface-Based Registration (Iterative Closest Point — ICP)
- No pre-placed fiducials required
- Intraoperatively: tracked probe sweeps across patient's facial surface (nose, orbit, forehead)
- Software matches point cloud to surface rendered from CT
- **Accuracy**: TRE ~1.5–2.5 mm — slightly less accurate than fiducial but more convenient
- **Advantage**: no pre-imaging preparation; easy to repeat
- Standard in most modern endoscopic skull base centres

### 3. Bone-Implanted Fiducials
- Titanium screws implanted at known skull positions under local anaesthesia, then imaged
- **Most accurate** (TRE <1.0 mm)
- **Disadvantage**: invasive, requires second procedure; rarely used except for stereotactic radiosurgery

### 4. Hybrid Registration
- Combines ICP surface matching + anatomical landmark confirmation
- Practical balance of accuracy and convenience

### Registration Accuracy Verification
After registration, surgeon touches a **known anatomical landmark** (e.g., nasion, lateral orbital rim) with tracked probe and checks that displayed position matches expected location on CT/MRI. Acceptable error: <2 mm.

---

## Tracking Systems

### Electromagnetic (EM) Tracking
- **Principle**: magnetic field generator creates a reference field around the surgical site; sensors in instruments detect field and report position
- **Advantage**: no **line-of-sight** requirement — instruments can be tracked even when not visible to camera (e.g., deep in nose, around corners)
- **Disadvantage**: susceptible to **metallic interference** (retractors, bipolar forceps near the field degrade accuracy)
- Common in ENT/endoscopic skull base (no direct line of sight in nasal cavity)
- Systems: Medtronic StealthStation ENT, Brainlab Kick

### Optical (Infrared) Tracking
- **Principle**: infrared cameras track reflective (passive) or LED (active) markers attached to reference arrays on instruments and on patient's head
- **Advantage**: highly accurate; no metallic interference
- **Disadvantage**: requires **unobstructed line of sight** between cameras and trackers — can be blocked by surgical drapes or assistant's hands
- Gold standard for open cranial surgery (no line-of-sight problem in field)
- Systems: Brainlab Curve, Stryker Navigation

### Comparison

| Feature | Electromagnetic | Optical |
|---|---|---|
| Line of sight required | No | Yes |
| Metallic interference | Yes (problematic) | No |
| Accuracy | ~1.5–2.5 mm | ~1.0–1.5 mm |
| Best application | FESS, endoscopic skull base | Open cranial surgery |

---

## Clinical Applications

| Procedure | Role of Neuronavigation |
|---|---|
| **Endoscopic skull base surgery** (EEES, FESS) | Landmark identification (optic nerve, ICA, skull base); real-time margin checking |
| **Anterior skull base** (CFR, endoscopic) | Confirmation of clearance at cribriform plate; see [[Answers/Skull Base/Craniofacial Resection\|CFR]] |
| **Temporal bone surgery** | Facial nerve tracking; cochlea identification in revision cases |
| **Orbital surgery** | Orbital apex localisation; avoid optic nerve |
| **Second-look surgery** | Distorted anatomy after prior surgery or radiation |
| **Spinal / C1–C2 surgery** | Odontoid peg; atlantoaxial instrumentation |

---

## Brain Shift: The Critical Limitation

**Brain shift** = intraoperative displacement of brain tissue relative to the preoperative imaging used for navigation.

### Causes
1. **CSF drainage** — brain falls away from inner table as CSF is released
2. **Tumour resection** — creates a cavity; brain may fall into it
3. **Gravity** (dependent positioning)
4. **Oedema** (late shift)

### Consequence
The preoperative CT/MRI no longer matches the current anatomy → navigation becomes progressively **inaccurate** during a long resection.

### Solutions
1. **Intraoperative MRI (iMRI)**: rescans patient mid-surgery → updates navigation with current anatomy; most accurate but expensive and operationally demanding
2. **Intraoperative ultrasound**: real-time soft tissue imaging; cheaper; can update navigation
3. **Finite element modelling**: computational correction for expected shift based on resection volume — emerging research

---

## Limitations of Neuronavigation

| Limitation | Clinical Impact |
|---|---|
| Brain shift (see above) | Accuracy degrades progressively during surgery |
| Initial registration error | Even best fiducial registration has 1–2 mm error |
| Does not replace anatomical knowledge | Surgeon must interpret data; not autonomous |
| Setup time and cost | Adds 15–30 min to OR time; significant capital cost |
| Metallic interference (EM) | Limits use near metallic instruments |
| Cannot track soft tissue deformation | Rigid body assumption fails in soft tissue surgery |

---

> [!example] Examiner's Summary
> Neuronavigation correlates preoperative CT/MRI to intraoperative anatomy via registration (fiducial-based: most accurate at ~1–2 mm TRE; surface ICP: more convenient; bone fiducials: most accurate but invasive). Electromagnetic tracking suits endoscopic skull base surgery (no line-of-sight requirement), while optical infrared tracking is the gold standard for open cranial surgery. The most important clinical limitation is **brain shift** — progressive displacement of brain tissue as CSF is drained and tumour is resected — which is corrected by intraoperative MRI or ultrasound to update the navigation dataset.

> [!tip] Clinical Pearls
> 1. Neuronavigation **does not replace** anatomical knowledge — it is a guide that requires surgical judgement to interpret.
> 2. **Fiducial markers must be placed before imaging** — post-imaging fiducials defeat the purpose of the registration algorithm.
> 3. Verify registration accuracy by touching a **known landmark** (nasion, orbital rim) — acceptable error is <2 mm.
> 4. **Electromagnetic tracking** is preferred for FESS/endoscopic skull base because the endoscope blocks line of sight for optical systems.
> 5. **Brain shift** begins the moment CSF is released — reassess navigation accuracy at key milestones in long resections.
> 6. Intraoperative MRI is the gold standard for correcting brain shift but requires a dedicated MRI-compatible operating environment (non-ferromagnetic instruments, patient transport within suite).
> 7. Navigation is particularly valuable in **revision skull base surgery** where anatomy is distorted by scarring from prior surgery or radiotherapy.
> 8. The navigation system has a finite **target registration error** — the reported accuracy reflects the registration, not the inherent accuracy of finding the tumour margin.

---

END OF ANSWER

> [!compass]- Navigate
> **Parent:** [[Answers/Skull Base/index|Skull Base]]
>
> **Related Notes:**
> - [[Answers/Skull Base/Anterior Skull Base Anatomy and Endoscopic Surgery|Anterior Skull Base Anatomy and EEES]]
> - [[Answers/Skull Base/Craniofacial Resection|Craniofacial Resection]]
> - [[Answers/Skull Base/Middle Cranial Fossa Approaches|Middle Cranial Fossa Approaches]]
> - [[Answers/Skull Base/Raveh Subcranial Approach|Raveh Subcranial Approach]]
> - [[Answers/Skull Base/Parapharyngeal Space Tumours and Approaches|Parapharyngeal Space Tumours]]
>
> **See Also:**
> - [[Answers/General/PET-CT in Head and Neck Cancer|PET-CT in HNC]]
> - [[Answers/Radiotherapy and Chemotherapy/IMRT and IGRT in Head and Neck Cancer|IMRT and IGRT]]
