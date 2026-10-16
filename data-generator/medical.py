from builder import make, career_doc

MED_PASS_MBBS = [
    "NMC GMER 2023 (CBME): you must get 50% aggregate in each subject (theory + practical together).",
    "You also need at least 40% in theory and 40% in practical/clinical separately.",
    "4 professional exams: Phase I, II, III-Part 1 and III-Part 2. A supplementary exam is held for failures.",
    "A maximum of 9 years is allowed to finish MBBS, and at most 4 attempts for First Professional (check current NMC rules).",
]

LOCAL = ["Telangana local-candidate rule (GO 33, 2024): you must have studied classes 9–12 in Telangana for local status in state-quota medical seats. Check the current rule in the KNRUHS prospectus."]

NEET = [
    "Conducted by NTA, usually on the first Sunday of May. It is a pen-and-paper exam.",
    "180 questions (all compulsory, no optional section), 720 marks, 3 hours. Physics 45, Chemistry 45, Botany 45, Zoology 45.",
    "Marking: +4 for a correct answer, −1 for a wrong one, 0 for unattempted.",
    "Eligibility: 12th with Physics, Chemistry, Biology and English. Minimum 50% in PCB for General, 40% for SC/ST/OBC, 45% for General-PwD.",
    "Minimum age 17 by 31 December of the admission year. No upper age limit at present.",
    "Qualifying percentile: 50th (General), 40th (SC/ST/OBC), 45th (PwD).",
]

TG_COUNSEL = [
    "15% All India Quota (govt colleges) + Deemed/Central universities (AIIMS Bibinagar, ESIC Sanathnagar): MCC counselling (mcc.nic.in).",
    "85% State Quota: KNRUHS (Kaloji Narayana Rao University of Health Sciences, Warangal) web counselling – knruhs.telangana.gov.in.",
    "Private medical colleges: Category A (Convener quota – regulated low fee), Category B (Management), Category C (NRI) – all through KNRUHS.",
    "Fee approx: Govt college about ₹10,000/year; Private Cat-A about ₹60,000/year; Cat-B about ₹11–13 lakh/year; Cat-C higher (check TAFRC fee G.O.).",
    "Fee reimbursement / scholarships for eligible SC/ST/BC/EWS/Minority students on convener seats.",
] + LOCAL

# ---------------------------------------------------------------- MBBS PG specialities
# (name, folder, common title, treats, next superspeciality, type)
MD = [
    ("MD General Medicine", "MD_General_Medicine", "Physician / Internal Medicine Specialist", ["Fever, diabetes, BP, infections, heart/kidney/liver illness – all adult non-surgical diseases"], "DM Cardiology, Neurology, Nephrology, Gastroenterology, Endocrinology, Oncology, etc.", "clinical"),
    ("MD Paediatrics", "MD_Paediatrics", "Child Specialist (Paediatrician)", ["Newborn & child illness, vaccination, growth problems"], "DM Neonatology, Paediatric Neurology/Cardiology", "clinical"),
    ("MD Obstetrics & Gynaecology (MS/MD OBG)", "MS_MD_Obstetrics_Gynaecology", "Gynaecologist", ["Pregnancy, delivery, C-section, women's health, infertility"], "MCh Gynaecological Oncology, Reproductive Medicine", "clinical"),
    ("MD Dermatology, Venereology & Leprosy", "MD_Dermatology", "Skin Specialist (Dermatologist)", ["Skin, hair, nail diseases, cosmetology, STDs, leprosy"], "Fellowships in cosmetology/dermatosurgery", "clinical"),
    ("MD Psychiatry", "MD_Psychiatry", "Psychiatrist", ["Depression, anxiety, schizophrenia, addiction, child mental health"], "DM Child & Adolescent Psychiatry, Addiction Psychiatry", "clinical"),
    ("MD Respiratory Medicine", "MD_Respiratory_Medicine", "Pulmonologist / Chest Physician", ["Asthma, TB, COPD, lung infections, sleep disorders"], "DM Pulmonary Critical Care", "clinical"),
    ("MD Anaesthesiology", "MD_Anaesthesiology", "Anaesthetist", ["Anaesthesia for surgeries, ICU care, pain management"], "DM Cardiac Anaesthesia, Neuro-anaesthesia, Critical Care, Pain Medicine", "clinical"),
    ("MD Radio-diagnosis", "MD_Radiodiagnosis", "Radiologist", ["X-ray, Ultrasound, CT, MRI reporting, guided procedures"], "DM Interventional Radiology, Neuroradiology", "clinical"),
    ("MD Radiation Oncology", "MD_Radiation_Oncology", "Radiation Oncologist (Cancer)", ["Radiotherapy for cancer patients"], "Fellowships", "clinical"),
    ("MD Emergency Medicine", "MD_Emergency_Medicine", "Emergency Physician", ["Accidents, heart attack, poisoning, trauma in casualty"], "DM Critical Care", "clinical"),
    ("MD Family Medicine", "MD_Family_Medicine", "Family Physician", ["Whole-family primary care, chronic disease management"], "—", "clinical"),
    ("MD Geriatrics", "MD_Geriatrics", "Geriatrician (Elderly care)", ["Diseases of old age, dementia, falls, multiple medicines"], "—", "clinical"),
    ("MD Physical Medicine & Rehabilitation", "MD_PMR_Rehabilitation", "Rehabilitation Physician (Physiatrist)", ["Rehab after stroke, spinal injury, amputation, disability"], "—", "clinical"),
    ("MD Sports Medicine", "MD_Sports_Medicine", "Sports Medicine Doctor", ["Sports injuries, athlete fitness, doping control"], "—", "clinical"),
    ("MD Nuclear Medicine", "MD_Nuclear_Medicine", "Nuclear Medicine Physician", ["PET-CT, isotope scans & therapy (thyroid, cancer)"], "—", "clinical"),
    ("MD Palliative Medicine", "MD_Palliative_Medicine", "Palliative Care Specialist", ["Pain & symptom relief in cancer and terminal illness"], "—", "clinical"),
    ("MD Infectious Diseases / Tropical Medicine", "MD_Infectious_Diseases", "Infectious Disease Specialist", ["HIV, TB, dengue, malaria, hospital infections"], "DM Infectious Diseases", "clinical"),
    ("MD Pathology", "MD_Pathology", "Pathologist", ["Biopsy, blood tests, cancer diagnosis, blood bank, lab reports"], "DM Haematopathology, Onco-pathology", "para"),
    ("MD Microbiology", "MD_Microbiology", "Microbiologist", ["Culture tests, infection control, virology lab"], "DM Virology / Infectious Diseases", "para"),
    ("MD Pharmacology", "MD_Pharmacology", "Pharmacologist", ["Drug action, clinical trials, drug safety (pharmacovigilance)"], "DM Clinical Pharmacology", "para"),
    ("MD Forensic Medicine", "MD_Forensic_Medicine", "Forensic Expert (Post-mortem doctor)", ["Post-mortem, medico-legal cases, court evidence"], "—", "para"),
    ("MD Community Medicine (PSM)", "MD_Community_Medicine", "Public Health Specialist", ["Epidemics, vaccination programmes, health planning"], "—", "para"),
    ("MD Immunohaematology & Blood Transfusion", "MD_Transfusion_Medicine", "Blood Bank Specialist", ["Blood bank, component separation, transfusion safety"], "—", "para"),
    ("MD Hospital Administration", "MD_Hospital_Administration", "Hospital Administrator", ["Running hospitals – quality, NABH, operations"], "—", "para"),
    ("MD Anatomy", "MD_Anatomy", "Anatomist (Teaching)", ["Teaching human body structure to medical students"], "—", "pre"),
    ("MD Physiology", "MD_Physiology", "Physiologist (Teaching)", ["Teaching body functions; research"], "—", "pre"),
    ("MD Biochemistry", "MD_Biochemistry", "Biochemist (Teaching + Lab)", ["Clinical biochemistry lab, teaching"], "—", "pre"),
]
MS = [
    ("MS General Surgery", "MS_General_Surgery", "General Surgeon", ["Appendix, hernia, gall bladder, trauma, laparoscopic surgery"], "MCh in any surgical super-speciality", "clinical"),
    ("MS Orthopaedics", "MS_Orthopaedics", "Bone Specialist (Orthopaedic Surgeon)", ["Fractures, joint replacement, spine, sports injuries"], "Fellowships (arthroplasty, spine), MCh Hand Surgery", "clinical"),
    ("MS ENT (Otorhinolaryngology)", "MS_ENT", "ENT Surgeon", ["Ear, nose, throat diseases, hearing loss, sinus, tonsils"], "MCh Head & Neck Surgery", "clinical"),
    ("MS Ophthalmology", "MS_Ophthalmology", "Eye Specialist (Ophthalmologist)", ["Cataract, glaucoma, retina, LASIK, squint"], "Fellowships (retina, cornea) – LV Prasad Eye Institute Hyderabad", "clinical"),
    ("MS Traumatology & Surgery", "MS_Traumatology", "Trauma Surgeon", ["Road-accident & emergency trauma surgery"], "—", "clinical"),
]
DM = [
    ("DM Cardiology", "DM_Cardiology", "Heart Specialist (Cardiologist)", ["Heart attack, angiography, stents, pacemakers"]),
    ("DM Neurology", "DM_Neurology", "Neurologist", ["Stroke, epilepsy, Parkinson's, headache, nerve diseases"]),
    ("DM Nephrology", "DM_Nephrology", "Kidney Specialist (Nephrologist)", ["Kidney failure, dialysis, kidney transplant medicine"]),
    ("DM Gastroenterology", "DM_Gastroenterology", "Gastroenterologist", ["Stomach, liver, intestine diseases, endoscopy (AIG Hyderabad is a world leader)"]),
    ("DM Endocrinology", "DM_Endocrinology", "Endocrinologist (Diabetes & Hormones)", ["Diabetes, thyroid, hormone disorders, growth"]),
    ("DM Medical Oncology", "DM_Medical_Oncology", "Medical Oncologist (Cancer)", ["Chemotherapy, immunotherapy, targeted cancer therapy"]),
    ("DM Clinical Haematology", "DM_Clinical_Haematology", "Haematologist", ["Blood cancers, anaemia, bleeding disorders, bone-marrow transplant"]),
    ("DM Neonatology", "DM_Neonatology", "Neonatologist (Newborn ICU)", ["Premature and sick newborn care (NICU)"]),
    ("DM Pulmonary & Critical Care Medicine", "DM_Pulmonary_Critical_Care", "Pulmonologist / Intensivist", ["Advanced lung disease, ICU ventilation"]),
    ("DM Critical Care Medicine", "DM_Critical_Care", "Intensivist (ICU Specialist)", ["Critically ill patients in ICU"]),
    ("DM Rheumatology / Clinical Immunology", "DM_Rheumatology", "Rheumatologist", ["Arthritis, lupus, autoimmune diseases"]),
    ("DM Hepatology", "DM_Hepatology", "Liver Specialist (Hepatologist)", ["Liver cirrhosis, hepatitis, liver transplant medicine"]),
    ("DM Infectious Diseases", "DM_Infectious_Diseases", "ID Specialist", ["Complex infections, HIV, antimicrobial stewardship"]),
    ("DM Paediatric Neurology / Cardiology", "DM_Paediatric_Neuro_Cardio", "Paediatric Neurologist / Cardiologist", ["Children's brain or heart diseases"]),
    ("DM Interventional Radiology", "DM_Interventional_Radiology", "Interventional Radiologist", ["Image-guided procedures without open surgery"]),
    ("DM Cardiac / Neuro Anaesthesia", "DM_Cardiac_Neuro_Anaesthesia", "Super-specialist Anaesthetist", ["Anaesthesia for heart & brain surgeries"]),
    ("DM Clinical Pharmacology", "DM_Clinical_Pharmacology", "Clinical Pharmacologist", ["Drug trials, therapeutic drug monitoring"]),
]
MCH = [
    ("MCh Cardio-Thoracic & Vascular Surgery (CTVS)", "MCh_CTVS", "Heart Surgeon", ["Bypass surgery, valve replacement, heart transplant"]),
    ("MCh Neurosurgery", "MCh_Neurosurgery", "Brain & Spine Surgeon", ["Brain tumours, head injury, spine surgery"]),
    ("MCh Urology", "MCh_Urology", "Urologist", ["Kidney stones, prostate, urinary tract surgery, kidney transplant surgery"]),
    ("MCh Plastic & Reconstructive Surgery", "MCh_Plastic_Surgery", "Plastic Surgeon", ["Burns, cleft lip, reconstruction, cosmetic surgery"]),
    ("MCh Paediatric Surgery", "MCh_Paediatric_Surgery", "Paediatric Surgeon", ["Surgery for newborns and children"]),
    ("MCh Surgical Oncology", "MCh_Surgical_Oncology", "Cancer Surgeon", ["Removal of cancers – breast, mouth, stomach etc."]),
    ("MCh Surgical Gastroenterology / GI Surgery", "MCh_Surgical_Gastroenterology", "GI Surgeon", ["Liver, pancreas, stomach, intestine surgery; liver transplant"]),
    ("MCh Vascular Surgery", "MCh_Vascular_Surgery", "Vascular Surgeon", ["Blood vessel diseases, varicose veins, aneurysms"]),
    ("MCh Endocrine Surgery", "MCh_Endocrine_Surgery", "Endocrine Surgeon", ["Thyroid, parathyroid, adrenal surgery"]),
    ("MCh Hand & Microsurgery", "MCh_Hand_Microsurgery", "Hand Surgeon", ["Hand injuries, re-attachment of fingers"]),
    ("MCh Head & Neck Surgery", "MCh_Head_Neck_Surgery", "Head & Neck Surgeon", ["Head-neck cancers"]),
    ("MCh Gynaecological Oncology", "MCh_Gynae_Oncology", "Gynae-Oncologist", ["Cancers of uterus, ovary, cervix"]),
    ("MCh Reproductive Medicine", "MCh_Reproductive_Medicine", "Infertility Specialist", ["IVF, infertility surgery"]),
    ("MCh Paediatric Cardiothoracic Surgery", "MCh_Paediatric_CTVS", "Paediatric Heart Surgeon", ["Heart surgery in children"]),
]

