from deg_common import UG_PASS, DOST, DOST_COLLEGES

BSC_HIGHER = ["M.Sc via TG CPGET (Telangana universities) or IIT JAM / CUET-PG (IITs, NITs, central universities)",
              "MCA via TG ICET / NIMCET", "MBA via TG ICET / CAT", "B.Ed via TG EdCET → school teacher",
              "PhD → scientist / lecturer (CSIR-NET / UGC-NET / TG SET)"]

SCI_GOVT = [
    ("School Assistant (Maths / Physical Science / Bio Science)", "TG DSC (School Education)", "Degree with subject + B.Ed + TG TET"),
    ("Junior Lecturer (after PG)", "TGPSC", "PG 50% in subject"),
    ("Scientific Assistant / Technical Assistant", "ISRO, DRDO, BARC, IICT, CCMB, NGRI (Hyderabad labs)", "B.Sc / M.Sc in subject"),
    ("Statistical Investigator / Junior Statistical Officer", "SSC CGL, TGPSC", "Degree with Statistics / Maths"),
    ("Forensic Science Lab Assistant / Scientific Officer", "TG FSL", "B.Sc / M.Sc in Chemistry, Physics, Biology"),
]

D = {}

D["bsc_mpcs"] = ("BSc_MPCs_Maths_Physics_Computers", "B.Sc MPCs – Mathematics, Physics, Computer Science", dict(
    about=["A 3-year science degree with Maths, Physics and Computer Science as main subjects.", "It is the most popular B.Sc for MPC students who want an IT career without doing B.Tech."],
    duration="3 years (6 semesters). 4-year Honours is available in some colleges.",
    eligibility=["Inter MPC (40%+). MEC students may be allowed for Maths-based combinations; check DOST rules."],
    admission=DOST, colleges=DOST_COLLEGES,
    subjects=["Calculus, Algebra, Real Analysis, Linear Algebra", "Mechanics, Optics, Electricity, Modern Physics, Electronics",
              "Programming in C/Python, Data Structures, DBMS, OOP with Java, Web Technologies", "English, second language, skill-enhancement courses"],
    pass_rules=UG_PASS, skills=["Python, SQL, Git", "Full-stack basics (HTML, JS, React)", "Aptitude for campus drives"],
    private=[("Software Trainee / Associate", "TCS, Infosys, Wipro, Cognizant, HCL", "₹20,000–35,000"),
             ("Technical Support / IT Help Desk", "IT services, BPO", "₹15,000–25,000"),
             ("Junior Data Analyst", "Analytics firms", "₹20,000–35,000"),
             ("Tutor / Coaching faculty (Maths, Physics)", "Coaching centres, ed-tech", "₹15,000–30,000")],
    govt=SCI_GOVT, any_degree=True, higher=BSC_HIGHER,
    route=["Inter MPC → DOST → B.Sc MPCs", "Learn programming plus one stack during the degree", "Apply in campus or off-campus drives, OR do MCA (ICET) for better IT roles", "OR take M.Sc + B.Ed for a teaching career"]))

D["bsc_mscs"] = ("BSc_MSCs_Maths_Statistics_Computers", "B.Sc MSCs – Mathematics, Statistics, Computer Science", dict(
    about=["Combines Maths, Statistics and Computers. It is a strong base for data analytics and actuarial careers."],
    duration="3 years", eligibility=["Inter MPC / MEC with Maths (40%+)."], admission=DOST, colleges=DOST_COLLEGES,
    subjects=["Descriptive & Inferential Statistics, Probability, Sampling, Regression", "Calculus, Algebra, Numerical Methods", "Programming, DBMS, Python/R for data"],
    pass_rules=UG_PASS, skills=["Excel, SQL, Power BI/Tableau", "Python (pandas) / R"],
    private=[("Data Analyst", "Banks, e-commerce, analytics firms", "₹25,000–40,000"),
             ("MIS Executive", "Corporates", "₹18,000–28,000"),
             ("Research Analyst (market research)", "Market research firms", "₹20,000–30,000"),
             ("Actuarial Trainee (with exams)", "Insurance companies", "₹30,000–50,000")],
    govt=SCI_GOVT + [("Indian Statistical Service (after PG)", "UPSC ISS", "PG in Statistics / Maths / Economics")],
    any_degree=True, higher=["M.Sc Statistics / Data Science", "M.Stat at ISI (ISI Hyderabad centre)"] + BSC_HIGHER[1:]))

