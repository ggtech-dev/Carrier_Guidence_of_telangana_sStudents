"""Profession profiles: top-10 countries with demand, licence/recognition and approx salary (Oct 2026 guide values)."""

P = {}

def prof(key, name, sector, rows, exams, steps, portals=None, tips=None):
    assert len(rows) == 10, key
    P[key] = dict(name=name, sector=sector, rows=rows, exams=exams, steps=steps, portals=portals or [], tips=tips or [])

TECH_PORTALS = ["LinkedIn Jobs", "Wellfound (startups worldwide)", "Turing / Arc.dev / Toptal (remote jobs for Indians)", "GitHub & portfolio – employers check it"]
ENG_PORTALS = ["LinkedIn Jobs", "Engineering company career sites (L&T, Aramco, Bechtel, Siemens, ABB, AECOM, Jacobs, WSP)", "EURES (EU jobs)"]
HEALTH_PORTALS = ["LinkedIn Jobs", "Hospital group career sites (NHS, HSE, HMC, SEHA, Aster, Cleveland Clinic)", "Only MEA-registered healthcare recruiters for Gulf"]
TRADE_PORTALS = ["eMigrate (emigrate.gov.in) – verified recruiting agents & jobs", "NSDC International (nsdcindia.org) – govt-backed overseas placements",
                 "TOMCOM – Telangana Overseas Manpower Company (Telangana govt agency)", "Naukrigulf / Bayt (Gulf)"]

# ----------------------------------------------------------------- TECH / ENGINEERING
prof("it_software", "Software / IT / Computer Science professionals", "tech", [
    ("USA", "World's biggest tech job market (Seattle, Bay Area, Texas)", "No licence; H-1B / OPT visa route", "US$ 90,000–150,000/yr"),
    ("CAN", "Express Entry STEM category, Toronto/Vancouver tech", "ECA (WES) for PR", "CA$ 70,000–110,000/yr"),
    ("GBR", "London, Manchester tech; Skilled Worker visa", "No licence", "£40,000–70,000/yr"),
    ("DEU", "Huge IT shortage; Blue Card lower threshold for IT", "anabin degree check", "€50,000–75,000/yr"),
    ("AUS", "ICT on skills lists; ACS skills assessment", "ACS (Australian Computer Society) assessment", "AU$ 85,000–130,000/yr"),
    ("UAE", "Dubai/Abu Dhabi tech, fintech, govt digital", "Degree attestation", "AED 12,000–30,000/month (tax-free)"),
    ("SGP", "Asia tech hub, banks & big tech", "EP + COMPASS", "S$ 5,600–10,000/month"),
    ("NLD", "Amsterdam tech, English workplace", "Recognised sponsor employer", "€45,000–75,000/yr"),
    ("IRL", "European HQs of Google, Meta, Microsoft", "Critical Skills permit", "€45,000–80,000/yr"),
    ("JPN", "IT shortage; English roles increasing", "JLPT helps", "¥5–9 million/yr")],
    ["IELTS/PTE/TOEFL (for visa & study)", "Cloud certifications: AWS, Azure, Google Cloud", "Optional: MS (USA/Canada/Germany) to enter via study route"],
    ["Build strong DSA + one stack + GitHub projects", "Get 2–3 years experience in India (MNC preferred) – or do an MS abroad", "Apply on LinkedIn to companies that sponsor visas; use internal transfer (L-1 / ICT) from Indian MNCs",
     "Prepare for system design + behavioural interviews", "After offer: visa → degree attestation → travel"], TECH_PORTALS,
    ["Internal transfer from TCS/Infosys/Accenture to their US/UK/EU offices is a common first step."])

prof("data_analytics", "Data Analyst / Data Scientist / Statistician", "tech", [
    ("USA", "Highest demand & pay for data science", "No licence", "US$ 85,000–140,000/yr"), ("CAN", "STEM category; banks & retail analytics", "ECA (WES)", "CA$ 70,000–100,000/yr"),
    ("GBR", "Finance, NHS, govt analytics", "No licence", "£35,000–60,000/yr"), ("DEU", "Industry 4.0, automotive analytics", "anabin check", "€50,000–70,000/yr"),
    ("AUS", "Data scientists on skills list", "ACS / VETASSESS assessment", "AU$ 90,000–130,000/yr"), ("IRL", "Tech & pharma analytics", "Critical Skills permit", "€45,000–70,000/yr"),
    ("NLD", "E-commerce & logistics data", "Recognised sponsor", "€45,000–70,000/yr"), ("SGP", "Banks & fintech", "EP", "S$ 5,600–9,000/month"),
    ("UAE", "Govt digital & banking", "Attestation", "AED 12,000–25,000/month"), ("SWE", "Tech & research", "Work permit", "SEK 40,000–60,000/month")],
    ["Python, SQL, Power BI/Tableau certifications", "MS in Data Science (common route)", "IELTS/PTE"],
    ["Build a portfolio (Kaggle, GitHub, dashboards)", "2+ years experience or MS abroad", "Apply via LinkedIn; target companies with visa sponsorship"], TECH_PORTALS)

prof("electronics", "Electronics / VLSI / Embedded / Telecom Engineers", "eng", [
    ("USA", "Semiconductor boom (Intel, Qualcomm, Nvidia, Micron)", "No licence; MS helps", "US$ 100,000–150,000/yr"), ("DEU", "Automotive electronics, Infineon, Bosch", "anabin", "€50,000–72,000/yr"),
    ("SGP", "Chip fabs & design centres", "EP", "S$ 5,600–9,000/month"), ("JPN", "Semiconductor & electronics manufacturing", "JLPT helps", "¥5–8 million/yr"),
    ("CAN", "Telecom & STEM category", "ECA; P.Eng for 'Engineer' title", "CA$ 75,000–105,000/yr"), ("NLD", "ASML, NXP – chip equipment", "Sponsor employer", "€50,000–75,000/yr"),
    ("GBR", "Telecom, defence electronics, chip design", "IET/Engineering Council optional", "£38,000–60,000/yr"), ("AUS", "Telecom & defence", "Engineers Australia", "AU$ 90,000–125,000/yr"),
    ("UAE", "Telecom (e&, du), smart city projects", "Society of Engineers registration", "AED 12,000–25,000/month"), ("KOR", "Samsung, SK Hynix ecosystem", "E-7 visa", "₩50–80 million/yr")],
    ["IELTS/PTE", "MS in VLSI/Embedded (USA/Germany) is a strong route", "Engineers Australia / WES assessments"],
    ["Learn industry tools (Cadence/Synopsys, Verilog, Embedded C, RTOS)", "Work 2–3 yrs in Hyderabad/Bangalore chip companies (Qualcomm, AMD, Micron, Intel)", "Internal transfer or MS abroad"], ENG_PORTALS)

prof("electrical", "Electrical / Power / Renewable Energy Engineers", "eng", [
    ("UAE", "Power, metro, solar mega-projects", "Society of Engineers registration", "AED 10,000–22,000/month"), ("SAU", "Giga projects (NEOM), utilities", "SCE accreditation compulsory", "SAR 10,000–20,000/month"),
    ("QAT", "Power & infrastructure (Kahramaa)", "MME/UPDA engineer registration", "QAR 10,000–20,000/month"), ("AUS", "Renewables & grid upgrades", "Engineers Australia", "AU$ 95,000–135,000/yr"),
    ("CAN", "STEM category; hydro & grid", "ECA; P.Eng licence", "CA$ 80,000–110,000/yr"), ("DEU", "Energy transition (Energiewende)", "anabin + German helps", "€50,000–70,000/yr"),
    ("GBR", "Grid & offshore wind", "Engineering Council optional", "£38,000–60,000/yr"), ("OMN", "Utilities & oil/gas", "Ministry registration", "OMR 900–1,800/month"),
    ("NZL", "Electrical engineers on Green List", "Engineering NZ", "NZ$ 85,000–120,000/yr"), ("USA", "Utilities, EV & data-centre power", "PE licence optional (FE/PE exams)", "US$ 85,000–120,000/yr")],
    ["Gulf: degree attestation + engineer registration", "Australia/NZ: Engineers Australia (Washington Accord or CDR)", "IELTS"],
    ["Get site experience (substations, solar EPC, MEP) in India 2–3 years", "Get degree attested (MEA + embassy) for Gulf", "Apply via Naukrigulf/Bayt/LinkedIn & EPC company sites"], ENG_PORTALS)