SAL = {"clinical": "₹1.5–4 lakh/month (junior consultant, Hyderabad); much higher with experience/private practice",
       "para": "₹1–2.5 lakh/month (labs, hospitals, teaching)",
       "pre": "₹1–2 lakh/month (mostly teaching in medical colleges)",
       "super": "₹3–8 lakh+/month (consultant, Hyderabad corporate hospitals)"}

SPEC_GOVT = [("Civil Assistant Surgeon Specialist", "MHSRB (TVVP / DPH hospitals)", "PG in specialty + TS Medical Council registration; pay approx ₹58,850–1,37,050"),
             ("Assistant Professor", "DME Telangana (Govt Medical Colleges), NIMS", "MD/MS + NMC teaching norms"),
             ("Specialist / Senior Resident", "AIIMS Bibinagar, ESIC, Railways, CGHS, Singareni hospitals", "PG degree"),
             ("Specialist Medical Officer", "UPSC / Armed Forces Medical Services / CAPFs", "PG degree")]
SUPER_GOVT = [("Assistant Professor (Super-speciality)", "NIMS Hyderabad, Osmania/Gandhi Medical Colleges (DME)", "DM/MCh"),
              ("Consultant / Faculty", "AIIMS, ESIC super-speciality hospitals, MNJ Cancer Hospital", "DM/MCh")]

PRIV_HOSP = "Apollo, Yashoda, KIMS, Care, AIG, Continental, Rainbow, Star, Medicover, Basavatarakam Cancer Hospital"


def spec_docs(base):
    for kind, lst, yrs in (("MD", MD, "3 years"), ("MS", MS, "3 years")):
        sub = f"{base}/{kind}_Specialist"
        for name, fn, common, treats, nxt, typ in lst:
            career_doc(f"{sub}/{fn}.docx", f"{name} – {common}", dict(
                about=[f"Commonly called: {common}.", "Post-graduate specialisation after MBBS."],
                duration=f"{yrs} (MD/MS). A DNB (National Board) of the same name is equal.",
                eligibility=["MBBS + 1-year internship completed + permanent registration."],
                admission=["NEET-PG (NBEMS). 50% All India Quota via MCC; 50% state quota via KNRUHS (Telangana).", "NExT may replace NEET-PG in future; NEET-PG continues for now."],
                extra=[("What this doctor treats / does", treats), ("Next step (super-speciality)", [nxt])],
                private=[(f"Consultant {common}", PRIV_HOSP, SAL[typ]), ("Own clinic / practice", "Self", "Depends on practice")] +
                        ([("Medical Advisor / Clinical Research Physician", "Pharma companies, CROs", "₹1–2.5 lakh")] if typ != "clinical" else []),
                govt=SPEC_GOVT), subtitle="MBBS → NEET-PG → Specialisation")
    for kind, lst in (("DM", DM), ("MCh", MCH)):
        sub = f"{base}/Super_Speciality_{kind}"
        for name, fn, common, treats in lst:
            career_doc(f"{sub}/{fn}.docx", f"{name} – {common}", dict(
                about=[f"Commonly called: {common}.", "Super-speciality = the highest level of clinical training in India."],
                duration="3 years after MD/MS",
                eligibility=["DM: MD in the feeder specialty (e.g. MD Medicine/Paediatrics)." if kind == "DM" else "MCh: MS in the feeder specialty (e.g. MS General Surgery/ENT/OBG)."],
                admission=["NEET-SS (NBEMS) → MCC counselling (all seats)."],
                extra=[("What this doctor treats / does", treats),
                       ("Full route", ["10th → Inter BiPC → NEET-UG → MBBS (5.5 yrs) → NEET-PG → MD/MS (3 yrs) → NEET-SS → " + kind + " (3 yrs)", "Total about 11–12 years after Inter"])],
                private=[(f"Consultant {common}", PRIV_HOSP, SAL["super"])], govt=SUPER_GOVT), subtitle="MBBS → MD/MS → Super-speciality")

    make(f"{base}/00_All_Doctor_Specialisations_List.docx", "All Doctor Specialisations after MBBS", [
        ("How specialisation works", ["MBBS (general doctor) → MD/MS/DNB (specialist, 3 yrs) → DM/MCh (super-specialist, 3 yrs).",
                                      "PG Diplomas (2 yrs) also exist in some branches (e.g. DCH, DGO, DA). NMC is converting most diplomas into degrees."]),
        ("MD branches (3 years)", [("table", ["Course", "Doctor is called", "Type"], [[m[0], m[2], {"clinical": "Clinical", "para": "Para-clinical", "pre": "Pre-clinical"}[m[5]]] for m in MD])]),
        ("MS branches (3 years)", [("table", ["Course", "Doctor is called"], [[m[0], m[2]] for m in MS])]),
        ("DM super-specialities (after MD)", [("table", ["Course", "Doctor is called"], [[m[0], m[2]] for m in DM])]),
        ("MCh super-specialities (after MS)", [("table", ["Course", "Doctor is called"], [[m[0], m[2]] for m in MCH])]),
        ("Each specialisation has its own Word file", ["See the sub-folders MD_Specialist, MS_Specialist, Super_Speciality_DM and Super_Speciality_MCh."]),
    ], subtitle="MBBS → Specialist → Super-specialist")


