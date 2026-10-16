from deg_common import UG_PASS, DOST, DOST_COLLEGES

COM_HIGHER = ["M.Com via TG CPGET", "MBA via TG ICET / CAT / MAT", "CA / CMA / CS (direct entry after degree)", "B.Ed via TG EdCET (Commerce teaching)", "CFA / FRM (finance certifications)"]

COM_GOVT = [
    ("Bank PO / Clerk", "IBPS, SBI", "Any degree"),
    ("Assistant Section Officer / Auditor / Accountant / Tax Assistant", "SSC CGL", "Any degree"),
    ("Junior Accounts Officer / Senior Accountant", "TGPSC / Telangana Accounts Dept", "B.Com preferred"),
    ("Assistant Audit Officer (State Audit)", "TGPSC Group II/III", "Any degree"),
    ("GST / Commercial Tax Officer (ACTO)", "TGPSC Group II", "Any degree"),
    ("Accounts Officer (after CA/CMA)", "PSUs (NTPC, ONGC, SCCL, BHEL)", "CA / CMA"),
]

D = {}

def bcom(key, folder, title, about, subjects, extra_private):
    D[key] = (folder, title, dict(
        about=about, duration="3 years (6 semesters)",
        eligibility=["Inter in any group (MEC/CEC preferred). MPC/BiPC/HEC students can also join B.Com."],
        admission=DOST, colleges=DOST_COLLEGES, subjects=subjects, pass_rules=UG_PASS,
        skills=["Tally Prime with GST", "Advanced Excel", "Income Tax return filing", "Communication & interview skills"],
        private=[("Accounts Executive / Junior Accountant", "Companies, CA firms", "₹15,000–25,000"),
                 ("Audit Assistant / Article (with CA)", "CA firms", "₹8,000–20,000 stipend"),
                 ("Banking Operations / Customer Service", "HDFC, ICICI, Axis banks", "₹18,000–28,000"),
                 ("Process Associate – Finance & Accounting (F&A)", "Genpact, Deloitte, EY, Accenture GCCs in Hyderabad", "₹18,000–30,000")] + extra_private,
        govt=COM_GOVT, any_degree=True, higher=COM_HIGHER,
        route=["Inter → DOST → B.Com", "Learn Tally/GST/Excel in 1st year", "Start CA/CMA/CS or bank exam prep in 2nd year",
               "Final year: placements (F&A, banking) OR MBA/M.Com OR govt exams"]))

bcom("bcom_general", "BCom_General", "B.Com (General)",
     ["A commerce degree covering accounting, business law, taxation and economics."],
     ["Financial Accounting, Corporate Accounting, Cost Accounting", "Business Law, Company Law", "Income Tax, GST", "Business Economics, Statistics", "Auditing, Management Accounting"], [])
bcom("bcom_computers", "BCom_Computers_Computer_Applications", "B.Com (Computers / Computer Applications)",
     ["B.Com plus computer subjects. It is the most popular B.Com in Telangana."],
     ["All B.Com accounting & tax subjects", "Programming basics, DBMS/SQL, Web Technologies, Tally/ERP", "E-Commerce"],
     [("MIS / Data Entry / ERP Executive", "Corporates", "₹15,000–25,000")])
bcom("bcom_ba", "BCom_Business_Analytics", "B.Com (Business Analytics)",
     ["B.Com with data analytics – Excel, SQL, Power BI, Python basics."],
     ["Accounting & finance subjects", "Business Statistics", "Data Analytics, Data Visualization", "SQL, Python/R basics"],
     [("Junior Business / Data Analyst", "Analytics, GCCs", "₹22,000–35,000")])
bcom("bcom_hons", "BCom_Honours", "B.Com (Honours)",
     ["A more in-depth B.Com with extra papers and project work. It suits CA/CMA aspirants."],
     ["Advanced Accounting, Financial Management", "Corporate Tax, Auditing", "Research project"], [])
bcom("bcom_tax", "BCom_Taxation", "B.Com (Taxation / Tax Procedure)",
     ["B.Com specialising in Income Tax and GST practice."],
     ["Direct Taxes, GST Law & Practice", "Tax Planning", "Customs", "Practical tax filing"],
     [("Tax Assistant / GST Practitioner", "CA firms, own practice", "₹15,000–25,000")])
bcom("bcom_bank", "BCom_Banking_and_Insurance", "B.Com (Banking & Insurance)",
     ["B.Com with focus on banking operations and insurance."],
     ["Banking Law & Practice", "Insurance Principles", "Financial Services, Mutual Funds", "Risk Management"],
     [("Relationship / Sales Officer", "Banks, insurance (LIC agents, private insurers)", "₹18,000–30,000 + incentives")])

