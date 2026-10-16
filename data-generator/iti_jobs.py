from builder import make

ITI = "03_After_10th_ITI_Trades"
VOC = "04_After_10th_Other_Options"
J10 = "05_After_10th_Govt_Jobs_Telangana"
J12 = "06_After_Inter_Govt_Jobs"

ITI_PASS = [("table", ["Item", "Typical pass requirement (NCVT/AITT – CTS)"], [
    ["Trade Practical", "~60%"],
    ["Trade Theory, Workshop Calculation & Science, Engineering Drawing, Employability Skills", "~33% each"],
    ["Attendance", "80% needed to sit the exam"],
]), "Exam: All India Trade Test (AITT) conducted by DGT; certificate = NTC (National Trade Certificate).",
    "Verify current rules on dgt.gov.in / ncvtmis.gov.in."]

TRADES = [
    ("01_Electrician", "Electrician", "2 yrs", "10th with Science & Maths",
     ["Electrical safety & tools", "Wiring (domestic & industrial)", "DC/AC machines, transformers", "Motor winding", "Electrical estimation", "Solar installation basics"],
     ["Junior Lineman (TG DISCOMs)", "Railway Group D / Technician", "Singareni, NTPC, BHEL apprentices", "Electrical contractor (with licence)"]),
    ("02_Fitter", "Fitter", "2 yrs", "10th with Science & Maths",
     ["Measuring tools", "Filing, drilling, tapping", "Fitting & assembly", "Pipe fitting", "Maintenance of machines"],
     ["Railway Technician / Group D", "Ordnance factories", "BHEL, HAL apprentices", "Manufacturing plants"]),
    ("03_Electronics_Mechanic", "Electronics Mechanic", "2 yrs", "10th with Science & Maths",
     ["Electronic components", "Soldering & PCB", "Power supplies & amplifiers", "Digital electronics", "Repair of TV, mobile, inverters"],
     ["ECIL, BEL technician", "Mobile & electronics service centres", "Railway Technician"]),
    ("04_COPA_Computer_Operator", "Computer Operator & Programming Assistant (COPA)", "1 yr", "10th",
     ["Computer basics, Windows/Linux", "MS Office", "Internet & e-mail", "Basic programming (Python/JavaScript)", "DBMS basics", "Web design basics"],
     ["Data Entry Operator", "Computer Operator in offices", "MeeSeva / CSC centre operator", "DTP operator"]),
    ("05_Mechanic_Motor_Vehicle_MMV", "Mechanic Motor Vehicle (MMV)", "2 yrs", "10th with Science & Maths",
     ["Engine systems", "Fuel & ignition systems", "Transmission & brakes", "Vehicle electricals", "Servicing"],
     ["TGSRTC Shramik/Mechanic", "Automobile service centres", "Army technical trades"]),
    ("06_Welder", "Welder (Gas & Electric)", "1 yr", "8th/10th",
     ["Arc welding", "Gas welding & cutting", "TIG/MIG basics", "Welding safety", "Inspection of welds"],
     ["Shipyards, construction, fabrication", "Railways, SCCL", "Gulf jobs (good demand)"]),
    ("07_Plumber", "Plumber", "1 yr", "8th/10th",
     ["Pipe types & fittings", "Water supply lines", "Sanitary fittings", "Drainage"],
     ["Municipal bodies, HMWSSB contractors", "Construction companies", "Self-employment"]),
    ("08_Draughtsman_Civil", "Draughtsman (Civil)", "2 yrs", "10th with Science & Maths",
     ["Engineering drawing", "Building drawing", "Surveying", "AutoCAD", "Estimation"],
     ["Draughtsman in R&B, Irrigation", "Construction & architect firms"]),
    ("09_Draughtsman_Mechanical", "Draughtsman (Mechanical)", "2 yrs", "10th with Science & Maths",
     ["Machine drawing", "Geometric dimensioning", "AutoCAD / SolidWorks"],
     ["Design assistant in manufacturing firms", "Defence production units"]),
    ("10_Turner", "Turner", "2 yrs", "10th with Science & Maths",
     ["Lathe operations", "Threading & taper turning", "CNC basics"],
     ["Ordnance factories, HAL, BHEL", "Machine shops"]),
    ("11_Machinist", "Machinist", "2 yrs", "10th with Science & Maths",
     ["Milling, shaping, grinding", "CNC machining", "Measuring instruments"],
     ["Manufacturing & defence production units", "Railway workshops"]),
    ("12_Refrigeration_and_AC_Technician", "Refrigeration & Air-Conditioning Technician", "2 yrs", "10th with Science & Maths",
     ["Refrigeration cycle", "Compressors", "Split & window AC", "Cold storage", "Gas charging"],
     ["AC service companies", "Railways (AC coaches)", "Gulf jobs", "Self-employment"]),
    ("13_Wireman", "Wireman", "2 yrs", "8th/10th",
     ["House wiring", "Earthing", "Meters & panels", "Cable jointing"],
     ["Junior Lineman (TG DISCOMs)", "Electrical contractors"]),
    ("14_Mechanic_Diesel", "Mechanic Diesel", "1 yr", "10th",
     ["Diesel engines", "Fuel injection", "Engine overhaul", "Generators"],
     ["TGSRTC, Railways", "Generator & tractor service", "Army tradesman"]),
    ("15_Sewing_Technology", "Sewing Technology / Dress Making", "1 yr", "8th/10th",
     ["Pattern making", "Cutting & stitching", "Garment finishing", "Embroidery"],
     ["Garment industry", "Boutique / self-employment", "Textile parks"]),
]