def mbbs(base):
    b = f"{base}/01_MBBS_Doctor"
    career_doc(f"{b}/01_About_MBBS.docx", "MBBS – Bachelor of Medicine & Bachelor of Surgery", dict(
        about=["The main course to become a modern-medicine (allopathy) doctor. After MBBS + internship + registration you can treat patients and prescribe all medicines."],
        duration="5.5 years = 4.5 years study + 1 year compulsory rotating internship (CRMI)",
        eligibility=["Inter BiPC with English; 50% in PCB (40% SC/ST/BC).", "NEET-UG qualified.", "Age 17+."],
        admission=TG_COUNSEL, colleges=["Govt: Osmania Medical College, Gandhi Medical College, Kakatiya MC (Warangal), and 30+ district Govt Medical Colleges",
                                         "Central: AIIMS Bibinagar, ESIC Medical College Sanathnagar", "Private: Kamineni, Deccan, Mallareddy, MediCiti, Apollo, Bhaskar, etc."],
        extra=[("Year-wise subjects", [("table", ["Phase", "Subjects"], [
            ["Phase I (1st yr)", "Anatomy, Physiology, Biochemistry (+ Foundation course, Family Adoption Programme)"],
            ["Phase II (2nd yr)", "Pathology, Microbiology, Pharmacology, Forensic Medicine & Toxicology"],
            ["Phase III Part 1", "Community Medicine, ENT, Ophthalmology"],
            ["Phase III Part 2", "General Medicine, General Surgery, OBG, Paediatrics (+ Orthopaedics, Dermatology, Psychiatry, Anaesthesia, Radiology clinical postings)"],
            ["Internship (1 yr)", "Rotation in all departments, rural health posting"]])])],
        pass_rules=MED_PASS_MBBS,
        private=[("Duty Medical Officer / RMO", PRIV_HOSP, "₹60,000–1,00,000"), ("Casualty Medical Officer", "Corporate & multi-speciality hospitals", "₹70,000–1,20,000"),
                 ("Tele-consultation Doctor", "Practo, Tata 1mg, Apollo 24/7", "₹50,000–1,00,000"), ("Medical Advisor / Medical Writer", "Pharma, CROs, GCCs", "₹60,000–1,20,000"),
                 ("Company / Industrial Medical Officer", "Pharma & manufacturing plants", "₹70,000–1,20,000")],
        govt=[("Civil Assistant Surgeon / Medical Officer", "MHSRB Telangana (DPH, TVVP)", "MBBS + TS Medical Council regn; age 18–46 (check notification); pay approx ₹58,850–1,37,050"),
              ("Medical Officer – Basti Dawakhana / Palle Dawakhana / NHM", "Telangana NHM (contract)", "MBBS"),
              ("Medical Officer – CMS", "UPSC Combined Medical Services (Railways, CGHS, Ordnance)", "MBBS; age up to 32"),
              ("Short Service Commission – Army Medical Corps", "Armed Forces Medical Services", "MBBS (NEET-PG score + interview)"),
              ("Insurance Medical Officer", "ESIC", "MBBS"),
              ("Medical Officer", "CAPFs (ITBP-led recruitment), Singareni, TGSRTC, Railways", "MBBS"),
              ("Tutor / Junior Resident", "Govt Medical Colleges, AIIMS", "MBBS")],
        self_emp=["Own clinic (after registration) – general practice", "Diagnostic centre or nursing home (with partners)"],
        higher=["NEET-PG → MD/MS/DNB (see folder 03_Specialisations)", "MPH, MBA Hospital Management", "USMLE (USA), PLAB/UKMLA (UK), DHA/DOH licence (UAE)"],
        route=["Class 11–12 BiPC: NEET coaching (NCERT Biology is the key)", "NEET-UG → KNRUHS/MCC counselling", "MBBS 4.5 yrs → internship 1 yr → TSMC permanent registration",
               "Job as MO OR prepare NEET-PG → MD/MS → DM/MCh"],
        tips=["Telangana has a high number of MBBS seats per population. Govt seats give the best value.", "Avoid unrecognised foreign colleges – check the NMC FMGL rules (54-month course, 12-month internship, same university)."]),
        subtitle="BiPC → NEET → Doctor")

    career_doc(f"{b}/02_MBBS_Abroad_and_FMGE.docx", "MBBS Abroad – Rules & FMGE/NExT", dict(
        about=["Many Telangana students study MBBS in Russia, Georgia, Kazakhstan, Kyrgyzstan, Uzbekistan, Philippines, Bangladesh, Nepal."],
        eligibility=["NEET-UG qualification is compulsory even for abroad MBBS.", "NMC Foreign Medical Graduate Licentiate Regulations 2021: course of at least 54 months in English, 12-month internship in the same institution, registration in that country."],
        extra=[("After return", ["Pass FMGE (pass mark 150/300) – or NExT when it starts.", "Then 1–2 years internship in India (as directed by NMC) → registration.", "FMGE pass rates are often low (about 20–30%), so choose good universities."]),
               ("Cost", ["About ₹20–50 lakh total, depending on country."])],
        private=[("Same as Indian MBBS after registration", PRIV_HOSP, "₹50,000–1,00,000")], govt=[("Same as Indian MBBS after registration", "MHSRB / UPSC", "Needs FMGE/NExT pass + Indian internship + NMC/State registration")]))

    career_doc(f"{b}/03_Specialisations/01_NEET_PG_and_PG_Admission.docx", "NEET-PG – How to Become a Specialist", dict(
        about=["NEET-PG (by NBEMS) is the entrance for MD/MS/DNB/PG Diploma. NExT (National Exit Test) has been postponed; NEET-PG continues for now."],
        eligibility=["MBBS + internship completed by the cut-off date."],
        admission=["50% All-India seats: MCC counselling", "50% State seats: KNRUHS (Telangana)", "INI-CET for AIIMS/JIPMER/PGIMER"],
        extra=[("Pattern (recent)", ["200 MCQs, 800 marks, +4/−1, single computer-based session (check latest)"])],
        tips=["Clinical branches with high demand: Radiology, Dermatology, General Medicine, Paediatrics, OBG, Orthopaedics."]))
    spec_docs(f"{b}/03_Specialisations")


