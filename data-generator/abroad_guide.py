from builder import make
from abroad_countries import C
from abroad_prof import P

G = "08_Work_and_Study_Abroad_Guide"
S = "09_Scholarships_and_Student_Support"

ECR = ["Afghanistan", "Bahrain", "Indonesia", "Iraq", "Jordan", "Kuwait", "Lebanon", "Libya*", "Malaysia", "Oman", "Qatar", "Saudi Arabia", "Iran", "South Sudan", "Sudan", "Syria", "Thailand", "UAE", "Yemen*"]


def guide():
    idx = [[p["name"], ", ".join(C[r[0]]["name"].split(" (")[0] for r in p["rows"][:3])] for p in P.values()]
    make(f"{G}/00_Read_First_Abroad_Guide.docx", "Work & Study Abroad – Read First", [
        ("How this folder works", ["Every course folder in this project now has an 'Abroad_Jobs' sub-folder with 3 files: Top 10 countries, Job search apps by country, Step-by-step plan.",
                                   "This folder (08) has the common information: country guides, language tests, documents, safe emigration, study-abroad route and costs."]),
        ("Profession → top 3 countries (quick view)", [("table", ["Profession", "Top 3 countries"], idx)]),
        ("Golden rules", ["Experience in India first (1–3 years) makes abroad jobs much easier.", "One target country at a time – each has its own exams.",
                          "Never pay agents for visas or 'guaranteed jobs'.", "Learn English well; for Germany/Japan/France learn the local language."]),
    ], subtitle="Abroad Guide")

    for code, c in C.items():
        profs = [p["name"] for p in P.values() if any(r[0] == code for r in p["rows"])]
        secs = [("Work visa routes", c["visa"]), ("Language", [c["lang"]]), ("Permanent stay / PR", [c["pr"]]),
                ("Job search apps & websites", c["general"])]
        if c.get("health"):
            secs.append(("Healthcare jobs & licensing", c["health"]))
        if c.get("eng"):
            secs.append(("Engineering registration", c["eng"]))
        if c.get("edu"):
            secs.append(("Teaching jobs", c["edu"]))
        secs += [("Official / government portal", [c["official"]]), ("Indian Embassy / Consulate", [c["embassy"]]),
                 ("Professions from this project that have this country in their Top 10", profs or ["—"]), ("Important", [c["note"]])]
        fn = c["name"].split(" (")[0].replace(" & ", "_and_").replace(" ", "_").replace("/", "_")
        make(f"{G}/01_Country_Guides/{fn}.docx", f"Country Guide – {c['name']}", secs, subtitle="Abroad Guide – Country")

    make(f"{G}/02_Language_Tests.docx", "Language Tests for Abroad (English, German, Japanese, French)", [
        ("English tests", [("table", ["Test", "Used for", "Score needed (typical)", "Validity"], [
            ["IELTS Academic / General / UKVI", "UK, Australia, NZ, Ireland, Canada (General), study abroad", "6.0–7.5 overall (health jobs 7+)", "2 years"],
            ["PTE Academic / PTE Core", "Australia, NZ, UK, Canada (Core)", "50–79 depending on purpose", "2 years"],
            ["TOEFL iBT", "USA study, many universities", "80–100+", "2 years"],
            ["OET (Occupational English Test)", "Doctors, nurses, pharmacists, physios – UK, Ireland, Australia, NZ, USA (ECFMG)", "Grade B (350) in each skill for most", "2 years"],
            ["CELPIP General", "Canada PR only", "CLB 7–9+", "2 years"],
            ["Duolingo English Test", "Many universities (not visas)", "110–130", "2 years"]])]),
        ("Other languages", [("table", ["Language", "Test", "Levels"], [
            ["German", "Goethe-Zertifikat, telc, ÖSD (telc Medizin C1 for doctors)", "A1 → C2 (B1/B2 for most jobs, C1 medical)"],
            ["Japanese", "JLPT (July & December)", "N5 (basic) → N1 (expert); N4 for SSW, N2 for office jobs"],
            ["French", "TEF / TCF (Canada & France), DELF/DALF", "A1 → C2; extra Canada points"],
            ["Arabic", "Not required usually for Gulf jobs", "Basic spoken Arabic helps"]])]),
        ("Preparation tips", ["Start 3–6 months before you need the score.", "Use the official free practice tests on each test website.", "Speaking: practise daily with recordings; Writing: get feedback."]),
    ], subtitle="Abroad Guide")

    make(f"{G}/03_Documents_Attestation_Verification.docx", "Documents, Attestation, Apostille & Credential Verification", [
        ("Two ways to legalise Indian certificates", [("table", ["Method", "Countries (examples)", "Process"], [
            ["MEA Apostille (Hague Convention)", "USA, UK, Germany, France, Netherlands, Australia, NZ, Ireland, Japan, South Korea, Singapore, Canada, Saudi Arabia, Oman, Bahrain",
             "State verification of the certificate → MEA Apostille sticker (MEA Branch Secretariat Hyderabad / MEA-authorised agencies)"],
            ["MEA Attestation + Embassy attestation", "UAE, Qatar, Kuwait (non-Apostille countries)", "State verification → MEA attestation → Embassy of that country in India → (sometimes) Foreign Ministry after arrival"]])]),
        ("Step 1 – State verification (Telangana)", ["Educational certificates must first be verified by the state-designated authority (Telangana General Administration Department / education department, after the Board or University confirms them) before MEA Apostille.",
                                                    "Personal documents (birth/marriage) are verified by the state Home/GAD department.", "Check the latest process at mea.gov.in (Apostille / Attestation page)."]),
        ("Credential evaluation (separate from attestation)", [("table", ["Country", "Body"], [
            ["Canada", "WES, ICAS, IQAS, CES (ECA for Express Entry)"], ["USA", "WES, ECE (NACES members); ECFMG for doctors; CGFNS for nurses"],
            ["UK", "UK ENIC (Statement of Comparability)"], ["Germany", "anabin database (H+), ZAB Statement of Comparability"],
            ["Australia", "Profession's assessing authority (Engineers Australia, ACS, ANMAC, AMC, VETASSESS, CPA/CA ANZ)"], ["New Zealand", "NZQA"],
            ["Gulf (UAE, Qatar, Oman, Saudi, Bahrain, Kuwait)", "DataFlow primary source verification (healthcare & many professions)"]])]),
        ("Other documents", ["Passport – apply at passportindia.gov.in; 10th pass gets ECNR (no emigration check)", "Police Clearance Certificate (PCC) – Passport Seva Kendra",
                             "Experience letters on company letterhead + salary slips", "Professional registration (medical/nursing/pharmacy council)"]),
    ], subtitle="Abroad Guide")

    make(f"{G}/04_Safe_Emigration_and_Avoiding_Fraud.docx", "Safe Emigration – eMigrate, ECR, Insurance, Helplines & Fraud Signs", [
        ("ECR countries (19) – emigration clearance needed for ECR passport holders", [", ".join(ECR), "* Emigration clearance for Libya and Yemen is currently suspended (MEA, April 2026)."]),
        ("eMigrate (emigrate.gov.in)", ["ECR workers must get emigration clearance online.", "Shows MEA-registered recruiting agents and notified illegal agents.", "Foreign employers must be registered before recruiting from India."]),
        ("PBBY – Pravasi Bharatiya Bima Yojana (compulsory for ECR workers)", ["₹10 lakh cover for accidental death or permanent disability + hospitalisation, repatriation, legal expenses.", "Premium about ₹275 (2 years) / ₹375 (3 years)."]),
        ("Help lines (24x7, in 11 languages)", ["Toll-free: 1800 11 3090", "From abroad: +91-11-26885021", "WhatsApp: +91 74283 21144", "Email: helpline@mea.gov.in", "MADAD grievance portal: madad.gov.in"]),
        ("Telangana government help", ["TOMCOM – Telangana Overseas Manpower Company Ltd (govt recruiting agency) – overseas jobs with training", "Telangana NRI / Gulf workers welfare support through the state govt"]),
        ("Signs of a FAKE job offer", ["Asks money for visa/'processing'/medical before an interview", "Offer from Gmail/Yahoo address, no company website", "Very high salary for easy work",
                                       "Visit visa promised to be 'converted' to work visa", "Agent not found on eMigrate list", "Pressure to decide quickly; contract not shown"]),
    ], subtitle="Abroad Guide")

    make(f"{G}/05_Study_Abroad_then_Work.docx", "Study Abroad First, Then Work – Post-Study Work Visas", [
        ("Why this route", ["Arts, commerce, science and many other graduates find it easier to get jobs abroad after a local degree (Masters).", "A local degree removes most recognition problems."]),
        ("Post-study work visas (2026 – check official sites)", [("table", ["Country", "Post-study work permission"], [
            ["USA", "OPT 12 months + STEM OPT 24 months (STEM degrees)"], ["UK", "Graduate Route 2 years (18 months for applications from January 2027); PhD 3 years"],
            ["Canada", "PGWP up to 3 years (field-of-study and language rules apply)"], ["Australia", "Temporary Graduate visa (485) – duration depends on degree"],
            ["Germany", "18 months to find a job after graduation"], ["Ireland", "Stamp 1G – 1 year (bachelor's) / 2 years (Masters)"],
            ["New Zealand", "Post-Study Work Visa up to 3 years"], ["France", "APS / job-search permit after Masters"], ["Netherlands", "Orientation Year (1 year)"],
            ["Singapore", "Long-term visit pass to search for work (then EP)"]])]),
        ("Entrance / tests", ["GRE / GMAT (some programmes)", "IELTS / TOEFL / PTE / Duolingo", "SOP, LORs, CV"]),
        ("Funding", ["Telangana overseas scholarships up to ₹20 lakh – see folder 09", "DAAD (Germany), Chevening (UK), Fulbright-Nehru (USA), Commonwealth, Erasmus Mundus (EU), MEXT (Japan), Eiffel (France)",
                     "Germany: most public universities charge no tuition (semester fee only)"]),
    ], subtitle="Abroad Guide")

    make(f"{G}/06_Cost_Planner_Abroad.docx", "Cost Planner – How Much Money You Need", [
        ("Typical one-time costs (approx, 2026)", [("table", ["Item", "Approx cost"], [
            ["Passport (normal)", "₹1,500–2,000"], ["IELTS / PTE / OET", "₹17,000–40,000 per attempt"], ["Credential verification (DataFlow/WES)", "₹10,000–35,000"],
            ["Licensing exams – Gulf Prometric", "₹15,000–30,000"], ["Licensing exams – UK PLAB 1 + 2", "£268 + £981 (~₹1.4 lakh) + travel"],
            ["Licensing exams – Australia AMC (doctors)", "AU$ 2,920 (MCQ) + ~AU$ 4,000 (clinical)"], ["Visa fees", "₹10,000 – ₹2.5 lakh depending on country (UK adds Immigration Health Surcharge)"],
            ["Flight", "₹15,000 (Gulf) – ₹80,000 (USA/Canada)"], ["First 2 months living money (West)", "₹2–4 lakh"]])]),
        ("Money-saving tips", ["Gulf/UK/Ireland employers often pay visa & flight – ask before you pay.", "Use education loans with interest subsidy (see folder 09).", "Don't pay agents for things you can do yourself online."]),
    ], subtitle="Abroad Guide")


