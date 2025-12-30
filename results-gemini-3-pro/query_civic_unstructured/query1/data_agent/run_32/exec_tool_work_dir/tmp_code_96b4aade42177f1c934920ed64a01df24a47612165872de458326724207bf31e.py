code = """import json

funding_path = locals()["var_function-call-4570374009180656928"]
docs_path = locals()["var_function-call-13689454801406461365"]

with open(funding_path, "r") as f:
    funding = json.load(f)

candidates = []
for x in funding:
    try:
        if int(x["Amount"]) > 50000:
            candidates.append(x["Project_Name"])
    except:
        pass

with open(docs_path, "r") as f:
    docs = json.load(f)

confirmed = set()

for d in docs:
    txt = d.get("text", "")
    s = txt.find("Capital Improvement Projects (Design)")
    if s == -1: continue
    
    e = len(txt)
    m1 = txt.find("Capital Improvement Projects (Construction)", s)
    if m1 != -1 and m1 < e: e = m1
    m2 = txt.find("Capital Improvement Projects (Not Started)", s)
    if m2 != -1 and m2 < e: e = m2
    m3 = txt.find("Disaster Recovery Projects", s)
    if m3 != -1 and m3 < e: e = m3
    m4 = txt.find("Staff has also prepared", s)
    if m4 != -1 and m4 < e: e = m4
    
    section = txt[s:e]
    lines = section.split("\n")
    
    for ln in lines:
        ln = ln.strip()
        if len(ln) < 5: continue
        
        best_match = ""
        for cand in candidates:
            if cand in ln:
                if len(cand) > len(best_match):
                    best_match = cand
        
        if best_match != "":
            confirmed.add(best_match)

print("__RESULT__:")
print(json.dumps(list(confirmed)))"""

env_args = {'var_function-call-4570374009180656928': 'file_storage/function-call-4570374009180656928.json', 'var_function-call-12751430188961870496': 'file_storage/function-call-12751430188961870496.json', 'var_function-call-13689454801406461365': 'file_storage/function-call-13689454801406461365.json', 'var_function-call-6647682698323320664': ['Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH Median Improvements Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure']}

exec(code, env_args)
