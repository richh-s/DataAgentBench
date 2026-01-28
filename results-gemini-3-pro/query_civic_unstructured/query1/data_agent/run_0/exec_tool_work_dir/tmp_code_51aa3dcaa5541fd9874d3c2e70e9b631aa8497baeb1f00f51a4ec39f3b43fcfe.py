code = """import json

sqlite_data = json.load(open(locals()['var_function-call-13773859182325991137']))
mongo_data = json.load(open(locals()['var_function-call-15526337120589505523']))

funded_names = []
for p in sqlite_data:
    funded_names.append(p["Project_Name"])

design_projects = []

for doc in mongo_data:
    text = doc["text"]
    start = text.find("Capital Improvement Projects (Design)")
    if start == -1: continue
    
    end = len(text)
    for token in ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]:
        idx = text.find(token, start)
        if idx != -1 and idx < end:
            end = idx
    
    section = text[start:end]
    rows = section.split(chr(10))
    
    for i in range(len(rows)):
        line = rows[i].strip()
        if len(line) < 5: continue
        if "Capital Improvement" in line: continue
        if "Page" in line and "of" in line: continue
        if "Agenda Item" in line: continue
        if "(cid" in line: continue
        if "Updates:" in line: continue
        if "Project Schedule" in line: continue
        
        is_proj = False
        for j in range(1, 10):
            if i + j >= len(rows): break
            nxt = rows[i+j].strip()
            if len(nxt) == 0: continue
            if "(cid" in nxt or "Updates" in nxt or "Project Description" in nxt:
                is_proj = True
                break
            break

        if is_proj:
            if line not in design_projects:
                design_projects.append(line)

print("DEBUG_EXTRACTED:", design_projects)

match_count = 0
matched_names = []

for dp in design_projects:
    d_norm = dp.lower().strip()
    found = False
    for fp in funded_names:
        f_norm = fp.lower().strip()
        if d_norm in f_norm or f_norm in d_norm:
            found = True
            break
    if found:
        match_count += 1
        matched_names.append(dp)

print("DEBUG_MATCHED:", matched_names)
print("__RESULT__:")
print(json.dumps(match_count))"""

env_args = {'var_function-call-13773859182325991137': 'file_storage/function-call-13773859182325991137.json', 'var_function-call-13773859182325990970': 'file_storage/function-call-13773859182325990970.json', 'var_function-call-15526337120589505523': 'file_storage/function-call-15526337120589505523.json'}

exec(code, env_args)