D["bsc_mpc"] = ("BSc_MPC_Maths_Physics_Chemistry", "B.Sc MPC – Mathematics, Physics, Chemistry", dict(
    about=["A classic science degree. It suits teaching, research, labs and competitive exams."],
    duration="3 years", eligibility=["Inter MPC (40%+)."], admission=DOST, colleges=DOST_COLLEGES,
    subjects=["Mathematics (Calculus, Algebra, Analysis)", "Physics (Mechanics, Thermodynamics, Optics, Electronics)", "Chemistry (Organic, Inorganic, Physical, Analytical)"],
    pass_rules=UG_PASS,
    private=[("QC / QA Chemist", "Pharma & chemical companies (Hyderabad pharma hub)", "₹15,000–25,000"),
             ("Lab Assistant", "Industries, testing labs", "₹12,000–20,000"),
             ("Teacher / Tutor", "Private schools, coaching", "₹12,000–25,000")],
    govt=SCI_GOVT, any_degree=True, higher=BSC_HIGHER))

D["bsc_cs_hons"] = ("BSc_Honours_Computer_Science", "B.Sc (Honours) Computer Science – 4 years", dict(
    about=["A 4-year honours degree (NEP pattern) focused on Computer Science, with a research/project year.", "It counts as a 4-year degree, which helps for some MS-abroad admissions."],
    duration="4 years (exit after 3 years with a B.Sc is allowed)", eligibility=["Inter MPC (some colleges allow Maths in any group)."], admission=DOST,
    subjects=["Programming (C, Python, Java)", "Data Structures & Algorithms", "DBMS, OS, Networks", "AI/ML, Cloud, Web development", "4th-year research project / internship"],
    pass_rules=UG_PASS,
    private=[("Software Developer", "IT services/product companies", "₹25,000–50,000"),
             ("Cloud / DevOps Associate", "IT companies", "₹25,000–45,000"),
             ("QA / Test Engineer", "IT companies", "₹20,000–35,000")],
    govt=SCI_GOVT[:3], any_degree=True, higher=["MS abroad", "M.Sc CS / MCA", "M.Tech (via GATE)"] + BSC_HIGHER[2:]))

D["bsc_data_science"] = ("BSc_Data_Science", "B.Sc Data Science / B.Sc (Hons) Data Science", dict(
    about=["Teaches statistics, programming and machine learning to analyse data."],
    duration="3 years (Honours: 4 years)", eligibility=["Inter MPC / MEC (Maths needed)."], admission=DOST,
    subjects=["Statistics & Probability", "Python, R, SQL", "Machine Learning", "Data Visualization", "Big Data tools"], pass_rules=UG_PASS,
    private=[("Data Analyst", "All industries", "₹25,000–45,000"), ("Business Analyst", "Consulting/IT", "₹25,000–40,000"),
             ("ML Engineer (junior)", "AI startups", "₹30,000–60,000")],
    govt=SCI_GOVT[3:4], any_degree=True, higher=["M.Sc Data Science / Statistics", "MBA Business Analytics", "MS abroad"]))

D["bsc_statistics"] = ("BSc_Statistics", "B.Sc Statistics combinations", dict(
    about=["Statistics with Maths/Computers/Economics."], duration="3 years", eligibility=["Inter MPC / MEC."], admission=DOST,
    subjects=["Probability, Distributions", "Statistical Inference", "Sampling & Design of Experiments", "Econometrics / Operations Research"], pass_rules=UG_PASS,
    private=[("Data / Statistical Analyst", "Analytics, pharma (clinical data)", "₹22,000–40,000"), ("Actuarial Analyst (with exams)", "Insurance", "₹30,000–50,000")],
    govt=SCI_GOVT[3:] + [("Indian Statistical Service", "UPSC", "PG in Statistics")], any_degree=True, higher=["M.Sc Statistics", "M.Stat (ISI)", "Actuarial exams (IAI)"]))

