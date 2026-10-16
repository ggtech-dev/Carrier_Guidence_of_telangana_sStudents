from deg_common import UG_PASS, DOST, DOST_COLLEGES

ARTS_HIGHER = ["M.A. via TG CPGET / CUET-PG (UoH, EFLU, MANUU)", "B.Ed via TG EdCET → teacher", "LLB 3-year via TG LAWCET",
               "UGC-NET / TG SET → Assistant Professor", "Civil services preparation (UPSC / TGPSC)"]
ARTS_GOVT = [
    ("Group I (Deputy Collector, DSP, CTO, RDO)", "TGPSC", "Any degree; Age 18–46 (check notification)"),
    ("Group II (Municipal Commissioner Gr III, Sub-Registrar, ACTO, Excise SI)", "TGPSC", "Any degree"),
    ("Group III / IV (Senior Assistant, Junior Assistant, Typist)", "TGPSC", "Degree / Inter as per post"),
    ("Sub-Inspector of Police", "TGSLPRB", "Any degree + physical tests"),
    ("Village / Revenue posts (Gram Panchayat Officer etc.)", "Telangana Govt", "Degree as per notification"),
    ("School Assistant (Social Studies / Languages)", "TG DSC", "Degree + B.Ed + TET"),
]

D = {}

def ba(key, folder, title, about, subjects, private, govt_extra=None, higher_extra=None):
    D[key] = (folder, title, dict(
        about=about, duration="3 years (6 semesters)", eligibility=["Inter in any group (HEC best fit)."], admission=DOST, colleges=DOST_COLLEGES,
        subjects=subjects, pass_rules=UG_PASS, private=private, govt=(govt_extra or []) + ARTS_GOVT, any_degree=True,
        higher=(higher_extra or []) + ARTS_HIGHER))

ba("ba_history", "BA_History", "B.A. History (HEC/HPP combinations)",
   ["Studies Indian, Telangana and world history. It is a strong base for civil services."],
   ["Ancient, Medieval & Modern India", "History & Culture of Telangana", "World History", "Indian National Movement", "Archaeology & Museology (elective)"],
   [("Content / Research Writer", "Publishers, ed-tech", "₹15,000–25,000"), ("Tour Guide / Heritage Executive", "Tourism", "₹12,000–25,000"), ("Teacher (with B.Ed)", "Private schools", "₹12,000–25,000")],
   [("Archaeology / Museum Assistant", "TG Heritage Dept, ASI", "History degree/PG")], ["M.A. History / Archaeology"])
ba("ba_polsci", "BA_Political_Science", "B.A. Political Science",
   ["Studies government, constitution, politics and international relations."],
   ["Indian Constitution & Government", "Political Theory", "International Relations", "Public Policy", "Telangana Politics"],
   [("Political / Policy Research Associate", "Think tanks, campaigns, media", "₹18,000–30,000"), ("Journalist (politics desk)", "Media", "₹15,000–25,000"), ("NGO Program Associate", "NGOs", "₹15,000–25,000")])
ba("ba_pubadmin", "BA_Public_Administration", "B.A. Public Administration / Public Policy & Governance",
   ["Studies how government departments and public policy work. It is useful for Group I/II and UPSC exams."],
   ["Administrative Theory", "Indian Administration", "Local Government (Panchayat Raj)", "Public Policy", "E-Governance"],
   [("Administrative Executive", "Corporates, hospitals", "₹15,000–25,000"), ("Program / Policy Associate", "NGOs, CSR foundations", "₹18,000–30,000")])
ba("ba_sociology", "BA_Sociology", "B.A. Sociology",
   ["Studies society, family, caste, rural and urban change."],
   ["Introduction to Sociology", "Indian Society", "Rural & Urban Sociology", "Social Research Methods", "Gender Studies"],
   [("Field / Social Research Associate", "NGOs, research firms", "₹15,000–25,000"), ("CSR Executive", "Corporates", "₹18,000–28,000"), ("HR Assistant", "Companies", "₹15,000–22,000")])
ba("ba_psychology", "BA_BSc_Psychology", "B.A. / B.Sc Psychology",
   ["Studies the human mind and behaviour. You need an M.A./M.Sc + M.Phil (RCI) to become a clinical psychologist."],
   ["General Psychology", "Developmental Psychology", "Abnormal Psychology", "Social & Organisational Psychology", "Counselling basics", "Psychological testing"],
   [("HR / Talent Assessment Executive", "Companies", "₹18,000–28,000"), ("School Counsellor Assistant", "Schools", "₹15,000–25,000"), ("Behavioural Research Assistant", "Research firms", "₹18,000–30,000")],
   [("Counsellor / Psychologist (after PG + RCI)", "Govt hospitals (IMH Erragadda), schools, Police", "PG + RCI registration")],
   ["M.A./M.Sc Psychology → M.Phil Clinical Psychology (RCI) → Clinical Psychologist"])
