from builder import make, folder

B = "01_After_10th_Intermediate"

INTER_PASS = [
    "Pass mark: 35% in each subject (theory), e.g. 26/75, 21/60, 35/100.",
    "Practicals (MPC/BiPC science subjects): 30 marks each in 2nd year; pass needs 35% of practical marks.",
    "No overall aggregate needed to pass, but each subject must be cleared separately.",
    "Divisions: 75%+ Distinction, 60%+ First Class, 50–59% Second Class, 35–49% Pass.",
    "Failed subjects can be cleared in the Advanced Supplementary Exams (May/June) of the same year.",
    "Improvement exam: students who passed can rewrite 1st-year papers to improve marks.",
    "TGBIE is introducing reforms (internal assessment, revised syllabus). Check tgbie.cgg.gov.in for the latest scheme.",
]


def overview():
    make(f"{B}/00_About_Intermediate_TGBIE.docx", "Intermediate (11th & 12th) in Telangana", [
        ("What is Intermediate?", [
            "Two-year course after 10th (1st year = 11th, 2nd year = 12th).",
            "Conducted by TGBIE – Telangana Board of Intermediate Education (earlier TSBIE).",
            "Annual public exams in both years (usually Feb–March); results in April.",
            "Available in Government Junior Colleges (free), Aided, Private, TG Model Schools, Residential (TSWREIS, TTWREIS, MJPTBCWREIS, TMREIS, KGBV).",
        ]),
        ("Admission", [
            "Eligibility: SSC / 10th pass (any board) – CBSE/ICSE students also eligible.",
            "Admission via TGBIE online admission schedule (usually May–June) or directly at college.",
            "Residential colleges admit through entrance tests (e.g. TG RJC CET / Gurukul CET).",
        ]),
        ("All Streams (Groups)", [("table", ["Group", "Main Subjects", "Best For"], [
            ["MPC", "Maths, Physics, Chemistry", "Engineering, B.Arch, B.Sc, NDA, Defence"],
            ["BiPC", "Botany, Zoology, Physics, Chemistry", "MBBS, BDS, Pharmacy, Agriculture, Nursing"],
            ["MEC", "Maths, Economics, Commerce", "CA, CMA, CS, B.Com, BBA, Finance"],
            ["CEC", "Civics, Economics, Commerce", "B.Com, CA, Banking, BBA"],
            ["HEC", "History, Economics, Civics", "BA, Law, Civil Services, Teaching"],
            ["MBiPC*", "Maths + BiPC (bridge course)", "Keep both Engineering & Medical options"],
            ["Vocational", "Job-oriented trades", "Early employment, Diploma lateral"],
        ])]),
        ("Language Subjects (all groups)", [
            "Part I: English – 100 marks per year.",
            "Part II: Second language – Telugu / Hindi / Sanskrit / Urdu / Arabic / French etc. – 100 marks per year.",
            "Ethics & Human Values, Environmental Education (qualifying, not added to total).",
        ]),
        ("Pass Percentage Rules", INTER_PASS),
        ("How to choose your group", [
            "Good in Maths & logic → MPC or MEC.",
            "Interested in biology, doctors, health → BiPC.",
            "Interested in business, accounts → MEC / CEC.",
            "Interested in society, history, law, civil services → HEC.",
            "Want quick job after 2 years → Vocational intermediate or Polytechnic/ITI instead.",
        ]),
    ])


MPC_SUBJ = [("table", ["Subject", "1st Year", "2nd Year"], [
    ["English", "100", "100"], ["Second Language", "100", "100"],
    ["Mathematics IA (Algebra, Vectors, Trigonometry)", "75", "-"],
    ["Mathematics IB (Coordinate Geometry, Calculus)", "75", "-"],
    ["Mathematics IIA (Complex Numbers, Probability, Binomial)", "-", "75"],
    ["Mathematics IIB (Circles, Conics, Integration, DE)", "-", "75"],
    ["Physics", "60", "60 + 30 practical"], ["Chemistry", "60", "60 + 30 practical"],
    ["Total", "470", "530  (Grand total 1000)"]])]