prof("mechanical", "Mechanical / Automobile / Robotics / Mechatronics / Industrial Engineers", "eng", [
    ("DEU", "Automotive & machinery leaders (VW, BMW, Bosch, Siemens)", "anabin; German B1+ helps a lot", "€48,000–70,000/yr"), ("UAE", "MEP, HVAC, oil & gas, facilities", "Society of Engineers", "AED 9,000–20,000/month"),
    ("SAU", "Oil & gas (Aramco), giga projects", "SCE accreditation", "SAR 9,000–20,000/month"), ("QAT", "Oil & gas, MEP", "UPDA registration", "QAR 9,000–18,000/month"),
    ("CAN", "Manufacturing & STEM category", "ECA; P.Eng", "CA$ 70,000–100,000/yr"), ("AUS", "Mining equipment, defence, manufacturing", "Engineers Australia", "AU$ 85,000–125,000/yr"),
    ("USA", "Automotive, aerospace, EVs", "PE optional", "US$ 75,000–110,000/yr"), ("JPN", "Manufacturing & automotive (Toyota, Honda suppliers)", "JLPT N3+", "¥4.5–7 million/yr"),
    ("KWT", "Oil & gas, HVAC", "Engineer registration", "KWD 600–1,300/month"), ("NZL", "Manufacturing & infrastructure", "Engineering NZ", "NZ$ 80,000–115,000/yr")],
    ["CAD (SolidWorks, CATIA), HVAC design, Six Sigma certifications", "German language (for Germany)", "IELTS"],
    ["Experience in MEP/HVAC/manufacturing 2–3 years", "Gulf: attestation + registration; Germany: language + Blue Card", "Apply via LinkedIn/Naukrigulf/StepStone"], ENG_PORTALS)

prof("aerospace", "Aerospace / Aeronautical Engineers", "eng", [
    ("USA", "Boeing, SpaceX, Lockheed (many need US citizenship)", "Security clearance for defence jobs", "US$ 85,000–130,000/yr"), ("FRA", "Airbus Toulouse, Safran, Dassault", "French helps", "€42,000–65,000/yr"),
    ("DEU", "Airbus Hamburg, MTU, DLR research", "German helps", "€50,000–70,000/yr"), ("GBR", "Rolls-Royce, BAE, Airbus UK", "Some roles need clearance", "£35,000–60,000/yr"),
    ("CAN", "Bombardier, Pratt & Whitney Canada, CAE", "ECA; P.Eng", "CA$ 75,000–105,000/yr"), ("UAE", "Emirates/Etihad engineering, Strata, Sanad", "Society of Engineers", "AED 12,000–25,000/month"),
    ("SGP", "MRO hub (ST Engineering, SIA Engineering)", "EP", "S$ 5,600–8,500/month"), ("AUS", "Defence aerospace, Qantas engineering", "Engineers Australia", "AU$ 90,000–130,000/yr"),
    ("NLD", "Fokker services, ESA ESTEC", "Sponsor employer", "€45,000–70,000/yr"), ("SAU", "Saudia Technic, defence localisation", "SCE accreditation", "SAR 12,000–22,000/month")],
    ["MS in Aerospace (common route)", "CATIA/ANSYS skills", "EASA Part-66 for maintenance roles"],
    ["Work at HAL/DRDO/Tata Advanced Systems/Airbus India first", "MS abroad or internal transfer", "Note: US/UK defence jobs often require citizenship"], ENG_PORTALS)

prof("civil", "Civil / Structural / Environmental Engineers", "eng", [
    ("UAE", "Construction & real estate boom", "Society of Engineers + Dubai Municipality grading", "AED 9,000–22,000/month"), ("SAU", "NEOM, Red Sea, Riyadh metro giga projects", "SCE accreditation compulsory", "SAR 9,000–22,000/month"),
    ("QAT", "Infrastructure & ongoing projects", "UPDA/MME engineer registration", "QAR 9,000–20,000/month"), ("AUS", "Infrastructure pipeline; civil on skills list", "Engineers Australia (CDR)", "AU$ 90,000–130,000/yr"),
    ("CAN", "Housing & infrastructure; STEM category", "ECA; P.Eng licence", "CA$ 70,000–100,000/yr"), ("NZL", "Civil engineers on Green List", "Engineering NZ / CPEng", "NZ$ 85,000–120,000/yr"),
    ("GBR", "HS2, housing, water projects", "ICE chartership optional", "£35,000–55,000/yr"), ("OMN", "Roads & infrastructure", "Ministry registration", "OMR 800–1,600/month"),
    ("KWT", "Govt infrastructure projects", "Engineer registration (Kuwait Society of Engineers)", "KWD 600–1,300/month"), ("AFR", "Indian EPC firms in Africa (roads, water)", "Local registration", "US$ 2,000–4,000/month")],
    ["AutoCAD, STAAD Pro, ETABS, Primavera certifications", "Gulf: degree attestation + exam/registration", "Australia: Engineers Australia CDR"],
    ["3+ years site/design experience (L&T, Megha, Shapoorji, Afcons)", "Attest degree (MEA apostille/embassy)", "Apply via Naukrigulf/Bayt/LinkedIn and EPC company sites"], ENG_PORTALS)

prof("chemical_process", "Chemical / Petroleum / Metallurgical / Textile / Process Engineers", "eng", [
    ("SAU", "Aramco, SABIC – petrochemicals", "SCE accreditation", "SAR 10,000–25,000/month"), ("UAE", "ADNOC, refineries, chemicals", "Society of Engineers", "AED 12,000–25,000/month"),
    ("QAT", "LNG giants (QatarEnergy)", "UPDA", "QAR 12,000–25,000/month"), ("KWT", "KOC, KNPC refineries", "Registration", "KWD 700–1,500/month"),
    ("OMN", "PDO, OQ refineries", "Registration", "OMR 900–1,800/month"), ("CAN", "Oil sands (Alberta), chemicals", "ECA; P.Eng", "CA$ 80,000–115,000/yr"),
    ("AUS", "LNG, mining processing", "Engineers Australia", "AU$ 95,000–140,000/yr"), ("USA", "Chemicals, pharma process", "PE optional", "US$ 80,000–120,000/yr"),
    ("DEU", "BASF, Bayer, chemical parks", "anabin + German", "€50,000–70,000/yr"), ("SGP", "Jurong Island petrochemicals", "EP", "S$ 5,600–8,500/month")],
    ["Process simulation (Aspen HYSYS), HSE certifications (NEBOSH)", "IELTS"],
    ["Experience at Reliance, IOCL, ONGC, pharma/bulk drug plants", "NEBOSH/IOSH safety certificate helps in Gulf", "Apply via Naukrigulf, Rigzone (oil & gas), LinkedIn"], ENG_PORTALS + ["Rigzone (oil & gas jobs)"])

prof("mining", "Mining Engineers", "eng", [
    ("AUS", "World's biggest mining employer (WA, Queensland)", "Engineers Australia + state mine manager certificates", "AU$ 110,000–170,000/yr"), ("CAN", "Mining in Ontario, BC, Quebec", "P.Eng", "CA$ 85,000–125,000/yr"),
    ("SAU", "Ma'aden & new mining push", "SCE accreditation", "SAR 12,000–24,000/month"), ("AFR", "Copper/gold/coal mines (Zambia, Tanzania, Ghana)", "Local certificates", "US$ 3,000–6,000/month"),
    ("OMN", "Mining & quarrying", "Registration", "OMR 900–1,600/month"), ("USA", "Mining (Nevada, Arizona)", "PE optional", "US$ 85,000–120,000/yr"),
    ("NZL", "Mining & quarrying", "Engineering NZ", "NZ$ 90,000–130,000/yr"), ("UAE", "Quarries & mining companies", "Society of Engineers", "AED 10,000–20,000/month"),
    ("GBR", "Mining company HQs & consulting (London – Anglo American, Rio Tinto)", "Skilled Worker", "£45,000–70,000/yr"), ("POL", "Coal & copper (KGHM)", "Polish language helps", "PLN 8,000–15,000/month")],
    ["DGMS mine manager certificates (First Class) – valued abroad", "IELTS"],
    ["Gain underground/open-cast experience at SCCL/Coal India/NMDC", "Get First Class Mine Manager certificate", "Apply to global miners (BHP, Rio Tinto, Vedanta Africa)"], ENG_PORTALS)

prof("technician_engineering", "Diploma Engineers / Technicians (Civil, Mech, Electrical, Electronics, Auto)", "trade", [
    ("UAE", "Site supervisors, MEP & HVAC technicians", "Attested diploma", "AED 4,000–9,000/month"), ("SAU", "Giga projects need technicians & supervisors", "SCE professional classification (technician)", "SAR 4,000–9,000/month"),
    ("QAT", "Facilities, MEP, oil & gas technicians", "Attestation", "QAR 4,000–8,000/month"), ("KWT", "Oil & gas, power technicians", "Attestation", "KWD 300–700/month"),
    ("OMN", "Utilities & construction", "Attestation", "OMR 350–800/month"), ("DEU", "Skilled-worker visa / Ausbildung for technicians", "Recognition + German B1", "€2,500–3,500/month"),
    ("JPN", "SSW: construction, manufacturing, automobile maintenance", "SSW skills test + JLPT N4", "¥200,000–300,000/month"), ("POL", "Factory & maintenance technicians", "Work permit", "€1,000–1,800/month"),
    ("CAN", "Trades category in Express Entry (electricians, mechanics)", "Provincial trade certification (Red Seal)", "CA$ 25–40/hour"), ("AUS", "Trades on skills list", "TRA (Trades Recognition Australia) assessment", "AU$ 35–50/hour")],
    ["Gulf: attested diploma + experience letters", "Germany: German B1 + recognition", "Japan: JLPT N4 + SSW test"],
    ["Get 2+ years experience in India with good experience letters", "Learn safety (OSHA/NEBOSH-IGC) & AutoCAD/PLC", "Apply via eMigrate-verified agents, Naukrigulf, TOMCOM"], TRADE_PORTALS)