def dental_ayush(base):
    b = f"{base}/02_BDS_Dentist"
    career_doc(f"{b}/01_About_BDS.docx", "BDS – Bachelor of Dental Surgery (Dentist)", dict(
        about=["Dentist for teeth, gums and mouth. You register with the Dental Council of India / Telangana State Dental Council."],
        duration="5 years (4 years + 1 year internship)", eligibility=["Inter BiPC 50% (40% reserved); NEET-UG."],
        admission=["NEET-UG → KNRUHS counselling (state) / MCC (AIQ)"], colleges=["Govt Dental College Hyderabad (Afzalgunj)", "Private dental colleges (Sri Sai, Panineeya, Mamata, Kamineni, etc.)"],
        subjects=["Dental Anatomy, Dental Materials", "Oral Pathology", "Prosthodontics, Conservative Dentistry, Orthodontics", "Oral Surgery, Periodontics, Pedodontics", "General Medicine & Surgery basics"],
        pass_rules=["DCI regulations: 50% in theory and 50% in practical per subject (approx)."],
        private=[("Associate Dentist", "Dental chains (Clove, FMS, Partha), clinics", "₹25,000–60,000"), ("Dental Consultant (with MDS)", "Hospitals, chains", "₹80,000–2 lakh"),
                 ("Clinical Research / Medical Coding", "CROs, GCCs", "₹25,000–40,000")],
        govt=[("Dental Assistant Surgeon", "MHSRB (TVVP / DPH)", "BDS + registration"), ("Dental Surgeon", "Army Dental Corps, Railways, ESIC, CGHS", "BDS/MDS"), ("Assistant Professor", "Govt Dental College", "MDS")],
        self_emp=["Own dental clinic (most common path)"], higher=["MDS via NEET-MDS (3 years)", "MPH, MBA Healthcare"],
        extra=[("MDS specialisations (3 years each)", [("table", ["MDS branch", "Specialist does"], [
            ["Orthodontics", "Braces, aligners – teeth alignment"], ["Prosthodontics", "Dentures, crowns, implants"],
            ["Conservative Dentistry & Endodontics", "Root canal, fillings"], ["Oral & Maxillofacial Surgery", "Tooth extraction, jaw surgery, face trauma"],
            ["Periodontology", "Gum diseases, implants"], ["Pedodontics", "Children's dentistry"], ["Oral Pathology", "Lab diagnosis of mouth diseases"],
            ["Oral Medicine & Radiology", "Mouth disease diagnosis, dental X-rays"], ["Public Health Dentistry", "Community dental programmes"]])])]),
        subtitle="BiPC → NEET → Dentist")

    AY = [
        ("03_BAMS_Ayurveda", "BAMS – Ayurvedic Doctor", "Ayurveda (Indian traditional medicine)", "Dr. B.R.K.R. Govt Ayurvedic College, Hyderabad (Erragadda) + private colleges",
         ["Padartha Vigyan, Rachana & Kriya Sharir", "Dravyaguna (herbal medicines), Rasashastra", "Kayachikitsa (medicine), Shalya (surgery), Panchakarma"], "AYUSH Medical Officer (Ayurveda)"),
        ("04_BHMS_Homeopathy", "BHMS – Homeopathic Doctor", "Homeopathy", "Govt Homeopathic Medical College, Ramanthapur (Hyderabad) + private colleges",
         ["Homoeopathic Materia Medica", "Organon of Medicine", "Repertory", "Anatomy, Physiology, Pathology, Medicine"], "AYUSH Medical Officer (Homeopathy)"),
        ("05_BUMS_Unani", "BUMS – Unani Doctor", "Unani medicine", "Govt Nizamia Tibbi College, Charminar (Hyderabad) + private",
         ["Kulliyat (basic principles)", "Ilmul Advia (pharmacology)", "Moalijat (medicine)", "Ilaj bit Tadbeer (regimenal therapy)"], "AYUSH Medical Officer (Unani)"),
        ("06_BNYS_Naturopathy_Yoga", "BNYS – Naturopathy & Yoga Doctor", "Naturopathy & Yoga", "Govt Nature Cure Hospital Begumpet (Hyderabad) – Govt Naturopathy college + private",
         ["Yoga therapy", "Hydrotherapy, Diet therapy", "Anatomy, Physiology, Pathology"], "Naturopathy / Yoga Medical Officer"),
        ("07_BSMS_Siddha", "BSMS – Siddha Doctor", "Siddha medicine (mainly in Tamil Nadu)", "Mostly in Tamil Nadu/Kerala colleges via AACCC counselling",
         ["Siddha basic principles", "Siddha pharmacology", "Varmam therapy"], "Siddha Medical Officer (mainly Tamil Nadu)"),
    ]
    for fn, title, sys_, cols, subj, govt_post in AY:
        career_doc(f"{base}/{fn}/About_{fn[3:]}.docx", title, dict(
            about=[f"Doctor of {sys_}. Regulated by NCISM / NCH. Registration with the Telangana AYUSH (Ayurveda, Unani, Homeopathy, Naturopathy) Board.",
                   "AYUSH doctors practise their own system. Prescribing modern (allopathic) medicines is NOT generally allowed except where specific state rules permit."],
            duration="5.5 years (4.5 years + 1 year internship)", eligibility=["Inter BiPC 50% (40% reserved); NEET-UG."],
            admission=["NEET-UG → KNRUHS AYUSH counselling (state) / AACCC (all India & central institutes)"], colleges=[cols], subjects=subj,
            pass_rules=["NCISM/NCH regulations: 50% in theory and practical per subject (approx)."],
            private=[(f"{sys_.split('(')[0].strip()} Consultant", "Wellness centres, AYUSH hospitals, Patanjali/Kerala Ayurveda/Dr Batra's clinics", "₹25,000–60,000"),
                     ("Medical Officer (duty doctor)", "Private hospitals (non-prescribing roles)", "₹25,000–45,000"),
                     ("Medical Coding / Clinical Research", "GCCs, CROs", "₹20,000–35,000")],
            govt=[(govt_post, "Telangana AYUSH Dept (via MHSRB/TGPSC)", "Degree + registration"), ("Medical Officer (AYUSH)", "NHM (Palle Dawakhana / AYUSH wings), CGHS, ESIC, Railways", "Degree"),
                  ("Research Officer", "CCRAS / CCRH / CCRUM (central research councils – Hyderabad units)", "PG")],
            self_emp=["Own clinic / panchakarma or wellness centre"], higher=["MD/MS (AYUSH) via AIAPGET"]), subtitle="BiPC → NEET → AYUSH Doctor")


def doctors_overview(base):
    make(f"{base}/00_NEET_UG_and_Telangana_Counselling.docx", "NEET-UG & Telangana Medical Counselling", [
        ("NEET-UG exam", NEET), ("Courses through NEET", ["MBBS, BDS, BAMS, BHMS, BUMS, BSMS, BNYS", "BVSc (15% all-India seats)", "B.Sc Nursing in Military Nursing Service (women)", "Some central nursing / allied courses (AIIMS)"]),
        ("Telangana counselling", TG_COUNSEL),
        ("Preparation plan", ["Class 11 + 12 NCERT line by line (Biology = 360 marks)", "Daily MCQ practice + weekly full mock tests", "Previous 10 years NEET papers", "Target: 600+ for Govt MBBS in Telangana (cut-offs change yearly)"]),
    ], subtitle="BiPC → Doctor courses")

    make(f"{base}/00_Types_of_Doctors_Explained.docx", "Types of Doctors – Who is a Real Doctor?", [
        ("All doctor types in India", [("table", ["Title", "Course", "Years after Inter", "Can prescribe allopathy?"], [
            ["General Doctor (Allopathy)", "MBBS", "5.5", "YES"], ["Specialist (Physician, Surgeon, Gynaecologist...)", "MBBS + MD/MS", "8.5", "YES"],
            ["Super-specialist (Cardiologist, Neurosurgeon...)", "MBBS + MD/MS + DM/MCh", "11.5", "YES"], ["Dentist", "BDS (+MDS)", "5 (+3)", "Dental medicines only"],
            ["Ayurvedic doctor", "BAMS", "5.5", "No (own system)"], ["Homeopathic doctor", "BHMS", "5.5", "No (own system)"], ["Unani doctor", "BUMS", "5.5", "No (own system)"],
            ["Naturopathy/Yoga doctor", "BNYS", "5.5", "No"], ["Siddha doctor", "BSMS", "5.5", "No"], ["Veterinary doctor (animals)", "BVSc & AH", "5.5", "Animal medicines"],
            ["Physiotherapist", "BPT", "4.5", "No – therapy only"], ["Doctor of Pharmacy", "Pharm-D", "6", "No – clinical pharmacist"],
            ["Optometrist", "B.Sc Optometry", "4", "No – eye tests & glasses"],
            ["RMP / PMP (village practitioner)", "No recognised medical degree", "—", "NO – see RMP folder"]])]),
        ("Nursing & technicians (not doctors, but essential health workers)", ["ANM/MPHW, GNM, B.Sc Nursing", "Lab Technician, Radiographer, OT/Anaesthesia technician, Dialysis technician, ECG technician", "Pharmacist (D.Pharm/B.Pharm)"]),
    ], subtitle="BiPC → Health careers")


