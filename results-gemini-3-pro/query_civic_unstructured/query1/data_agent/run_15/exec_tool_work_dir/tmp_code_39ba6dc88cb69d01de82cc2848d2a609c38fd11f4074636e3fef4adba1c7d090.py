code = """import json

fund_key = 'var_function-call-1599065279211733274'
docs_key = 'var_function-call-1599065279211735013'

with open(locals()[fund_key], 'r') as f:
    funding = json.load(f)
with open(locals()[docs_key], 'r') as f:
    docs = json.load(f)

funded = {}
for x in funding:
    try:
        s = str(x.get('Amount', '0')).replace(',', '').replace('$', '')
        if float(s) > 50000:
            funded[x.get('Project_Name', '').strip()] = float(s)
    except:
        pass

projects = set()
marker = "Capital Improvement Projects (Design)"
end_markers = ["Capital Improvement Projects (Construction)", "Agenda Item", "Disaster Recovery Projects"]

u_str = "Updates"
c_str = "(cid:"
d_str = "Project Description"

for d in docs:
    txt = d.get('text', '')
    start = txt.find(marker)
    if start < 0: continue
    
    sub = txt[start + len(marker):]
    limit = len(sub)
    for m in end_markers:
        idx = sub.find(m)
        if idx != -1 and idx < limit:
            limit = idx
            
    section = sub[:limit]
    lines = [l.strip() for l in section.splitlines() if l.strip()]
    
    for i in range(len(lines) - 1):
        line = lines[i]
        nxt = lines[i+1]
        
        is_p = False
        if u_str in nxt: is_p = True
        if c_str in nxt: is_p = True
        if d_str in nxt: is_p = True
        
        if is_p:
            if u_str not in line and "Page " not in line and len(line) > 5:
                projects.add(line)

matches = []
for p in projects:
    if p in funded:
        matches.append(p)

print("__RESULT__:")
print(json.dumps({
    "count": len(matches),
    "matches": matches,
    "extracted_sample": list(projects),
    "funded_skate": [k for k in funded if 'Skate' in k],
    "extracted_skate": [k for k in projects if 'Skate' in k]
}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json', 'var_function-call-3315802796629298163': {'count': 1, 'projects': ['PCH Median Improvements Project']}}

exec(code, env_args)