prof("skilled_trades", "ITI Skilled Trades (Electrician, Fitter, Welder, Plumber, Mechanic, AC Tech, etc.)", "trade", [
    ("UAE", "Construction, facilities, AC & electrical maintenance", "Trade test by employer", "AED 1,800–4,500/month + housing"), ("SAU", "Giga projects – very high demand", "Saudi Skill Verification Program (SVP) test", "SAR 1,800–4,500/month + housing"),
    ("QAT", "Facilities & construction", "Trade test", "QAR 1,800–4,000/month + housing"), ("KWT", "Oil, construction, maintenance", "Trade test", "KWD 120–350/month + housing"),
    ("OMN", "Construction & maintenance", "Trade test", "OMR 150–350/month + housing"), ("BHR", "Construction & services", "Trade test", "BHD 150–350/month"),
    ("ISR", "G2G recruitment for construction workers (NSDC)", "Skill test by Israeli team", "₪ 6,000–8,000/month"), ("JPN", "SSW: construction, welding, automobile, building cleaning", "SSW skills test + JLPT N4", "¥180,000–260,000/month"),
    ("DEU", "Ausbildung (paid training) for electricians, mechatronics, plumbers", "German B1/B2", "€1,000–1,300/month training → €2,500+ after"), ("POL", "Welders, fitters, factory workers", "Work permit", "€900–1,600/month")],
    ["Saudi SVP skill verification (for many trades)", "Japanese JLPT N4 (for Japan)", "German B1 (for Germany)"],
    ["Complete ITI + apprenticeship (NAC) – experience letters matter", "Check your passport: ECR or ECNR; ECR needs eMigrate clearance", "Use only MEA-registered agents (emigrate.gov.in) or TOMCOM; take PBBY insurance (₹275–375)", "Never pay more than the legal service charge; get the contract in a language you understand"], TRADE_PORTALS,
    ["Gulf employers must pay visa & ticket costs – do not pay agents for 'visa'.", "Keep copies of passport & contract with family; register with the Indian embassy."])

# ----------------------------------------------------------------- HEALTH
prof("doctor", "Doctors (MBBS – General Doctor)", "health", [
    ("GBR", "NHS needs doctors; Health & Care visa", "PLAB 1 + PLAB 2 (or UKMLA) + IELTS 7.5 / OET B → GMC registration", "£36,000–50,000/yr (trainee/Trust grade)"),
    ("UAE", "Fast-growing private & govt healthcare; Golden Visa for doctors", "DHA/DOH/MOHAP licence: DataFlow + Prometric exam; usually 2 yrs post-internship experience", "AED 20,000–40,000/month (GP)"),
    ("SAU", "Large govt & private hospitals", "SCFHS (Mumaris+) + SMLE exam", "SAR 18,000–35,000/month"),
    ("QAT", "HMC & PHCC hospitals", "DHP licence (Prometric) + experience", "QAR 20,000–35,000/month"),
    ("USA", "Highest pay; residency needed", "USMLE Step 1 (pass/fail) + Step 2 CK + ECFMG Pathway (OET Medicine) → Match residency", "Resident US$ 65,000–75,000/yr; attending US$ 230,000+"),
    ("AUS", "Rural & regional shortage", "AMC CAT MCQ + AMC Clinical/WBA (Standard pathway) + IELTS 7 / OET → AHPRA", "AU$ 85,000–110,000/yr (junior)"),
    ("CAN", "Physician shortage; new Express Entry physician category", "MCCQE1 + NAC + PRA/residency (CaRMS)", "CA$ 250,000+/yr (licensed family doctor)"),
    ("IRL", "HSE hiring non-EU doctors", "Medical Council registration (PRES exam or exemption) + IELTS/OET", "€50,000–75,000/yr"),
    ("DEU", "Big doctor shortage", "German B2 + Medical German C1 (FSP) + Kenntnisprüfung → Approbation", "€55,000–70,000/yr (Assistenzarzt)"),
    ("NZL", "Doctors on Green List", "NZREX Clinical or approved pathway → Medical Council of NZ", "NZ$ 90,000–120,000/yr")],
    ["PLAB 1 & 2 (UK)", "USMLE Step 1, Step 2 CK, Step 3 (USA)", "AMC CAT + Clinical (Australia)", "MCCQE1 + NAC (Canada)", "Gulf Prometric (DHA/DOH/SCFHS/DHP/OMSB)", "German FSP + Kenntnisprüfung", "IELTS Academic / OET Medicine"],
    ["Finish MBBS + internship + permanent registration in India", "Choose ONE target country – each exam takes 1–2 years", "Start primary source verification early (DataFlow for Gulf, EPIC/ECFMG for UK-AMC-USA routes)",
     "Pass English test (OET is accepted by UK, US-ECFMG, Australia, Ireland, NZ)", "Pass licensing exam → register → apply to hospitals", "Gulf jobs: typically need 2+ years experience after internship"], HEALTH_PORTALS,
    ["Do not pay agents for 'guaranteed' UK/US jobs – licensing exams cannot be skipped.", "Many doctors first work in Gulf, then move to UK/Australia."])

prof("doctor_specialist", "Specialist & Super-specialist Doctors (MD/MS/DM/MCh)", "health", [
    ("UAE", "Golden Visa; specialists in very high demand", "DHA/DOH 'Specialist' or 'Consultant' title: PG degree + experience; Prometric/exemption", "AED 40,000–90,000/month"),
    ("SAU", "Specialists & consultants – big hiring", "SCFHS classification (Specialist/Consultant)", "SAR 35,000–80,000/month"),
    ("QAT", "HMC/Sidra specialist posts", "DHP evaluation", "QAR 35,000–70,000/month"),
    ("GBR", "Specialty doctor / consultant posts; CESR (now Portfolio pathway) for specialist register", "GMC registration (PLAB or sponsorship by Royal College – MTI) + Portfolio pathway", "£55,000–110,000+/yr"),
    ("AUS", "Specialist pathway via specialist colleges", "AMC + specialist college assessment (comparability) → AHPRA", "AU$ 250,000–450,000/yr"),
    ("IRL", "Consultant & registrar posts in HSE", "Medical Council specialist registration", "€90,000–220,000/yr"),
    ("NZL", "Vocational scope specialists", "MCNZ vocational registration", "NZ$ 200,000–300,000/yr"),
    ("CAN", "Specialists via provincial practice-ready assessment", "Royal College (RCPSC) route / provincial licence", "CA$ 300,000+/yr"),
    ("OMN", "Ministry of Health specialists", "OMSB", "OMR 2,500–5,000/month"),
    ("KWT", "MOH Kuwait specialists", "MOH licensing", "KWD 1,800–4,000/month")],
    ["MRCP / MRCS / FRCR / MRCOG (UK Royal College exams – very useful in Gulf & UK)", "European board exams (e.g. EDAIC for anaesthesia)", "IELTS/OET"],
    ["Complete MD/MS/DM/MCh in India + some years as Senior Resident/Consultant", "Take UK Royal College membership exams – recognised widely in Gulf & UK", "Apply through hospital career sites / healthcare recruiters"], HEALTH_PORTALS)

prof("dentist", "Dentists (BDS / MDS)", "health", [
    ("UAE", "Large private dental market", "DHA/DOH/MOHAP licence + Prometric; experience needed", "AED 15,000–35,000/month"), ("SAU", "Govt & private clinics", "SCFHS + Prometric", "SAR 12,000–30,000/month"),
    ("QAT", "Private clinics, HMC", "DHP licence", "QAR 15,000–30,000/month"), ("OMN", "MOH & private", "OMSB", "OMR 1,200–2,500/month"),
    ("KWT", "MOH & private", "MOH licence", "KWD 900–2,000/month"), ("GBR", "NHS dental shortage", "ORE Part 1 & 2 (GDC) + IELTS 7", "£50,000–100,000/yr (associate)"),
    ("AUS", "Rural shortage", "ADC exams (written + practical)", "AU$ 120,000–200,000/yr"), ("CAN", "Dentists needed", "NDEB Equivalency process", "CA$ 150,000+/yr"),
    ("USA", "Very high pay but long process", "INBDE + 2–3 yr Advanced Standing DDS/DMD", "US$ 150,000+/yr"), ("NZL", "Dentists needed", "NZDREX", "NZ$ 120,000–180,000/yr")],
    ["Gulf Prometric dental exams", "UK ORE", "Australia ADC", "Canada NDEB", "USA INBDE"], ["Get 2–3 years clinical experience", "Pick one country and its exam", "DataFlow verification for Gulf"], HEALTH_PORTALS)