def nursing(base):
    b = f"{base}/02_Nursing"
    NGOV = [("Nursing Officer (Staff Nurse)", "MHSRB Telangana (DME, TVVP, DPH)", "GNM / B.Sc Nursing + TG Nursing Council regn; age 18–46 (check notification); pay approx ₹36,750–1,06,990"),
            ("Nursing Officer", "AIIMS (NORCET) – incl. AIIMS Bibinagar", "B.Sc Nursing / GNM + 2 yrs exp; Level-7 ₹44,900+"),
            ("Staff Nurse", "ESIC, Railways (RRB Paramedical), CGHS, NIMS", "GNM / B.Sc Nursing"),
            ("Community Health Officer (CHO)", "Telangana NHM – Palle Dawakhana / Ayushman Arogya Mandir", "B.Sc Nursing / GNM + CCH certificate (contract)"),
            ("Military Nursing Service (Lieutenant)", "Indian Army", "B.Sc Nursing (MNS) – women"),
            ("Nursing Tutor / Lecturer", "Govt nursing colleges", "M.Sc Nursing")]
    NPRIV = [("Staff Nurse", PRIV_HOSP, "₹18,000–30,000"), ("ICU / OT / Dialysis Nurse", "Corporate hospitals", "₹22,000–40,000"),
             ("Home Care Nurse", "Portea, Care24, home-care agencies", "₹18,000–30,000"), ("Nurse abroad (Gulf/UK/USA)", "See Nursing_Jobs_Abroad file", "₹1–3 lakh+")]
    career_doc(f"{b}/00_All_Nursing_Paths.docx", "Nursing – All Paths after Inter", dict(
        about=["Nursing is one of the most job-secure health careers in India and abroad."],
        extra=[("Nursing courses", [("table", ["Course", "Duration", "Eligibility", "Admission (Telangana)"], [
            ["ANM / MPHW (Female)", "2 years", "Inter (any group)", "Merit – Commissioner of Health & FW / private schools"],
            ["GNM – General Nursing & Midwifery", "3 years", "Inter (any group, science preferred), age 17–35", "Merit on Inter marks"],
            ["B.Sc Nursing", "4 years", "Inter BiPC + English", "TG EAPCET (BiPC) score → KNRUHS counselling"],
            ["Post-Basic B.Sc Nursing", "2 years", "GNM + registration", "KNRUHS"],
            ["M.Sc Nursing", "2 years", "B.Sc Nursing + 1 yr exp", "KNRUHS PG entrance"],
            ["Nurse Practitioner in Critical Care", "2 years", "B.Sc Nursing + exp", "INC-approved institutes"]])]),
               ("Path diagram", ["Inter → ANM (2 yrs) → village health worker", "Inter → GNM (3 yrs) → Staff Nurse → Post-Basic B.Sc → M.Sc", "Inter BiPC → B.Sc Nursing (4 yrs) → Nursing Officer → M.Sc → Tutor/Professor"])],
        private=NPRIV, govt=NGOV), subtitle="After Inter → Nursing")
    career_doc(f"{b}/01_ANM_MPHW_Female/About_ANM.docx", "ANM / MPHW (Female) – Auxiliary Nurse Midwife", dict(
        about=["Village/urban health worker – mother & child care, vaccination, family planning, health surveys."],
        duration="2 years", eligibility=["Inter pass (any group) as per INC norms; women only (MPHW-F).", "Age 17–35 (approx)."],
        admission=["Govt ANM training centres (Commissioner of Health & Family Welfare) and private INC-approved schools – merit based."],
        subjects=["Community Health Nursing", "Health Promotion", "Primary Health Care", "Child Health", "Midwifery"],
        pass_rules=["INC: about 50% in each subject (theory + practical)."],
        private=[("Nurse Aide / Ward Nurse", "Private hospitals, nursing homes", "₹12,000–18,000")],
        govt=[("Multi-Purpose Health Assistant (Female) – MPHA(F)", "MHSRB Telangana / DPH", "ANM/MPHW(F) + TG Nursing Council registration"), ("Second ANM (contract)", "NHM", "ANM")],
        higher=["GNM (some states allow ANM→GNM lateral)", "B.Sc Nursing / Post-Basic"]), subtitle="Nursing")
    career_doc(f"{b}/02_GNM_General_Nursing_Midwifery/About_GNM.docx", "GNM – General Nursing & Midwifery", dict(
        about=["A 3-year diploma that makes you a Registered Nurse & Registered Midwife (RN-RM)."],
        duration="3 years", eligibility=["Inter pass with English (science preferred) – about 40% marks.", "Age 17–35."],
        admission=["Merit on Inter marks – Govt GNM schools (attached to teaching hospitals) & private nursing schools."],
        subjects=["Anatomy & Physiology, Microbiology", "Fundamentals of Nursing", "Medical-Surgical Nursing", "Child Health, Mental Health Nursing", "Midwifery & Gynaecology", "Community Health Nursing"],
        pass_rules=["INC: about 50% per subject (theory & practical) – check the latest INC syllabus."],
        private=NPRIV, govt=NGOV, higher=["Post-Basic B.Sc Nursing (2 yrs)", "Nursing abroad"],
        tips=["INC has discussed phasing GNM into B.Sc Nursing. Check if GNM admissions continue in your year."]), subtitle="Nursing")
    career_doc(f"{b}/03_BSc_Nursing/About_BSc_Nursing.docx", "B.Sc Nursing (4 years)", dict(
        about=["A degree-level nursing course. It is preferred for govt Nursing Officer, AIIMS, the Army and abroad jobs."],
        duration="4 years (including internship)", eligibility=["Inter BiPC with English; Telangana local status rules apply.", "Age 17+."],
        admission=["Telangana: TG EAPCET (BiPC – Agriculture & Pharmacy stream) score with percentile cut-off → KNRUHS web counselling (2025 rule).",
                   "AIIMS B.Sc (Hons) Nursing: AIIMS entrance; Military Nursing Service: NEET-UG + interview."],
        colleges=["Govt College of Nursing (Hyderabad, Warangal, other Govt Medical Colleges)", "NIMS College of Nursing", "Private nursing colleges under KNRUHS"],
        subjects=["Anatomy, Physiology, Biochemistry, Nutrition", "Nursing Foundations, Medical-Surgical Nursing", "Child Health, Mental Health, Community Health Nursing", "Midwifery & OBG Nursing", "Nursing Research & Management"],
        pass_rules=["INC (2021 syllabus): about 50% in each course (internal + external), 50% practical."],
        private=NPRIV + [("Clinical Instructor", "Nursing colleges", "₹20,000–35,000")], govt=NGOV,
        higher=["M.Sc Nursing", "Nurse Practitioner", "MHA / MPH"]), subtitle="Nursing")
    career_doc(f"{b}/04_Post_Basic_and_MSc_Nursing/About_PostBasic_MSc_Nursing.docx", "Post-Basic B.Sc Nursing, M.Sc Nursing & Nurse Practitioner", dict(
        extra=[("Post-Basic B.Sc Nursing", ["2 years for GNM nurses → degree level", "KNRUHS admission"]),
               ("M.Sc Nursing", ["2 years; specialities: Medical-Surgical, Child Health, OBG, Psychiatric, Community Health Nursing", "Needed for Nursing Tutor / Lecturer / Principal posts"]),
               ("Nurse Practitioner in Critical Care", ["2-year residency programme for ICU nursing (INC)"])],
        private=[("Nursing Supervisor / Nursing Superintendent", "Corporate hospitals", "₹40,000–80,000"), ("Nursing Faculty", "Nursing colleges", "₹30,000–60,000")],
        govt=[("Nursing Superintendent / Tutor / Lecturer", "MHSRB, DME, NIMS", "M.Sc Nursing")]), subtitle="Nursing")
    career_doc(f"{b}/05_Nursing_Jobs_Abroad/Nursing_Abroad_Gulf_UK_USA.docx", "Nursing Jobs Abroad – Gulf, UK, USA, Europe", dict(
        about=["Indian nurses are in high demand worldwide. Plan the licensing exams early."],
        extra=[("Country-wise requirements", [("table", ["Country", "Exam / licence", "Other needs", "Approx salary"], [
            ["UAE – Dubai", "DHA licence (Prometric exam) + DataFlow verification", "2 years experience usually", "AED 5,000–12,000/month"],
            ["UAE – Abu Dhabi", "DOH licence (Prometric)", "Experience", "AED 6,000–14,000"],
            ["Saudi Arabia", "SCFHS registration (Prometric)", "Experience", "SAR 5,000–10,000"],
            ["Qatar / Oman / Kuwait", "QCHP / OMSB / MOH exams", "Experience", "Varies"],
            ["UK", "NMC CBT + OSCE", "IELTS 7.0 or OET B", "£28,000–35,000/year"],
            ["USA", "NCLEX-RN + CGFNS/VisaScreen", "IELTS/TOEFL", "$60,000–90,000/year"],
            ["Australia / NZ", "AHPRA / NCNZ + OSCE", "IELTS/OET", "AUD 70,000+"],
            ["Germany", "Recognition + German B1/B2", "Language course", "€2,500–3,500/month"]])]),
               ("Safety", ["Use TOMCOM (Telangana Overseas Manpower Company) or registered recruiting agents only.", "Check the eMigrate (MEA) registration of agents."])]), subtitle="Nursing")