def iti():
    make(f"{ITI}/00_About_ITI_Telangana.docx", "ITI – Industrial Training Institutes (Telangana)", [
        ("What is ITI?", [
            "Skill-based trade courses of 1 or 2 years under the Craftsmen Training Scheme (CTS).",
            "Managed in Telangana by the Department of Employment & Training (DET); national standard by DGT (NCVT).",
            "Govt ITIs have very low fees; many private ITIs also exist.",
        ]),
        ("Admission", [
            "Online application at the Telangana ITI admissions portal (usually June–August).",
            "Selection on merit of 10th marks (no entrance test); district-wise counselling.",
            "Age: minimum 14 years.",
        ]),
        ("Trades list (see each folder)", [("table", ["#", "Trade", "Duration", "Eligibility"], [[i + 1, t[1], t[2], t[3]] for i, t in enumerate(TRADES)])]),
        ("Pass Percentage", ITI_PASS),
        ("After ITI", [
            "Apprenticeship (1 year, stipend) – then NAC (National Apprenticeship Certificate).",
            "Lateral entry into 2nd year Polytechnic diploma (for 2-year ITI pass students).",
            "Govt jobs: Railway Group D/Technician, Junior Lineman, Ordnance factories, SCCL, defence tradesman.",
            "Gulf & overseas jobs (through TOMCOM – Telangana Overseas Manpower Company).",
        ]),
    ])
    for fn, name, dur, elig, syll, jobs in TRADES:
        make(f"{ITI}/{fn}/About_{fn[3:]}.docx", f"ITI Trade – {name}", [
            ("Course details", [f"Duration: {dur}", f"Eligibility: {elig}", "Certificate: NTC (NCVT) after AITT exam."]),
            ("What you learn", syll),
            ("Pass Percentage", ITI_PASS),
            ("Jobs & career", jobs),
            ("Next steps", ["Apprenticeship → NAC certificate", "Polytechnic lateral entry (2-yr trades)", "Start own service business with MUDRA / PMEGP loan"]),
        ], subtitle="After 10th → ITI Trade")


