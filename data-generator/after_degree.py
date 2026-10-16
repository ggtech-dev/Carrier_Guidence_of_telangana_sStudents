from builder import make

B = "07_After_Degree_Govt_and_Private_Jobs"
G = f"{B}/01_Govt_Jobs_for_Any_Degree"

REL_C = "Age relaxation (central): SC/ST +5, OBC +3, PwBD +10 years."
REL_S = "Age relaxation (Telangana): SC/ST/BC +5, PwBD +10, govt employees +5 years."

JOBS = [
    ("01_UPSC_Civil_Services_IAS_IPS", "UPSC Civil Services – IAS, IPS, IFS, IRS", "UPSC", ["Any degree"], ["21–32 years (General).", REL_C, "Attempts: 6 (General), 9 (OBC), unlimited till age (SC/ST)."],
     ["Prelims (GS + CSAT qualifying 33%)", "Mains (9 papers incl. essay, GS I–IV, optional ×2)", "Interview (275)"], "Level 10 – ₹56,100 basic + DA, HRA (IAS starting)", "upsc.gov.in"),
    ("02_TGPSC_Group_I", "TGPSC Group I – Deputy Collector, DSP, CTO, RTO, DM&HO admin posts", "TGPSC", ["Any degree"], ["18–46 years (check the latest notification)", REL_S],
     ["Prelims (GS, 150 marks)", "Mains (English qualifying + 6 papers)", "No interview in recent notifications"], "Approx ₹54,220–1,33,630 (varies by post)", "tspsc.gov.in"),
    ("03_TGPSC_Group_II", "TGPSC Group II – Municipal Commissioner Gr-III, Sub-Registrar, ACTO, Excise SI, Deputy Tahsildar", "TGPSC", ["Any degree"], ["18–44/46 years (check notification)", REL_S],
     ["Written exam – 4 papers (GS, History & Polity, Economy & Development, Telangana Movement)"], "Approx ₹31,000–1,00,000 range by post", "tspsc.gov.in"),
    ("04_TGPSC_Group_III_IV", "TGPSC Group III & IV – Senior Assistant, Junior Assistant, Typist, Bill Collector", "TGPSC", ["Group III: degree; Group IV: Inter/degree as per post"], ["18–44/46 years (check notification)", REL_S],
     ["Objective written exam(s)"], "State pay scales (Junior Assistant approx ₹24,280–72,850)", "tspsc.gov.in"),
    ("05_SSC_CGL", "SSC CGL – Income Tax Inspector, Excise Inspector, ASO, Auditor, Accountant", "Staff Selection Commission", ["Any degree (JSO: Maths/Stats)"], ["18–32 years by post", REL_C],
     ["Tier-I (CBT)", "Tier-II (Maths, Reasoning, English, GA, Computer + skill test)"], "Level 4 to Level 7 (₹25,500–₹44,900 basic)", "ssc.gov.in"),
    ("06_IBPS_SBI_Bank_PO_Clerk", "Bank PO & Clerk – IBPS, SBI, RRB (Telangana Grameena Bank)", "IBPS / SBI", ["Any degree; local language (Telugu) for clerk & RRB"], ["PO 20–30; Clerk 20–28 years", REL_C],
     ["Prelims → Mains → Interview (PO)", "Prelims → Mains (Clerk)"], "PO approx ₹48,480 basic (+ allowances); Clerk approx ₹24,050 basic+", "ibps.in, sbi.co.in"),
    ("07_RBI_Grade_B_and_Assistant", "RBI Grade B Officer & RBI Assistant", "Reserve Bank of India", ["Grade B: degree 60% (50% SC/ST)", "Assistant: degree 50%"], ["21–30 years", REL_C],
     ["Phase I, Phase II, Interview (Grade B)", "Prelims, Mains, LPT (Assistant)"], "Grade B approx ₹1 lakh+ gross; Assistant approx ₹45,000+ gross", "rbi.org.in"),
    ("08_RRB_NTPC_Graduate", "RRB NTPC (Graduate) – Station Master, Goods Guard, Senior Clerk, Commercial Supervisor", "Railway Recruitment Boards", ["Any degree"], ["18–36 years", REL_C],
     ["CBT-1, CBT-2, skill/aptitude test, medical"], "Level 5–6 (₹29,200–₹35,400 basic)", "rrbsecunderabad.gov.in"),
    ("09_TG_Police_Sub_Inspector", "Telangana Police Sub-Inspector (Civil, AR, TGSP, Fire, SPF)", "TGSLPRB", ["Any degree"], ["21–25/28 years (+ relaxations)", REL_S],
     ["Prelims", "PET/PMT (running, long jump, shot put)", "Final written exam"], "Approx ₹42,300–1,15,270", "tgprb.in"),
    ("10_Teacher_BEd_TET_DSC", "Government Teacher – School Assistant via B.Ed + TG TET + DSC", "School Education Dept, Telangana", ["Degree in subject + B.Ed (TG EdCET)", "Pass TG TET Paper II"], ["18–44/46 years (check notification)", REL_S],
     ["DSC/TRT written exam + TET weightage"], "School Assistant approx ₹42,300–1,15,270", "schooledu.telangana.gov.in"),
    ("11_Central_Teaching_KVS_NVS_CTET", "KVS / NVS / Army Schools – TGT & PGT", "KVS, NVS", ["Degree/PG + B.Ed + CTET"], ["Up to 35/40 years by post", REL_C],
     ["Written + interview / demo"], "TGT Level 7 (₹44,900); PGT Level 8 (₹47,600)", "kvsangathan.nic.in, navodaya.gov.in"),
    ("12_Defence_Officer_CDS_AFCAT", "Defence Officer after Degree – CDS, AFCAT, TA, SSC Tech", "UPSC / IAF / Army", ["CDS: any degree (IMA/OTA), engineering for INA/AFA", "AFCAT: degree 60% with Maths & Physics in 12th"],
     ["19–25 years by entry"], ["Written exam → SSB interview → medical"], "Level 10 – ₹56,100 + MSP", "upsc.gov.in, afcat.cdac.in"),
    ("13_LIC_AAO_and_Insurance", "LIC AAO / ADO & General Insurance Officers (NIACL, UIIC)", "LIC / insurance companies", ["Any degree"], ["21–30 years", REL_C],
     ["Prelims → Mains → Interview"], "AAO approx ₹88,000 gross (metro)", "licindia.in"),
    ("14_SSC_CHSL_MTS_Steno_for_Graduates", "Other SSC exams open to graduates (CHSL, Steno, CPO-SI)", "SSC", ["CHSL/Steno: 12th (graduates can apply)", "CPO SI (Delhi Police, CAPF): degree"], ["18–27/25 years", REL_C],
     ["CBT + skill / physical tests"], "Level 2–6", "ssc.gov.in"),
    ("15_Postgraduate_Lecturer_JL_DL", "Lecturer posts – Junior Lecturer, Degree Lecturer, Polytechnic Lecturer", "TGPSC / TREI-RB (residential)", ["JL: PG 50% in subject", "DL: PG 55% + NET/SET/PhD"], ["18–44/46 years (check notification)", REL_S],
     ["Written exam + demo / interview"], "JL approx ₹54,220+; DL UGC scales", "tspsc.gov.in, treirb.telangana.gov.in"),
]