def pharmacy(base, sub="03_Pharmacy"):
    b = f"{base}/{sub}" if sub else base
    PGOV = [("Pharmacist Grade-II", "MHSRB Telangana", "D.Pharm/B.Pharm/Pharm-D + TG Pharmacy Council regn; age 18–46 (check notification)"),
            ("Drug Inspector", "TGPSC (Drug Control Administration)", "B.Pharm / Pharm-D / M.Pharm"), ("Drug Inspector (central)", "UPSC – CDSCO", "B.Pharm/M.Pharm"),
            ("Pharmacist", "Railways (RRB Paramedical), ESIC, CGHS, Army (Group C)", "D.Pharm/B.Pharm"), ("Assistant Professor", "Govt pharmacy colleges", "M.Pharm/PhD")]
    PPRIV = [("QC / QA Executive", "Dr. Reddy's, Aurobindo, Hetero, Granules, MSN, Divi's", "₹18,000–30,000"), ("Production Officer", "Pharma plants", "₹18,000–28,000"),
             ("Medical Representative", "Pharma sales", "₹18,000–30,000 + incentives"), ("Hospital / Clinical Pharmacist", PRIV_HOSP, "₹18,000–35,000"),
             ("Pharmacovigilance / Drug Safety Associate", "IQVIA, Accenture, Cognizant, Novartis GCC", "₹22,000–35,000"), ("Regulatory Affairs Associate", "Pharma companies", "₹20,000–35,000"),
             ("Retail Pharmacist", "Apollo Pharmacy, MedPlus", "₹15,000–22,000")]
    career_doc(f"{b}/01_D_Pharm/About_D_Pharm.docx", "D.Pharm – Diploma in Pharmacy", dict(
        about=["A 2-year diploma that qualifies you as a registered pharmacist. You can open a medical shop (drug licence needs a registered pharmacist)."],
        duration="2 years + 500 hours practical training", eligibility=["Inter MPC or BiPC."], admission=["Through DOST / PCI-approved colleges (check annual Telangana notification)."],
        subjects=["Pharmaceutics, Pharmaceutical Chemistry, Pharmacognosy", "Human Anatomy & Physiology", "Pharmacology, Community Pharmacy, Hospital Pharmacy"],
        pass_rules=["PCI ER-2020: about 40% per subject (theory & practical separately)", "PCI has notified a D.Pharm Exit Examination – check if it applies to your batch."],
        private=PPRIV, govt=PGOV, self_emp=["Own medical/pharmacy store"], higher=["B.Pharm lateral entry (2nd year) via TG ECET (Pharmacy)"]), subtitle="Pharmacy")
    career_doc(f"{b}/02_B_Pharm/About_B_Pharm.docx", "B.Pharm – Bachelor of Pharmacy", dict(
        about=["A 4-year degree in medicines – manufacturing, quality, research and dispensing. Hyderabad is called the 'Bulk Drug Capital of India'."],
        duration="4 years", eligibility=["Inter MPC or BiPC."], admission=["TG EAPCET (MPC students via Engineering stream rank, BiPC via A&P stream) → TGCHE counselling."],
        colleges=["University College of Pharmaceutical Sciences (KU, Warangal), OU College of Technology, JNTUH Sultanpur, NIPER Hyderabad (PG)", "Many private pharmacy colleges"],
        subjects=["Pharmaceutics, Medicinal Chemistry", "Pharmacology, Pharmacognosy", "Pharmaceutical Analysis", "Biopharmaceutics, Industrial Pharmacy", "Pharmaceutical Jurisprudence"],
        pass_rules=["PCI B.Pharm regulations: 50% in each subject (internal + end exam)."],
        private=PPRIV, govt=PGOV, self_emp=["Pharmacy store, pharma distribution / franchise"],
        higher=["M.Pharm via GPAT / TG PGECET (NIPER Hyderabad via NIPER JEE)", "MBA Pharma Management", "PG Diploma in Clinical Research"]), subtitle="Pharmacy")
    career_doc(f"{b}/03_Pharm_D/About_Pharm_D.docx", "Pharm-D – Doctor of Pharmacy", dict(
        about=["A 6-year clinical pharmacy programme (5 years + 1 year internship). Graduates may use the 'Dr.' prefix but cannot prescribe."],
        duration="6 years", eligibility=["Inter MPC or BiPC."], admission=["TG EAPCET → counselling"],
        subjects=["All B.Pharm subjects + Clinical Pharmacy, Pharmacotherapeutics", "Hospital rotations, clinical research"], pass_rules=["PCI Pharm-D regulations: 50% per subject"],
        private=[("Clinical Pharmacist", PRIV_HOSP, "₹25,000–45,000"), ("Pharmacovigilance / Clinical Research", "CROs, GCCs", "₹25,000–45,000"),
                 ("Medical Writer / Coder", "Healthcare GCCs", "₹25,000–40,000")], govt=PGOV,
        higher=["Abroad: Pharm-D is accepted for some licensing routes (USA FPGEE etc.)", "PhD"]), subtitle="Pharmacy")


AHS = [  # (folder, name, what, govt post)
    ("01_BPT_Physiotherapy", "BPT – Bachelor of Physiotherapy (4.5 yrs incl. internship)", "Treats pain, stroke, fractures, sports injuries with exercise & electrotherapy", "Physiotherapist – MHSRB / TVVP, Railways, ESIC, Sports Authority"),
    ("02_BSc_MLT_Medical_Lab_Technology", "B.Sc Medical Laboratory Technology (MLT)", "Performs blood, urine, culture & biochemistry tests", "Lab Technician Gr-II – MHSRB; Railways, ESIC, blood banks"),
    ("03_BSc_Anaesthesia_Technology", "B.Sc Anaesthesia Technology", "Assists anaesthetists – machines, monitoring, ICU", "Anaesthesia Technician – TVVP, DME hospitals, NIMS"),
    ("04_BSc_Operation_Theatre_Technology", "B.Sc Operation Theatre Technology", "Prepares OT, sterilisation, surgical assistance", "OT Technician / Assistant – Govt hospitals"),
    ("05_BSc_Cardiac_Cardiovascular_Technology", "B.Sc Cardiac & Cardiovascular Technology", "ECG, ECHO, TMT, Cath-lab assistance", "Cardiology Technician – NIMS, Gandhi, Osmania, Railways"),
    ("06_BSc_Renal_Dialysis_Technology", "B.Sc Renal Dialysis Technology", "Runs dialysis machines for kidney patients", "Dialysis Technician – Aarogyasri / NHM dialysis centres (high demand)"),
    ("07_BSc_Optometry", "B.Sc Optometry", "Eye testing, glasses & contact lenses, assisting eye surgeons", "Ophthalmic Assistant / Optometrist – NPCB, RBSK, Kanti Velugu programmes"),
    ("08_BSc_Respiratory_Therapy", "B.Sc Respiratory Therapy", "Ventilators, oxygen therapy, lung function tests", "Respiratory Therapist – Govt ICUs, NIMS"),
    ("09_BSc_Neuro_Science_Technology", "B.Sc Neuro-Science Technology", "EEG, EMG, nerve conduction studies", "Neuro Technician – NIMS, teaching hospitals"),
    ("10_BSc_Critical_Care_Technology", "B.Sc Critical Care Technology", "ICU equipment and patient monitoring", "ICU Technician – Govt hospitals"),
    ("11_BSc_Radiology_Imaging_Technology", "B.Sc Radiology & Imaging Technology", "X-ray, CT, MRI, ultrasound assistance", "Radiographer – MHSRB, Railways, ESIC, TVVP"),
    ("12_BSc_Audiology_Speech_Therapy", "B.Sc Audiology & Speech-Language Pathology (BASLP)", "Hearing tests, hearing aids, speech therapy (needs RCI registration)", "Audiologist / Speech Therapist – Govt hospitals, DEIC (RBSK), special schools"),
    ("13_BSc_Medical_Records_Science", "B.Sc Medical Record Science", "Patient records, coding, hospital data", "Medical Record Officer / Technician – MHSRB, Govt hospitals"),
    ("14_BSc_Nuclear_Medicine_Technology", "B.Sc Nuclear Medicine Technology", "PET-CT and isotope scan handling", "Nuclear Medicine Technologist – NIMS, MNJ Cancer Hospital, BARC-linked units"),
    ("15_BSc_Radiotherapy_Technology", "B.Sc Radiotherapy Technology", "Operates cancer radiotherapy machines (LINAC)", "Radiotherapy Technician – MNJ Cancer Hospital, NIMS"),
]

TGPMB = [  # (folder, name, what)
    ("01_DMLT_Medical_Lab_Technician", "DMLT – Diploma in Medical Lab Technician", "Laboratory tests"),
    ("02_DMIT_Medical_Imaging_Technician", "DMIT – Diploma in Medical Imaging Technician", "X-ray, CT, MRI support"),
    ("03_DANS_Anaesthesia_Technician", "DANS – Diploma in Anaesthesia Technician", "Anaesthesia & ICU support"),
    ("04_DCARDIO_Cardiology_Technician", "D.Cardio – Diploma in Cardiology Technician", "ECG, ECHO, TMT"),
    ("05_DCLT_Cath_Lab_Technician", "DCLT – Diploma in Cath Lab Technician", "Angiography / cath-lab support"),
    ("06_DRGA_Radiographic_Assistant", "DRGA – Diploma in Radiographic Assistant", "X-ray assistance"),
    ("07_DDRA_Dark_Room_Assistant", "DDRA – Diploma in Dark Room Assistant", "Film processing / digital imaging room"),
    ("08_DECG_ECG_Technician", "DECG – Diploma in ECG Technician", "ECG recording"),
    ("09_DPERFU_Perfusion_Technician", "D.Perfusion – Diploma in Perfusion Technician", "Heart-lung machine during heart surgery"),
    ("10_DHFSM_Hospital_Food_Service_Mgmt", "DHFSM – Diploma in Hospital Food Service Management", "Patient diet & hospital kitchen"),
    ("11_DMST_Sterilisation_OT_Technician", "DMST – Diploma in Medical Sterilisation & OT Technician", "OT sterilisation & theatre support"),
    ("12_DDIALY_Dialysis_Technician", "D.Dialysis – Diploma in Dialysis Technician", "Dialysis machines"),
    ("13_DREST_Respiratory_Therapy_Technician", "D.REST – Diploma in Respiratory Therapy Technician", "Ventilator & oxygen therapy"),
]