D["bsc_electronics"] = ("BSc_Electronics", "B.Sc Electronics combinations (MPE / MECs)", dict(
    about=["Science degree with Electronics plus Maths/Physics/Computers."], duration="3 years", eligibility=["Inter MPC."], admission=DOST,
    subjects=["Circuit Analysis", "Analog & Digital Electronics", "Microprocessors & Microcontrollers", "Communication Systems", "Embedded C / IoT"], pass_rules=UG_PASS,
    private=[("Electronics Technician / Service Engineer", "Electronics & telecom firms", "₹15,000–25,000"), ("Embedded Trainee", "Embedded companies", "₹18,000–30,000")],
    govt=SCI_GOVT[:3] + [("Technician / Technical Assistant", "ECIL, BEL, BDL (Hyderabad PSUs)", "B.Sc Electronics")], any_degree=True,
    higher=["M.Sc Electronics", "MCA", "M.Tech (via GATE)"]))

D["bsc_chem_tech"] = ("BSc_Chemistry_and_Chemical_Technology", "B.Sc Chemistry / Chemical Technology / Industrial Chemistry", dict(
    about=["Chemistry-focused degrees with direct demand in Hyderabad's pharma and bulk-drug industry."],
    duration="3 years", eligibility=["Inter MPC or BiPC (Chemistry needed)."], admission=DOST,
    subjects=["Organic, Inorganic, Physical, Analytical Chemistry", "Instrumental Analysis (HPLC, GC, UV)", "Industrial Chemistry / Unit Operations", "GMP & GLP basics"], pass_rules=UG_PASS,
    private=[("QC Chemist (HPLC/GC)", "Dr. Reddy's, Aurobindo, Hetero, MSN, Divi's", "₹15,000–25,000"), ("Production Chemist", "Bulk drug units (Pashamylaram, Jeedimetla)", "₹15,000–22,000"),
             ("R&D Trainee (after M.Sc)", "Pharma R&D", "₹25,000–40,000")],
    govt=SCI_GOVT + [("Chemist / Junior Scientific Officer", "TG Pollution Control Board, Drug Control lab", "B.Sc/M.Sc Chemistry")], any_degree=True,
    higher=["M.Sc Organic / Analytical / Pharmaceutical Chemistry (CPGET)"] + BSC_HIGHER[2:]))

D["bsc_bed"] = ("Integrated_BSc_BEd_BA_BEd", "Integrated B.Sc B.Ed / B.A. B.Ed (ITEP – 4 years)", dict(
    about=["A 4-year integrated teacher education programme. You get a degree and a B.Ed together, saving one year."],
    duration="4 years", eligibility=["Inter in any relevant group (B.Sc B.Ed: MPC/BiPC; B.A. B.Ed: any group)."],
    admission=["Through DOST in some Telangana colleges; NCET (NTA) for ITEP in central/state institutions."],
    subjects=["Degree subjects + pedagogy, child psychology, school internship"], pass_rules=UG_PASS,
    private=[("School teacher", "Private schools (CBSE/State)", "₹15,000–30,000"), ("Ed-tech content developer", "Ed-tech companies", "₹20,000–35,000")],
    govt=[("School Assistant (SA)", "TG DSC / TRT", "Degree + B.Ed + TG TET Paper II"), ("PGT/TGT", "KVS, NVS, Army schools, TSWREIS", "Degree/PG + B.Ed + CTET")],
    any_degree=True, higher=["M.Ed", "M.A./M.Sc → Junior Lecturer"]))