BIPC_SUBJ = [("table", ["Subject", "1st Year", "2nd Year"], [
    ["English", "100", "100"], ["Second Language", "100", "100"],
    ["Botany", "60", "60 + 30 practical"], ["Zoology", "60", "60 + 30 practical"],
    ["Physics", "60", "60 + 30 practical"], ["Chemistry", "60", "60 + 30 practical"],
    ["Total", "440", "560  (Grand total 1000)"]])]

MEC_SUBJ = [("table", ["Subject", "1st Year", "2nd Year"], [
    ["English", "100", "100"], ["Second Language", "100", "100"],
    ["Mathematics IA + IB", "75 + 75", "-"], ["Mathematics IIA + IIB", "-", "75 + 75"],
    ["Economics", "100", "100"], ["Commerce (incl. Accountancy)", "100", "100"],
    ["Total", "500", "500  (Grand total 1000)"]])]

CEC_SUBJ = [("table", ["Subject", "1st Year", "2nd Year"], [
    ["English", "100", "100"], ["Second Language", "100", "100"],
    ["Civics (Political Science)", "100", "100"], ["Economics", "100", "100"],
    ["Commerce (incl. Accountancy)", "100", "100"],
    ["Total", "500", "500  (Grand total 1000)"]])]

HEC_SUBJ = [("table", ["Subject", "1st Year", "2nd Year"], [
    ["English", "100", "100"], ["Second Language", "100", "100"],
    ["History", "100", "100"], ["Economics", "100", "100"], ["Civics", "100", "100"],
    ["Total", "500", "500  (Grand total 1000)"]])]