def other():
    make(f"{VOC}/01_Open_School_TOSS.docx", "Telangana Open School Society (TOSS)", [
        ("About", ["Distance-mode SSC and Intermediate for students who cannot attend regular college.", "TOSS Intermediate is accepted for degree, govt jobs and most entrance exams (check specific exam rules)."]),
        ("Who should choose", ["Working students, drop-outs, those who need flexibility."]),
        ("Pass mark", ["33%–35% per subject (check TOSS rules)."]),
    ])
    make(f"{VOC}/02_Apprenticeship.docx", "Apprenticeship after 10th / ITI", [
        ("Schemes", ["Apprentices Act – trade apprentices in Railways, PSUs, private industry (apprenticeshipindia.gov.in).", "NATS – for diploma/degree holders.", "Stipend paid every month; certificate (NAC) valued in govt jobs."]),
        ("Telangana opportunities", ["South Central Railway (RRC Secunderabad), BHEL, HAL, ECIL, NFC, SCCL, TGSRTC, private industries."]),
    ])
    make(f"{VOC}/03_Short_Term_Skill_Courses.docx", "Short-Term Skill & Certificate Courses", [
        ("Free / subsidised programmes", ["PMKVY – Pradhan Mantri Kaushal Vikas Yojana (3–6 months).", "DDU-GKY – rural youth placement-linked training.", "TASK – Telangana Academy for Skill & Knowledge.", "Young India Skills University (Telangana) programmes – check eligibility.", "National Academy of Construction (NAC) Hyderabad – construction trades."]),
        ("Popular courses", ["Computer basics, Tally & GST, DTP, Data Entry", "Mobile repair, CCTV installation, Solar technician", "Beautician, Tailoring, Driving (LMV/HMV)", "Hospitality, Retail sales, Health care assistant"]),
    ])
    make(f"{VOC}/04_Other_Career_Paths_after_10th.docx", "Other Paths after 10th", [
        ("Options", [
            "Defence at young age: Army Agniveer, Navy Agniveer MR, Coast Guard Navik DB (see Govt Jobs folder).",
            "Sports: Telangana Sports Schools / SATS hostels for talented athletes.",
            "Arts: Music, dance (Telugu University certificate courses), painting.",
            "Paramedical certificate courses (some need inter – check).",
            "Family business / agriculture with skill training (KVK Krishi Vigyan Kendras).",
        ]),
        ("Compare main paths", [("table", ["Path", "Duration", "Best for", "Next step"], [
            ["Intermediate", "2 yrs", "Degree, professional courses", "Engineering/Medical/Degree"],
            ["Polytechnic", "3 yrs", "Technical career, early job", "Job or B.Tech (ECET)"],
            ["ITI", "1–2 yrs", "Fast job, skilled trade", "Apprenticeship / Govt technical jobs"],
            ["Vocational Inter", "2 yrs", "Job-oriented + inter equivalent", "Job or degree"],
        ])]),
    ])


# ---------- Govt jobs after 10th: one file per job ----------
REL_C = "Age relaxation (central): SC/ST +5 yrs, OBC +3 yrs, PwBD +10 yrs, Ex-servicemen as per rules."
REL_S = "Age relaxation (Telangana): SC/ST/BC +5 yrs, PwBD +10 yrs, State Govt employees +5 yrs, Ex-servicemen +3 yrs (as per notification)."

