"""Generate all docs (via main.py) and export every record to JSON for the React app."""
import json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
import builder
import main  # noqa: runs the full generation (docx + records)
import abroad_build
from abroad_countries import C, ORDER_HELP
from abroad_prof import P

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public", "data")
os.makedirs(OUT, exist_ok=True)

FIX = [(r"\bBSc\b", "B.Sc"), (r"\bBCom\b", "B.Com"), (r"\bBTech\b", "B.Tech"), (r"\bBArch\b", "B.Arch"), (r"\bMSc\b", "M.Sc"), (r"\bBEd\b", "B.Ed"),
       (r"\bDElEd\b", "D.El.Ed"), (r"\bBVSc\b", "BVSc"), (r"\bBFSc\b", "B.F.Sc"), (r"\bBPharm\b|\bB Pharm\b", "B.Pharm"), (r"\bD Pharm\b", "D.Pharm"), (r"\bPharm D\b", "Pharm-D"),
       (r"\bMCh\b", "MCh"), (r"\bLLB\b", "LLB"), (r"\bBA\b", "B.A."), (r"\bBBA\b", "BBA"), (r"\bBCA\b", "BCA"), (r"\b10th\b", "10th")]


ROOTNAMES = {"01_After_10th_Intermediate": "Intermediate", "02_After_10th_Polytechnic_Diploma": "Polytechnic", "03_After_10th_ITI_Trades": "ITI trades",
             "04_After_10th_Other_Options": "Other options after 10th", "05_After_10th_Govt_Jobs_Telangana": "Govt jobs after 10th", "06_After_Inter_Govt_Jobs": "Govt jobs after Inter",
             "07_After_Degree_Govt_and_Private_Jobs": "Jobs after degree", "08_Work_and_Study_Abroad_Guide": "Work & study abroad", "09_Scholarships_and_Student_Support": "Scholarships & support"}


def pretty(seg):
    if seg in ROOTNAMES:
        return ROOTNAMES[seg]
    m = re.match(r"^After_12th_(\w+)$", seg)
    if m:
        return "Courses after Inter " + m.group(1)
    if seg == "After_Vocational_Inter":
        return "Courses after Vocational Inter"
    s = re.sub(r"^\d\d_", "", seg)
    s = s.replace("_and_", " & ").replace("_", " ")
    for a, b in FIX:
        s = re.sub(a, b, s)
    return s.strip()


def slug(path):
    return re.sub(r"\.docx$", "", path)


docs = [r for r in builder.RECORDS if "/Abroad_Jobs/" not in r["path"]]
# reuse classification without regenerating files
abroad_folders = {}
for dp, dn, fn in os.walk(builder.ROOT):
    rel = os.path.relpath(dp, builder.ROOT).replace(os.sep, "/")
    if rel == "." or "Abroad_Jobs" in rel.split("/"):
        continue
    k = abroad_build.classify(rel)
    if k:
        abroad_folders[rel] = k

folders = {}

def ensure(path):
    if path in folders or path == "":
        return
    parent = os.path.dirname(path)
    ensure(parent)
    folders[path] = {"id": path, "name": pretty(os.path.basename(path)), "parent": parent, "folders": [], "docs": [], "abroad": abroad_folders.get(path)}
    if parent:
        folders[parent]["folders"].append(path)
    else:
        roots.append(path)

roots = []
root_docs = []
chunks = collections.defaultdict(dict)
search = []
for r in docs:
    p = r["path"]
    d = os.path.dirname(p)
    did = slug(p)
    parts = p.split("/")
    chunk = "root" if len(parts) == 1 else (parts[0] + "__" + parts[1] if parts[0] == "01_After_10th_Intermediate" and len(parts) > 2 else parts[0])
    chunk = re.sub(r"[^A-Za-z0-9_]", "_", chunk)
    meta = {"id": did, "title": r["title"], "sub": r["sub"], "folder": d, "chunk": chunk, "file": pretty(os.path.basename(did))}
    if d:
        ensure(d)
        folders[d]["docs"].append(meta)
    else:
        root_docs.append(meta)
    chunks[chunk][did] = {"title": r["title"], "sub": r["sub"], "s": r["s"]}
    text = " ".join([sec["h"] + " " + " ".join(b.get("x", "") if b["t"] != "table" else " ".join(" ".join(row) for row in b["r"]) for b in sec["b"]) for sec in r["s"]])
    search.append({"id": did, "t": r["title"], "f": d, "c": chunk, "x": re.sub(r"\s+", " ", text)[:1500]})

for k, v in folders.items():
    v["folders"].sort()
    v["docs"].sort(key=lambda m: m["id"])
ALIAS = {"GBR": "UK England Britain London", "USA": "US America", "UAE": "Dubai Abu Dhabi Sharjah Gulf", "SAU": "Saudi KSA Riyadh Jeddah Gulf", "QAT": "Doha Gulf",
         "OMN": "Muscat Gulf", "KWT": "Gulf", "BHR": "Gulf", "CAN": "Toronto Vancouver", "AUS": "Sydney Melbourne", "NZL": "NZ", "DEU": "German", "IRL": "Dublin",
         "SGP": "Singapore", "JPN": "Japanese Tokyo", "SEA": "ship shipping", "CRU": "cruise ship"}
# abroad folders without own docs still exist (all have docs) – add abroad search entries
for rel, k in abroad_folders.items():
    ensure(rel)
    p = P[k]
    search.append({"id": "abroad:" + rel, "t": f"Abroad jobs – {pretty(os.path.basename(rel))}", "f": rel, "c": "abroad",
                   "x": p["name"] + " " + " ".join(C[c]["name"] + " " + ALIAS.get(c, "") + " " + why + " " + lic for c, why, lic, _ in p["rows"])})
for code, c in C.items():
    search.append({"id": "country:" + code, "t": f"Country guide – {c['name']}", "f": "", "c": "country", "x": ALIAS.get(code, "") + " " + " ".join(c["visa"] + c["general"] + c.get("health", []) + [c["lang"], c["pr"], c["note"]])})

roots.sort()
tree = {"roots": roots, "rootDocs": root_docs, "folders": folders}
json.dump(tree, open(f"{OUT}/tree.json", "w"), ensure_ascii=False, separators=(",", ":"))
for ch, data in chunks.items():
    json.dump(data, open(f"{OUT}/docs-{ch}.json", "w"), ensure_ascii=False, separators=(",", ":"))
json.dump(search, open(f"{OUT}/search.json", "w"), ensure_ascii=False, separators=(",", ":"))
json.dump({"profiles": P, "countries": C, "orderHelp": ORDER_HELP, "safety": abroad_build.SAFETY}, open(f"{OUT}/abroad.json", "w"), ensure_ascii=False, separators=(",", ":"))
print("docs:", len(docs), "folders:", len(folders), "chunks:", len(chunks), "abroad folders:", len(abroad_folders), "search entries:", len(search))