D["bba"] = ("BBA_All_Specialisations", "BBA – Bachelor of Business Administration (all specialisations)", dict(
    about=["A management degree that teaches how businesses run – marketing, HR, finance, operations."],
    duration="3 years (some 4-year honours)", eligibility=["Inter in any group."], admission=DOST + ["IPMAT for 5-year integrated MBA at IIMs."],
    extra=[("Specialisations available in Telangana (DOST list)", [("table", ["Specialisation", "Good for"], [
        ["BBA General", "Management, sales, HR"], ["BBA Business Analytics / Data Analytics / AI", "Analytics jobs"],
        ["BBA Tourism & Travel / Hospitality", "Hotels, airlines, travel"], ["BBA Logistics / E-Commerce Operations", "Amazon, Flipkart, logistics"],
        ["BBA Retail Operations", "Retail chains"], ["BBA Health Care Management", "Hospitals"], ["BBA Media Business Management", "Media houses"],
        ["BBA Computer Applications", "IT + management"]])])],
    subjects=["Principles of Management", "Marketing, HR, Finance", "Business Communication", "Organisational Behaviour", "Business Law", "Entrepreneurship"], pass_rules=UG_PASS,
    private=[("Sales / Business Development Executive", "All industries", "₹18,000–30,000 + incentives"), ("HR Executive / Recruiter", "Companies, consultancies", "₹15,000–25,000"),
             ("Operations Executive", "Logistics, e-commerce", "₹18,000–28,000"), ("Marketing / Digital Marketing Executive", "Agencies, startups", "₹15,000–30,000"),
             ("Hospital Front Office / Admin (Healthcare BBA)", "Hospitals", "₹15,000–25,000")],
    govt=COM_GOVT[:2], any_degree=True, higher=["MBA (ICET/CAT/XAT/GMAT)", "PGDM"], self_emp=["Start a small business (with T-Hub / WE-Hub support, MUDRA loans)"]))

D["bca"] = ("BCA_Computer_Applications", "BCA – Bachelor of Computer Applications", dict(
    about=["A computer-applications degree – programming, databases, web development. It is open to all groups in Telangana."],
    duration="3 years", eligibility=["Inter in any group (some colleges prefer Maths)."], admission=DOST,
    subjects=["C, C++, Java, Python", "Data Structures, DBMS/SQL", "Web Technologies, PHP/JavaScript", "Operating Systems, Networks", "Software Engineering, Cloud basics"], pass_rules=UG_PASS,
    skills=["Build 3–4 projects on GitHub", "One stack: Java Spring / MERN / Python Django"],
    private=[("Junior Software Developer", "IT companies", "₹18,000–35,000"), ("Web Developer", "Agencies, startups", "₹15,000–30,000"),
             ("Technical Support / System Admin", "IT services", "₹15,000–25,000"), ("Software Tester", "IT companies", "₹18,000–30,000")],
    govt=[("Computer Operator / Programmer", "TG departments, courts", "BCA / degree + computer"), ("IT Assistant", "Banks (IBPS SO after PG)", "Degree")],
    any_degree=True, higher=["MCA (TG ICET / NIMCET) – needed for many top IT roles", "M.Sc CS", "MBA IT"]))

D["ca"] = ("CA_Chartered_Accountant", "CA – Chartered Accountant (ICAI)", dict(
    about=["India's top accounting qualification. CAs do audit, taxation, finance and advisory work."],
    duration="About 4.5–5 years after 12th (including 2 years of articleship)",
    eligibility=["Foundation: after 12th (register after 10th, write after 12th) – any stream, commerce easiest.", "Direct entry after graduation (55% commerce / 60% others) – skips Foundation."],
    extra=[("Stages", [("table", ["Level", "Papers", "Pass rule"], [
        ["CA Foundation", "4 papers (Accounting, Law, Maths & Stats, Economics)", "40% each + 50% aggregate"],
        ["CA Intermediate", "6 papers in 2 groups", "40% each + 50% aggregate per group"],
        ["Articleship", "2 years practical training under a CA (stipend)", "—"],
        ["CA Final", "6 papers in 2 groups", "40% each + 50% aggregate per group"],
        ["ICITSS, AICITSS courses", "IT & soft skills (mandatory)", "—"]])])],
    admission=["Register on icai.org; Hyderabad ICAI branch (SIRC) runs classes."],
    private=[("Chartered Accountant (fresher)", "Big 4 (Deloitte, EY, KPMG, PwC), corporates", "₹70,000–1.5 lakh"),
             ("Financial Analyst / Controller", "MNCs, GCCs", "₹80,000+"), ("Tax Consultant / Auditor", "CA firms", "₹60,000+")],
    govt=[("Accounts / Finance Officer", "PSUs (ONGC, NTPC, SCCL, BHEL), RBI, SEBI", "CA"), ("Assistant Audit Officer / Officer posts", "CAG, banks (SO)", "CA")],
    self_emp=["Own CA practice – audit, GST, income tax, company formation"], higher=["CFA, CPA (US), ACCA", "Specialisation courses of ICAI"]))