ba("ba_journalism", "BA_Journalism_Mass_Communication", "B.A. Journalism & Mass Communication / BJMC",
   ["Trains you for newspapers, TV, digital media, advertising and PR."],
   ["Reporting & Editing", "Media Laws & Ethics", "TV & Radio Production", "Digital & Social Media", "Advertising & PR", "Photography & Video"],
   [("Reporter / Sub-Editor", "Eenadu, Sakshi, Deccan Chronicle, Telangana Today, TV9, NTV", "₹12,000–25,000"),
    ("Content Writer / Social Media Executive", "Agencies, startups", "₹15,000–30,000"), ("Video Editor / Anchor", "TV/YouTube channels", "₹15,000–35,000"), ("PR Executive", "PR agencies", "₹18,000–30,000")],
   [("Assistant Public Relations Officer", "TG I&PR Dept (TGPSC)", "Degree + journalism"), ("News Reader / Program Executive", "Prasar Bharati (DD, AIR)", "Degree")],
   ["MA / PG Diploma Mass Communication (UoH, IIMC)"])
ba("ba_english", "BA_English_Literature", "B.A. English Literature (B.A.(L))",
   ["Studies English language & literature. There is strong demand for good English skills."],
   ["British, American, Indian writing in English", "Linguistics & Phonetics", "Creative Writing", "Translation"],
   [("Content Writer / Copywriter", "Agencies, IT firms", "₹15,000–30,000"), ("Technical Writer", "IT companies", "₹25,000–45,000"),
    ("Customer Support (Voice)", "BPOs", "₹15,000–25,000"), ("English Trainer", "Institutes", "₹15,000–30,000")],
   higher_extra=["M.A. English (EFLU Hyderabad – top university for English)"])
ba("ba_languages", "BA_Telugu_Hindi_Urdu_Sanskrit", "B.A. Languages – Telugu / Hindi / Urdu / Sanskrit / Arabic",
   ["Literature and language degrees. They are useful for teaching, translation, media and govt language posts."],
   ["Classical & modern literature", "Grammar & Linguistics", "Translation", "Journalism in the language"],
   [("Translator / Transcriptionist", "Media, localisation companies, AI data firms", "₹15,000–30,000"), ("Language Teacher", "Schools", "₹12,000–25,000"), ("Dubbing / Content artist", "Media", "Varies")],
   [("Language Pandit / School Assistant (Language)", "TG DSC", "Degree + Language Pandit Training / B.Ed"), ("Hindi Translator / Officer", "SSC JHT, central offices", "PG Hindi/English")],
   ["M.A. in language (Telugu University, OU, MANUU for Urdu)"])
ba("ba_general", "BA_General_HEP_HPP_Other_Combinations", "B.A. General Combinations (HEP, HPP, EPP and others)",
   ["Three-subject B.A. combinations chosen from History, Economics, Political Science, Public Administration, Sociology, Geography, Psychology and Journalism."],
   ["Three chosen main subjects + English + second language", "Skill & value-added courses"],
   [("Office Administration / Back Office", "Companies", "₹12,000–20,000"), ("Customer Service", "BPOs", "₹15,000–22,000")])