JOBS10 = [
    ("01_India_Post_GDS", "India Post – Gramin Dak Sevak (BPM / ABPM / Dak Sevak)", "Department of Posts (Telangana Postal Circle)",
     ["10th pass with Mathematics & English (passed).", "Studied Telugu (local language) up to 10th.", "Basic computer knowledge; cycling knowledge."],
     ["18–40 years.", REL_C],
     ["No written exam – merit list on 10th marks.", "Document verification."],
     "TRCA: BPM ~₹12,000–29,380; ABPM/Dak Sevak ~₹10,000–24,470 per month.",
     "indiapostgdsonline.gov.in"),
    ("02_SSC_MTS_and_Havaldar", "SSC Multi-Tasking Staff (MTS) & Havaldar (CBIC/CBN)", "Staff Selection Commission",
     ["10th pass from a recognised board."],
     ["MTS: 18–25 years (some posts 18–27).", "Havaldar: 18–27 years.", REL_C],
     ["Computer Based Exam: Numerical & Reasoning, General English & General Awareness (two sessions).", "Havaldar: PET/PST (walking test).", "Document verification."],
     "Pay Level-1: ₹18,000 basic + allowances (~₹22,000–28,000 in hand).",
     "ssc.gov.in"),
    ("03_SSC_GD_Constable", "SSC GD Constable (BSF, CISF, CRPF, ITBP, SSB, Assam Rifles, SSF, NCB)", "Staff Selection Commission",
     ["10th pass."],
     ["18–23 years.", REL_C],
     ["CBT: 80 questions, 160 marks (Reasoning, GK, Maths, English/Hindi).", "PET (running: men 5 km in 24 min, women 1.6 km in 8.5 min – check notification) & PST (height/chest).", "Detailed medical exam, document verification."],
     "Pay Level-3: ₹21,700–69,100 + allowances.",
     "ssc.gov.in"),
    ("04_Railway_Group_D_Level1", "Railway Group D (Level-1) – Track Maintainer, Helper, Assistant, Pointsman", "Railway Recruitment Boards (RRB/RRC Secunderabad)",
     ["10th pass OR ITI OR National Apprenticeship Certificate (check notification)."],
     ["18–33 years (varies by notification).", REL_C],
     ["CBT: 100 questions (Maths, Reasoning, General Science, GK).", "PET: Men – lift 35 kg & walk 100 m in 2 min, run 1000 m in 4 min 15 s; Women – 20 kg, 1000 m in 5 min 40 s.", "Document verification & medical."],
     "Pay Level-1: ₹18,000 basic + DA, HRA (~₹28,000–35,000 gross).",
     "rrbsecunderabad.gov.in / indianrailways.gov.in"),
    ("05_Railway_Act_Apprentice_SCR", "Railway Act Apprentice – South Central Railway", "RRC Secunderabad",
     ["10th with 50% marks + ITI in the notified trade."],
     ["15–24 years.", REL_C],
     ["No exam – merit list on average of 10th & ITI marks.", "Medical & document verification."],
     "Stipend as per Apprentices Act during 1-year training; preference in Railway Group D later.",
     "scr.indianrailways.gov.in"),
    ("06_Army_Agniveer_GD_and_Tradesman", "Indian Army – Agniveer (General Duty / Tradesman)", "Indian Army (ARO Secunderabad covers Telangana)",
     ["Agniveer GD: 10th with 45% aggregate and 33% in each subject.", "Agniveer Tradesman: 10th pass (some trades 8th pass) – 33% each subject.", "(Clerk/Store Keeper & Technical need 12th.)"],
     ["17.5–21 years.", "Height ~166 cm for Telangana region (varies by region/notification)."],
     ["Online Common Entrance Exam (CEE).", "Recruitment rally: 1.6 km run, pull-ups, 9 ft ditch, zig-zag balance.", "Medical test."],
     "Agnipath: 4 years service, ₹30,000/month rising to ₹40,000 (approx); Seva Nidhi package ~₹10 lakh at exit; up to 25% retained as regular soldiers.",
     "joinindianarmy.nic.in"),
    ("07_Navy_Agniveer_MR", "Indian Navy – Agniveer MR (Matric Recruit)", "Indian Navy",
     ["10th pass (Chef, Steward, Hygienist roles)."],
     ["17.5–21 years (unmarried)."],
     ["Online written exam.", "PFT: 1.6 km run, squats, push-ups, sit-ups.", "Medical."],
     "Agnipath package – same as Army Agniveer.",
     "joinindiannavy.gov.in"),
    ("08_Coast_Guard_Navik_DB", "Indian Coast Guard – Navik (Domestic Branch)", "Indian Coast Guard",
     ["10th pass."],
     ["18–22 years.", REL_C],
     ["Stage I: CBT.", "Stage II: assessment & adaptability test, PFT (1.6 km in 7 min, squats, push-ups).", "Stage III/IV: documents & medical."],
     "Pay Level-3: ₹21,700 + allowances.",
     "joinindiancoastguard.cdac.in"),
    ("09_TG_Anganwadi_Teacher_and_Helper", "Telangana Anganwadi Teacher & Anganwadi Helper", "Women Development & Child Welfare Dept, Telangana (district-wise)",
     ["10th pass (minimum; higher may get preference).", "Woman candidate, resident of the same village/ward."],
     ["Usually 21–35 years (check district notification)."],
     ["Merit + interview by district selection committee.", "Reservation as per state roster."],
     "Honorarium fixed by Govt of Telangana (Teacher ~₹13,650; Helper ~₹7,800 – revised from time to time).",
     "wdcw.tg.nic.in / district website"),
    ("10_TG_Courts_Process_Server_Office_Subordinate", "Telangana District Courts – Process Server, Office Subordinate, Copyist", "High Court for the State of Telangana",
     ["Process Server: 10th pass.", "Office Subordinate: 7th pass (degree holders may not be eligible).", "Copyist/Typist: 10th + typing (higher grade)."],
     ["18–34 years generally (state relaxations apply).", REL_S],
     ["Computer-based / written test + interview (as per notification)."],
     "State pay scale (Office Subordinate approx ₹19,000–58,850; Process Server/Copyist higher).",
     "tshc.gov.in"),
    ("11_TG_Junior_Lineman_Electricity", "Junior Lineman (JLM) – TGSPDCL / TGNPDCL", "Telangana Power Distribution Companies",
     ["10th pass + ITI in Electrical / Wireman, OR Intermediate Vocational (Electrical)."],
     ["18–35 years.", REL_S],
     ["Written test (ITI-level electrical).", "Pole climbing test (qualifying).", "Document verification."],
     "Approx ₹24,000–30,000 per month at start (pay revision applies).",
     "tgsouthernpower.org / tgnpdcl.com"),
    ("12_TGSRTC_Driver_Shramik_Conductor", "TGSRTC – Driver, Shramik (Mechanic helper), Conductor", "Telangana State Road Transport Corporation",
     ["Driver: 10th + Heavy Passenger Motor Vehicle licence with experience.", "Shramik: 10th + ITI (MMV, Diesel, Fitter, Welder, Electrician etc.).", "Conductor: 10th / Inter + conductor licence (check latest)."],
     ["Driver: 22–35 yrs; Shramik: 18–30 yrs (approx).", REL_S],
     ["Written test / driving test / medical (recruitments sometimes via TGSLPRB)."],
     "TGSRTC pay scales – revised periodically.",
     "tgsrtc.telangana.gov.in"),
    ("13_CAPF_Constable_Tradesman", "Constable (Tradesman) – BSF / CISF / CRPF / ITBP", "Respective Central Armed Police Force",
     ["10th pass + skill in trade (Cook, Cobbler, Tailor, Barber, Washerman, Sweeper, Carpenter etc.); ITI preferred for technical trades."],
     ["18–23 years (BSF up to 25 in some posts).", REL_C],
     ["PST & PET, document check, trade test, written exam, medical."],
     "Pay Level-3: ₹21,700–69,100.",
     "rectt.bsf.gov.in, cisfrectt.cisf.gov.in, rect.crpf.gov.in"),
    ("14_Defence_Civilian_Group_C", "Defence Civilian Group 'C' (MTS, Cook, Washerman, Fireman)", "Army units, Ordnance, EME, Navy depots (unit-wise notifications)",
     ["10th pass (some posts need trade experience)."],
     ["18–25 years.", REL_C],
     ["Written test + skill/trade test."],
     "Pay Level-1 / Level-2.",
     "Employment News & unit websites"),
    ("15_SCCL_ITI_Trade_Posts", "Singareni Collieries (SCCL) – ITI Trade / Worker Posts", "Singareni Collieries Company Ltd (Telangana)",
     ["10th + ITI in Electrician, Fitter, Welder, Turner, Motor Mechanic etc."],
     ["18–30 years (as per notification); local reservation for Telangana districts in SCCL area."],
     ["Written exam / merit as per notification; medical fitness."],
     "SCCL wage board pay – among the best for ITI holders.",
     "scclmines.com"),
]

