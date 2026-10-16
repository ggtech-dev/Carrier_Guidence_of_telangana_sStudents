from deg_common import UG_PASS, DOST, DOST_COLLEGES

LIFE_HIGHER = ["M.Sc via TG CPGET / CUET-PG / IIT JAM (Biotechnology)", "B.Ed → Bio Science teacher", "MBA (Pharma / Healthcare / Agri-business)",
               "PhD → scientist (CSIR-NET, ICMR, DBT-JRF)"]
LIFE_GOVT = [
    ("School Assistant (Bio Science)", "TG DSC", "B.Sc with Botany/Zoology + B.Ed + TET"),
    ("Lab Technician Grade II (with MLT/Microbiology/Biochemistry)", "MHSRB Telangana", "B.Sc MLT / Microbiology / Biochemistry"),
    ("Technical Assistant / Project Assistant", "CCMB, CDFD, NIN, IICT (Hyderabad)", "B.Sc / M.Sc"),
    ("Food Safety Officer (after PG/specific degrees)", "TGPSC / FSSAI", "Degree in Food Tech / Chemistry / Microbiology etc."),
    ("Forest Section Officer", "TGPSC", "B.Sc (science)"),
]

D = {}

def bsc(key, folder, title, about, subjects, private, govt_extra=None, higher_extra=None, duration="3 years", elig=None):
    D[key] = (folder, title, dict(about=about, duration=duration, eligibility=elig or ["Inter BiPC (40%+). Some combinations also accept MPC."],
        admission=DOST, colleges=DOST_COLLEGES, subjects=subjects, pass_rules=UG_PASS, private=private,
        govt=(govt_extra or []) + LIFE_GOVT, any_degree=True, higher=(higher_extra or []) + LIFE_HIGHER))

bsc("bsc_bzc", "BSc_BZC_Botany_Zoology_Chemistry", "B.Sc BZC – Botany, Zoology, Chemistry",
    ["The traditional life-science degree. It is the base for teaching, labs, pharma QC and many govt jobs."],
    ["Plant diversity, Plant physiology", "Animal diversity, Cell biology, Genetics", "Organic, Inorganic & Physical Chemistry"],
    [("QC Chemist / Lab Assistant", "Pharma, testing labs", "₹15,000–22,000"), ("Medical Representative", "Pharma companies", "₹18,000–30,000 + incentives"),
     ("Clinical Research Coordinator (with training)", "CROs", "₹18,000–28,000")])
bsc("bsc_biotech", "BSc_Biotechnology", "B.Sc Biotechnology (and 4-year Honours)",
    ["Uses living cells for medicines, vaccines, agriculture and industry. Hyderabad's Genome Valley is India's vaccine hub."],
    ["Cell & Molecular Biology", "Genetics & Genetic Engineering", "Microbiology", "Immunology", "Bioprocess Technology", "Bioinformatics"],
    [("Lab / Research Assistant", "Bharat Biotech, Biological E, Indian Immunologicals", "₹15,000–25,000"), ("Production / QC Executive", "Vaccine & biopharma units", "₹18,000–28,000"),
     ("Bioinformatics Associate", "Biotech/IT firms", "₹20,000–35,000")])
bsc("bsc_micro", "BSc_Microbiology", "B.Sc Microbiology combinations",
    ["Studies bacteria, viruses and fungi. Needed in hospitals, pharma, food and water testing."],
    ["General & Medical Microbiology", "Immunology", "Food & Industrial Microbiology", "Molecular Biology"],
    [("Microbiologist (QC)", "Pharma, food, dairy companies", "₹15,000–25,000"), ("Lab Technician", "Hospitals, diagnostic labs (Vijaya, Apollo)", "₹15,000–22,000")])
bsc("bsc_genetics", "BSc_Genetics", "B.Sc Genetics combinations",
    ["Studies genes, heredity and genetic testing."], ["Classical & Molecular Genetics", "Human Genetics", "Cytogenetics", "Genomics"],
    [("Genetic Lab Technician", "Diagnostic & genomics labs", "₹18,000–28,000"), ("Research Assistant", "Research institutes", "₹15,000–25,000")],
    higher_extra=["M.Sc Genetic Counselling / Human Genetics"])
bsc("bsc_nutrition", "BSc_Nutrition_and_Dietetics", "B.Sc Nutrition & Dietetics / Home Science",
    ["Food, nutrition and diet planning for health and disease."], ["Human Nutrition", "Food Science", "Clinical Nutrition & Dietetics", "Community Nutrition"],
    [("Dietitian (with internship)", "Hospitals, gyms, wellness apps", "₹15,000–30,000"), ("Nutritionist", "Food companies, NGOs", "₹15,000–25,000")],
    [("Nutrition Officer / CDPO / Supervisor", "Women & Child Welfare (ICDS)", "Degree in Home Science/Nutrition"), ("Research Fellow", "NIN Hyderabad (ICMR)", "M.Sc Nutrition")],
    ["M.Sc Food & Nutrition / Clinical Nutrition; Registered Dietitian (IDA)"])