D["law5"] = ("Law_5yr_BA_LLB_BBA_LLB_BCom_LLB", "Law – 5-year Integrated LLB (BA LLB / BBA LLB / BCom LLB)", dict(
    about=["A 5-year law degree right after Inter. After it you can register with the Bar Council and practise as an advocate."],
    duration="5 years (10 semesters)", eligibility=["Inter in any group; 45% (OC), 42% (BC), 40% (SC/ST) – BCI rule."],
    admission=["TG LAWCET (5-year) conducted by OU for TGCHE.", "CLAT for National Law Universities – NALSAR Hyderabad (top 3 in India).", "AILET for NLU Delhi."],
    colleges=["NALSAR University of Law, Hyderabad", "University College of Law (OU), Kakatiya University Law College", "Private law colleges affiliated to OU/KU"],
    subjects=["Constitutional Law, Contract, Torts, Criminal Law (BNS), CrPC (BNSS), Evidence (BSA)", "Family Law, Property Law, Labour Law", "Company Law, Tax Law, Cyber Law, IPR", "Moot court & internships"],
    pass_rules=["University rules (OU: about 40% per subject)", "Then pass the All India Bar Examination (AIBE) to practise"],
    private=[("Junior Advocate", "Courts (High Court of Telangana, District Courts)", "₹10,000–30,000 initially; grows with practice"),
             ("Corporate Lawyer / Legal Associate", "Law firms, companies", "₹30,000–1 lakh (NLU grads higher)"), ("Legal Analyst / Contract Manager", "GCCs, legal process outsourcing", "₹25,000–45,000")],
    govt=[("Civil Judge (Junior Division)", "High Court for the State of Telangana", "LLB + age 23–35"), ("Assistant Public Prosecutor", "TGSLPRB / TGPSC", "LLB + practice"),
          ("Law Officer / Legal Officer", "Banks (IBPS SO), PSUs (via CLAT PG)", "LLB"), ("JAG Entry (Army Judge Advocate)", "Indian Army", "LLB 55%")],
    any_degree=True, self_emp=["Own legal practice, notary, legal consultancy"], higher=["LLM (TG PGLCET / CLAT PG)", "PhD in law"]))

D["law3"] = ("Law_3yr_LLB_after_Degree", "Law – 3-year LLB (after any degree)", dict(
    about=["For graduates who want to become lawyers."], duration="3 years", eligibility=["Any degree with 45% (OC) / 42% (BC) / 40% (SC/ST)."],
    admission=["TG LAWCET (3-year)"], subjects=["Same core law subjects as 5-year LLB"], pass_rules=["University rules + AIBE"],
    private=[("Advocate / Legal Associate", "Courts, firms", "₹10,000–40,000")], govt=[("Civil Judge, APP, Law Officer", "TG High Court, TGPSC", "LLB")]))

D["hotel"] = ("Hotel_Management_Hospitality", "Hotel Management & Catering Technology", dict(
    about=["Trains you for hotels, restaurants, airlines catering, cruise ships and tourism."],
    duration="B.Sc HHA: 3 years; BHM: 4 years; Diploma (DHMCT): 3 years; Craft courses: 6 months–1.5 years",
    eligibility=["Inter in any group (English as a subject)."],
    admission=["NCHM JEE (NTA) for IHM Hyderabad (central institute).", "DOST (BBA Hospitality / DHMCT) and private colleges for state seats."],
    colleges=["IHM Hyderabad (DD Colony)", "State Institute of Hotel Management (Telangana)", "Private hotel management colleges"],
    subjects=["Food Production (Cookery)", "Food & Beverage Service", "Front Office", "Housekeeping", "Hotel Accounts & Management"],
    pass_rules=["Institute/university rules (NCHMCT: 40% theory, 50% practicals approx.)"],
    private=[("Management Trainee / Chef / F&B Associate", "Taj, ITC, Marriott, Hyatt, Novotel (Hyderabad)", "₹15,000–30,000"),
             ("Cruise Ship Staff", "International cruise lines", "$600–1,500/month"), ("Gulf Hotel Jobs", "Dubai/UAE hotels", "AED 2,500–6,000 + food & stay"),
             ("Airline Catering / Cabin Crew", "TajSATS, airlines", "₹18,000–35,000")],
    govt=[("Catering Officer / Assistant", "Railways (IRCTC), Defence messes", "Hotel mgmt degree"), ("Tourism Officer", "TG Tourism Development Corp", "Degree in tourism/hotel mgmt")],
    self_emp=["Restaurant, cloud kitchen, catering business, bakery"], higher=["MBA Hospitality", "M.Sc Hospitality Administration"]))

D["design"] = ("Design_Fashion_NIFT_NID", "Design – Fashion, Product, Communication (NIFT / NID / B.Des)", dict(
    about=["Creative degrees in fashion design, textile, product design, UI/UX and communication design."],
    duration="4 years (B.Des) / 3 years (B.Sc Fashion Design)", eligibility=["Inter in any group."],
    admission=["NIFT entrance (NIFT Hyderabad campus at Madhapur)", "NID DAT (NID campuses)", "UCEED (IIT Hyderabad B.Des, IIT Bombay etc.)", "DOST for B.Sc Fashion Design & Technology, BA Fashion Design (AEP)"],
    subjects=["Design fundamentals, drawing", "Fashion illustration / garment construction", "UI/UX, Typography", "Design research & portfolio"],
    private=[("Fashion Designer (junior)", "Brands, export houses", "₹18,000–35,000"), ("UI/UX Designer", "IT & product companies", "₹30,000–70,000"),
             ("Graphic Designer", "Agencies", "₹15,000–30,000"), ("Merchandiser", "Garment exporters", "₹18,000–30,000")],
    govt=[("Designer posts", "Handloom & Textiles Dept, Khadi & Village Industries, NIFT faculty", "B.Des/PG")], any_degree=True,
    self_emp=["Own boutique / brand", "Freelance design"], higher=["M.Des, M.F.Tech"]))