prof("ayush", "AYUSH Doctors (BAMS / BHMS / BUMS / BNYS / BSMS)", "health", [
    ("UAE", "DHA/DOH license Ayurveda & Homeopathy as TCAM practitioners", "DHA/DOH TCAM licence + exam + experience", "AED 8,000–18,000/month"), ("OMN", "Ayurveda centres & hotels", "MOH licence", "OMR 500–1,000/month"),
    ("BHR", "Ayurveda/Homeopathy clinics", "NHRA licence", "BHD 500–1,000/month"), ("QAT", "Limited TCAM licences", "DHP", "QAR 8,000–15,000/month"),
    ("MUS", "Ayurveda & homeopathy recognised", "Local council registration", "MUR 40,000–80,000/month"), ("MYS", "Traditional & complementary medicine (T&CM)", "T&CM Council registration", "MYR 5,000–9,000/month"),
    ("DEU", "Naturopathy / Ayurveda wellness (Heilpraktiker route)", "Heilpraktiker exam (German)", "€2,500–4,000/month"), ("AFR", "Ayurveda & homeopathy clinics", "Local registration", "US$ 1,000–2,500/month"),
    ("MDV", "Resort spa & wellness doctors", "Work permit", "US$ 1,500–3,000/month"), ("GBR", "Wellness/Ayurveda practitioners (not as medical doctors)", "Voluntary registers", "£25,000–40,000/yr")],
    ["Country-specific TCAM/complementary medicine licensing", "Yoga certifications (QCI/Yoga Certification Board)"],
    ["Get clinical/panchakarma experience in India", "Check that the country recognises your system before paying for anything", "Wellness resorts (Gulf, Maldives) hire Ayurveda doctors & therapists"], HEALTH_PORTALS,
    ["AYUSH degrees are NOT accepted as MBBS-equivalent abroad – roles are wellness/complementary medicine."])

prof("nurse", "Nurses (B.Sc Nursing / GNM / ANM)", "health", [
    ("GBR", "NHS recruits thousands of Indian nurses", "NMC CBT + OSCE + IELTS 7 / OET B", "£31,000–37,500/yr (NHS Band 5)"),
    ("UAE", "Huge private & govt demand", "DHA/DOH/MOHAP Prometric; B.Sc graduates may not need experience (DHA)", "AED 6,000–14,000/month"),
    ("SAU", "Govt hospitals hire through agents", "SCFHS + Prometric", "SAR 5,000–10,000/month"),
    ("IRL", "HSE hiring continuously", "NMBI registration + IELTS/OET + adaptation", "€35,000–45,000/yr"),
    ("AUS", "Registered nurses are a national shortage occupation", "ANMAC skills assessment; AHPRA registration via NCLEX-RN + OSCE (IQNM pathway)", "AU$ 75,000–95,000/yr"),
    ("CAN", "Healthcare category in Express Entry", "NNAS + provincial college exam (NCLEX-RN)", "CA$ 75,000–100,000/yr"),
    ("USA", "Very high pay; green card route", "NCLEX-RN + CGFNS/VisaScreen + IELTS/OET", "US$ 70,000–100,000/yr"),
    ("NZL", "Nurses on Green List", "NCNZ competence programme + OET/IELTS", "NZ$ 75,000–95,000/yr"),
    ("DEU", "Big shortage; Triple Win programme", "German B1/B2 + recognition (Anerkennung)", "€2,800–3,800/month"),
    ("QAT", "HMC, Sidra, private hospitals", "DHP Prometric", "QAR 6,000–12,000/month")],
    ["IELTS Academic 7 / OET B", "NMC CBT + OSCE (UK)", "NCLEX-RN (USA/Canada/Australia)", "Gulf Prometric (DHA/DOH/SCFHS/DHP)", "German B1/B2"],
    ["Get your Telangana Nursing Council registration", "Gain 1–2 years experience (ICU/OT/Emergency is valued most)", "Clear English test (OET or IELTS)", "Clear country exam (CBT/NCLEX/Prometric)", "Apply via NHS Jobs, HSE, hospital sites or MEA-registered recruiters"], HEALTH_PORTALS,
    ["ANM-only nurses have limited options abroad – upgrade to GNM/B.Sc Nursing.", "UK/Ireland employers often pay visa & OSCE costs – avoid agents who charge lakhs."])

prof("pharmacist", "Pharmacists (D.Pharm / B.Pharm / Pharm-D / M.Pharm)", "health", [
    ("UAE", "Retail chains & hospitals", "DHA/DOH/MOHAP Prometric (B.Pharm/Pharm-D)", "AED 8,000–15,000/month"), ("SAU", "Hospital & retail pharmacists", "SCFHS + Prometric (SPLE)", "SAR 7,000–14,000/month"),
    ("QAT", "Hospital & retail", "DHP Prometric", "QAR 8,000–14,000/month"), ("KWT", "MOH & private", "MOH licence", "KWD 500–1,000/month"),
    ("OMN", "MOH & retail", "OMSB / MOH licence", "OMR 600–1,100/month"), ("GBR", "Pharmacist shortage", "OSPAP + foundation training + GPhC exam", "£40,000–50,000/yr"),
    ("CAN", "Pharmacists in healthcare category", "PEBC Evaluating & Qualifying exams", "CA$ 90,000–120,000/yr"), ("AUS", "Pharmacists needed", "APC assessment + intern year + exams", "AU$ 75,000–100,000/yr"),
    ("USA", "Pharm-D paths", "FPGEE + NAPLEX + MPJE (state)", "US$ 120,000+/yr"), ("IRL", "Hospital pharmacists", "PSI recognition", "€45,000–65,000/yr")],
    ["Gulf Prometric pharmacist exams", "UK OSPAP", "Canada PEBC", "US FPGEE/NAPLEX"],
    ["Register with Telangana Pharmacy Council", "1–2 years experience (hospital/retail)", "Clear the target country exam", "Pharma industry roles (QA/QC/regulatory) are also open in Gulf & Africa"], HEALTH_PORTALS)

prof("physio", "Physiotherapists (BPT / MPT)", "health", [
    ("UAE", "Rehab centres, sports clinics", "DHA/DOH Prometric", "AED 7,000–15,000/month"), ("SAU", "Hospitals & rehab", "SCFHS + Prometric", "SAR 6,000–12,000/month"),
    ("QAT", "HMC Qatar Rehabilitation Institute, Aspetar sports", "DHP", "QAR 8,000–15,000/month"), ("GBR", "NHS physio shortage", "HCPC registration + IELTS 7", "£29,000–40,000/yr"),
    ("AUS", "Physios on skills list", "APC (Australian Physiotherapy Council) assessment + exams", "AU$ 75,000–100,000/yr"), ("CAN", "Healthcare category", "CAPR credential + PCE exam", "CA$ 70,000–95,000/yr"),
    ("NZL", "Physios needed", "Physiotherapy Board NZ", "NZ$ 65,000–90,000/yr"), ("IRL", "HSE physios", "CORU registration", "€40,000–55,000/yr"),
    ("USA", "Needs DPT-equivalency", "FCCPT credential + NPTE exam", "US$ 85,000–100,000/yr"), ("KWT", "MOH & private", "Licence", "KWD 500–1,000/month")],
    ["Prometric (Gulf)", "HCPC (UK)", "APC (Australia)", "PCE (Canada)", "NPTE (USA)"], ["Register in India, gain experience (sports/neuro/ortho)", "English test + country exam", "Apply to hospitals & rehab centres"], HEALTH_PORTALS)

prof("lab_tech", "Medical Laboratory Technologists (DMLT / B.Sc MLT)", "health", [
    ("UAE", "Hospitals & diagnostic labs", "DHA/DOH Prometric (B.Sc MLT preferred)", "AED 5,000–10,000/month"), ("SAU", "Govt & private labs", "SCFHS + Prometric", "SAR 4,500–9,000/month"),
    ("QAT", "HMC labs", "DHP", "QAR 5,000–9,000/month"), ("KWT", "MOH labs", "Licence", "KWD 400–800/month"), ("OMN", "MOH labs", "Licence", "OMR 450–900/month"),
    ("GBR", "Biomedical Scientists in NHS", "IBMS assessment + HCPC", "£29,000–36,000/yr"), ("AUS", "Medical scientists", "AIMS assessment", "AU$ 70,000–90,000/yr"),
    ("CAN", "Lab technologists", "CSMLS certification exam", "CA$ 60,000–85,000/yr"), ("USA", "Lab shortage", "ASCP International (MLS(ASCPi)) + state licence", "US$ 55,000–75,000/yr"),
    ("NZL", "Medical laboratory scientists", "MSCNZ registration", "NZ$ 60,000–80,000/yr")],
    ["Gulf Prometric", "ASCPi (USA)", "IBMS/HCPC (UK)", "CSMLS (Canada)"], ["B.Sc MLT gives far more options than DMLT abroad", "Gain 2 years lab experience", "Clear exam → apply"], HEALTH_PORTALS)