D["barch"] = ("BArch_Architecture", "B.Arch – Bachelor of Architecture", dict(
    about=["A 5-year professional course to design buildings and spaces. You must register with the Council of Architecture (CoA) to practise."],
    duration="5 years (10 semesters, including 1 semester of practical training)",
    eligibility=["Inter MPC with Maths, Physics, Chemistry; 50% aggregate."],
    admission=["NATA (Council of Architecture) and/or JEE Main Paper 2A.", "Telangana B.Arch counselling is done by JNAFAU using NATA/JEE scores.", "NITs (Trichy, Calicut etc.) and SPA Vijayawada through JoSAA (JEE Main Paper 2A rank)."],
    colleges=["JNAFAU School of Planning & Architecture, Hyderabad", "Private architecture colleges affiliated to JNAFAU"],
    subjects=["Architectural Design Studio", "Building Construction & Materials", "History of Architecture", "Structures", "Climatology", "Building Services", "Town Planning", "AutoCAD, Revit, SketchUp, 3ds Max"],
    pass_rules=["University (JNAFAU) rules: about 40–50% per subject. Studio/design subjects have separate jury marks."],
    private=[("Junior Architect", "Architecture firms", "₹20,000–40,000"), ("Interior Designer", "Interior firms", "₹18,000–35,000"),
             ("BIM / Revit Modeller", "Engineering & design firms", "₹20,000–40,000"), ("Urban Designer", "Consultancies", "₹25,000–45,000")],
    govt=[("Assistant Architect", "TG R&B Dept, GHMC, HMDA (TGPSC)", "B.Arch + CoA registration"), ("Town Planning Officer", "DTCP / HMDA / TGPSC", "B.Arch / B.Planning"),
          ("Architect", "CPWD, Railways, MES (Defence)", "B.Arch")],
    self_emp=["Own architecture practice after CoA registration", "Interior design business"],
    higher=["M.Arch, M.Plan (via GATE AR / CEED)", "Master of Urban Design"]))

D["imsc"] = ("Integrated_MSc_Research_IISER_NISER", "Integrated BS-MS / M.Sc for Research (IISER, NISER, UoH)", dict(
    about=["A 5-year science research programme for students who want to become scientists."],
    duration="5 years", eligibility=["Inter MPC/BiPC with 60%+ (relaxation for reserved categories)."],
    admission=["IISER Aptitude Test (IAT) for the 7 IISERs.", "NEST for NISER Bhubaneswar and UM-DAE CEBS.", "University of Hyderabad Integrated M.Sc via CUET-UG.", "IISc Bangalore BS (Research) via JEE/NEET/IAT scores."],
    subjects=["Physics, Chemistry, Biology, Maths, Earth Sciences; specialisation in the final 2 years", "Research thesis"],
    pass_rules=["Institute grading (CGPA). A minimum CGPA is needed to continue."],
    private=[("Research Scientist / Data Scientist", "R&D labs, biotech, AI firms", "₹40,000–80,000"), ("Quant Analyst", "Finance firms", "₹60,000+")],
    govt=[("Scientist (after PhD)", "CSIR labs (CCMB, IICT, NGRI in Hyderabad), DRDO, ISRO, BARC", "PhD / M.Sc"), ("Assistant Professor", "IITs/IISERs/universities", "PhD")],
    higher=["PhD (India/abroad with scholarships)", "DST INSPIRE-SHE scholarship (₹80,000/year) for top students"]))

D["nda"] = ("NDA_Defence_Officer", "NDA – Army / Navy / Air Force Officer after Inter", dict(
    about=["The National Defence Academy trains cadets for 3 years to become officers, with a free degree (JNU)."],
    duration="3 years at NDA + 1 year at IMA/INA/AFA",
    eligibility=["Unmarried, age 16.5–19.5 years.", "Army: 12th in any stream. Navy/Air Force: 12th with Physics & Maths.", "Women are eligible (since 2021)."],
    admission=["UPSC NDA written exam (Maths 300 + General Ability 600) twice a year → SSB interview (5 days) → medical → merit."],
    extra=[("Other officer entries after 12th", ["Indian Navy 10+2 B.Tech Cadet Entry (via JEE Main rank + SSB)", "Army TES (Technical Entry Scheme, PCM 60%+ and JEE Main) + SSB"])],
    private=[("After service: corporate security, management, aviation (Air Force pilots)", "Corporates", "Very good")],
    govt=[("Lieutenant / Sub-Lieutenant / Flying Officer", "Indian Army / Navy / Air Force", "Level 10 pay ₹56,100 + MSP & allowances")],
    route=["Class 11: start NDA Maths + GK preparation", "Apply in 12th (NDA I in Jan, NDA II in May)", "Clear written exam → SSB → merit list", "3 years NDA → 1 year academy → commissioned officer"],
    tips=["Sainik School Kalikiri and RIMC-style coaching help", "Physical fitness: run 2.4 km under 10 minutes, push-ups, swimming"]))

