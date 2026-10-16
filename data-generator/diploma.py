from builder import make

B = "02_After_10th_Polytechnic_Diploma"

PASS = [("table", ["Item", "Minimum to pass (TGSBTET, typical C-21/C-24 rules)"], [
    ["Theory subject – semester-end exam", "35% of end-exam marks"],
    ["Theory subject – overall (internal + end exam)", "35%"],
    ["Practical / Lab / Drawing", "50%"],
    ["Industrial training (6th semester)", "Must be completed and assessed – usually 50%"],
    ["Class", "First Class with Distinction 75%+, First Class 60%+, Second Class 50%+, Pass 35%+"],
]), "Supplementary exams are held for failed subjects; backlogs must be cleared to receive the diploma.",
    "Rules can change with each curriculum (C-21, C-24...). Confirm on sbtet.telangana.gov.in."]

COMMON_Y1 = ["English", "Engineering Mathematics I", "Engineering Physics", "Engineering Chemistry & Environmental Studies", "Engineering Drawing", "Basic Workshop Practice", "Computer Fundamentals Lab"]

BRANCHES = [
    ("01_Civil_Engineering_DCE", "Diploma in Civil Engineering (DCE)",
     ["Surveying I & II", "Construction Materials", "Strength of Materials", "Hydraulics", "Building Construction", "Civil Engineering Drawing"],
     ["Design of RCC Structures", "Steel Structures", "Water Supply & Sanitary Engineering", "Highway & Railway Engineering", "Estimating & Costing", "Irrigation Engineering", "AutoCAD / Revit", "Industrial Training"],
     ["Site Supervisor", "Draughtsman", "Surveyor", "Work Inspector / Technical Officer (Govt)", "AE (after B.Tech)"]),
    ("02_Mechanical_Engineering_DME", "Diploma in Mechanical Engineering (DME)",
     ["Engineering Mechanics", "Basic Thermodynamics", "Workshop Technology", "Material Science", "Machine Drawing"],
     ["Strength of Materials", "Production Technology", "Thermal Engineering", "Fluid Mechanics & Machines", "Design of Machine Elements", "CNC & CAD/CAM", "Refrigeration & AC", "Industrial Management", "Industrial Training"],
     ["Production Supervisor", "Maintenance Technician", "CNC Programmer", "Quality Inspector", "Railway / RTC technical posts"]),
    ("03_Electrical_and_Electronics_EEE", "Diploma in Electrical & Electronics Engineering (EEE)",
     ["Basic Electrical Engineering", "Electrical Circuits", "Electronics Basics", "Electrical Drawing"],
     ["DC & AC Machines", "Power Systems (Generation, Transmission, Distribution)", "Electrical Measurements", "Power Electronics", "Utilization of Electrical Energy", "PLC & Automation", "Electrical Estimating", "Industrial Training"],
     ["Sub-Engineer / Junior Engineer (TG DISCOMs, TRANSCO)", "Electrical Supervisor (with licence)", "Maintenance Technician", "Solar / EV technician"]),
    ("04_Electronics_and_Communication_ECE", "Diploma in Electronics & Communication Engineering (ECE)",
     ["Electronic Components & Devices", "Circuit Theory", "Digital Electronics", "Electronic Workshop"],
     ["Analog Circuits", "Communication Systems", "Microcontrollers & Embedded Systems", "Industrial Electronics", "Optical & Mobile Communication", "PCB Design", "IoT", "Industrial Training"],
     ["Electronics Technician", "Telecom Technician", "Service Engineer", "Embedded Testing", "ECIL / BEL technician posts"]),
    ("05_Computer_Engineering_CME", "Diploma in Computer Engineering (CME)",
     ["Programming in C", "Digital Electronics", "Computer Organisation", "Office Automation Lab"],
     ["Data Structures", "Python / Java Programming", "DBMS (SQL)", "Operating Systems", "Computer Networks", "Web Design", "Software Engineering", "Cloud & Cyber Security basics", "Industrial Training"],
     ["Junior Programmer", "Web Developer", "Computer Operator / Data Entry", "Hardware & Network Technician", "IT Support"]),
    ("06_AI_and_Machine_Learning_Diploma", "Diploma in Artificial Intelligence & Machine Learning",
     ["Python Programming", "Mathematics for AI", "Digital Electronics", "Computer Fundamentals"],
     ["Data Structures", "Machine Learning", "Data Analytics", "Deep Learning basics", "DBMS", "Industrial Training"],
     ["Junior Data Analyst", "AI/ML Support", "Then B.Tech CSE/AI via ECET"]),
    ("07_Automobile_Engineering_DAE", "Diploma in Automobile Engineering (DAE)",
     ["Engineering Mechanics", "Automobile Engines", "Workshop Technology"],
     ["Automobile Chassis & Transmission", "Auto Electrical & Electronics", "Vehicle Maintenance", "Electric Vehicles", "Motor Vehicle Act basics", "Industrial Training"],
     ["Service Advisor / Technician", "Assistant Motor Vehicle Inspector (TG Transport Dept – with experience/licence)", "TGSRTC technical posts"]),
    ("08_Chemical_Engineering_DCH", "Diploma in Chemical Engineering (DCH)",
     ["Chemistry", "Chemical Process Principles", "Material & Energy Balance"],
     ["Unit Operations", "Heat & Mass Transfer", "Chemical Technology", "Process Instrumentation", "Pollution Control", "Industrial Training"],
     ["Plant Operator", "Lab Chemist / QC (pharma)", "Process Technician"]),
    ("09_Mining_Engineering_DMNG", "Diploma in Mining Engineering",
     ["Mining Geology", "Mine Surveying", "Elements of Mining"],
     ["Mining Methods", "Mine Ventilation", "Mine Machinery", "Mine Safety & Legislation", "Practical training in mines"],
     ["Overman / Mining Sirdar (with certificate)", "Singareni (SCCL) jobs", "Coal India, NMDC"]),
    ("10_Metallurgical_Engineering_DMT", "Diploma in Metallurgical Engineering",
     ["Elements of Metallurgy", "Fuels & Refractories", "Material Testing"],
     ["Iron & Steel Making", "Foundry Technology", "Heat Treatment", "Welding Metallurgy", "Industrial Training"],
     ["Metallurgy Technician", "QC Inspector in steel & foundry plants", "Midhani / DMRL technician"]),
    ("11_Textile_Technology_DTT", "Diploma in Textile Technology",
     ["Textile Fibres", "Yarn Manufacture", "Fabric Structure"],
     ["Weaving", "Textile Chemical Processing", "Garment Technology", "Textile Testing", "Industrial Training"],
     ["Textile mill supervisor", "Quality Controller", "Handloom & Textiles Dept posts"]),
    ("12_Architectural_Assistantship_DARCH", "Diploma in Architectural Assistantship",
     ["Architectural Drawing", "Building Materials", "History of Architecture"],
     ["Building Construction", "Architectural Design", "Interior Design", "AutoCAD / SketchUp / Revit", "Estimating"],
     ["Architectural Draughtsman", "Interior Designer assistant", "Town Planning Building Overseer"]),
    ("13_Electronics_and_Instrumentation_DEIE", "Diploma in Electronics & Instrumentation",
     ["Electronic Devices", "Electrical Technology", "Measurements"],
     ["Transducers & Sensors", "Process Control", "PLC & SCADA", "Biomedical Instrumentation", "Industrial Training"],
     ["Instrument Technician", "Control Room Operator", "Biomedical equipment technician"]),
    ("14_Commercial_and_Computer_Practice_DCCP", "Diploma in Commercial & Computer Practice (DCCP)",
     ["Typewriting / Keyboarding", "Accountancy", "Business Communication"],
     ["Shorthand", "Computer Applications (MS Office, Tally)", "Office Management", "Banking & Insurance basics"],
     ["Office Assistant", "Junior Assistant / Typist", "Steno", "Accounts Assistant"]),
]