prof("radiographer", "Radiographers / Imaging & Radiotherapy Technologists", "health", [
    ("UAE", "Imaging centres & hospitals", "DHA/DOH Prometric", "AED 6,000–12,000/month"), ("SAU", "Hospitals", "SCFHS + Prometric", "SAR 5,000–10,000/month"),
    ("QAT", "HMC & private", "DHP", "QAR 6,000–11,000/month"), ("GBR", "Diagnostic & therapeutic radiographers on shortage list", "HCPC registration", "£29,000–38,000/yr"),
    ("AUS", "Medical imaging technologists", "ASMIRT assessment", "AU$ 75,000–100,000/yr"), ("CAN", "MRT shortage", "CAMRT certification", "CA$ 70,000–95,000/yr"),
    ("NZL", "MRTs needed", "MRTB registration", "NZ$ 70,000–95,000/yr"), ("IRL", "HSE radiographers", "CORU registration", "€38,000–50,000/yr"),
    ("USA", "Imaging techs", "ARRT certification + state licence", "US$ 65,000–85,000/yr"), ("KWT", "MOH", "Licence", "KWD 450–900/month")],
    ["Gulf Prometric", "HCPC (UK)", "ASMIRT (Australia)", "ARRT (USA)"], ["Prefer a B.Sc degree for abroad", "Gain CT/MRI experience", "English test + licensing"], HEALTH_PORTALS)

prof("allied_health", "Allied Health Technologists (Anaesthesia, OT, Cardiac, Dialysis, Respiratory, Neuro, Perfusion, ECG, Audiology)", "health", [
    ("UAE", "Hospitals need OT, dialysis, cath-lab & respiratory therapists", "DHA/DOH Prometric (by profession)", "AED 5,000–12,000/month"), ("SAU", "Large hospital network", "SCFHS + Prometric", "SAR 4,500–10,000/month"),
    ("QAT", "HMC & Sidra", "DHP", "QAR 5,000–10,000/month"), ("KWT", "MOH hospitals", "Licence", "KWD 400–900/month"), ("OMN", "MOH hospitals", "Licence", "OMR 450–900/month"),
    ("BHR", "Hospitals", "NHRA", "BHD 400–800/month"), ("GBR", "Some roles (perfusionist, ODP, audiologist) via HCPC/RCCP", "HCPC / RCCP registration", "£28,000–40,000/yr"),
    ("AUS", "Perfusionists, sonographers, cardiac scientists", "Profession-specific assessment", "AU$ 70,000–110,000/yr"), ("IRL", "HSE clinical measurement & respiratory roles", "CORU / HSE recognition", "€35,000–50,000/yr"),
    ("MDV", "Hospitals & resort clinics", "Work permit", "US$ 1,200–2,500/month")],
    ["Gulf Prometric for your exact profession", "Profession-specific registration abroad"], ["Prefer B.Sc (degree) over diploma", "Gain 2+ years experience in a big hospital", "Check the Gulf licence category for your exact job title before applying"], HEALTH_PORTALS)

prof("optometrist", "Optometrists", "health", [
    ("UAE", "Optical chains & eye hospitals", "DHA/DOH Prometric", "AED 6,000–12,000/month"), ("SAU", "Optical chains", "SCFHS", "SAR 5,000–10,000/month"),
    ("QAT", "Eye clinics", "DHP", "QAR 6,000–11,000/month"), ("GBR", "Optometrists", "GOC registration (Route to Registration)", "£35,000–55,000/yr"),
    ("AUS", "Shortage in regions", "OCANZ competency exam", "AU$ 80,000–110,000/yr"), ("CAN", "Optometrists", "FORAC/IOBP exams", "CA$ 90,000–130,000/yr"),
    ("NZL", "Optometrists", "OCANZ", "NZ$ 80,000–110,000/yr"), ("IRL", "Optometrists", "CORU", "€40,000–60,000/yr"),
    ("OMN", "Eye care", "Licence", "OMR 600–1,000/month"), ("AFR", "Eye care NGOs & chains", "Local registration", "US$ 1,200–2,500/month")],
    ["Prometric (Gulf)", "OCANZ (Australia/NZ)", "GOC (UK)"], ["4-year B.Optom preferred", "Experience in eye hospitals (LV Prasad etc.)", "Exam + registration"], HEALTH_PORTALS)

prof("health_general", "Other Health Careers (EMT, Medical Coding, Clinical Research, Public Health, Dietitian, Psychology, Hospital Admin)", "health", [
    ("UAE", "Hospitals, insurance coding, admin", "DHA licence for clinical roles", "AED 6,000–15,000/month"), ("SAU", "Hospitals & health clusters", "SCFHS (clinical roles)", "SAR 6,000–14,000/month"),
    ("USA", "Medical coding (US-based work done remotely from India too), clinical research", "AAPC CPC / AHIMA CCS; ACRP/SOCRA", "US$ 45,000–80,000/yr"), ("GBR", "Public health, NHS admin, dietitians (HCPC)", "HCPC for dietitians", "£28,000–45,000/yr"),
    ("CAN", "Public health & health admin", "Profession-specific", "CA$ 60,000–90,000/yr"), ("AUS", "Dietitians (DA), public health", "Dietitians Australia assessment", "AU$ 75,000–95,000/yr"),
    ("IRL", "Clinical research & pharma", "—", "€35,000–55,000/yr"), ("SGP", "Clinical trials hub", "EP", "S$ 4,500–7,500/month"),
    ("QAT", "Hospital admin & quality", "—", "QAR 8,000–15,000/month"), ("AFR", "NGO public health programmes (WHO, UNICEF, MSF)", "MPH preferred", "US$ 2,000–5,000/month")],
    ["CPC (AAPC) for coding", "ACRP/SOCRA for clinical research", "MPH for public health"], ["Get certified + 2 years experience", "Many coding/clinical-research jobs are remote from India for US companies"],
    HEALTH_PORTALS + ["UN Careers, ReliefWeb, Devex (public health)"])

prof("vet", "Veterinary Doctors (BVSc & AH)", "health", [
    ("AUS", "Vets on skills list", "AVBC National Veterinary Examination (NVE)", "AU$ 80,000–120,000/yr"), ("NZL", "Vets on Green List", "Veterinary Council of NZ (AVBC NVE exam)", "NZ$ 80,000–120,000/yr"),
    ("GBR", "Vet shortage", "RCVS Statutory Membership Exam", "£35,000–55,000/yr"), ("CAN", "Rural vets", "CVMA National Examining Board (BCSE + NAVLE + clinical exam)", "CA$ 90,000–130,000/yr"),
    ("USA", "Vets", "ECFVG or PAVE + NAVLE", "US$ 100,000+/yr"), ("IRL", "Farm vets", "VCI registration", "€50,000–70,000/yr"),
    ("UAE", "Camel, equine, pet clinics", "MOCCAE licence", "AED 10,000–20,000/month"), ("SAU", "Livestock & poultry farms", "Ministry licence", "SAR 8,000–15,000/month"),
    ("QAT", "Equine & pets", "Licence", "QAR 10,000–18,000/month"), ("OMN", "Livestock & fisheries", "Licence", "OMR 700–1,200/month")],
    ["NVE (Australia/NZ)", "RCVS exam (UK)", "NAVLE (USA/Canada)"], ["Gain clinical experience (large & small animals)", "Pass country exam", "Apply to clinics & farms"], HEALTH_PORTALS)

# ----------------------------------------------------------------- SCIENCE / AGRI
prof("life_science", "Life Science / Biotech / Microbiology / Chemistry graduates", "science", [
    ("USA", "Biotech & pharma (Boston, San Diego) – usually after MS/PhD", "MS/PhD route", "US$ 55,000–90,000/yr"), ("DEU", "Research institutes (Max Planck), pharma", "Masters + German", "€45,000–60,000/yr"),
    ("GBR", "Research & pharma", "—", "£28,000–40,000/yr"), ("IRL", "Pharma manufacturing hub (Cork, Dublin)", "Critical Skills permit", "€35,000–50,000/yr"),
    ("SGP", "Biopolis research", "EP", "S$ 4,500–7,000/month"), ("CAN", "Biotech & research", "ECA", "CA$ 55,000–80,000/yr"),
    ("AUS", "Research & labs", "VETASSESS", "AU$ 70,000–95,000/yr"), ("UAE", "Labs, QC, pharma distribution", "Attestation", "AED 6,000–12,000/month"),
    ("SAU", "Pharma localisation & labs", "Attestation", "SAR 6,000–12,000/month"), ("AFR", "Indian pharma plants & labs in Africa", "Local permit", "US$ 1,500–3,000/month")],
    ["GRE/IELTS for MS", "CSIR-NET/GATE helps for research"], ["Best route: MS/PhD abroad with funding (Germany, USA, Europe)", "Industry route: QC/QA experience in Hyderabad pharma → Gulf/Africa/Ireland"],
    ["EURAXESS (EU research jobs)", "Nature Careers", "Academic Positions", "jobs.ac.uk (UK)"])