def mpc():
    p = f"{B}/MPC"
    make(f"{p}/About_MPC.docx", "MPC – Maths, Physics, Chemistry", [
        ("Who should take MPC", ["Students strong in Maths & science who want Engineering, Architecture, Defence (NDA), pure sciences or data/computer careers."]),
        ("Subjects & Marks (TGBIE)", MPC_SUBJ),
        ("Pass Percentage", INTER_PASS),
        ("Entrance exams you can prepare for during MPC", [
            "TG EAPCET (Engineering stream) – state engineering seats.",
            "JEE Main → NITs, IIITs, GFTIs; JEE Advanced → IITs.",
            "BITSAT, VITEEE, SRMJEEE and other private university tests.",
            "NDA (UPSC) – can apply in 12th; Indian Navy 10+2 B.Tech entry; Agniveer Vayu.",
            "NATA / JEE Main Paper-2 for B.Arch.",
            "IISER Aptitude Test, NEST, IAT for science research.",
        ]),
        ("Career paths after MPC", [
            "B.Tech/BE (4 yrs) – see folder After_12th_MPC/01_Engineering_BTech.",
            "B.Arch (5 yrs), B.Planning.",
            "B.Sc (Maths, Physics, Chemistry, Statistics, Computers, Data Science).",
            "BCA, B.Sc Computer Science, B.Com (also allowed).",
            "Defence: NDA → Army/Navy/Air Force officer.",
            "Merchant Navy (B.Sc Nautical Science, Marine Engineering).",
            "Commercial Pilot Licence (CPL).",
            "Every other option has its own folder inside After_12th_MPC. Govt jobs after Inter are in folder 06_After_Inter_Govt_Jobs.",
        ]),
    ])
    a = f"{p}/After_12th_MPC"
    e = f"{a}/01_Engineering_BTech"
    make(f"{e}/Engineering_Entrance_Exams.docx", "Entrance Exams for Engineering (after MPC)", [
        ("TG EAPCET (Engineering)", [
            "Conducted by JNTU Hyderabad on behalf of TGCHE (usually April–May).",
            "160 MCQs, 160 marks, 3 hours: Maths 80, Physics 40, Chemistry 40. No negative marks.",
            "Qualifying: 25% (40/160); no minimum for SC/ST for ranking.",
            "Inter eligibility for admission: 45% in MPC group subjects (40% reserved categories).",
            "Inter marks weightage was removed – rank is based only on EAPCET score.",
            "Counselling: TGCHE web options (tgeapcet.nic.in) – convenor seats (fee reimbursement possible for eligible students).",
        ]),
        ("JEE Main", [
            "Conducted by NTA, two sessions (January & April).",
            "Paper 1 (B.E/B.Tech): Maths, Physics, Chemistry – 300 marks, negative marking.",
            "Admission to NITs (NIT Warangal in Telangana), IIITs (IIIT Hyderabad has own process), GFTIs via JoSAA.",
            "Needs 75% in 12th (65% SC/ST) or top-20 percentile for NIT/IIT admission.",
        ]),
        ("JEE Advanced", ["Top ~2.5 lakh JEE Main qualifiers can write; admission to IITs (IIT Hyderabad in Telangana)."]),
        ("Other exams", ["BITSAT (BITS Hyderabad campus), VITEEE, SRMJEEE, Amrita, MET, KIIT, CUET-UG (some universities)."]),
        ("Top engineering colleges in Telangana", [
            "IIT Hyderabad, NIT Warangal, IIIT Hyderabad, BITS Pilani-Hyderabad.",
            "JNTUH College of Engineering (Hyderabad, Sultanpur, Jagtial, Manthani), OU College of Engineering, KU College of Engineering.",
            "CBIT, VNR VJIET, Vasavi, MVSR, MGIT, Sreenidhi, CVR, Gokaraju Rangaraju, Mahindra University, etc.",
        ]),
        ("Lateral entry", ["Diploma holders join 2nd year B.Tech through TG ECET – see Polytechnic folder."]),
    ])

    BR = [
        ("01_Computer_Science_Engineering_CSE", "Computer Science & Engineering (CSE)",
         ["Programming (C, Python, Java)", "Data Structures & Algorithms", "DBMS", "Operating Systems", "Computer Networks", "Software Engineering", "Compiler Design", "Cloud & Web Technologies"],
         ["Software Developer", "Full-stack / Backend Engineer", "DevOps / Cloud Engineer", "Database Developer", "Cyber Security Analyst", "Product Engineer"],
         ["TCS, Infosys, Wipro, Accenture, Cognizant", "Microsoft, Google, Amazon, Deloitte (Hyderabad campuses)", "Startups at T-Hub Hyderabad"]),
        ("02_AI_and_Machine_Learning", "Artificial Intelligence & Machine Learning (AI&ML)",
         ["Python & Maths for ML (Linear Algebra, Probability)", "Machine Learning", "Deep Learning", "NLP & Computer Vision", "Big Data", "MLOps"],
         ["ML Engineer", "AI Engineer", "Data Scientist", "Computer Vision Engineer", "AI Research Assistant"],
         ["Product companies, AI startups, analytics firms, Global Capability Centres in Hyderabad"]),
        ("03_Data_Science", "Data Science (CSD / CS-DS)",
         ["Statistics & Probability", "Python, R, SQL", "Data Mining & Warehousing", "Machine Learning", "Data Visualization (Power BI, Tableau)", "Big Data (Hadoop, Spark)"],
         ["Data Analyst", "Data Scientist", "Data Engineer", "Business Intelligence Developer"],
         ["Banks, e-commerce, consulting, healthcare analytics, IT services"]),
        ("04_Information_Technology", "Information Technology (IT)",
         ["Programming", "Web Technologies", "DBMS", "Networks", "Information Security", "Cloud Computing", "Software Testing"],
         ["Software Engineer", "Web Developer", "System / Network Administrator", "QA / Test Engineer"],
         ["IT services & product companies"]),
        ("05_Electronics_and_Communication_ECE", "Electronics & Communication Engineering (ECE)",
         ["Electronic Devices & Circuits", "Signals & Systems", "Digital Electronics", "Analog & Digital Communication", "Microprocessors & Embedded Systems", "VLSI Design", "Antennas & Wave Propagation"],
         ["VLSI / Chip Design Engineer", "Embedded Engineer", "Telecom Engineer", "Software roles (many ECE grads move to IT)"],
         ["Qualcomm, Intel, AMD, Micron (Hyderabad)", "BEL, ECIL, DRDO labs, ISRO", "Telecom companies"]),
        ("06_Electrical_and_Electronics_EEE", "Electrical & Electronics Engineering (EEE)",
         ["Electrical Circuits", "Electrical Machines", "Power Systems", "Power Electronics", "Control Systems", "Renewable Energy", "Electric Vehicles"],
         ["Electrical Design Engineer", "Power Plant Engineer", "AE in TG TRANSCO / GENCO / DISCOMs", "EV & Solar Engineer"],
         ["TG GENCO, TRANSCO, TGSPDCL/TGNPDCL, NTPC, BHEL, Power Grid, Siemens, ABB, Schneider"]),
        ("07_Mechanical_Engineering", "Mechanical Engineering",
         ["Engineering Mechanics", "Thermodynamics", "Strength of Materials", "Manufacturing Processes", "Fluid Mechanics", "Machine Design", "CAD/CAM", "Heat Transfer"],
         ["Design Engineer", "Production / Manufacturing Engineer", "Maintenance Engineer", "Quality Engineer"],
         ["BHEL, HAL, DRDO, Tata, L&T, Mahindra, Cyient, automobile & aerospace firms"]),
        ("08_Civil_Engineering", "Civil Engineering",
         ["Surveying", "Building Materials & Construction", "Structural Analysis", "RCC & Steel Design", "Geotechnical Engineering", "Transportation Engineering", "Water Resources & Environment"],
         ["Site / Structural Engineer", "AE in R&B, Panchayat Raj, Irrigation (TGPSC)", "Quantity Surveyor", "Urban Planner"],
         ["L&T, Megha Engineering, NCC, GMR, HMDA, GHMC, irrigation department"]),
        ("09_Chemical_Engineering", "Chemical Engineering",
         ["Chemical Process Calculations", "Mass & Heat Transfer", "Chemical Reaction Engineering", "Process Control", "Plant Design"],
         ["Process Engineer", "Production Engineer (pharma, petrochemicals)", "Safety Engineer"],
         ["Pharma companies in Hyderabad (Dr. Reddy's, Aurobindo, Hetero), IOCL, ONGC, Reliance"]),
        ("10_Aerospace_Engineering", "Aerospace / Aeronautical Engineering",
         ["Aerodynamics", "Aircraft Structures", "Propulsion", "Flight Mechanics", "Avionics"],
         ["Aircraft Design Engineer", "Maintenance Engineer", "Scientist at DRDO/ISRO"],
         ["HAL, DRDO (DRDL, RCI Hyderabad), ISRO, Tata Advanced Systems, Airbus, Boeing"]),
        ("11_Automobile_Engineering", "Automobile Engineering",
         ["Automotive Engines", "Vehicle Dynamics", "Transmission Systems", "Electric & Hybrid Vehicles", "Automotive Electronics"],
         ["Automotive Design Engineer", "Service / Quality Engineer", "EV Engineer"],
         ["Maruti, Tata Motors, Mahindra, Hyundai, Ola Electric, TVS"]),
        ("12_Robotics_Engineering", "Robotics Engineering",
         ["Kinematics & Dynamics of Robots", "Sensors & Actuators", "Control Systems", "Embedded Programming", "AI for Robotics"],
         ["Robotics Engineer", "Automation Engineer", "Drone Engineer"],
         ["Manufacturing automation, drone startups, defence labs"]),
        ("13_Mechatronics_Engineering", "Mechatronics Engineering",
         ["Mechanics", "Electronics", "PLC & SCADA", "Control Systems", "Industrial Automation"],
         ["Automation Engineer", "Maintenance Engineer", "Instrumentation Engineer"],
         ["Siemens, Bosch, ABB, manufacturing plants"]),
        ("14_Biotechnology_Engineering", "Biotechnology Engineering",
         ["Cell & Molecular Biology", "Genetic Engineering", "Bioprocess Engineering", "Immunology", "Bioinformatics"],
         ["Research Associate", "Production / QC in pharma & vaccines", "Bioinformatics Analyst"],
         ["Bharat Biotech, Biological E (Genome Valley, Hyderabad), CCMB, research labs"]),
        ("15_Petroleum_Engineering", "Petroleum Engineering",
         ["Petroleum Geology", "Drilling Engineering", "Reservoir Engineering", "Production Engineering"],
         ["Drilling Engineer", "Reservoir Engineer", "Production Engineer"],
         ["ONGC, Oil India, Cairn, Reliance, Schlumberger"]),
        ("16_Agricultural_Engineering", "Agricultural Engineering",
         ["Farm Machinery", "Soil & Water Conservation", "Irrigation & Drainage", "Food Processing", "Renewable Energy in Agriculture"],
         ["Agricultural Engineer", "AEO in Agriculture Department", "Farm Machinery Designer"],
         ["PJTSAU (Telangana), NABARD, tractor & irrigation companies"]),
        ("17_Mining_Engineering", "Mining Engineering",
         ["Mine Surveying", "Mining Methods", "Mine Ventilation", "Rock Mechanics", "Mine Safety & Legislation"],
         ["Mining Engineer", "Mine Manager (with certificate)", "Safety Officer"],
         ["Singareni Collieries (SCCL – Telangana), Coal India, NMDC"]),
        ("18_Marine_Engineering", "Marine Engineering",
         ["Marine Engines", "Ship Construction", "Naval Architecture basics", "Marine Electrical Systems"],
         ["Marine Engineer on ships", "Port / Shipyard Engineer"],
         ["Shipping companies, Cochin Shipyard, Navy (technical entry)"]),
        ("19_Metallurgical_Engineering", "Metallurgical & Materials Engineering",
         ["Physical Metallurgy", "Extractive Metallurgy", "Material Testing", "Heat Treatment", "Corrosion"],
         ["Metallurgist", "Quality / Materials Engineer"],
         ["SAIL, Tata Steel, JSW, Midhani & DMRL (Hyderabad)"]),
        ("20_Textile_Engineering", "Textile Engineering / Technology",
         ["Fibre Science", "Yarn & Fabric Manufacturing", "Textile Chemical Processing", "Garment Technology"],
         ["Production Engineer in textile mills", "Quality Controller"],
         ["Textile mills, Kakatiya Mega Textile Park (Warangal), apparel exporters"]),
        ("21_Environmental_Engineering", "Environmental Engineering",
         ["Water & Wastewater Treatment", "Air Pollution Control", "Solid Waste Management", "Environmental Impact Assessment"],
         ["Environmental Engineer", "Pollution Control Board officer", "EHS Officer"],
         ["TG Pollution Control Board, municipal bodies, consultancies, industries"]),
        ("22_Food_Technology", "Food Technology",
         ["Food Chemistry & Microbiology", "Food Processing & Preservation", "Food Packaging", "Food Safety (FSSAI)"],
         ["Food Technologist", "Quality Assurance", "Food Safety Officer"],
         ["ITC, Nestle, PepsiCo, dairy units (Vijaya Telangana), FSSAI"]),
        ("23_Industrial_Engineering", "Industrial / Production Engineering",
         ["Operations Research", "Production Planning", "Work Study & Ergonomics", "Supply Chain", "Lean & Six Sigma"],
         ["Industrial Engineer", "Operations Manager", "Supply Chain Analyst"],
         ["Manufacturing, logistics & e-commerce companies"]),
    ]
    for folder_name, name, subj, roles, recruiters in BR:
        make(f"{e}/Engineering_Branches/{folder_name}/About_{folder_name[3:]}.docx", name, [
            ("Course details", [
                "Degree: B.Tech / B.E. – 4 years (8 semesters).",
                "Admission: TG EAPCET / JEE Main / JEE Advanced (IITs) / private university tests.",
                "Pass rule (JNTUH R22, typical): min 35% in semester-end exam and 40% overall (internal + external) per subject; credits needed to be promoted.",
            ]),
            ("Main subjects", subj),
            ("Job roles", roles),
            ("Recruiters / where you can work", recruiters),
            ("Higher studies", ["M.Tech / M.E. via GATE or TG PGECET", "MS abroad (GRE/IELTS)", "MBA via CAT / TG ICET", "Research (PhD)"]),
            ("Route map (year by year)", [
                "Year 1: Strong basics – maths, programming, communication.",
                "Year 2: Core subjects + 1–2 small projects; learn tools of your branch.",
                "Year 3: Internship, certifications, mini-project; start GATE/placement prep.",
                "Year 4: Major project, campus placements, GATE / higher-study exams.",
            ]),
            ("Government job options", ["See folder 'Govt_Jobs_after_Engineering' – GATE PSUs, ESE, TGPSC AE/AEE, RRB JE, SSC JE, ISRO/DRDO."]),
        ], subtitle="After Inter MPC → Engineering Branch")
    make(f"{e}/Engineering_Branches/00_Compare_All_Branches.docx", "All Engineering Branches – Quick Comparison", [
        ("Branches list", [("table", ["#", "Branch", "Main job area"], [
            [i + 1, b[1], b[3][0]] for i, b in enumerate(BR)])]),
        ("How to pick a branch", [
            "Choose interest first, then college quality, then branch demand.",
            "CSE/AI/DS/IT: highest software demand, but competition is also highest.",
            "ECE/EEE/Mech/Civil: core + government job opportunities (AE, JE, PSUs).",
            "Specialised branches (Mining, Petroleum, Marine) have fewer but specific jobs – check placement record.",
        ]),
    ])
    make(f"{e}/Govt_Jobs_after_Engineering/Govt_Jobs_after_BTech.docx", "Government Jobs after Engineering (B.Tech)", [
        ("Central jobs", [("table", ["Exam / Job", "Conducted by", "Eligibility"], [
            ["GATE → PSU jobs (NTPC, IOCL, BHEL, ONGC, Power Grid, BEL)", "IITs (GATE)", "B.Tech in relevant branch"],
            ["Engineering Services (IES/ESE)", "UPSC", "B.Tech, age 21–30"],
            ["Civil Services (IAS/IPS)", "UPSC", "Any degree, age 21–32"],
            ["SSC JE (Civil/Mech/Elec)", "SSC", "Diploma / B.Tech"],
            ["RRB JE / SSE", "Railway Recruitment Boards", "Diploma / B.Tech"],
            ["ISRO Scientist/Engineer 'SC'", "ISRO ICRB", "B.Tech 65%+"],
            ["DRDO Scientist 'B'", "DRDO (GATE based)", "B.Tech + GATE"],
            ["Indian Army/Navy/AF technical entry (TGC, SSC Tech, AFCAT)", "Defence", "B.Tech"],
            ["Bank IT Officer / SO", "IBPS / SBI", "B.Tech"],
        ])]),
        ("Telangana state jobs", [("table", ["Job", "Recruiter", "Branch"], [
            ["Assistant Engineer / AEE (Irrigation, R&B, PR, Public Health)", "TGPSC", "Civil, Mech, Elec"],
            ["AE / Sub-Engineer (TG GENCO, TRANSCO, SPDCL, NPDCL)", "Power utilities", "EEE, ECE, Civil, Mech"],
            ["Group I / II / III services", "TGPSC", "Any degree"],
            ["Lecturers (Polytechnic)", "TGPSC", "M.Tech / B.Tech"],
            ["Singareni (SCCL) Management Trainee", "SCCL", "Mining, Mech, Elec"],
            ["HMWSSB / GHMC engineers", "TGPSC / board", "Civil, Elec"],
        ])]),
    ])