D["bsw"] = ("BSW_Social_Work", "BSW – Bachelor of Social Work", dict(
    about=["Professional degree to work with communities, NGOs, hospitals and welfare programmes."],
    duration="3 years", eligibility=["Inter in any group (40%)."], admission=DOST,
    subjects=["Social Work Methods", "Community Development", "Social Welfare Policies", "Field work (practical)"], pass_rules=UG_PASS,
    private=[("Field / Community Officer", "NGOs, CSR foundations", "₹15,000–25,000"), ("Medical Social Worker", "Hospitals", "₹15,000–25,000"), ("HR / Labour Welfare Assistant", "Industries", "₹15,000–25,000")],
    govt=[("Welfare Officer / Supervisor", "Women & Child Welfare, Tribal Welfare, SC/BC Welfare depts", "Degree/MSW"), ("Counsellor", "NHM, DMHP, ICDS", "BSW/MSW")],
    any_degree=True, higher=["MSW (OU, TISS Hyderabad)"]))

D["deled"] = ("DElEd_Primary_Teacher_Training", "D.El.Ed – Diploma in Elementary Education (Primary teacher)", dict(
    about=["A 2-year teacher-training diploma. It makes you eligible to become a Secondary Grade Teacher (SGT) for classes 1–5."],
    duration="2 years", eligibility=["Inter with 50% (45% SC/ST/BC/PwD), any group.", "Age 17+."],
    admission=["TG DEECET entrance → counselling (Govt DIETs & private colleges)."],
    subjects=["Child development & pedagogy", "Teaching methods – Telugu, English, Maths, EVS", "School internship"],
    private=[("Primary Teacher", "Private schools", "₹10,000–20,000"), ("Tutor / Play-school teacher", "Self / centres", "Varies")],
    govt=[("Secondary Grade Teacher (SGT)", "TG DSC (after TG TET Paper I)", "Inter + D.El.Ed"), ("Primary Teacher", "KVS / NVS (CTET)", "Inter + D.El.Ed")]))

D["bfa"] = ("BFA_Fine_Arts_Animation", "BFA – Fine Arts (Painting, Sculpture, Photography, Animation)", dict(
    about=["Creative arts degree. JNAFAU (Hyderabad) is the main university."], duration="4 years", eligibility=["Inter in any group."],
    admission=["JNAFAU entrance test (BFA)", "DOST for B.Sc Animation / Graphic Design / Gaming (AEP)"],
    subjects=["Drawing & Painting", "Sculpture", "Applied Arts", "Photography", "Animation & VFX (2D/3D)"],
    private=[("Animator / VFX Artist", "Hyderabad animation & VFX studios (Prasad, Makuta, Annapurna)", "₹15,000–40,000"),
             ("Graphic Designer / Illustrator", "Agencies, ed-tech", "₹15,000–30,000"), ("Photographer / Videographer", "Self / studios", "Varies")],
    govt=[("Art Teacher / Drawing Master", "TG DSC (art teacher posts)", "BFA / certificate"), ("Artist / Designer", "Doordarshan, TG I&PR", "BFA")],
    self_emp=["Freelance art, wedding photography, YouTube animation"]))

D["performing"] = ("Performing_Arts_Music_Dance", "Performing Arts – Music, Dance, Theatre", dict(
    about=["Degrees and certificates in Carnatic/Hindustani music, Kuchipudi, Bharatanatyam, Perini and theatre."],
    duration="3–4 years (degree), 1–2 years (certificate)", eligibility=["Inter any group; aptitude test."],
    admission=["Potti Sreeramulu Telugu University (Hyderabad), Govt music & dance colleges, DOST BA Performing Arts (AEP)"],
    private=[("Performer / Teacher", "Academies, cinema, events", "Varies"), ("Music Producer / Sound Engineer", "Studios", "₹15,000–40,000")],
    govt=[("Music / Dance Teacher", "Govt schools, Residential schools", "Degree in music/dance"), ("Artist", "AIR / Doordarshan (graded)", "Audition")]))
