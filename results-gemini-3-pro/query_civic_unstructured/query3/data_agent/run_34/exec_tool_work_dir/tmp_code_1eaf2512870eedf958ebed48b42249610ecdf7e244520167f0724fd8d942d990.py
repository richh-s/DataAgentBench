code = """import json

path_docs = locals()["var_function-call-7662231611514557955"]
path_fund = locals()["var_function-call-16376562458933732175"]

docs = json.load(open(path_docs))
fund = json.load(open(path_fund))

fund_map = {}
for x in fund:
    n = x["Project_Name"]
    if n not in fund_map: fund_map[n] = []
    fund_map[n].append(x)

res = []
seen = set()

for d in docs:
    lines = d["text"].splitlines()
    stat = "Design"
    cname = None
    cdesc = []
    
    for l in lines:
        l = l.strip()
        if not l: continue
        
        if "Capital Improvement Projects (Design)" in l:
            if cname: res.append((cname, stat, " ".join(cdesc)))
            cname = None; cdesc = []; stat = "Design"
            continue
        if "Capital Improvement Projects (Construction)" in l:
            if cname: res.append((cname, stat, " ".join(cdesc)))
            cname = None; cdesc = []; stat = "Construction"
            continue
        if "Capital Improvement Projects (Not Started)" in l:
            if cname: res.append((cname, stat, " ".join(cdesc)))
            cname = None; cdesc = []; stat = "Not Started"
            continue
        if "Disaster Recovery Projects" in l:
            if cname: res.append((cname, stat, " ".join(cdesc)))
            cname = None; cdesc = []; stat = "Design"
            continue
            
        m = None
        if l in fund_map: m = l
        elif l.endswith(" Project"):
             b = l[:-8]
             if b in fund_map: m = b
        
        if m:
            if cname: res.append((cname, stat, " ".join(cdesc)))
            cname = m; cdesc = []
        else:
            if cname: cdesc.append(l)

    if cname: res.append((cname, stat, " ".join(cdesc)))

final = []
for n, s, desc in res:
    d = desc.lower()
    if s == "Construction":
        if "completed" in d and ("notice of completion" in d or "construction was completed" in d):
            s = "Completed"
    
    if "emergency" in d or "fema" in d or "emergency" in n.lower() or "fema" in n.lower():
        recs = list(fund_map.get(n, []))
        for k in fund_map:
            if k != n and k.startswith(n) and ("FEMA" in k or "CalOES" in k):
                recs.extend(fund_map[k])
        
        for r in recs:
            if r["Funding_ID"] not in seen:
                seen.add(r["Funding_ID"])
                final.append({
                    "Project_Name": r["Project_Name"],
                    "Funding_Source": r["Funding_Source"],
                    "Amount": r["Amount"],
                    "Status": s
                })

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_function-call-7451868806044347925': 'file_storage/function-call-7451868806044347925.json', 'var_function-call-16376562458933732175': 'file_storage/function-call-16376562458933732175.json', 'var_function-call-7662231611514557955': 'file_storage/function-call-7662231611514557955.json'}

exec(code, env_args)
