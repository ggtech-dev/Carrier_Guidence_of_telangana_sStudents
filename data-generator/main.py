import os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
import builder
from builder import make, ROOT
import intermediate, diploma, iti_jobs, streams, abroad_build, abroad_guide

if os.path.exists(ROOT):
    shutil.rmtree(ROOT)

make("00_READ_ME_FIRST_Project_Overview.docx", "Career Guidance Project – Telangana (India)", [
    ("Purpose", ["A simple folder-wise guide for Telangana students: what to do after 10th, which course, subjects, pass marks, entrance exams and government jobs."]),
    ("Folder structure", [("table", ["Folder", "What's inside"], [
        ["01_After_10th_Intermediate", "MPC, BiPC, MEC, CEC, HEC, Vocational Inter – subjects, marks, pass %. Inside each group: After_12th folder with EVERY eligible degree (own folder + Word file with private & govt jobs). BiPC has full medical: MBBS + all MD/MS/DM/MCh, BDS, AYUSH, nursing, pharmacy, allied health, paramedical, RMP facts"],
        ["02_After_10th_Polytechnic_Diploma", "TG POLYCET, 14 diploma branches with year-wise subjects & pass %, agri diplomas, ECET, jobs"],
        ["03_After_10th_ITI_Trades", "15 ITI trades – syllabus, pass %, jobs"],
        ["04_After_10th_Other_Options", "Open school (TOSS), apprenticeship, skill courses, other paths"],
        ["05_After_10th_Govt_Jobs_Telangana", "15 govt jobs – each in a separate file with eligibility, age, selection, salary"],
        ["06_After_Inter_Govt_Jobs", "9 govt jobs after 12th – separate files"],
        ["07_After_Degree_Govt_and_Private_Jobs", "15 govt exams for any degree (separate files), private jobs by sector, PG entrance exams, 3-yr LLB"],
        ["08_Work_and_Study_Abroad_Guide", "Country guides (27), language tests, attestation/apostille, safe emigration (eMigrate, ECR, helplines), study-abroad route, cost planner"],
        ["09_Scholarships_and_Student_Support", "TG ePASS, Telangana overseas scholarships (₹20 lakh), central scholarships, education loans, free coaching, helplines"],
        ["Abroad_Jobs (inside EVERY course folder)", "1) Top 10 countries  2) Job search apps by country  3) Step-by-step plan to go abroad"],
    ])]),
    ("Student flow", [
        "10th Pass → Intermediate (2 yrs) → Degree / Engineering / Medical → Jobs / Higher studies",
        "10th Pass → Polytechnic (3 yrs) → Job or B.Tech 2nd year (ECET)",
        "10th Pass → ITI (1–2 yrs) → Apprenticeship → Technical jobs",
        "Inter → Degree (DOST / EAPCET / NEET / LAWCET ...) → Govt exams or private job or PG",
        "10th Pass → Govt jobs directly (GDS, MTS, GD Constable, Agniveer, Railway Group D ...)",
    ]),
    ("Key official websites", [
        "TGBIE (Intermediate): tgbie.cgg.gov.in", "TGSBTET / POLYCET: sbtet.telangana.gov.in, tgpolycet.nic.in",
        "TGCHE (EAPCET, ECET, DOST): tgche.ac.in, dost.cgg.gov.in", "ITI: Department of Employment & Training, Telangana",
        "TGPSC: tspsc.gov.in · TGSLPRB: tgprb.in · SSC: ssc.gov.in · Railways: rrbsecunderabad.gov.in",
    ]),
], subtitle="Prepared for Goutham Goud – folder-wise project")

intermediate.run(); diploma.run(); iti_jobs.run(); streams.run()
abroad_guide.run()
folders, n = abroad_build.add_all()
abroad_build.extras()
print("abroad folders:", len(folders), "abroad docs:", n)
print("docs:", builder.COUNT)