def run():
    make(f"{B}/00_Read_First_After_Degree_Guide.docx", "After Degree – Govt Jobs, Private Jobs & PG Options", [
        ("Three paths after any degree", ["1) Government job exams (central & Telangana) – see folder 01_Govt_Jobs_for_Any_Degree (one file per job)",
                                         "2) Private jobs – see 02_Private_Jobs_by_Sector", "3) Higher studies (PG) – see 03_PG_Entrance_Exams"]),
        ("All govt exams at a glance", [("table", ["#", "Exam / job", "Recruiter"], [[i + 1, j[1], j[2]] for i, j in enumerate(JOBS)])]),
        ("Course-specific govt jobs", ["Each degree's own Word file (inside the Intermediate stream folders) lists the govt jobs specific to that degree."]),
    ], subtitle="After Degree")
    for fn, title, rec, edu, age, sel, pay, site in JOBS:
        make(f"{G}/{fn}.docx", title, [
            ("Recruiting organisation", [rec]), ("Educational qualification", edu), ("Age limit", age), ("Selection process", sel),
            ("Salary / pay", [pay]), ("How to apply", [f"Official website: {site}", "Follow Employment News and Eenadu/Sakshi Pratibha job pages."]),
            ("Preparation tips", ["Start in the final year of the degree", "Previous-year papers + mock tests", "Daily current affairs (The Hindu / Eenadu)",
                                  "For Telangana exams: Telangana history, movement, culture, schemes and geography are very important"]),
        ], subtitle="Govt Job after Degree")

    P = f"{B}/02_Private_Jobs_by_Sector"
    SECT = [
        ("01_IT_and_Software", "IT & Software (Hyderabad HITEC City, Gachibowli)", [("Software Engineer / Developer", "B.Tech, MCA, B.Sc CS, BCA", "₹25,000–60,000"), ("QA / Tester", "Any IT degree", "₹20,000–35,000"),
                                                                                    ("Data Analyst", "B.Sc Stats/Maths, B.Com BA, B.Tech", "₹25,000–45,000"), ("Cloud / DevOps Engineer", "B.Tech / B.Sc + certifications", "₹30,000–60,000"),
                                                                                    ("Technical Support", "Any degree", "₹15,000–25,000")]),
        ("02_Banking_Finance_Accounts", "Banking, Finance & Accounts", [("F&A Process Associate", "B.Com/BBA", "₹18,000–30,000"), ("Relationship / Sales Officer", "Any degree", "₹18,000–30,000"),
                                                                     ("Financial Analyst", "B.Com + CA/CFA/MBA", "₹40,000–1 lakh"), ("Insurance Advisor", "Any degree", "Commission based")]),
        ("03_Pharma_Biotech_Healthcare", "Pharma, Biotech & Healthcare", [("QC / Production Chemist", "B.Sc Chemistry / B.Pharm", "₹15,000–28,000"), ("Medical Representative", "B.Sc / B.Pharm", "₹18,000–30,000 + incentive"),
                                                                        ("Medical Coder", "Life science degree", "₹18,000–30,000"), ("Lab / Imaging technician", "Allied health degree", "₹15,000–30,000")]),
        ("04_Sales_Marketing_HR", "Sales, Marketing & HR", [("Business Development Executive", "BBA/any degree", "₹18,000–30,000 + incentive"), ("Digital Marketing Executive", "Any degree + course", "₹15,000–30,000"),
                                                          ("HR Recruiter", "BBA/MBA HR", "₹15,000–25,000")]),
        ("05_Core_Engineering_Manufacturing", "Core Engineering & Manufacturing", [("Graduate Engineer Trainee", "B.Tech Mech/EEE/Civil/ECE", "₹20,000–40,000"), ("Site Engineer", "Civil", "₹20,000–35,000"),
                                                                               ("Design Engineer", "Mech/ECE with CAD/VLSI", "₹25,000–50,000")]),
        ("06_Media_Design_Hospitality", "Media, Design, Hospitality & Aviation", [("Content Writer / Editor", "BA/BJMC", "₹15,000–30,000"), ("Graphic / UI Designer", "BFA/B.Des", "₹15,000–50,000"),
                                                                               ("Hotel / F&B Associate", "Hotel Mgmt", "₹15,000–30,000"), ("Cabin Crew / Ground Staff", "Any degree", "₹20,000–60,000")]),
        ("07_Gulf_and_Abroad_Jobs", "Gulf & Abroad Jobs (UAE, Saudi, Qatar, Europe)", [("Accountant / Admin", "B.Com/BBA + experience", "AED 4,000–10,000"), ("Nurse / Technician", "Nursing / Allied health + licence", "AED 4,000–12,000"),
                                                                                    ("Engineer", "B.Tech + experience", "AED 6,000–15,000"), ("Hotel staff", "Hotel Mgmt", "AED 2,500–6,000 + stay")]),
    ]
    for fn, title, rows in SECT:
        make(f"{P}/{fn}.docx", f"Private Jobs – {title}", [
            ("Popular roles", [("table", ["Role", "Degree needed", "Starting salary (approx/month)"], [list(r) for r in rows])]),
            ("How to get these jobs", ["Campus placements", "Naukri, LinkedIn, Indeed, Foundit, Apna", "Telangana job melas (TASK, DEET – Digital Employment Exchange of Telangana)",
                                       "Gulf/abroad: use TOMCOM (Telangana Overseas Manpower Company) or eMigrate-registered agents only"]),
            ("Skills that increase salary", ["Communication in English", "Computer skills (Excel, typing, basic coding)", "Industry certifications", "Internships & projects"]),
        ], subtitle="Private Jobs after Degree")

    make(f"{B}/03_PG_Entrance_Exams/All_PG_Entrance_Exams.docx", "Post-Graduate Entrance Exams (Telangana & National)", [
        ("Telangana (TGCHE) entrances", [("table", ["Exam", "For"], [
            ["TG ICET", "MBA, MCA"], ["TG PGECET", "M.Tech, M.Pharm, M.Arch"], ["TG CPGET", "M.A., M.Sc, M.Com in Telangana universities"],
            ["TG EdCET", "B.Ed (2 years)"], ["TG PECET", "B.P.Ed / D.P.Ed (Physical Education)"], ["TG LAWCET / PGLCET", "LLB (3-yr) / LLM"]])]),
        ("National entrances", [("table", ["Exam", "For"], [
            ["GATE", "M.Tech at IITs/NITs, PSU jobs"], ["CAT / XAT / MAT / GMAT", "MBA at IIMs & B-schools"], ["IIT JAM", "M.Sc at IITs/IISc"], ["CUET-PG", "Central universities (UoH, EFLU, MANUU)"],
            ["NIMCET", "MCA at NITs"], ["NEET-PG / NEET-MDS / AIAPGET", "Medical, dental, AYUSH PG"], ["GPAT / NIPER JEE", "M.Pharm"], ["UGC-NET / CSIR-NET / TG SET", "Lecturer eligibility & JRF"],
            ["CLAT PG", "LLM at NLUs"], ["GRE / GMAT / IELTS / TOEFL", "Studies abroad"]])]),
    ], subtitle="After Degree → PG")