D["merchant_navy"] = ("Merchant_Navy", "Merchant Navy – B.Sc Nautical Science / B.Tech Marine Engineering / GP Rating", dict(
    about=["You work on commercial ships as a Deck officer (Navigation) or an Engine officer. The pay is high and the job involves long months at sea."],
    duration="B.Sc Nautical Science: 3 years; B.Tech Marine Engg: 4 years; DNS: 1 year + sea time; GP Rating: 6 months",
    eligibility=["12th PCM 60% (Maths & Physics) and English 50%.", "Age 17–25. Eyesight 6/6 with no colour blindness (for deck)."],
    admission=["IMU-CET (Indian Maritime University) or DG Shipping-approved institutes."],
    private=[("Deck Cadet → Third Officer → Captain", "Shipping companies", "Cadet ₹30,000–60,000; officers ₹1.5–8 lakh+"),
             ("Trainee Marine Engineer → Chief Engineer", "Shipping companies", "₹40,000 → ₹5–8 lakh+")],
    govt=[("Officers in Shipping Corporation of India", "SCI", "Competency certificate"), ("Navigation / Engineering posts", "Indian Navy / Coast Guard", "Separate exams")],
    tips=["Verify that the institute is DG Shipping approved – many fake agents exist"]))

D["pilot"] = ("Commercial_Pilot_CPL", "Commercial Pilot Licence (CPL) – Become a Pilot", dict(
    about=["Training at a DGCA-approved flying school to fly commercial aircraft."],
    duration="About 18–24 months (200 flying hours) + type rating",
    eligibility=["12th with Physics & Maths (others can clear Physics & Maths via NIOS)", "Age 17+", "DGCA Class 2 then Class 1 medical"],
    admission=["DGCA ground exams (Air Navigation, Meteorology, Regulations, Technical) plus flying hours.", "Telangana State Aviation Academy (Begumpet, Hyderabad); IGRUA Rae Bareli; airline cadet programmes (IndiGo, Air India)."],
    extra=[("Cost", ["Training costs about ₹40 lakh–1 crore including type rating. Education loans are available."])],
    private=[("First Officer (co-pilot)", "IndiGo, Air India, Akasa, SpiceJet", "₹1.5–3 lakh"), ("Captain", "Airlines", "₹4–10 lakh"), ("Flight Instructor", "Flying schools", "₹50,000–1.5 lakh")],
    govt=[("Pilot (Flying Branch)", "Indian Air Force via NDA / AFCAT / CDS", "Separate route"), ("Pilot", "State govt aviation / BSF Air Wing", "CPL + experience")]))

D["ame"] = ("Aircraft_Maintenance_Engineering_AME", "Aircraft Maintenance Engineering (AME) / B.Sc Aviation", dict(
    about=["AMEs inspect and certify aircraft. They need a DGCA licence (B1 – mechanical, B2 – avionics)."],
    duration="2–4 years (DGCA CAR-147 institutes)", eligibility=["12th PCM 50%."],
    admission=["Entrance + interview at DGCA-approved institutes (several in Hyderabad near Begumpet/Shamshabad)."],
    private=[("Aircraft Maintenance Technician", "Airlines, MRO (GMR Aero Technic, Air India Engineering)", "₹25,000–45,000"), ("Licensed AME", "Airlines", "₹80,000–2 lakh")],
    govt=[("Technician", "HAL, Air India Engineering Services, AAI", "AME licence / diploma")]))

D["cabin_crew"] = ("Aviation_Cabin_Crew_and_Airport_Jobs", "Air Hostess / Cabin Crew / Airport Ground Staff", dict(
    about=["Service jobs in airlines and airports. Hyderabad RGIA is a major hub."], duration="Short courses 6–12 months (not compulsory) / BBA Aviation 3 years",
    eligibility=["12th any group (degree preferred)", "Age 18–27, height and fitness as per airline", "Good English communication"],
    admission=["Direct airline walk-ins and online applications; aviation academies"],
    private=[("Cabin Crew", "IndiGo, Air India, Emirates, Qatar, Etihad", "₹30,000–60,000 (Gulf airlines higher, tax-free)"), ("Ground Staff / Customer Service", "Airlines, GMR Hyderabad Airport", "₹18,000–30,000"),
             ("Airport Operations", "GMR, ground handling companies", "₹20,000–35,000")],
    govt=[("Junior Assistant (Fire / Office)", "Airports Authority of India", "12th / degree as per post")], any_degree=True))
