code = """import json
import re

c_path = locals()['var_function-call-2424790631309893722']
f_path = locals()['var_function-call-2424790631309895007']

with open(c_path, "r") as f:
    docs = json.load(f)
with open(f_path, "r") as f:
    funds = json.load(f)

projs = []
b_char = chr(190)
nl_char = chr(10)

for d in docs:
    txt = d["text"]
    chunks = txt.split(b_char)
    for i in range(1, len(chunks)):
        chunk_curr = chunks[i]
        chunk_prev = chunks[i-1].strip()
        
        if not chunk_prev: continue
        
        lines = chunk_prev.split(nl_char)
        name = None
        
        for line in reversed(lines):
            line = line.strip()
            if not line: continue
            if "Capital" in line: continue
            if "Agenda" in line: continue
            if "Page" in line: continue
            if line.endswith(":"): line = line[:-1]
            name = line
            break
            
        if not name: continue
        
        # Date
        # Use regex but avoid backslashes if possible
        # "Begin Construction: ..."
        # [ \t]* matches whitespace
        pattern = "Begin Construction:[ \t]*(.*)"
        m = re.search(pattern, chunk_curr, re.IGNORECASE)
        if m:
            dt = m.group(1).strip()
            projs.append({"n": name, "d": dt})

# Filter
tn = []
sp = ["March", "April", "May", "Spring"]
target = "2022"

for p in projs:
    ds = p["d"]
    if target in ds:
        found = False
        for s in sp:
            if s.lower() in ds.lower():
                found = True
        if found:
            tn.append(p["n"])

tn = list(set(tn))

# Sum
total = 0
cnt = 0
f_map = {}
for r in funds:
    fn = r["Project_Name"].strip()
    fa = int(r["Amount"])
    if fn in f_map:
        f_map[fn] += fa
    else:
        f_map[fn] = fa

matched = []
for n in tn:
    if n in f_map:
        total += f_map[n]
        cnt += 1
        matched.append(n)

print("__RESULT__:")
print(json.dumps({"count": cnt, "total_funding": total, "matched_projects": matched}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json', 'var_function-call-11236971759880299880': 'Check OK'}

exec(code, env_args)
