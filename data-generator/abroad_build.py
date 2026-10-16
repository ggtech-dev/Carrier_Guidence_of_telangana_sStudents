import os, re
from builder import make, ROOT
from abroad_countries import C, ORDER_HELP
from abroad_prof import P
import streams

SAFETY = ["Use only MEA-registered recruiting agents (check on emigrate.gov.in) or govt agencies like TOMCOM (Telangana) and NSDC International.",
          "Never pay money for a 'job visa'. Gulf/UK/Ireland employers normally pay visa costs.",
          "Get the job offer/contract in writing, check the company online, and keep copies with family.",
          "24x7 MEA helpline (Pravasi Bharatiya Sahayata Kendra): 1800 11 3090 (toll-free) · +91-11-26885021 · WhatsApp +91 74283 21144 · helpline@mea.gov.in"]

DEG_MAP = {
    "bsc_mpcs": "it_software", "bsc_cs_hons": "it_software", "bca": "it_software", "bsc_mscs": "data_analytics", "bsc_data_science": "data_analytics", "bsc_statistics": "data_analytics",
    "bsc_mpc": "science_research", "imsc": "science_research", "bsc_electronics": "electronics", "bsc_chem_tech": "life_science", "bsc_bed": "teacher", "deled": "teacher",
    "barch": "architect", "merchant_navy": "merchant_navy", "pilot": "pilot", "ame": "aircraft_maint", "cabin_crew": "cabin_crew",
    "bcom_general": "accountant", "bcom_computers": "accountant", "bcom_ba": "data_analytics", "bcom_hons": "accountant", "bcom_tax": "accountant", "bcom_bank": "accountant",
    "ca": "accountant", "cma": "accountant", "acca": "accountant", "cs": "law", "actuarial": "actuary", "bba": "business", "ipm": "business",
    "ba_economics": "arts_general", "ba_history": "arts_general", "ba_polsci": "arts_general", "ba_pubadmin": "arts_general", "ba_sociology": "arts_general", "ba_general": "arts_general",
    "performing": "arts_general", "ba_psychology": "psychology", "ba_journalism": "media", "ba_english": "media", "ba_languages": "media", "law5": "law", "law3": "law",
    "hotel": "hospitality", "design": "design", "bfa": "design", "bsw": "social_work",
    "bsc_bzc": "life_science", "bsc_biotech": "life_science", "bsc_micro": "life_science", "bsc_genetics": "life_science", "bsc_forensic": "life_science", "bsc_biomed": "life_science",
    "bsc_nutrition": "health_general", "bsc_mlt_dost": "lab_tech", "bsc_agri": "agri_food", "bsc_horti": "agri_food", "bfsc": "agri_food", "btech_food_dairy": "agri_food", "bvsc": "vet",
}
FOLDER_MAP = {streams.ALL[k][0]: v for k, v in DEG_MAP.items()}

ENG_RULES = [(r"Data_Science", "data_analytics"), (r"Computer_Science|AI_and_Machine|Information_Technology", "it_software"), (r"Electronics", "electronics"),
             (r"Electrical", "electrical"), (r"Aerospace", "aerospace"), (r"Mechanical|Automobile|Robotics|Mechatronics|Industrial", "mechanical"),
             (r"Civil|Environmental", "civil"), (r"Chemical|Petroleum|Metallurgical|Textile", "chemical_process"), (r"Mining", "mining"), (r"Marine", "merchant_navy"),
             (r"Biotechnology", "life_science"), (r"Agricultural|Food_Technology", "agri_food")]
ALLIED_RULES = [(r"BPT", "physio"), (r"MLT|DMLT", "lab_tech"), (r"Radiology|Nuclear|Radiotherapy|DMIT|DRGA|DDRA", "radiographer"), (r"Optometry", "optometrist")]


