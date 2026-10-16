from builder import make, career_doc
import deg_science, deg_commerce, deg_arts, deg_life, medical, after_degree

ALL = {}
for m in (deg_science, deg_commerce, deg_arts, deg_life):
    ALL.update(m.D)

I = "01_After_10th_Intermediate"

LAYOUT = {
    "MPC": [
        ("02_Architecture_BArch", ["barch"]),
        ("03_BSc_Science_Degrees", ["bsc_mpcs", "bsc_mscs", "bsc_mpc", "bsc_cs_hons", "bsc_data_science", "bsc_statistics", "bsc_electronics", "bsc_chem_tech", "bsc_bed"]),
        ("04_Pharmacy", "PHARMACY"),
        ("05_Defence_Merchant_Navy_Aviation", ["nda", "merchant_navy", "pilot", "ame", "cabin_crew"]),
        ("06_Research_Integrated_MSc", ["imsc"]),
        ("07_Paramedical_Diplomas_MPC_Allowed", "PARAMED"),
        ("08_Food_Dairy_Technology", ["btech_food_dairy"]),
        ("09_Commerce_Management_Professional", ["bcom_general", "bcom_computers", "bcom_ba", "bba", "bca", "ca", "cma", "cs", "acca", "actuarial", "ipm"]),
        ("10_Arts_Law_Design_Others", ["ba_general", "ba_economics", "law5", "hotel", "design", "ba_journalism", "bfa", "bsw", "deled", "performing"]),
    ],
    "BiPC": [
        ("08_Agriculture_Veterinary_Fisheries", ["bsc_agri", "bsc_horti", "bvsc", "bfsc", "btech_food_dairy"]),
        ("09_BSc_Life_Science_Degrees", ["bsc_bzc", "bsc_biotech", "bsc_micro", "bsc_genetics", "bsc_nutrition", "bsc_forensic", "bsc_biomed", "bsc_mlt_dost", "bsc_chem_tech", "ba_psychology", "bsc_bed", "imsc"]),
        ("10_Commerce_Management_Arts_Law", ["bcom_general", "bcom_computers", "bba", "bca", "ca", "cs", "ba_general", "law5", "hotel", "design", "ba_journalism", "bsw", "deled", "cabin_crew"]),
    ],
    "MEC": [
        ("01_Professional_CA_CMA_CS_ACCA_Actuary", ["ca", "cma", "cs", "acca", "actuarial", "ipm"]),
        ("02_BCom_Degrees", ["bcom_general", "bcom_computers", "bcom_ba", "bcom_hons", "bcom_tax", "bcom_bank"]),
        ("03_BBA_Management", ["bba"]),
        ("04_Computers_Data_Statistics", ["bca", "bsc_mscs", "bsc_data_science", "bsc_statistics"]),
        ("05_BA_Economics_and_Arts", ["ba_economics", "ba_general", "ba_journalism", "ba_psychology"]),
        ("06_Law_Hotel_Design_Others", ["law5", "hotel", "design", "cabin_crew", "bsw", "deled", "bfa"]),
    ],
    "CEC": [
        ("01_Professional_CA_CMA_CS_ACCA", ["ca", "cma", "cs", "acca", "ipm"]),
        ("02_BCom_Degrees", ["bcom_general", "bcom_computers", "bcom_ba", "bcom_hons", "bcom_tax", "bcom_bank"]),
        ("03_BBA_Management", ["bba"]),
        ("04_BCA_Computers", ["bca"]),
        ("05_BA_Degrees", ["ba_economics", "ba_polsci", "ba_pubadmin", "ba_general", "ba_journalism", "ba_psychology"]),
        ("06_Law_Hotel_Design_Others", ["law5", "hotel", "design", "cabin_crew", "bsw", "deled", "bfa"]),
    ],
    "HEC": [
        ("01_BA_Degrees", ["ba_history", "ba_polsci", "ba_pubadmin", "ba_economics", "ba_sociology", "ba_psychology", "ba_english", "ba_languages", "ba_journalism", "ba_general"]),
        ("02_Law_LLB", ["law5"]),
        ("03_Teaching_DElEd_BEd", ["deled", "bsc_bed"]),
        ("04_Social_Work_Fine_Arts_Design_Hotel", ["bsw", "bfa", "performing", "design", "hotel", "cabin_crew"]),
        ("05_Commerce_and_Computers", ["bcom_general", "bcom_computers", "bba", "bca"]),
    ],
    "Vocational_Intermediate": [
        ("01_Degree_Options", ["bcom_general", "bcom_computers", "bba", "bca", "ba_general", "hotel", "deled", "bsw"]),
    ],
}

