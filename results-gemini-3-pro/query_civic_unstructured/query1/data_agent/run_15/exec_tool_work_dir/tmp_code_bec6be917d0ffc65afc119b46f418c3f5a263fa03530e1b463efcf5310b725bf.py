code = """import json

fund_key = 'var_function-call-1599065279211733274'
docs_key = 'var_function-call-1599065279211735013'

with open(locals()[fund_key], 'r') as f:
    funding = json.load(f)
with open(locals()[docs_key], 'r') as f:
    docs = json.load(f)

funded = set()
for x in funding:
    try:
        s = str(x.get('Amount', '0')).replace(',', '').replace('$', '')
        if float(s) > 50000:
            funded.add(x.get('Project_Name', '').strip())
    except:
        pass

projects = set()
marker = "Capital Improvement Projects (Design)"
end_markers = ["Capital Improvement Projects (Construction)", "Agenda Item", "Disaster Recovery Projects"]

updates_str = "Updates:"
cid_str = "cid:"
desc_str = "Project Description"

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
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for i in range(len(lines) - 1):
        line = lines[i]
        nxt = lines[i+1]
        
        is_p = False
        if updates_str in nxt: is_p = True
        if cid_str in nxt: is_p = True
        if desc_str in nxt: is_p = True
        
        if is_p:
            if updates_str not in line and "Page " not in line:
                projects.add(line)

common = projects.intersection(funded)
print("__RESULT__:")
print(json.dumps({"count": len(common), "projects": list(common)}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json'}

exec(code, env_args)