def classify(rel):
    parts = rel.split("/")
    base = parts[-1]
    if "Abroad_Jobs" in parts:
        return None
    if "Engineering_Branches" in parts and re.match(r"^\d\d", base):
        for pat, k in ENG_RULES:
            if re.search(pat, base):
                return k
    if parts[0] == "02_After_10th_Polytechnic_Diploma":
        if base.startswith("Agriculture"):
            return "agri_food"
        if re.match(r"^\d\d_", base) and len(parts) == 2:
            return "business" if "Commercial" in base else "technician_engineering"
        if base == "After_Diploma":
            return "technician_engineering"
        return None
    if parts[0] == "03_After_10th_ITI_Trades" and re.match(r"^\d\d_", base):
        return "skilled_trades"
    if base == "02_Nursing":
        return "nurse"
    if base in ("04_Allied_Health_Degrees_KNRUHS", "05_Paramedical_Diplomas_TGPMB"):
        return "allied_health"
    if base == "03_Specialisations":
        return "doctor_specialist"
    if base == "After_Diploma":
        return "technician_engineering"
    if base == "01_MBBS_Doctor":
        return "doctor"
    if base in ("MD_Specialist", "MS_Specialist", "Super_Speciality_DM", "Super_Speciality_MCh"):
        return "doctor_specialist"
    if base == "02_BDS_Dentist":
        return "dentist"
    if re.match(r"^0[3-7]_B(AMS|HMS|UMS|NYS|SMS)", base):
        return "ayush"
    if len(parts) >= 2 and parts[-2] == "02_Nursing":
        return "nurse"
    if base in ("01_D_Pharm", "02_B_Pharm", "03_Pharm_D"):
        return "pharmacist"
    if len(parts) >= 2 and parts[-2] in ("04_Allied_Health_Degrees_KNRUHS", "05_Paramedical_Diplomas_TGPMB"):
        for pat, k in ALLIED_RULES:
            if re.search(pat, base):
                return k
        return "allied_health"
    if base == "07_Paramedical_Diplomas_MPC_Allowed":
        return "allied_health"
    if base == "07_Other_Health_Careers":
        return "health_general"
    if base in FOLDER_MAP:
        return FOLDER_MAP[base]
    if base == "04_Courses_after_Degree":
        return "law"
    return None


def pretty(base):
    b = re.sub(r"^\d\d_", "", base).replace("_", " ")
    return b


def sector_list(code, sector):
    c = C[code]
    key = {"health": "health", "edu": "edu", "eng": "eng"}.get(sector)
    return c.get(key, []) if key else []