def bipc():
    p = f"{B}/BiPC"
    make(f"{p}/About_BiPC.docx", "BiPC – Botany, Zoology, Physics, Chemistry", [
        ("Who should take BiPC", ["Students interested in medicine, life sciences, agriculture, pharmacy and health care."]),
        ("Subjects & Marks (TGBIE)", BIPC_SUBJ),
        ("Pass Percentage", INTER_PASS),
        ("Entrance exams", [
            "NEET-UG (NTA) – MBBS, BDS, AYUSH (BAMS, BHMS, BUMS, BNYS), BVSc in some colleges.",
            "TG EAPCET (Agriculture & Pharmacy stream) – B.Sc Agriculture, Horticulture, B.Pharm, Pharm-D, BVSc, B.Tech Biotech/Food Tech/Dairy, Fisheries.",
            "CUET-UG, AIIMS nursing / paramedical exams, IISER aptitude test.",
        ]),
    ])


def commerce_arts():
    p = f"{B}/MEC"
    make(f"{p}/About_MEC.docx", "MEC – Maths, Economics, Commerce", [
        ("Who should take MEC", ["Students good at maths who want CA, CMA, CS, finance, banking, analytics or business careers."]),
        ("Subjects & Marks (TGBIE)", MEC_SUBJ),
        ("Pass Percentage", INTER_PASS),
        ("After MEC", [("table", ["Course", "Notes"], [
            ["CA (Chartered Accountant)", "ICAI: Foundation → Intermediate → Final + articleship"],
            ["CMA (Cost & Management Accountant)", "ICMAI"],
            ["CS (Company Secretary)", "ICSI – CSEET entry"],
            ["B.Com (General, Computers, Hons, Taxation, Business Analytics)", "DOST / CUET-UG"],
            ["BBA, BBA Business Analytics", "DOST / university"],
            ["B.Sc Maths/Statistics/Economics", "DOST"],
            ["BA Economics", "DOST / CUET-UG"],
            ["Integrated Law (BA LLB / BBA LLB)", "TG LAWCET (5-yr) / CLAT"],
            ["IPM (Integrated MBA)", "IIM IPMAT"],
        ])]),
        ("Govt jobs after degree", ["Bank PO/Clerk (IBPS, SBI), RBI Assistant, SSC CGL, TGPSC Group II/III, Accounts Officer, Income Tax Inspector."]),
    ])
    p = f"{B}/CEC"
    make(f"{p}/About_CEC.docx", "CEC – Civics, Economics, Commerce", [
        ("Who should take CEC", ["Students interested in commerce & business without heavy maths."]),
        ("Subjects & Marks (TGBIE)", CEC_SUBJ),
        ("Pass Percentage", INTER_PASS),
        ("After CEC", ["B.Com (all specialisations), BBA, BA, BA LLB (TG LAWCET/CLAT), CA/CMA/CS, Hotel Management, Journalism.", "Govt exams: SSC CHSL (after inter), Bank Clerk/PO, SSC CGL, TGPSC Groups (after degree)."]),
    ])
    p = f"{B}/HEC"
    make(f"{p}/About_HEC.docx", "HEC – History, Economics, Civics", [
        ("Who should take HEC", ["Students interested in history, politics, society, law, teaching and civil services."]),
        ("Subjects & Marks (TGBIE)", HEC_SUBJ),
        ("Pass Percentage", INTER_PASS),
        ("After HEC", ["BA (History, Political Science, Economics, Sociology, Public Administration, Psychology, Journalism).", "BA LLB (5 yrs) via TG LAWCET / CLAT.", "D.El.Ed (TG DEECET) → primary teacher (SGT); B.Ed after degree.", "Hotel Management, Mass Communication, Fine Arts, Social Work (BSW)."]),
        ("Govt jobs", ["Civil Services (UPSC) and TGPSC Group I/II – HEC subjects help a lot.", "Police (SI/Constable), Teacher (TG TET + DSC), Revenue & Panchayat posts."]),
    ])