D["cma"] = ("CMA_Cost_and_Management_Accountant", "CMA – Cost & Management Accountant (ICMAI)", dict(
    about=["A professional course in cost accounting, management accounting and financial management."],
    duration="About 3.5–4 years after 12th", eligibility=["Foundation after 12th; direct Intermediate after graduation."],
    extra=[("Stages", ["CMA Foundation → Intermediate (2 groups) → Final (2 groups) + 15 months practical training", "Pass: 40% each paper + 50% aggregate"])],
    private=[("Cost Accountant", "Manufacturing, pharma", "₹40,000–80,000"), ("Financial Analyst", "Corporates", "₹40,000–70,000")],
    govt=[("Cost Accountant / Finance Officer", "PSUs (NTPC, ONGC, BHEL, SCCL), Indian Cost Accounts Service (UPSC)", "CMA")],
    self_emp=["Cost audit practice"]))

D["cs"] = ("CS_Company_Secretary", "CS – Company Secretary (ICSI)", dict(
    about=["Company Secretaries handle company law compliance, board meetings and corporate governance."],
    duration="About 3–4 years", eligibility=["CSEET (CS Executive Entrance Test) after 12th or graduation."],
    extra=[("Stages", ["CSEET → CS Executive (2 groups) → CS Professional → training", "Pass: 40% each paper + 50% aggregate"])],
    private=[("Company Secretary", "Listed companies", "₹40,000–1 lakh"), ("Compliance Officer / Legal Associate", "Corporates, law firms", "₹30,000–60,000")],
    govt=[("Company Secretary / Compliance Officer", "PSUs, SEBI, RBI, NCLT", "CS")], self_emp=["Practising Company Secretary – firm registrations, compliance"]))

D["acca"] = ("ACCA_International_Accounting", "ACCA – Association of Chartered Certified Accountants (UK)", dict(
    about=["A global accounting qualification valued in the Gulf (Dubai/UAE), the UK, Singapore and MNC GCCs in Hyderabad."],
    duration="2–3 years (13 papers; exemptions for B.Com/CA students)", eligibility=["12th with 65% in English & Maths/Accounts, OR B.Com students (get exemptions)."],
    extra=[("Pass rule", ["50% in each paper", "Plus the ethics module and 3 years of practical experience for membership"])],
    private=[("Accountant / Financial Reporting Analyst", "Deloitte, EY, KPMG, PwC GCCs in Hyderabad", "₹30,000–60,000"), ("Accountant (Gulf)", "Dubai/UAE companies", "AED 6,000–15,000")],
    govt=[("Not directly a govt qualification in India", "—", "Useful mainly for private/MNC careers")]))

D["actuarial"] = ("Actuarial_Science", "Actuarial Science (IAI)", dict(
    about=["Actuaries use maths & statistics to calculate risk for insurance and pensions. It is a very well-paid profession."],
    duration="5–7 years of exams (can start after 12th)", eligibility=["ACET (Actuarial Common Entrance Test) after 12th – Maths strongly needed."],
    private=[("Actuarial Analyst", "LIC, ICICI Pru, HDFC Life, Swiss Re, Deloitte", "₹40,000–80,000 (rises fast with papers)")],
    govt=[("Actuary", "LIC, IRDAI, GIC Re", "Fellow actuary")], higher=["Fellowship of IAI / IFoA (UK)"]))

D["ipm"] = ("IPM_Integrated_MBA_IIM", "IPM – 5-year Integrated BBA+MBA at IIMs", dict(
    about=["A 5-year integrated management programme at IIM Indore, Rohtak, Ranchi, Bodh Gaya, Jammu."],
    duration="5 years", eligibility=["12th with 60%; age limit about 20 years."],
    admission=["IPMAT (IIM Indore/Rohtak), JIPMAT (Bodh Gaya/Jammu) + interview."],
    private=[("Management Trainee / Consultant / Analyst", "Top MNCs", "₹1–2 lakh+ (after 5 years)")],
    govt=[("All any-degree govt jobs (IAS, Group I, banks, SSC)", "UPSC / TGPSC / IBPS / SSC", "Eligible after the BBA part (year 3) is completed")]))

D["ba_economics"] = ("BA_Economics", "B.A. Economics / B.A. (Hons) Economics (4 years)", dict(
    about=["Studies how the economy works – markets, money, government budget, development."],
    duration="3 years (Honours: 4 years)", eligibility=["Inter any group (Maths helpful)."], admission=DOST,
    subjects=["Micro & Macro Economics", "Indian Economy & Telangana Economy", "Statistics & Econometrics", "Public Finance, Money & Banking", "Development Economics"], pass_rules=UG_PASS,
    private=[("Research / Policy Analyst", "Think tanks, NGOs, consulting", "₹20,000–35,000"), ("Banking / Financial Services", "Banks, NBFCs", "₹18,000–30,000"),
             ("Data / Market Research Analyst", "Research firms", "₹20,000–30,000")],
    govt=[("Indian Economic Service (after PG)", "UPSC IES", "PG Economics"), ("Economist / Research Officer", "RBI Grade B (DEPR), NITI Aayog", "PG Economics"),
          ("Assistant Statistical Officer", "TG Planning Dept", "Degree")], any_degree=True,
    higher=["M.A. Economics (CPGET, CUET-PG, UoH, JNU, Delhi School of Economics)", "MBA", "Civil services (Economics optional)"]))