def write_abroad(rel, key):
    p = P[key]
    course = pretty(rel.split("/")[-1])
    base = f"{rel}/Abroad_Jobs"
    rows = [[i + 1, C[c]["name"], why, lic, sal] for i, (c, why, lic, sal) in enumerate(p["rows"])]
    visa_rows = [[C[c]["name"], " | ".join(C[c]["visa"][:2]), C[c]["lang"], C[c]["pr"]] for c, *_ in p["rows"]]
    make(f"{base}/1_Top_10_Countries.docx", f"Top 10 Countries for Jobs Abroad – {course}", [
        ("Who this is for", [f"Students/professionals of: {course}", f"Profession group: {p['name']}", ORDER_HELP]),
        ("Top 10 countries", [("table", ["#", "Country", "Why jobs are there", "Licence / exam / recognition", "Approx salary"], rows)]),
        ("Visa, language & PR for these countries", [("table", ["Country", "Main work visa routes", "Language", "Permanent stay?"], visa_rows)]),
        ("Exams & certificates you will need", p["exams"]),
        ("Important notes", p["tips"] + ["Salaries are approximate gross figures (Oct 2026) – living costs differ hugely between countries. Gulf salaries are usually tax-free and often include housing/transport.",
                                         "Visa rules change often – always confirm on the official immigration website of that country."]),
    ], subtitle="Abroad Jobs – Top Countries")

    secs = [("Apps useful in every country for this profession", p["portals"] or ["LinkedIn Jobs"])]
    for code, *_ in p["rows"]:
        c = C[code]
        items = [("h2", "General job apps / websites")] + [("b", x) for x in c["general"]]
        sl = sector_list(code, p["sector"])
        if sl:
            items += [("h2", "Profession-specific portals & licensing")] + [("b", x) for x in sl]
        items += [("h2", "Official / government portal"), ("p", c["official"]), ("h2", "Indian Embassy / Consulate"), ("p", c["embassy"]), ("h2", "Watch out"), ("p", c["note"])]
        secs.append((c["name"], items))
    secs.append(("How to use job apps the right way", [
        "Make a 1–2 page CV in the country's format (no photo/age for UK/US/Canada/Australia; Gulf CVs often include photo & nationality).",
        "Complete your LinkedIn profile (headline, skills, photo) and set 'Open to work' for the target country.",
        "Create job alerts on 2–3 apps; apply within 48 hours of a job being posted.",
        "Check that the job is real: company website, official email domain, no payment requests.",
    ] + SAFETY))
    make(f"{base}/2_Job_Search_Apps_by_Country.docx", f"Job Search Apps & Websites – {course}", secs, subtitle="Abroad Jobs – Where to Search")

    timeline = [("table", ["When", "What to do"], [
        ["During your course", "Good marks, internships, English speaking practice, start building CV/portfolio"],
        ["Final year", "Decide target country; check licensing/assessment rules for your profession"],
        ["0–2 years after course", "Gain experience in India (most countries want 1–3 years); get registration in India where applicable"],
        ["Parallel", "English/language test, primary source verification, degree attestation/apostille"],
        ["After exams", "Apply on job apps, interviews, offer letter"],
        ["Before travel", "Visa, medical test, PCC, eMigrate clearance (if ECR), PBBY insurance, register with Indian embassy"]])]
    make(f"{base}/3_Steps_to_Go_Abroad.docx", f"Step-by-Step Plan to Work Abroad – {course}", [
        ("Steps special to this profession", p["steps"]),
        ("Timeline", timeline),
        ("Documents checklist", ["Passport (valid 2+ years; ECNR status if possible – 10th pass gets ECNR)", "10th, Inter, degree certificates + all marks memos/transcripts",
                                 "Attestation: MEA Apostille (most countries) or MEA + Embassy attestation (UAE, Qatar, Kuwait) – see folder 08 'Documents' file",
                                 "Experience letters with salary slips", "Professional registration certificate (council) if applicable", "Police Clearance Certificate (PCC) – from Passport Seva",
                                 "Language test score card", "Medical fitness (as per country)"]),
        ("Credential checks by country", ["Gulf healthcare: DataFlow primary source verification", "Canada: ECA by WES/ICAS/IQAS", "USA: WES/ECE evaluation (or ECFMG for doctors)",
                                          "UK: UK ENIC Statement of Comparability", "Germany: anabin / ZAB", "Australia: your profession's assessing authority", "New Zealand: NZQA / profession board"]),
        ("Safety & help", SAFETY + ["Ministry of External Affairs grievance portal MADAD (madad.gov.in) for problems abroad."]),
        ("More help in this project", ["Folder 08_Work_and_Study_Abroad_Guide – country guides, language tests, attestation, safe emigration, study-abroad route",
                                       "Folder 09_Scholarships_and_Student_Support – Telangana overseas scholarships (up to ₹20 lakh) and education loans"]),
    ], subtitle="Abroad Jobs – Step by Step")
    return 3


def add_all():
    count = 0
    folders = []
    for dirpath, dirnames, files in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT).replace(os.sep, "/")
        if rel == ".":
            continue
        k = classify(rel)
        if k:
            folders.append((rel, k))
    for rel, k in folders:
        count += write_abroad(rel, k)
    return folders, count


ENG_INDEX = [("CSE / AI&ML / IT", "it_software"), ("Data Science", "data_analytics"), ("ECE / Electronics", "electronics"), ("EEE / Electrical", "electrical"),
             ("Mechanical / Automobile / Robotics / Mechatronics / Industrial", "mechanical"), ("Aerospace", "aerospace"), ("Civil / Environmental", "civil"),
             ("Chemical / Petroleum / Metallurgy / Textile", "chemical_process"), ("Mining", "mining"), ("Marine", "merchant_navy"), ("Biotechnology", "life_science"),
             ("Agricultural / Food Technology", "agri_food"), ("Architecture (B.Arch)", "architect")]