def allied(base):
    b = f"{base}/04_Allied_Health_Degrees_KNRUHS"
    make(f"{b}/00_About_Allied_Health_Sciences.docx", "Allied Health Sciences (KNRUHS) – All Courses", [
        ("About", ["Allied health professionals are the technical team behind every doctor – lab, imaging, OT, dialysis, therapy.",
                   "Regulated nationally by NCAHP (National Commission for Allied & Healthcare Professions Act 2021).",
                   "Telangana: KNRUHS conducts admissions on state merit (Inter marks), with online application, merit list and web counselling."]),
        ("Courses", [("table", ["#", "Course", "Work"], [[i + 1, a[1], a[2]] for i, a in enumerate(AHS)])]),
        ("Duration & eligibility", ["B.Sc AHS: about 3–4 years including internship; BPT: 4.5 years.", "Inter BiPC (some courses accept MPC – check the KNRUHS prospectus)."]),
    ], subtitle="BiPC → Allied Health")
    for fn, name, what, gpost in AHS:
        career_doc(f"{b}/{fn}/About_{fn[3:]}.docx", name, dict(
            about=[f"Work: {what}."], duration="3–4 years incl. internship (BPT 4.5 years)", eligibility=["Inter BiPC (MPC for some courses) – check KNRUHS notification."],
            admission=["KNRUHS online application → state merit list → web counselling (Govt & private colleges)."],
            pass_rules=["KNRUHS regulations: about 50% per subject (theory + practical)."],
            private=[(name.split("–")[0].split("(")[0].strip().replace("B.Sc ", "") + " professional", PRIV_HOSP + ", diagnostic chains (Vijaya, Tenet, Lucid)", "₹15,000–30,000"),
                     ("Gulf / abroad jobs", "UAE, Saudi hospitals (DHA/DOH/SCFHS licence)", "AED 4,000–9,000")],
            govt=[(gpost.split(" – ")[0], gpost.split(" – ")[1] if " – " in gpost else "Govt", "Degree + registration with TG Paramedical Board / council")],
            higher=["M.Sc in the same field / MPT (for BPT)", "MHA – Hospital Administration", "MPH – Public Health"]), subtitle="BiPC → Allied Health Degree")

    p = f"{base}/05_Paramedical_Diplomas_TGPMB"
    make(f"{p}/00_About_Telangana_Paramedical_Board.docx", "Telangana State Paramedical Board (TGPMB) Diplomas", [
        ("About", ["2-year diploma courses after Inter BiPC or MPC.", "Offered in Govt Medical Colleges (DME) and private hospitals/institutes.",
                   "Admission: TGPMB notification → online application → merit (Inter marks) → counselling."]),
        ("All diplomas", [("table", ["#", "Diploma", "Work"], [[i + 1, t[1], t[2]] for i, t in enumerate(TGPMB)])]),
        ("Pass rule", ["Board exams at the end of each year – about 50% per subject (theory & practical). Confirm with TGPMB."]),
        ("After diploma", ["Register with TG Paramedical Board", "Jobs: technician posts in Govt & private hospitals", "Higher: B.Sc in the same field (lateral entry where allowed)"]),
    ], subtitle="After Inter → Paramedical Diploma")
    for fn, name, what in TGPMB:
        career_doc(f"{p}/{fn}/About_{fn[3:]}.docx", name, dict(
            about=[f"Work: {what}."], duration="2 years", eligibility=["Inter BiPC or MPC."], admission=["TGPMB notification → merit on Inter marks → counselling."],
            pass_rules=["About 50% per subject (check TGPMB)."],
            private=[("Technician", PRIV_HOSP + ", diagnostic centres", "₹12,000–22,000"), ("Gulf technician", "UAE/Saudi hospitals", "AED 3,000–6,000")],
            govt=[("Technician (relevant grade)", "MHSRB / TVVP / DME hospitals, Railways (RRB Paramedical), ESIC", "Diploma + TGPMB registration")],
            higher=["B.Sc Allied Health in same field"]), subtitle="Paramedical Diploma")


def rmp(base):
    b = f"{base}/06_RMP_PMP_Village_Doctor_Truth"
    make(f"{b}/01_RMP_PMP_Legal_Status.docx", "RMP / PMP 'Village Doctors' – Legal Facts Every Student Must Know", [
        ("Who are RMPs / PMPs?", ["RMP here means 'Rural Medical Practitioner' and PMP means 'Private Medical Practitioner' – people who give treatment in villages without a recognised medical degree.",
                                  "They are NOT Registered Medical Practitioners in law. 'RMP' does not mean 'registered'."]),
        ("What the law says", ["Under the National Medical Commission Act 2019 (Section 34), only a person registered with NMC/State Medical Council (MBBS or higher) may practise modern medicine.",
                               "Practising without registration: punishable with imprisonment up to 1 year and/or fine up to ₹5 lakh.",
                               "Prescribing antibiotics/steroids, giving injections, IV drips or running a 'clinic/hospital' without registration is illegal.",
                               "Telangana State Medical Council and the Drugs Control Administration conduct raids and file cases against unqualified practitioners."]),
        ("Government training (history)", ["Around 2015–2017, Telangana/AP proposed training RMPs/PMPs as 'Community Paramedics' (first-aid level, 6 months).",
                                           "Doctors' associations challenged this in court. It does NOT give a licence to treat patients as a doctor."]),
        ("Our advice", ["Do NOT pay for any 'RMP certificate course' – it gives no legal right to practise.", "Choose a recognised, legal health career instead (see next file)."]),
    ], subtitle="Health careers – Facts")
    make(f"{b}/02_Legal_Ways_to_Serve_Village_Health.docx", "Legal Ways to Work in Village Health Care", [
        ("Recognised options", [("table", ["Path", "Duration", "Role in village"], [
            ["MBBS", "5.5 yrs", "Doctor – PHC Medical Officer, own clinic"], ["BAMS/BHMS/BUMS", "5.5 yrs", "AYUSH doctor – own clinic legally"],
            ["B.Sc Nursing / GNM + CCH", "3–4 yrs", "Community Health Officer at Palle Dawakhana"], ["ANM / MPHW (F)", "2 yrs", "Village health worker (mother-child care)"],
            ["MPHW (Male) / Health Assistant", "Training course", "Disease control, malaria, sanitation"], ["D.Pharm / B.Pharm", "2–4 yrs", "Own medical shop (legal)"],
            ["Paramedical diploma (DMLT etc.)", "2 yrs", "Village diagnostic/lab centre"], ["EMT (108 ambulance)", "Short training", "Emergency first response"],
            ["ASHA worker", "Training", "Village health activist (women, NHM)"]])]),
        ("Why choose a legal path", ["Legal courses give a registration number – you can work in govt hospitals, private hospitals and abroad.", "Govt jobs (MHSRB, NHM) are open only to registered professionals.",
                                     "You avoid police cases, fines and closure of your clinic."]),
        ("Fast options for village service", ["Inter → ANM/MPHW (2 yrs) → Health worker at sub-centre", "Inter → D.Pharm (2 yrs) → own medical shop in the village",
                                              "Inter → DMLT (2 yrs) → village diagnostic lab", "Inter BiPC → B.Sc Nursing (4 yrs) + CCH → Community Health Officer at Palle Dawakhana"]),
    ], subtitle="Health careers – Legal paths")