JOBS12 = [
    ("01_TG_Police_Constable_TGSLPRB", "Telangana Police Constable (Civil, AR, TGSP, Fireman, Jail Warder)", "TGSLPRB",
     ["Intermediate (12th) pass."], ["18–22/25 years (varies; relaxations apply).", REL_S],
     ["Preliminary written test.", "PET/PMT: running, long jump, shot put; height men ~167.6 cm, women ~152.5 cm.", "Final written exam."],
     "Pay ~₹24,280–72,850 (state pay scale).", "tgprb.in"),
    ("02_SSC_CHSL", "SSC CHSL – LDC, Junior Secretariat Assistant, Data Entry Operator", "SSC",
     ["12th pass."], ["18–27 years.", REL_C], ["Tier I CBT, Tier II CBT + skill/typing test."], "Pay Level-2 to Level-5.", "ssc.gov.in"),
    ("03_NDA", "NDA – National Defence Academy (Officer entry)", "UPSC",
     ["12th pass (Army – any stream; Navy/Air Force – Physics & Maths)."], ["16.5–19.5 years, unmarried."],
     ["Written exam (Maths 300 + GAT 600).", "SSB interview (5 days).", "Medical."], "Officer pay (Lieutenant) after training ~₹56,100 + allowances.", "upsc.gov.in"),
    ("04_Air_Force_Agniveer_Vayu", "Indian Air Force – Agniveer Vayu", "IAF",
     ["12th with Maths, Physics, English 50% (Science) or any stream 50% with English 50%; or 3-yr diploma."], ["17.5–21 years."],
     ["Online test, PFT, adaptability test, medical."], "Agnipath package.", "agnipathvayu.cdac.in"),
    ("05_Navy_Agniveer_SSR", "Indian Navy – Agniveer SSR", "Indian Navy",
     ["12th with Maths & Physics + one of Chemistry/Biology/CS."], ["17.5–21 years."], ["CBT, PFT, medical."], "Agnipath package.", "joinindiannavy.gov.in"),
    ("06_RRB_NTPC_Undergraduate", "RRB NTPC (12th level) – Clerk, Ticket Clerk, Accounts Clerk, Trains Clerk", "RRB",
     ["12th pass."], ["18–33 years.", REL_C], ["CBT 1, CBT 2, typing/skill test."], "Pay Level-2 / Level-3.", "rrbsecunderabad.gov.in"),
    ("07_TG_Forest_Beat_Officer", "Telangana Forest Beat Officer / Forest Section Officer", "TGPSC",
     ["Intermediate (FBO); degree with science (FSO)."], ["18–30 years (approx).", REL_S],
     ["Written exam, walking test (men 25 km in 4 hrs, women 16 km), medical."], "State pay scale.", "tspsc.gov.in"),
    ("08_Primary_Teacher_DElEd_SGT", "Primary Teacher (SGT) via D.El.Ed", "TG DEECET → D.El.Ed (2 yrs) → TG TET → DSC",
     ["Intermediate 50% (45% reserved) for D.El.Ed admission."], ["17+ for D.El.Ed; 18–44 for DSC (relaxations)."],
     ["TG DEECET entrance → D.El.Ed course → TG TET → TRT/DSC exam."], "School Assistant/SGT state pay scale.", "schooledu.telangana.gov.in"),
    ("09_SSC_Stenographer", "SSC Stenographer Grade C & D", "SSC",
     ["12th pass."], ["18–27/30 years.", REL_C], ["CBT + shorthand skill test."], "Pay Level-4 / Level-6.", "ssc.gov.in"),
]