def extras():
    eng = "01_After_10th_Intermediate/MPC/After_12th_MPC/01_Engineering_BTech"
    rows = [[b, ", ".join(C[r[0]]["name"].split(" (")[0] for r in P[k]["rows"][:5])] for b, k in ENG_INDEX]
    make(f"{eng}/Abroad_Jobs_All_Engineering_Branches.docx", "Abroad Jobs for Engineers – All Branches (Index)", [
        ("Top 5 countries by branch", [("table", ["Branch", "Top 5 countries"], rows)]),
        ("Where to find full details", ["Open Engineering_Branches → your branch → Abroad_Jobs (3 files: Top 10 countries, Job apps by country, Step-by-step plan)."]),
        ("Engineer recognition abroad – key facts", ["Washington Accord: only NBA-accredited programmes of Tier-I institutions get automatic recognition (check your exact branch & years on nbaind.org).",
                                                     "Australia: Engineers Australia – Washington Accord route or CDR (Competency Demonstration Report).", "Canada: ECA (WES) for PR; P.Eng licence from the province to use the title 'Engineer'.",
                                                     "Saudi Arabia: Saudi Council of Engineers (SCE) professional accreditation is compulsory.", "UAE/Qatar/Oman/Kuwait: degree attestation + engineer registration with the local society/ministry.",
                                                     "Germany: anabin H+ status / ZAB; EU Blue Card salary rules."]),
    ], subtitle="Abroad Jobs – Engineering")
    bipc = "01_After_10th_Intermediate/BiPC/After_12th_BiPC"
    HK = [("MBBS doctor", "doctor"), ("Specialist doctor", "doctor_specialist"), ("Dentist", "dentist"), ("AYUSH doctor", "ayush"), ("Nurse", "nurse"), ("Pharmacist", "pharmacist"),
          ("Physiotherapist", "physio"), ("Lab technologist", "lab_tech"), ("Radiographer", "radiographer"), ("Allied health technologist", "allied_health"), ("Optometrist", "optometrist"),
          ("Veterinary doctor", "vet"), ("Life sciences", "life_science"), ("Agriculture / Food", "agri_food")]
    make(f"{bipc}/00_Abroad_Jobs_All_Health_Careers.docx", "Abroad Jobs for BiPC / Health Careers – Index", [
        ("Top 5 countries by career", [("table", ["Career", "Top 5 countries"], [[n, ", ".join(C[r[0]]["name"].split(" (")[0] for r in P[k]["rows"][:5])] for n, k in HK])]),
        ("Where to find full details", ["Every course folder has an Abroad_Jobs sub-folder with 3 files: Top 10 countries, Job apps by country, Step-by-step plan."]),
        ("Health licensing at a glance", ["Gulf: DataFlow verification + Prometric exam (DHA/DOH/MOHAP in UAE, SCFHS Saudi, DHP Qatar, OMSB Oman, NHRA Bahrain)",
                                          "UK: GMC (PLAB) for doctors, NMC (CBT+OSCE) for nurses, HCPC for allied, GPhC for pharmacists", "USA: USMLE (doctors), NCLEX-RN (nurses), NAPLEX (pharmacists)",
                                          "Australia: AMC (doctors), ANMAC/NCLEX (nurses), AHPRA registration", "Germany: Approbation (doctors, German C1), Anerkennung (nurses, German B1/B2)"]),
    ], subtitle="Abroad Jobs – Health")
    nda = "01_After_10th_Intermediate/MPC/After_12th_MPC/05_Defence_Merchant_Navy_Aviation/NDA_Defence_Officer"
    make(f"{nda}/Abroad_Note_for_Defence.docx", "Defence Officers & Abroad Opportunities", [
        ("While serving", ["Serving defence officers cannot take private jobs abroad.", "You may serve abroad on UN Peacekeeping missions, defence attaché posts and training courses with the Indian forces."]),
        ("After service (retirement / release)", ["Gulf & international security management (corporate security heads, aviation security)", "Ex-Air Force pilots → airlines (Gulf carriers hire experienced pilots)",
                                                  "Ex-Navy officers → merchant navy / offshore / port management (after certificate conversion)", "Ex-engineers & doctors from the forces → civilian jobs abroad after licensing"]),
    ], subtitle="Abroad Note")