bsc("bsc_forensic", "BSc_Forensic_Science", "B.Sc Forensic Science",
    ["Applies science to solve crimes – fingerprints, DNA, toxicology, documents."], ["Criminalistics", "Forensic Biology & Serology", "Forensic Chemistry & Toxicology", "Fingerprints & Questioned Documents", "Cyber Forensics"],
    [("Forensic Lab Assistant", "Private forensic labs", "₹15,000–25,000"), ("Fraud / Cyber Forensic Analyst", "Banks, IT security firms", "₹20,000–40,000")],
    [("Scientific Assistant / Officer", "Telangana State FSL (Hyderabad), CFSL Hyderabad", "B.Sc / M.Sc Forensic Science"), ("Fingerprint Expert", "TG Police", "Degree + training")],
    ["M.Sc Forensic Science (NFSU, OU)"])
bsc("bsc_biomed", "BSc_Honours_Biomedical_Science", "B.Sc (Honours) Biomedical Science (4 years)",
    ["Human body and disease at cell and molecular level – a bridge between biology and medicine."], ["Human Anatomy & Physiology", "Biochemistry", "Pathology", "Pharmacology", "Molecular Diagnostics"],
    [("Research Associate", "Hospitals, CROs, biotech", "₹18,000–30,000"), ("Clinical Data Coordinator", "CROs, GCCs", "₹20,000–30,000")], duration="4 years")
bsc("bsc_mlt_dost", "BSc_Life_Science_MLT", "B.Sc Life Science (Medical Lab Technology) – via DOST",
    ["A 3-year MLT degree offered in DOST degree colleges (another route besides the KNRUHS B.Sc MLT)."], ["Haematology", "Clinical Biochemistry", "Microbiology", "Histopathology", "Blood Banking"],
    [("Lab Technician", "Hospitals, diagnostic labs", "₹15,000–22,000")])

AGRI_PASS = ["University grading (ICAR pattern): minimum overall grade point (about 5.0/10) and a minimum per course; check PJTSAU academic regulations."]

D["bsc_agri"] = ("BSc_Hons_Agriculture", "B.Sc (Hons) Agriculture – PJTSAU", dict(
    about=["A professional degree in crop science, soil, plant protection and agri-business. It has many govt job openings."],
    duration="4 years (includes RAWEP – Rural Agricultural Work Experience)", eligibility=["Inter BiPC (also MPC for some seats). TG EAPCET (Agriculture & Pharmacy stream)."],
    admission=["TG EAPCET (A&P stream) rank → PJTSAU counselling.", "ICAR AIEEA (via CUET-UG) for 15% all-India seats.", "Farmer's quota / rural quota seats."],
    colleges=["Agricultural College, Rajendranagar (Hyderabad), Jagtial, Aswaraopet, Palem, Sircilla, Warangal and others (PJTSAU)"],
    subjects=["Agronomy, Soil Science", "Genetics & Plant Breeding", "Entomology, Plant Pathology", "Horticulture", "Agricultural Economics & Extension", "Agri Engineering basics"],
    pass_rules=AGRI_PASS,
    private=[("Field Officer / Agronomist", "Seed & fertiliser companies (Rasi, Nuziveedu, Syngenta, Bayer, Coromandel)", "₹20,000–35,000"),
             ("Agri-loan Officer", "Banks (rural branches), NABARD-related", "₹25,000–40,000"), ("Agri-tech Executive", "AgroStar, DeHaat, BigHaat", "₹20,000–35,000")],
    govt=[("Agricultural Officer (AO)", "TGPSC – Agriculture Dept", "B.Sc Agriculture"), ("Agricultural Extension Officer (AEO)", "Telangana Agriculture Dept", "Diploma/B.Sc Agriculture"),
          ("Agriculture Field Officer (AFO) – IBPS SO", "Public sector banks", "B.Sc Agriculture"), ("NABARD Grade A (Agriculture)", "NABARD", "B.Sc Agri 60%"),
          ("FCI Technical / Manager", "Food Corporation of India", "B.Sc Agriculture"), ("Scientist (ARS)", "ICAR – ASRB", "PG/PhD")],
    any_degree=True, self_emp=["Agri-input dealership (licence needs Agri degree)", "Nursery, organic farming, agri startup"],
    higher=["M.Sc Agriculture (ICAR AIEEA-PG / PJTSAU)", "MBA Agri-business (MANAGE Hyderabad)", "PhD → Agriculture Scientist"]))