def scholarships():
    make(f"{S}/01_TG_ePASS_Fee_Reimbursement_Post_Matric.docx", "Telangana ePASS – Post-Matric Scholarship & Fee Reimbursement", [
        ("What it gives", ["RTF – Reimbursement of Tuition Fee (paid to the college).", "MTF – Maintenance Fee (monthly, to student's bank account; more for hostel students)."]),
        ("Who can apply", ["Telangana resident students from Inter (Class 11) up to PG, diploma, ITI and professional courses.",
                           "Family income limit: SC/ST – below ₹2 lakh/year; BC/EBC/Minority – below ₹1.5 lakh/year (check current G.O. for each category/course)."]),
        ("Rules", ["75% attendance every term", "Only convener/competent-authority seats are fully covered in professional courses", "Aadhaar-linked bank account"]),
        ("How to apply", ["telanganaepass.cgg.gov.in – free to apply, no agent needed", "Fresh registration in the first year; renewal every year"]),
    ], subtitle="Scholarships")

    make(f"{S}/02_Telangana_Overseas_Scholarships.docx", "Telangana Overseas Scholarships (Study Abroad) – up to ₹20 Lakh", [
        ("Schemes", [("table", ["Scheme", "For", "Covers"], [
            ["Ambedkar Overseas Vidya Nidhi (SC Development)", "SC students", "Up to ₹20 lakh + one-way economy ticket + visa charges"],
            ["Ambedkar Overseas Vidya Nidhi (ST Welfare)", "ST students", "Up to ₹20 lakh + one-way ticket + visa charges"],
            ["Mahatma Jyothiba Phule Overseas Vidya Nidhi", "BC & EBC students", "Up to ₹20 lakh + one-way ticket + visa charges"],
            ["Chief Minister's Overseas Scholarship Scheme", "Minority students", "Up to ₹20 lakh + one-way ticket"]])]),
        ("Common eligibility", ["Family income below ₹5 lakh/year", "60% in graduation (for PG abroad)", "Age up to 35 years", "Only one child per family",
                                "Valid test scores – e.g. GRE 260 / GMAT 500 and TOEFL 60 / IELTS 6.0 / PTE 50", "Admission (I-20 / CAS / COE) from a university in an allowed country"]),
        ("Allowed countries", ["USA, UK, Australia, Canada, Singapore, Germany, New Zealand, Japan, France, South Korea"]),
        ("How to apply", ["telanganaepass.cgg.gov.in → Overseas scholarships (apply within the notified dates each season)", "Merit weightage (BC scheme): graduation 60%, GRE/GMAT 20%, English test 20%"]),
        ("Central scheme", ["National Overseas Scholarship (Ministry of Social Justice) for SC and other eligible groups – check nosmsje.gov.in"]),
    ], subtitle="Scholarships")

    make(f"{S}/03_Central_Govt_Scholarships_NSP.docx", "Central Government Scholarships (National Scholarship Portal)", [
        ("Main schemes", [("table", ["Scheme", "For", "Benefit (approx)"], [
            ["Central Sector Scheme of Scholarship for College & University Students", "Top 20 percentile in Class 12; family income ≤ ₹4.5 lakh", "₹12,000/yr (UG yrs 1–3), ₹20,000/yr (PG/professional later years)"],
            ["AICTE Pragati", "Girl students in AICTE diploma/degree (income ≤ ₹8 lakh)", "₹50,000/yr"],
            ["AICTE Saksham", "Students with disability (AICTE courses)", "₹50,000/yr"],
            ["INSPIRE-SHE (DST)", "Top 1% in Class 12 / top JEE-NEET ranks studying natural sciences", "₹80,000/yr"],
            ["NMMS – National Means-cum-Merit", "Class 8 exam → Classes 9–12; income ≤ ₹3.5 lakh", "₹12,000/yr"],
            ["PM YASASVI", "OBC / EBC / DNT students", "Pre/post-matric & top-class school/college scholarships"],
            ["Post-Matric Scholarship for SC/ST (centrally sponsored)", "Implemented in Telangana through ePASS", "Fees + maintenance"]])]),
        ("How to apply", ["scholarships.gov.in (NSP) – one-time registration (OTR) with Aadhaar", "Check the scheme's current status and dates every year (some schemes are revised)"]),
    ], subtitle="Scholarships")

    make(f"{S}/04_Education_Loans.docx", "Education Loans – PM Vidyalaxmi, Interest Subsidy & Banks", [
        ("PM-Vidyalaxmi (Govt of India, from Nov 2024)", ["Collateral-free, guarantor-free loans for students admitted to Quality Higher Education Institutions (NIRF-ranked list).",
                                                          "Govt guarantees 75% of default for loans up to ₹7.5 lakh.", "3% interest subvention during moratorium on loans up to ₹10 lakh for family income up to ₹8 lakh.",
                                                          "Apply through the PM-Vidyalaxmi portal (built on the Vidya Lakshmi portal)."]),
        ("CSIS – Central Sector Interest Subsidy", ["Full interest subsidy during the moratorium for family income up to ₹4.5 lakh (IBA model education loan, studies in India)."]),
        ("Bank loans (India & abroad)", ["SBI (Student Loan, Scholar Loan, Global Ed-Vantage for abroad), Bank of Baroda, Canara, Union Bank", "NBFCs for abroad (higher interest – compare carefully)",
                                         "Income Tax Section 80E: deduction on education-loan interest for up to 8 years"]),
        ("Tips", ["Apply to public-sector banks first (lower interest)", "Keep admission letter, fee structure, income certificate, Aadhaar/PAN ready", "Never pay 'loan agents' – apply directly"]),
    ], subtitle="Scholarships & Loans")

    make(f"{S}/05_Free_Coaching_Study_Circles.docx", "Free Coaching in Telangana – Study Circles & Residential Colleges", [
        ("Govt study circles (free coaching + often stipend)", ["TG BC Study Circle – Group I/II/III/IV, Civil Services, Banking, RRB, Police, DSC coaching",
                                                                "TG SC Study Circle – Civil Services & competitive exams", "TG Tribal (ST) Study Circle", "TG Minorities Study Circle",
                                                                "Selection is through an entrance test announced in newspapers and on the department websites"]),
        ("Residential (Gurukul) colleges – free education with hostel", ["TSWREIS (SC), TTWREIS (ST), MJPTBCWREIS (BC), TMREIS (Minorities) junior & degree colleges",
                                                                         "Many run special coaching for EAPCET, NEET, JEE, CA, civil services"]),
        ("Online free resources", ["SWAYAM / NPTEL (free courses with certificates)", "DIKSHA, e-PG Pathshala", "T-SAT (Telangana Skill & Knowledge network) TV/YouTube classes"]),
    ], subtitle="Student Support")

    make(f"{S}/06_Student_Helplines_and_Wellbeing.docx", "Student Helplines & Wellbeing", [
        ("Important helplines (India)", [("table", ["Need", "Number / site"], [
            ["Mental health support (Tele-MANAS – free, 24x7)", "14416 or 1-800-891-4416"], ["Emergency (police/fire/ambulance)", "112"], ["Women helpline", "181"],
            ["Child helpline", "1098"], ["Cyber crime / online fraud", "1930 · cybercrime.gov.in"], ["Anti-ragging (UGC)", "1800-180-5522 · antiragging.in"],
            ["Indians abroad (MEA)", "1800 11 3090"]])]),
        ("Exam & career stress tips", ["Everyone's path is different – many successful people changed courses.", "Talk to parents, teachers or a counsellor early.",
                                       "Plan B is normal: Polytechnic/ITI/degree routes all lead to good jobs.", "Sleep, exercise and breaks improve marks more than all-night study."]),
    ], subtitle="Student Support")


def run():
    guide()
    scholarships()