INTRO = {
    "MPC": "MPC students have the widest choice: engineering, architecture, science, pharmacy, defence, aviation, plus all commerce and arts degrees.",
    "BiPC": "BiPC opens doctor, nursing, pharmacy, allied health, paramedical, agriculture, veterinary and life-science careers, plus commerce/arts degrees.",
    "MEC": "MEC is the best base for CA/CMA/CS, B.Com, BBA, data and statistics careers.",
    "CEC": "CEC suits commerce, accounting, banking and business careers.",
    "HEC": "HEC suits civil services, law, teaching, journalism and social sciences.",
    "Vocational_Intermediate": "Vocational Inter students can join degree courses (some after a bridge course) or go for jobs in their trade.",
}


def place(base, key):
    folder, title, info = ALL[key]
    career_doc(f"{base}/{folder}/{folder}.docx", title, info, subtitle="After Intermediate → Degree")


def eng_private(base):
    career_doc(f"{base}/Private_Jobs_after_BTech.docx", "Private Jobs after Engineering (B.Tech)", dict(
        private=[("Software Engineer", "TCS, Infosys, Wipro, Accenture, Cognizant, Capgemini", "₹25,000–40,000"),
                 ("Software Engineer (product)", "Microsoft, Google, Amazon, Salesforce, ServiceNow (Hyderabad)", "₹80,000–2 lakh+"),
                 ("Data / AI Engineer", "GCCs, analytics firms", "₹40,000–1 lakh"), ("VLSI / Embedded Engineer", "Qualcomm, Micron, AMD, Intel", "₹50,000–1.2 lakh"),
                 ("Graduate Engineer Trainee (Core)", "L&T, Tata Projects, Megha, Cyient, Bosch", "₹25,000–45,000"), ("Site / Project Engineer", "Construction & infra", "₹20,000–35,000"),
                 ("Power / Electrical Engineer", "Siemens, ABB, Schneider, solar EPC", "₹25,000–45,000"), ("Process Engineer", "Pharma & chemical plants", "₹25,000–40,000")],
        extra=[("How to get placed", ["Maintain 60%+ / 6.5+ CGPA (cut-off for most companies)", "DSA + one tech stack + 2 projects + internship", "Hackathons, LeetCode/HackerRank, LinkedIn profile"])]),
        subtitle="After B.Tech")


def master(stream, base, cats, special_first=None):
    rows = []
    if special_first:
        rows += special_first
    for cat, keys in cats:
        if isinstance(keys, str):
            rows.append([cat, {"PHARMACY": "D.Pharm, B.Pharm, Pharm-D", "PARAMED": "13 Telangana Paramedical Board diplomas"}[keys]])
        else:
            rows.append([cat, ", ".join(ALL[k][1].split(" – ")[0].split(" (")[0] for k in keys)])
    make(f"{base}/00_All_Degree_Options_after_{stream}.docx", f"All Degree & Course Options after Inter {stream}", [
        ("Overview", [INTRO[stream]]),
        ("Every option (each has its own folder and Word file)", [("table", ["Folder", "Courses inside"], rows)]),
        ("What each course file contains", ["Duration, eligibility, admission (Telangana entrance/DOST)", "Subjects and pass percentage", "PRIVATE JOBS with salary", "GOVERNMENT JOBS with recruiter", "Higher studies & route map"]),
        ("After degree", ["Common govt exams & private sectors for any degree: folder 07_After_Degree_Govt_and_Private_Jobs"]),
    ], subtitle=f"Inter {stream} → Degree")


