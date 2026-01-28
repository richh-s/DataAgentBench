code = """import json

fp = locals()["var_function-call-5441404039575521335"]
dp = locals()["var_function-call-5441404039575519310"]

with open(fp) as f:
    fd = json.load(f)

high = {x["Project_Name"].strip() for x in fd if int(x.get("Amount", 0)) > 50000}

with open(dp) as f:
    docs = json.load(f)

found = set()
marker = "Capital Improvement Projects (Design)"
stops = ["Capital Improvement Projects (Construction)", "Disaster Recovery Projects"]

for d in docs:
    t = d.get("text", "")
    i = t.find(marker)
    if i < 0: continue
    sub = t[i+len(marker):]
    
    limit = len(sub)
    for s in stops:
        si = sub.find(s)
        if si != -1 and si < limit:
            limit = si
            
    sub = sub[:limit]
    
    for ln in sub.splitlines():
        ln = ln.strip()
        if not ln: continue
        if ln.startswith("(") or ln.startswith("Page") or ln.startswith("Agenda"): continue
        if ":" in ln: continue
        found.add(ln)

res = [p for p in found if p in high]
print("__RESULT__:")
print(json.dumps({"count": len(res), "matches": res}))"""

env_args = {'var_function-call-5441404039575521335': 'file_storage/function-call-5441404039575521335.json', 'var_function-call-5441404039575519310': 'file_storage/function-call-5441404039575519310.json'}

exec(code, env_args)