def run():
    make(f"{B}/00_About_Polytechnic_Diploma.docx", "Polytechnic Diploma after 10th – Telangana", [
        ("What is Polytechnic?", [
            "3-year diploma in engineering/technology (some 3.5 yrs with 6 months industrial training).",
            "Board: TGSBTET – State Board of Technical Education & Training, Telangana.",
            "Govt Polytechnics charge very low fees; fee reimbursement for eligible SC/ST/BC/EWS/minority students.",
            "Diploma = equivalent to Intermediate for many purposes and allows lateral entry into 2nd year B.Tech.",
        ]),
        ("Admission – TG POLYCET", [
            "Conducted by TGSBTET (usually April–May); eligibility 10th class (appearing students can also apply).",
            "Exam: 120 marks, 2 hours – Mathematics 60, Physics 30, Chemistry 30.",
            "Agriculture/Veterinary diplomas: Maths/Biology option (PJTSAU, PVNRTVU, SKLTGHU use POLYCET ranks).",
            "Qualifying mark 30% (36/120); no minimum for SC/ST.",
            "Counselling online: tgpolycet.nic.in – choose branch & college.",
        ]),
        ("All branches (see each folder)", [("table", ["#", "Branch"], [[i + 1, b[1]] for i, b in enumerate(BRANCHES)])]),
        ("Pass Percentage Rules", PASS),
        ("Year 1 common subjects (all engineering branches)", COMMON_Y1),
        ("After Diploma", ["TG ECET → B.Tech 2nd year (lateral entry).", "Jobs (private & govt) – see After_Diploma folder.", "Apprenticeship (NATS – 1 year paid training)."]),
    ])
    for fn, name, y2, y3, jobs in BRANCHES:
        make(f"{B}/{fn}/About_{fn[3:]}.docx", name, [
            ("Course details", ["Duration: 3 years (6 semesters) – some branches include 6 months industrial training.", "Admission: TG POLYCET rank → online counselling.", "Board: TGSBTET."]),
            ("Subjects – Semester 1–2 (common to all branches)", COMMON_Y1),
            ("Core branch subjects – Semester 2–4", y2),
            ("Advanced subjects + training – Semester 4–6", y3),
            ("Pass Percentage", PASS),
            ("Jobs after this diploma", jobs),
            ("Higher studies", ["TG ECET → B.Tech 2nd year in the same/related branch.", "AMIE (section A & B) – degree-equivalent while working.", "Part-time B.Tech for working professionals (JNTUH)."]),
        ], subtitle="After 10th → Polytechnic Diploma Branch")

    make(f"{B}/Agriculture_Veterinary_Horticulture_Diplomas/About_Agri_Diplomas.docx", "Agriculture, Horticulture & Veterinary Diplomas", [
        ("Courses (admission through TG POLYCET – Agri/Bio stream)", [("table", ["Diploma", "Duration", "University"], [
            ["Diploma in Agriculture", "2 years", "PJTSAU"],
            ["Diploma in Organic Agriculture", "2 years", "PJTSAU"],
            ["Diploma in Agricultural Engineering", "3 years", "PJTSAU"],
            ["Diploma in Horticulture", "2 years", "SKLTGHU"],
            ["Diploma in Animal Husbandry", "2 years", "PVNRTVU"],
            ["Diploma in Fisheries", "2 years", "PVNRTVU"],
        ])]),
        ("Eligibility", ["10th pass; preference to rural students (studied 4+ years in rural schools) for agriculture diplomas.", "Age usually 15–22."]),
        ("Pass rules", ["Grading system of the university – minimum grade point per course (usually ~50%). Check university academic rules."]),
        ("Jobs", ["Agricultural Extension Officer (AEO) – check latest eligibility", "Fertiliser/seed company field officer", "Livestock Assistant", "Self-employment – farming, nursery, dairy"]),
    ])

    make(f"{B}/After_Diploma/TG_ECET_Lateral_Entry.docx", "TG ECET – Diploma to B.Tech (Lateral Entry)", [
        ("About", ["Conducted by OU/JNTUH for TGCHE every year (May).", "Admission into 2nd year B.Tech / B.Pharm for diploma and B.Sc (Maths) holders."]),
        ("Pattern", ["200 marks: Mathematics 50, Physics 25, Chemistry 25, Branch subject 100.", "Qualifying 25%; no minimum for SC/ST."]),
        ("Benefit", ["Saves one year – complete B.Tech in 3 years after diploma.", "Fee reimbursement applies to eligible students."]),
    ])
    make(f"{B}/After_Diploma/Jobs_after_Diploma.docx", "Jobs after Polytechnic Diploma", [
        ("Government", [("table", ["Job", "Recruiter", "Branch"], [
            ["Junior Engineer (JE)", "SSC JE, RRB JE", "Civil, Mech, EEE, ECE"],
            ["Sub-Engineer / Junior Assistant Engineer", "TG DISCOMs (TGSPDCL, TGNPDCL), TRANSCO", "EEE, ECE, Civil"],
            ["Technician Grade I", "RRB", "EEE, ECE, Mech, CME"],
            ["Technical Officer / Work Inspector", "TG Panchayat Raj, Irrigation, R&B", "Civil"],
            ["Technical Assistant / Technician 'B'", "ISRO, DRDO, BARC, ECIL, BEL, HAL", "All core branches"],
            ["Junior Technical Officer", "Singareni (SCCL)", "Mining, Mech, EEE"],
            ["Indian Navy / Coast Guard Yantrik", "Navy / ICG", "Mech, EEE, ECE"],
            ["Army Technical / Air Force Group X", "Defence", "Diploma (any engineering)"],
        ])]),
        ("Private", ["Manufacturing, pharma, construction, IT support, automobile service, telecom.", "Apprenticeship under NATS (Board of Apprenticeship Training, Chennai) – stipend paid."]),
    ])