def other_health(base):
    b = f"{base}/07_Other_Health_Careers"
    OH = [
        ("01_Emergency_Medical_Technician_EMT", "Emergency Medical Technician (EMT) – 108 Ambulance", ["Gives first aid and life support in ambulances."], "Certificate / training (EMRI Green Health Services runs 108 in Telangana); B.Sc life sciences / nursing / pharmacy / paramedics eligible",
         [("EMT", "108 / 104 services, private ambulances", "₹15,000–22,000")], [("EMT (contract)", "Telangana 108 service", "As per notification")]),
        ("02_Medical_Coding", "Medical Coding (ICD-10, CPT)", ["Converts diagnoses into codes for US insurance billing. Hyderabad is a top hub."], "Any life-science / pharmacy / nursing / allied degree + CPC (AAPC) or CCS certification",
         [("Medical Coder", "Omega, Access Healthcare, Optum, R1 RCM, GeBBS", "₹18,000–30,000 (grows fast)")], []),
        ("03_Clinical_Research_Pharmacovigilance", "Clinical Research & Pharmacovigilance", ["Runs drug trials and monitors drug safety."], "B.Pharm / Pharm-D / life science + PG Diploma in Clinical Research",
         [("Clinical Research Coordinator", "Hospitals, CROs", "₹20,000–35,000"), ("Drug Safety Associate", "IQVIA, Parexel, Novartis", "₹22,000–38,000")], []),
        ("04_Hospital_Administration_MHA", "Hospital / Healthcare Administration (MHA, MBA Healthcare)", ["Manages hospital operations, quality (NABH) and billing."], "Any degree (health background preferred) + MHA / MBA HCM",
         [("Hospital Administrator", PRIV_HOSP, "₹30,000–60,000")], [("Hospital Administrator / Deputy Director", "DME, TVVP, NHM", "MHA / MD Hospital Admin")]),
        ("05_Public_Health_MPH", "Public Health (MPH)", ["Works on disease prevention, epidemics and health programmes."], "MBBS/BDS/AYUSH/Nursing/life sciences + MPH (IIPH Hyderabad, PHFI)",
         [("Public Health Officer", "WHO, UNICEF, NGOs, CSR", "₹40,000–80,000")], [("District Programme Manager / Epidemiologist", "NHM Telangana", "MPH")]),
        ("06_Sanitary_Health_Inspector", "Sanitary / Health Inspector", ["Inspects sanitation, food safety and disease control in towns."], "Inter / degree + Sanitary Inspector diploma (1 yr)",
         [("Sanitation Supervisor", "Private facility management", "₹15,000–22,000")], [("Sanitary Inspector / Health Assistant", "GHMC, municipalities, Railways", "Diploma")]),
        ("07_Dietitian_Nutrition", "Dietitian & Nutritionist", ["Plans diets for patients and wellness."], "B.Sc Nutrition & Dietetics + internship",
         [("Clinical Dietitian", PRIV_HOSP, "₹18,000–35,000")], [("Dietitian / Nutrition Officer", "Govt hospitals, ICDS, NIN", "B.Sc/M.Sc Nutrition")]),
        ("08_Clinical_Psychology_Counselling", "Clinical Psychology & Counselling", ["Diagnosis and therapy of mental health problems (non-medicine)."], "B.A./B.Sc Psychology → M.A./M.Sc → M.Phil Clinical Psychology (RCI)",
         [("Counsellor / Clinical Psychologist", "Hospitals, schools, corporates", "₹25,000–60,000")], [("Clinical Psychologist", "IMH Erragadda, NIMS, DMHP", "M.Phil + RCI")]),
    ]
    for fn, name, about, elig, priv, govt in OH:
        career_doc(f"{b}/{fn}.docx", name, dict(about=about, eligibility=[elig], private=priv, govt=govt), subtitle="Health careers")


def master_lists(base):
    make(f"{base}/00_All_Options_after_BiPC.docx", "All Options after Inter BiPC – Master List", [
        ("Folder guide", [("table", ["Folder", "Courses"], [
            ["01_Doctor_Courses_NEET", "NEET, Types of doctors, MBBS (+ all MD/MS/DM/MCh), BDS, BAMS, BHMS, BUMS, BNYS, BSMS"],
            ["02_Nursing", "ANM, GNM, B.Sc Nursing, Post-Basic, M.Sc, Nursing abroad"],
            ["03_Pharmacy", "D.Pharm, B.Pharm, Pharm-D"],
            ["04_Allied_Health_Degrees_KNRUHS", "BPT, B.Sc MLT + 13 Allied Health B.Sc courses"],
            ["05_Paramedical_Diplomas_TGPMB", "13 paramedical diplomas (DMLT, Dialysis, ECG...)"],
            ["06_RMP_PMP_Village_Doctor_Truth", "Legal facts + legal alternatives"],
            ["07_Other_Health_Careers", "EMT, Medical Coding, Clinical Research, Hospital Admin, MPH, Sanitary Inspector, Dietitian, Psychology"],
            ["08_Agriculture_Veterinary_Fisheries", "B.Sc Agri, Horticulture, BVSc, BFSc, Food/Dairy Tech"],
            ["09_BSc_Life_Science_Degrees", "BZC, Biotech, Microbiology, Genetics, Nutrition, Forensic, Biomedical, MLT"],
            ["10_Commerce_Management_Arts_Law (any group)", "B.Com, BBA, BCA, BA, Law, Hotel Mgmt, Design, BSW, D.El.Ed..."],
            ["11_Health_Jobs_Govt_and_Private", "Master lists of all health jobs"]])]),
        ("Entrance exams for BiPC", ["NEET-UG – doctors (MBBS, BDS, AYUSH)", "TG EAPCET (Agriculture & Pharmacy) – B.Sc Nursing, B.Pharm, Pharm-D, B.Sc Agri/Horti, BVSc, BFSc",
                                     "KNRUHS merit – BPT, MLT, Allied Health", "TGPMB merit – Paramedical diplomas", "DOST – B.Sc degrees", "CUET-UG – central universities"]),
    ], subtitle="BiPC → Everything")

    j = f"{base}/11_Health_Jobs_Govt_and_Private"
    make(f"{j}/01_All_Health_Govt_Jobs_Telangana_and_Central.docx", "All Government Health Jobs – Telangana & Central", [
        ("Telangana (MHSRB – Medical & Health Services Recruitment Board, mhsrb.telangana.gov.in)", [("table", ["Post", "Qualification", "Selection"], [
            ["Civil Assistant Surgeon / Medical Officer", "MBBS + TSMC registration", "Merit: ~80 marks academic/exam + ~20 weightage for govt contract service"],
            ["Civil Assistant Surgeon Specialist", "MD/MS/DNB", "Merit + service weightage"],
            ["Dental Assistant Surgeon", "BDS", "Merit"], ["AYUSH Medical Officer", "BAMS/BHMS/BUMS/BNYS", "Merit / exam"],
            ["Nursing Officer (Staff Nurse)", "GNM / B.Sc Nursing", "CBT (80) + service weightage (20)"],
            ["Multi-Purpose Health Assistant (Female)", "ANM/MPHW(F)", "Exam/merit + weightage"],
            ["Pharmacist Grade-II", "D.Pharm/B.Pharm/Pharm-D", "CBT (80) + weightage (20)"],
            ["Lab Technician Grade-II", "DMLT / B.Sc MLT / Microbiology / Biochemistry", "CBT (80) + weightage (20)"],
            ["Radiographer, Physiotherapist, ECG/Dialysis/OT technicians", "Relevant diploma/degree", "As per notification"]])]),
        ("Other Telangana", ["TGPSC: Drug Inspector, Veterinary Assistant Surgeon, Food Safety Officer, Assistant Professor (via DME)", "NHM Telangana (contract): CHO, MO, ANM, Lab Tech, Pharmacist, Counsellor",
                             "NIMS, Singareni hospitals, TGSRTC hospital, ESIC Sanathnagar"]),
        ("Central", ["UPSC CMS (Medical Officers – Railways, CGHS)", "AIIMS NORCET (Nursing Officer), AIIMS faculty/residents", "Armed Forces Medical Services (AMC, MNS, Army Dental Corps)",
                     "RRB Paramedical (Staff Nurse, Pharmacist, Lab Supdt, ECG Tech, Radiographer)", "ESIC, CGHS, ICMR (NIN Hyderabad), CAPF Medical Officers"]),
        ("Age & pay", ["MHSRB posts: usually 18–46 years (relaxations apply).", "Pay per Telangana PRC – check each notification."]),
    ], subtitle="Health jobs")
    make(f"{j}/02_All_Health_Private_Jobs.docx", "All Private Health Jobs – Hyderabad, India & Abroad", [
        ("Hospitals", [f"Corporate & multi-speciality: {PRIV_HOSP}", "Roles: doctors, nurses, technicians, pharmacists, physiotherapists, admin"]),
        ("Diagnostics", ["Vijaya Diagnostics, Tenet, Lucid, Dr. Lal PathLabs, Thyrocare – lab & imaging roles"]),
        ("Pharma & biotech", ["Dr. Reddy's, Aurobindo, Hetero, Divi's, Granules, Bharat Biotech, Biological E – production, QC/QA, R&D, regulatory, sales"]),
        ("Healthcare IT & GCCs", ["Medical coding, pharmacovigilance, clinical data, healthcare analytics – Optum, Novartis, IQVIA, Cognizant, Accenture"]),
        ("Pharmacy retail", ["Apollo Pharmacy, MedPlus, Netmeds, Tata 1mg"]),
        ("Abroad", ["Gulf (UAE DHA/DOH, Saudi SCFHS, Qatar QCHP), UK (NMC/GMC), USA (NCLEX/USMLE), Australia (AHPRA), Germany"]),
    ], subtitle="Health jobs")


def run(base):
    master_lists(base)
    d = f"{base}/01_Doctor_Courses_NEET"
    doctors_overview(d)
    mbbs(d)
    dental_ayush(d)
    nursing(base)
    pharmacy(base)
    allied(base)
    rmp(base)
    other_health(base)


def pharmacy_only(base):
    pharmacy(base, sub=None)


def paramedical_only(base):
    p = base
    make(f"{p}/00_About_Paramedical_for_MPC.docx", "Paramedical Diplomas – Also Open to MPC Students", [
        ("Key point", ["Telangana Paramedical Board 2-year diplomas accept Inter BiPC OR MPC.", "Full details of each diploma are in BiPC/After_12th_BiPC/05_Paramedical_Diplomas_TGPMB."]),
        ("Diplomas", [("table", ["#", "Diploma", "Work"], [[i + 1, t[1], t[2]] for i, t in enumerate(TGPMB)])]),
    ], subtitle="MPC → Health careers")