prof("science_research", "Science Graduates & Researchers (Physics, Maths, Chemistry, Integrated M.Sc)", "science", [
    ("USA", "Funded PhDs & research jobs", "GRE (some), research record", "PhD stipend US$ 30,000–40,000/yr"), ("DEU", "Max Planck, Helmholtz, DAAD", "—", "PhD €2,000–2,800/month"),
    ("GBR", "University research", "—", "£20,000 PhD stipend; postdoc £35,000+"), ("FRA", "CNRS, Paris research", "—", "€2,100+/month (PhD)"),
    ("NLD", "Research universities", "—", "€2,700+/month (PhD employee)"), ("SWE", "PhD positions are paid jobs", "—", "SEK 30,000+/month"),
    ("CAN", "University research", "—", "CA$ 25,000–35,000/yr (PhD)"), ("SGP", "NUS, NTU, A*STAR", "—", "S$ 2,500–3,500/month (PhD)"),
    ("JPN", "MEXT scholarship & labs", "—", "¥145,000/month (MEXT)"), ("KOR", "KAIST, POSTECH", "—", "₩2–3 million/month")],
    ["GRE (if required), IELTS/TOEFL", "Research papers / projects"], ["Do strong M.Sc projects; publish if possible", "Email professors with a tailored CV", "Apply for funded positions & scholarships (DAAD, MEXT, Fulbright)"],
    ["EURAXESS", "FindAPhD", "Academic Positions", "Nature Careers", "jobs.ac.uk"])

prof("agri_food", "Agriculture / Horticulture / Fisheries / Food & Dairy Technology", "science", [
    ("AUS", "Agriculture & food industry", "VETASSESS / relevant assessment", "AU$ 65,000–90,000/yr"), ("NZL", "Dairy & horticulture", "—", "NZ$ 55,000–80,000/yr"),
    ("CAN", "Agri-food & farms", "ECA", "CA$ 55,000–80,000/yr"), ("NLD", "World leader in agri-tech & greenhouses", "MSc route common", "€40,000–60,000/yr"),
    ("ISR", "Agri-tech & Agrostudies internships", "—", "Stipend-based"), ("UAE", "Food security, agri-tech, food processing", "Attestation", "AED 6,000–14,000/month"),
    ("SAU", "Agri-food & poultry projects", "Attestation", "SAR 6,000–14,000/month"), ("AFR", "Large farms & agri-business (Indian investors)", "Local permit", "US$ 1,500–3,500/month"),
    ("DEU", "Food processing & research", "German + recognition", "€40,000–55,000/yr"), ("USA", "Agri research (MS/PhD)", "MS/PhD route", "US$ 55,000–85,000/yr")],
    ["IELTS/TOEFL", "GRE for MS"], ["Gain farm/food-plant experience; HACCP/ISO 22000 certificates help", "MS in Netherlands/Germany/USA is a strong route"],
    ["AgCareers.com", "FAO / CGIAR careers", "LinkedIn"])

prof("psychology", "Psychologists / Counsellors", "health", [
    ("GBR", "NHS mental health roles", "HCPC (for practitioner psychologists – needs UK doctorate-level training)", "£28,000–45,000/yr"), ("AUS", "Psychologists in demand", "APS/AHPRA (Psychology Board) assessment", "AU$ 80,000–110,000/yr"),
    ("CAN", "Counsellors & psychologists", "Provincial college", "CA$ 60,000–90,000/yr"), ("UAE", "Counselling & school psychologists", "DHA/DOH licence", "AED 10,000–20,000/month"),
    ("NZL", "Psychologists on Green List", "NZ Psychologists Board", "NZ$ 80,000–110,000/yr"), ("IRL", "HSE psychology", "Psychological Society recognition", "€45,000–70,000/yr"),
    ("SGP", "Schools & hospitals", "SRP registration", "S$ 4,500–7,000/month"), ("USA", "Needs US licensure (PhD/PsyD)", "State licence", "US$ 80,000+/yr"),
    ("QAT", "Schools & hospitals", "DHP", "QAR 10,000–18,000/month"), ("SAU", "Hospitals & schools", "SCFHS", "SAR 8,000–15,000/month")],
    ["M.Phil Clinical Psychology (RCI) or abroad Masters", "Country registration"], ["Complete PG (+ M.Phil/RCI)", "Get supervised experience", "Apply for registration abroad"], HEALTH_PORTALS)

# ----------------------------------------------------------------- PROFESSIONAL / BUSINESS
prof("accountant", "Accountants (B.Com, CA, CMA, ACCA, CS)", "finance", [
    ("UAE", "VAT & corporate tax created huge demand", "Degree attestation; CA/ACCA valued", "AED 6,000–25,000/month"), ("SAU", "Finance & audit roles", "SOCPA for licensed auditors", "SAR 6,000–20,000/month"),
    ("QAT", "Finance, audit, banking", "Attestation", "QAR 7,000–20,000/month"), ("GBR", "Audit & finance; ICAEW/ACCA recognised", "ACCA/ICAEW (CA mutual recognition)", "£35,000–60,000/yr"),
    ("CAN", "Accountants in demand; CPA licence for senior roles", "CPA Canada / provincial body (check ICAI recognition)", "CA$ 60,000–95,000/yr"), ("AUS", "Accountants on skills list", "CPA Australia / CA ANZ / IPA assessment", "AU$ 70,000–100,000/yr"),
    ("SGP", "Finance hub", "EP; ISCA membership", "S$ 4,500–8,000/month"), ("IRL", "Funds & audit", "ACCA/Chartered Accountants Ireland", "€45,000–65,000/yr"),
    ("USA", "Big 4 & corporates", "US CPA (Indian CAs can sit for CPA)", "US$ 65,000–95,000/yr"), ("NZL", "Accountants needed", "CA ANZ", "NZ$ 60,000–85,000/yr")],
    ["ACCA (globally accepted)", "US CPA", "CMA (US) – IMA", "CPA Australia / CA ANZ", "Gulf: VAT & corporate tax certifications"],
    ["Get 2–3 years in Big 4 / MNC GCC in Hyderabad", "Add ACCA/CPA for abroad recognition", "Internal transfer (Big 4) or apply via LinkedIn/Bayt"], ["eFinancialCareers", "LinkedIn", "Big 4 career sites (Deloitte, EY, KPMG, PwC)"])

prof("actuary", "Actuaries", "finance", [
    ("GBR", "Insurance & pensions hub", "IFoA exams", "£40,000–90,000/yr"), ("USA", "Insurance", "SOA/CAS exams", "US$ 90,000–150,000/yr"), ("CAN", "Insurance", "SOA/CIA", "CA$ 80,000–130,000/yr"),
    ("AUS", "Insurance & super funds", "Actuaries Institute", "AU$ 90,000–150,000/yr"), ("IRL", "Insurance hub", "IFoA/SAI", "€50,000–100,000/yr"), ("SGP", "Asia insurance hub", "SAS/IFoA", "S$ 6,000–12,000/month"),
    ("HKG", "Insurance", "IFoA/SOA", "HK$ 40,000–80,000/month"), ("UAE", "Insurance", "IFoA", "AED 20,000–40,000/month"), ("BHR", "Insurance & Islamic finance", "IFoA", "BHD 1,500–3,000/month"), ("MUS", "Insurance & offshore finance", "IFoA", "MUR 80,000+/month")],
    ["IFoA (UK) – Indian IAI exams give exemptions", "SOA (USA)"], ["Clear early actuarial papers in India", "Work in insurance/consulting (Hyderabad has big actuarial GCCs)", "Transfer abroad"], ["eFinancialCareers", "LinkedIn", "Insurance company career sites"])

prof("business", "Management / BBA / MBA / Sales / HR / Operations", "finance", [
    ("UAE", "Business hub of the Middle East", "Degree attestation", "AED 6,000–25,000/month"), ("SAU", "Vision 2030 expansion", "Attestation", "SAR 6,000–25,000/month"),
    ("QAT", "Trading, logistics", "Attestation", "QAR 7,000–20,000/month"), ("SGP", "Asia HQs", "EP", "S$ 4,500–9,000/month"), ("GBR", "Graduate & MBA hires", "Skilled Worker", "£35,000–60,000/yr"),
    ("CAN", "Business roles via study/PNP route", "ECA", "CA$ 55,000–90,000/yr"), ("AUS", "Management roles", "VETASSESS", "AU$ 75,000–110,000/yr"), ("USA", "MBA route", "MBA + H-1B/OPT", "US$ 80,000–150,000/yr"),
    ("DEU", "Business roles (German needed)", "Recognition", "€45,000–65,000/yr"), ("OMN", "Trading & logistics", "Attestation", "OMR 600–1,500/month")],
    ["GMAT/GRE for MBA abroad", "Professional certificates (PMP, SHRM, CIPD, CSCP)"], ["Get 2–4 years experience", "Gulf: direct hiring via Bayt/Naukrigulf/LinkedIn", "West: often via MBA/Masters abroad"], ["LinkedIn", "Bayt", "Naukrigulf", "Company career sites"])