D["bsc_horti"] = ("BSc_Hons_Horticulture", "B.Sc (Hons) Horticulture – SKLTGHU", dict(
    about=["Fruits, vegetables, flowers, plantation crops and landscaping."], duration="4 years", eligibility=["Inter BiPC; TG EAPCET (A&P)."],
    admission=["TG EAPCET rank → SKLTGHU counselling (Mulugu, Siddipet & other colleges)."],
    subjects=["Fruit & Vegetable Science", "Floriculture & Landscaping", "Post-harvest Technology", "Plant Protection"], pass_rules=AGRI_PASS,
    private=[("Horticulture Field Officer", "Seed, nursery, food processing", "₹18,000–30,000"), ("Landscape Supervisor", "Real estate, landscaping firms", "₹18,000–28,000")],
    govt=[("Horticulture Officer (HO)", "TGPSC – Horticulture Dept", "B.Sc Horticulture"), ("AFO / Horticulture officer", "Banks, NABARD", "B.Sc Horticulture")],
    any_degree=True, self_emp=["Nursery, polyhouse farming, floriculture"]))

D["bvsc"] = ("BVSc_Veterinary_Doctor", "BVSc & AH – Veterinary Doctor (Animal Doctor)", dict(
    about=["Doctor for animals – cattle, poultry, pets. You register with the Veterinary Council to practise."],
    duration="5.5 years (including 1 year internship)", eligibility=["Inter BiPC with 50% (40% reserved)."],
    admission=["Telangana state seats: TG EAPCET (A&P) rank → PVNRTVU counselling.", "15% all-India seats: NEET-UG via VCI counselling."],
    colleges=["College of Veterinary Science, Rajendranagar (Hyderabad), Korutla, Mamnoor (Warangal) – PVNRTVU"],
    subjects=["Veterinary Anatomy, Physiology, Biochemistry", "Pharmacology, Pathology, Microbiology", "Animal Nutrition, Livestock Production", "Veterinary Medicine, Surgery, Gynaecology", "Poultry Science, Public Health"],
    pass_rules=["VCI MSVE regulations: about 50% in theory & practical per course"],
    private=[("Veterinarian", "Pet clinics, poultry companies (Suguna, Venkys, Sneha)", "₹30,000–60,000"), ("Technical Sales", "Animal pharma & feed companies", "₹30,000–50,000")],
    govt=[("Veterinary Assistant Surgeon (VAS)", "TGPSC – Animal Husbandry Dept", "BVSc + registration"), ("Veterinary Officer", "Army Remount Veterinary Corps, NDDB, Vijaya Dairy", "BVSc"),
          ("Scientist", "ICAR (NRC Meat, Directorate of Poultry Research – Hyderabad)", "MVSc/PhD")],
    self_emp=["Own pet clinic", "Poultry / dairy consultancy"], higher=["MVSc (ICAR AIEEA-PG)", "PhD"]))

D["bfsc"] = ("BFSc_Fisheries_Science", "B.F.Sc – Fisheries Science", dict(
    about=["Fish farming (aquaculture), processing and fisheries management. Telangana has a big inland fisheries sector (free fish-seed schemes)."],
    duration="4 years", eligibility=["Inter BiPC; TG EAPCET (A&P)."], admission=["TG EAPCET → PVNRTVU (College of Fishery Science, Pebbair)"],
    subjects=["Aquaculture", "Fish Biology", "Fish Processing", "Fisheries Economics & Extension"], pass_rules=AGRI_PASS,
    private=[("Aquaculture Technician / Manager", "Shrimp/fish farms, feed companies", "₹20,000–35,000")],
    govt=[("Fisheries Development Officer (FDO)", "TGPSC – Fisheries Dept", "B.F.Sc"), ("Assistant Director (Fisheries)", "TGPSC", "B.F.Sc/M.F.Sc")],
    self_emp=["Fish farming, hatchery"]))

D["btech_food_dairy"] = ("BTech_Food_Technology_Dairy_Technology", "B.Tech Food Technology / Dairy Technology (Agri route)", dict(
    about=["Engineering-style degrees for food processing and the dairy industry."], duration="4 years", eligibility=["Inter BiPC or MPC; TG EAPCET."],
    admission=["TG EAPCET → PJTSAU (Food Tech, Rudrur) / PVNRTVU (Dairy Tech, Kamareddy)"],
    subjects=["Food Chemistry & Microbiology", "Dairy Engineering", "Food Processing & Packaging", "Quality control (FSSAI)"], pass_rules=AGRI_PASS,
    private=[("Food Technologist / QA", "ITC, Nestle, Heritage, Jersey, Vijaya Dairy", "₹20,000–35,000"), ("Production Supervisor", "Food plants", "₹20,000–30,000")],
    govt=[("Food Safety Officer", "TGPSC / Telangana Food Safety", "Degree in Food Tech/Dairy Tech etc."), ("Technical Officer", "FSSAI, FCI, Vijaya Dairy (TGDDCF)", "B.Tech Food/Dairy")]))