def which_degree_matrix():
    groups = ["MPC", "BiPC", "MEC", "CEC", "HEC"]
    lines = [
        ["B.Tech / B.E.", "✔", "—", "—", "—", "—"], ["B.Arch", "✔", "—", "—", "—", "—"], ["MBBS / BDS / AYUSH (NEET)", "—", "✔", "—", "—", "—"],
        ["B.Sc Nursing", "—", "✔", "—", "—", "—"], ["GNM / ANM", "✔", "✔", "✔", "✔", "✔"], ["B.Pharm / Pharm-D", "✔", "✔", "—", "—", "—"],
        ["Allied Health / BPT (KNRUHS)", "some", "✔", "—", "—", "—"], ["Paramedical Diplomas (TGPMB)", "✔", "✔", "—", "—", "—"],
        ["B.Sc Agri / Horti / BVSc / BFSc", "some", "✔", "—", "—", "—"], ["B.Sc Maths/Physics/CS/Stats", "✔", "—", "Maths combos", "—", "—"],
        ["B.Sc Life Sciences", "—", "✔", "—", "—", "—"], ["NDA (Army)", "✔", "✔", "✔", "✔", "✔"], ["NDA (Navy/Air Force), Pilot, Merchant Navy", "✔", "—", "—", "—", "—"],
        ["B.Com / BBA / BCA / CA / CMA / CS", "✔", "✔", "✔", "✔", "✔"], ["B.A. (all subjects)", "✔", "✔", "✔", "✔", "✔"], ["Law (5-yr LLB)", "✔", "✔", "✔", "✔", "✔"],
        ["Hotel Mgmt, Design, BFA, BSW, D.El.Ed, Journalism", "✔", "✔", "✔", "✔", "✔"], ["Actuarial Science", "✔", "—", "✔", "—", "—"],
    ]
    make(f"{I}/00_Which_Degree_after_Which_Group.docx", "Which Degree Can I Join after My Inter Group?", [
        ("Eligibility matrix", [("table", ["Course"] + groups, lines)]),
        ("Notes", ["✔ = eligible, — = not eligible, 'some' = only certain courses/seats.", "DOST rule: B.Sc needs the relevant science subjects in Inter. B.A./B.Com/BBA/BCA/BSW are open to all groups.",
                   "Always confirm in the latest admission notification."]),
    ], subtitle="Intermediate → Degree")


def run():
    which_degree_matrix()
    for stream, cats in LAYOUT.items():
        base = f"{I}/{stream}/After_12th_{stream}" if stream != "Vocational_Intermediate" else f"{I}/{stream}/After_Vocational_Inter"
        for cat, keys in cats:
            if keys == "PHARMACY":
                medical.pharmacy_only(f"{base}/{cat}")
            elif keys == "PARAMED":
                medical.paramedical_only(f"{base}/{cat}")
            else:
                for k in keys:
                    place(f"{base}/{cat}", k)
        if stream == "MPC":
            eng_private(f"{base}/01_Engineering_BTech/Private_Jobs_after_Engineering")
            master(stream, base, cats, [["01_Engineering_BTech", "EAPCET/JEE, 23 branches, govt & private jobs after B.Tech"]])
        elif stream == "BiPC":
            medical.run(base)  # creates its own master list
        else:
            master(stream, base, cats)
    after_degree.run()
    career_doc(f"{after_degree.B}/04_Courses_after_Degree/Law_3yr_LLB.docx", ALL["law3"][1], ALL["law3"][2], subtitle="After Degree")