prof("law", "Lawyers / Legal professionals (LLB, CS)", "law", [
    ("UAE", "International law firms, in-house legal (English common-law courts in DIFC/ADGM)", "Legal consultant roles (local rights of audience restricted)", "AED 15,000–40,000/month"),
    ("GBR", "Solicitor route", "SQE 1 & 2 + 2 years qualifying work experience", "£40,000–100,000/yr"), ("SGP", "Foreign law firms & arbitration", "Foreign Practitioner Exam (FPE) for some roles", "S$ 6,000–12,000/month"),
    ("USA", "NY/California bar open to some foreign LLBs (LLM often needed)", "LLM + NY Bar", "US$ 80,000–200,000/yr"), ("CAN", "Lawyers via NCA", "NCA exams + provincial bar", "CA$ 70,000–120,000/yr"),
    ("AUS", "Lawyers via assessment", "State admission board assessment + PLT", "AU$ 75,000–120,000/yr"), ("QAT", "QFC & law firms", "Consultant roles", "QAR 15,000–35,000/month"),
    ("SAU", "In-house & firms (growing)", "Consultant roles", "SAR 15,000–35,000/month"), ("HKG", "Arbitration & finance law", "OLQE (Overseas Lawyers Qualification)", "HK$ 50,000+/month"),
    ("IRL", "Solicitor route / in-house legal roles", "Law Society of Ireland – check eligibility for Indian lawyers", "€45,000–80,000/yr")],
    ["UK SQE", "LLM abroad + NY Bar", "Canada NCA", "Legal process outsourcing (LPO) experience"], ["Work in a top Indian law firm or LPO 2–3 years", "LLM abroad (UK/US) is the most common route", "Gulf: legal consultant & in-house counsel roles"],
    ["LinkedIn", "Law firm career sites", "Lawgazettejobs (UK)", "Legal500 / Chambers firm lists"])

prof("teacher", "Teachers (B.Ed / D.El.Ed / Degree + B.Ed)", "edu", [
    ("UAE", "Hundreds of Indian-curriculum (CBSE) & British/American schools", "UAE Teacher Licence (TLS) + attestation", "AED 4,000–15,000/month + housing (varies)"),
    ("QAT", "Indian & international schools", "MOEHE licence", "QAR 5,000–12,000/month"), ("SAU", "International schools", "Attestation + licence", "SAR 5,000–12,000/month"),
    ("OMN", "Indian schools in Oman", "Attestation", "OMR 300–900/month"), ("KWT", "Indian & private schools", "Attestation", "KWD 300–700/month"),
    ("MDV", "Govt schools hire Indian teachers", "Ministry of Education contract", "MVR 15,000–25,000/month"), ("GBR", "Maths/Physics/Chemistry teacher shortage; international teacher route", "QTS (Qualified Teacher Status) via iQTS/route", "£31,000–45,000/yr"),
    ("USA", "J-1 exchange teachers (STEM, special education)", "State certification + J-1 sponsor", "US$ 45,000–65,000/yr"), ("AFR", "International & Indian schools", "Degree + B.Ed", "US$ 800–2,000/month"),
    ("SGP", "International schools", "EP", "S$ 4,500–7,000/month")],
    ["IELTS (for UK/US)", "CTET is valued by CBSE schools in Gulf", "UAE TLS licence", "UK QTS / iQTS"],
    ["Complete B.Ed + 2 years teaching experience (CBSE school preferred)", "Gulf CBSE schools recruit directly – apply on school websites, Teach Away, TES", "For UK/US use official routes (no agent fees)"],
    ["TES Jobs", "Teach Away", "Search Associates", "Schrole", "School group sites (GEMS, Taaleem, Indian High School Dubai)"])

prof("arts_general", "Arts / Social Science / Economics / Humanities graduates", "general", [
    ("UAE", "Admin, HR, customer service, media, education", "Degree attestation", "AED 4,000–12,000/month"), ("QAT", "Admin, hospitality, media", "Attestation", "QAR 4,000–10,000/month"),
    ("SAU", "Admin & service sectors", "Attestation", "SAR 4,000–10,000/month"), ("GBR", "Mostly via Masters + Graduate Route", "—", "£25,000–35,000/yr"),
    ("CAN", "Via Masters/PGWP", "ECA", "CA$ 45,000–65,000/yr"), ("AUS", "Via Masters/485 visa", "—", "AU$ 60,000–80,000/yr"),
    ("IRL", "Via Masters + Stamp 1G", "—", "€30,000–40,000/yr"), ("DEU", "Masters (free tuition) + German", "—", "€35,000–50,000/yr"),
    ("SGP", "Policy, research, NGOs", "EP", "S$ 4,000–6,000/month"), ("AFR", "NGOs & development work (UN, international NGOs)", "Masters preferred", "US$ 1,500–4,000/month")],
    ["IELTS/TOEFL", "GRE (some Masters)"], ["Best route for arts graduates: Masters abroad with scholarship, then work visa", "Gulf: admin/HR/customer service jobs with experience", "UN/NGO jobs via UN Careers & ReliefWeb"],
    ["UN Careers", "ReliefWeb", "Devex", "Idealist", "LinkedIn"])

prof("media", "Journalism / English / Languages / Content & Translation", "general", [
    ("UAE", "Gulf News, Khaleej Times, agencies, content", "Attestation", "AED 6,000–15,000/month"), ("GBR", "Media & publishing (Masters route)", "—", "£25,000–35,000/yr"),
    ("USA", "Media & content (Masters route)", "—", "US$ 45,000–70,000/yr"), ("CAN", "Content & communications", "ECA", "CA$ 45,000–70,000/yr"),
    ("SGP", "Regional media & marketing", "EP", "S$ 4,000–6,500/month"), ("QAT", "Al Jazeera & media", "Attestation", "QAR 8,000–18,000/month"),
    ("AUS", "Media & comms", "—", "AU$ 60,000–85,000/yr"), ("DEU", "Translation / localisation (German + English)", "Language C1", "€38,000–50,000/yr"),
    ("JPN", "Translation (Japanese N1/N2)", "JLPT", "¥3.5–6 million/yr"), ("SAU", "Media & PR growth", "Attestation", "SAR 6,000–15,000/month")],
    ["Portfolio of published work", "Language certificates (JLPT, Goethe, DELF)"], ["Build portfolio + digital skills (SEO, video)", "Freelance internationally (Upwork, Fiverr) to start", "Masters in Journalism/Comms abroad"],
    ["LinkedIn", "Upwork / Fiverr (freelance)", "ProZ (translators)", "Journalism.co.uk jobs"])

prof("hospitality", "Hotel Management / Chefs / Hospitality", "hospitality", [
    ("UAE", "Dubai/Abu Dhabi hotels – largest hiring", "Attestation", "AED 2,500–8,000/month + food & stay"), ("QAT", "Hotels & stadium hospitality", "—", "QAR 2,500–7,000/month + food & stay"),
    ("SAU", "Tourism boom (Red Sea, Riyadh)", "—", "SAR 2,500–8,000/month + food & stay"), ("MDV", "Luxury resorts", "Work permit", "US$ 600–2,000/month + service charge + stay"),
    ("CRU", "Cruise ships (chefs, F&B, housekeeping)", "STCW basic safety + C1/D visa", "US$ 800–2,500/month + tips"), ("OMN", "Hotels & resorts", "—", "OMR 250–700/month + stay"),
    ("BHR", "Hotels", "—", "BHD 250–700/month"), ("CAN", "Cooks via PNP/LMIA", "Trade cert (Red Seal for cooks)", "CA$ 16–25/hour"),
    ("AUS", "Chefs on skills list", "TRA / VETASSESS", "AU$ 65,000–80,000/yr"), ("GBR", "Chefs (if salary meets rules)", "Skilled Worker (senior chef roles)", "£30,000–40,000/yr")],
    ["Food safety (HACCP) certificates", "STCW for cruise ships"], ["Work 1–2 years in a 5-star hotel in India (Taj, ITC, Marriott)", "Apply via hotel group career sites & Hcareers/Hosco", "Cruise: only via cruise line authorised partners"],
    ["Hosco", "Hcareers", "Caterer.com (UK)", "Marriott/Hilton/Accor/IHG career sites"])

prof("design", "Designers / Architects-in-training / Fine Arts / Animation", "general", [
    ("UAE", "Interior, fit-out, branding agencies", "Portfolio + attestation", "AED 6,000–18,000/month"), ("SAU", "Giga projects need designers", "Attestation", "SAR 6,000–18,000/month"),
    ("CAN", "Animation & VFX (Vancouver, Montreal)", "ECA", "CA$ 50,000–80,000/yr"), ("GBR", "Design & VFX (London)", "Skilled Worker", "£28,000–45,000/yr"),
    ("USA", "UX/product design", "OPT/H-1B", "US$ 70,000–120,000/yr"), ("AUS", "Design & VFX", "VETASSESS", "AU$ 65,000–95,000/yr"),
    ("SGP", "UX & branding", "EP", "S$ 4,500–7,000/month"), ("NLD", "Design & UX", "Sponsor", "€40,000–60,000/yr"),
    ("DEU", "Industrial & UX design", "Blue Card", "€42,000–60,000/yr"), ("QAT", "Events & media design", "Attestation", "QAR 7,000–15,000/month")],
    ["Strong online portfolio (Behance, Dribbble, ArtStation)", "Masters in Design abroad (optional)"], ["Build portfolio + freelance international clients", "Apply via LinkedIn & studio websites"],
    ["Behance Jobs", "Dribbble Jobs", "ArtStation Jobs (VFX/animation)", "LinkedIn"])