def vocational_inter():
    p = f"{B}/Vocational_Intermediate"
    make(f"{p}/About_Vocational_Intermediate.docx", "Vocational Intermediate (TGBIE)", [
        ("What is it?", [
            "2-year intermediate equal to regular inter, but job-oriented with practical training and on-the-job training (OJT).",
            "Offered by TGBIE in Govt Junior Colleges and private vocational colleges.",
            "Bridge course allows entry to degree courses; some courses allow lateral entry to Polytechnic 2nd year.",
        ]),
        ("Popular vocational courses", [("table", ["Sector", "Courses"], [
            ["Engineering & Technology", "Electrical Technician, Automobile Engineering Technician, Construction Technology, Mechanical Technician, Electronics Technician, Computer Science & Engineering"],
            ["Paramedical", "Medical Lab Technician (MLT), Multipurpose Health Worker (Female/Male), Ophthalmic Technician, Physiotherapy Technician"],
            ["Business & Commerce", "Accounting & Taxation, Office Assistantship, Banking & Insurance"],
            ["Agriculture", "Crop Production, Dairying, Sericulture, Fisheries"],
            ["Home Science & Others", "Garment Making, Preschool Teacher Training, Tourism & Hospitality, Computer Graphics & Animation"],
        ])]),
        ("Pass percentage", ["35% in each theory paper; practicals usually require 50%.", "English + vocational theory + practicals/OJT."]),
        ("Jobs", ["Junior Lineman (electrical), lab assistant, health worker, accounts assistant, private hospitals & industries.", "Apprenticeship and self-employment."]),
    ])


def run():
    overview(); mpc(); bipc(); commerce_arts(); vocational_inter()