def _job(base, item, sub):
    fn, title, org, edu, age, sel, pay, site = item
    make(f"{base}/{fn}.docx", title, [
        ("Recruiting organisation", [org]),
        ("Educational qualification", edu),
        ("Age limit", age),
        ("Selection process", sel),
        ("Salary / pay", [pay]),
        ("How to apply", [f"Official website: {site}", "Watch Employment News, Eenadu/Sakshi job pages and the official site for notifications.", "Keep 10th memo, caste certificate, residence (local) certificate, Aadhaar and photos ready."]),
        ("Preparation tips", ["Practise previous year question papers.", "Daily: Maths/Reasoning 1 hr, GK & current affairs 30 min, English 30 min.", "For physical tests start running practice at least 3 months early."]),
    ], subtitle=sub)


def jobs():
    make(f"{J10}/00_All_Govt_Jobs_after_10th_List.docx", "Government Jobs after 10th – Telangana (Master List)", [
        ("All jobs (each has a separate Word file in this folder)", [("table", ["#", "Job", "Min. qualification", "Age"], [
            [i + 1, j[1], j[3][0], j[4][0]] for i, j in enumerate(JOBS10)])]),
        ("Important documents to keep ready", ["SSC (10th) memo", "Caste & income certificates (MeeSeva)", "Residence / local status certificate (study certificates 4th–10th)", "Aadhaar, photos, signature", "ITI / NAC certificate if any"]),
    ])
    for j in JOBS10:
        _job(J10, j, "Govt Job after 10th")
    make(f"{J12}/00_All_Govt_Jobs_after_Inter_List.docx", "Government Jobs after Intermediate (12th) – Master List", [
        ("All jobs (separate file for each)", [("table", ["#", "Job", "Qualification"], [[i + 1, j[1], j[3][0]] for i, j in enumerate(JOBS12)])]),
        ("How to use this folder", ["Open the separate Word file of each job for eligibility, age, selection process, salary and website.",
                                    "Most of these exams can be written while you continue a degree (distance/regular).", "Prepare with previous-year papers; for police/defence jobs start physical training early."]),
        ("After Inter you can also", ["Join a degree (see 01_After_10th_Intermediate → your group → After_12th folder)", "Write NDA / Agniveer exams (defence)", "Do D.El.Ed for primary teacher posts"]),
    ])
    for j in JOBS12:
        _job(J12, j, "Govt Job after Intermediate")


def run():
    iti(); other(); jobs()