prof("architect", "Architects (B.Arch)", "eng", [
    ("UAE", "Dubai/Abu Dhabi architecture firms", "Society of Engineers / municipality registration", "AED 10,000–25,000/month"), ("SAU", "Giga projects (NEOM, Red Sea, Diriyah)", "SCE accreditation", "SAR 10,000–25,000/month"),
    ("QAT", "Design firms", "UPDA", "QAR 10,000–20,000/month"), ("AUS", "Architects on skills list", "AACA assessment (NPrA)", "AU$ 80,000–110,000/yr"),
    ("NZL", "Architects on lists", "NZRAB", "NZ$ 75,000–100,000/yr"), ("CAN", "Architects", "BEFA (Broadly Experienced Foreign Architect) / CACB", "CA$ 65,000–95,000/yr"),
    ("GBR", "Architects (ARB registration)", "ARB prescribed exam", "£35,000–55,000/yr"), ("SGP", "Design firms", "EP", "S$ 4,500–7,500/month"),
    ("OMN", "Design & construction", "Registration", "OMR 800–1,600/month"), ("DEU", "Architecture (German needed)", "Chamber registration", "€42,000–60,000/yr")],
    ["Portfolio", "Revit/BIM certification", "Country registration exam (AACA, ARB)"], ["Work 2–3 years with good firms", "Strong BIM portfolio", "Gulf firms hire directly via LinkedIn/Bayt"], ENG_PORTALS)

prof("merchant_navy", "Merchant Navy Officers / Marine Engineers", "maritime", [
    ("SEA", "Indian seafarers work on foreign-flag ships worldwide", "DG Shipping CoC + STCW", "Cadet US$ 500–1,000; officers US$ 3,000–15,000+/month"),
    ("SGP", "Ship management hub (shore jobs after sea time)", "CoC + experience", "S$ 6,000–12,000/month (shore)"), ("UAE", "Offshore & port operations", "CoC", "AED 12,000–30,000/month"),
    ("GBR", "Shipping companies & offshore", "CoC (UK equivalent)", "£40,000–80,000/yr"), ("NLD", "Rotterdam port & dredging", "CoC", "€50,000–80,000/yr"),
    ("SWE", "Nordic shipping companies", "CoC", "Varies"), ("QAT", "LNG carriers (Nakilat)", "CoC", "US$ 4,000–12,000/month"),
    ("SAU", "Bahri shipping", "CoC", "US$ 3,000–10,000/month"), ("HKG", "Ship management", "CoC", "HK$ 40,000+/month (shore)"), ("AUS", "Offshore & coastal shipping", "AMSA recognition", "AU$ 120,000+/yr")],
    ["DG Shipping Certificate of Competency (CoC)", "STCW courses", "INDoS & CDC"], ["Join DG Shipping-approved institute only", "Sponsored cadetship from a shipping company", "Only DG Shipping licensed RPSL agencies – check the licence number"],
    ["Shipping company career sites", "dgshipping.gov.in (licensed RPSL list)"])

prof("pilot", "Pilots", "aviation", [
    ("UAE", "Emirates, Etihad, flydubai, Air Arabia", "ICAO licence + type rating + hours", "AED 30,000–70,000/month"), ("QAT", "Qatar Airways", "Hours + type rating", "QAR 30,000–60,000/month"),
    ("SAU", "Saudia, flynas, Riyadh Air", "GACA validation", "SAR 30,000–60,000/month"), ("SGP", "Singapore Airlines & Scoot", "CAAS conversion", "S$ 10,000–20,000/month"),
    ("OMN", "Oman Air, SalamAir", "Validation", "OMR 2,500–5,000/month"), ("USA", "Major airlines (needs US work rights)", "FAA licence", "US$ 100,000+/yr"),
    ("GBR", "Airlines (UK CAA licence)", "UK CAA conversion", "£50,000–120,000/yr"), ("AUS", "Regional airlines", "CASA conversion", "AU$ 90,000–200,000/yr"),
    ("CAN", "Transport category in Express Entry", "Transport Canada licence", "CA$ 70,000–180,000/yr"), ("HKG", "Cathay Pacific", "CAD HK", "HK$ 60,000+/month")],
    ["DGCA CPL + ATPL", "ICAO English Level 4+", "Type rating (A320/B737)"], ["Build hours in India first (IndiGo/Air India)", "Gulf airlines hire experienced pilots directly"], ["Airline career sites", "Aviation Job Search", "LinkedIn"])

prof("aircraft_maint", "Aircraft Maintenance Engineers / Technicians", "aviation", [
    ("UAE", "Emirates Engineering, Etihad Engineering", "EASA/GCAA Part-66 licence", "AED 12,000–30,000/month"), ("QAT", "Qatar Airways Engineering", "QCAA licence", "QAR 12,000–25,000/month"),
    ("SAU", "Saudia Technic", "GACA licence", "SAR 10,000–22,000/month"), ("SGP", "SIA Engineering, ST Engineering", "CAAS licence", "S$ 4,000–7,500/month"),
    ("GBR", "MRO & airlines", "UK CAA Part-66", "£35,000–55,000/yr"), ("IRL", "Aircraft leasing & MRO", "EASA Part-66", "€40,000–60,000/yr"),
    ("CAN", "Transport category (aircraft mechanics)", "Transport Canada AME", "CA$ 60,000–90,000/yr"), ("AUS", "MRO & airlines", "CASA licence", "AU$ 80,000–110,000/yr"),
    ("MYS", "MRO hub", "CAAM", "MYR 5,000–10,000/month"), ("OMN", "Oman Air", "Licence", "OMR 1,000–2,000/month")],
    ["DGCA B1/B2 licence", "EASA Part-66 modules"], ["Get DGCA licence + type training", "Apply to Gulf MROs"], ["Airline & MRO career sites", "Aviation Job Search", "LinkedIn"])

prof("cabin_crew", "Cabin Crew / Airport Staff", "aviation", [
    ("UAE", "Emirates, Etihad, flydubai, Air Arabia – open days", "Airline training", "AED 9,000–15,000/month incl. allowances + housing"), ("QAT", "Qatar Airways", "Airline training", "QAR 9,000–14,000/month + housing"),
    ("SAU", "Saudia, Riyadh Air, flynas", "Airline training", "SAR 8,000–14,000/month"), ("OMN", "Oman Air", "Airline training", "OMR 600–1,000/month"),
    ("BHR", "Gulf Air", "Airline training", "BHD 500–900/month"), ("SGP", "Singapore Airlines (few nationalities)", "Airline training", "S$ 3,000–5,000/month"),
    ("KWT", "Kuwait Airways, Jazeera", "Airline training", "KWD 400–800/month"), ("CRU", "Cruise guest services", "STCW", "US$ 1,000–2,000/month"),
    ("MDV", "Resort & airport hospitality", "—", "US$ 600–1,200/month"), ("HKG", "Cathay Pacific (limited)", "Airline training", "HK$ 20,000+/month")],
    ["Swimming, height/reach test, English interview"], ["Attend airline open days (check official airline websites)", "Never pay agents – airlines recruit for free"], ["Airline career sites (official only)", "LinkedIn"])

prof("social_work", "Social Workers (BSW / MSW)", "general", [
    ("GBR", "Social workers in high demand", "Social Work England registration", "£32,000–42,000/yr"), ("CAN", "Healthcare & social services Express Entry category", "Provincial college registration", "CA$ 60,000–85,000/yr"),
    ("AUS", "Social workers on skills list", "AASW assessment", "AU$ 75,000–100,000/yr"), ("NZL", "Social workers", "SWRB registration", "NZ$ 65,000–90,000/yr"),
    ("IRL", "HSE social workers", "CORU", "€45,000–60,000/yr"), ("USA", "Clinical social workers (needs US MSW)", "State licence", "US$ 55,000–75,000/yr"),
    ("UAE", "NGO & community roles", "—", "AED 8,000–15,000/month"), ("AFR", "International NGOs", "—", "US$ 1,500–4,000/month"),
    ("SGP", "Social service agencies", "SASW", "S$ 4,000–6,000/month"), ("QAT", "Community services", "—", "QAR 8,000–14,000/month")],
    ["MSW + registration", "IELTS"], ["MSW (TISS/OU) + 2 years field experience", "Register with the country's social work board"], ["UN Careers", "ReliefWeb", "Devex", "Community Care Jobs (UK)"])
