code = """import json

key_docs = "var_function-call-7662231611514557955"
key_fund = "var_function-call-16376562458933732175"
path_docs = locals()[key_docs]
path_fund = locals()[key_fund]

with open(path_docs, "r") as f:
    docs = json.load(f)

with open(path_fund, "r") as f:
    fund = json.load(f)

fund_map = {}
fund_names = set()
for x in fund:
    n = x["Project_Name"]
    fund_names.add(n)
    if n not in fund_map:
        fund_map[n] = []
    fund_map[n].append(x)

extracted = []

for d in docs:
    txt = d["text"]
    lines = txt.split("\n")
    
    cur_stat = "Design"
    cur_name = None
    cur_desc_list = []
    
    for line in lines:
        l = line.strip()
        if not l: continue
        
        if "Capital Improvement Projects (Design)" in l:
            if cur_name:
                extracted.append({"n": cur_name, "s": cur_stat, "d": "\n".join(cur_desc_list)})
            cur_name = None
            cur_desc_list = []
            cur_stat = "Design"
            continue
        
        if "Capital Improvement Projects (Construction)" in l:
            if cur_name:
                extracted.append({"n": cur_name, "s": cur_stat, "d": "\n".join(cur_desc_list)})
            cur_name = None
            cur_desc_list = []
            cur_stat = "Construction"
            continue
            
        if "Capital Improvement Projects (Not Started)" in l:
            if cur_name:
                extracted.append({"n": cur_name, "s": cur_stat, "d": "\n".join(cur_desc_list)})
            cur_name = None
            cur_desc_list = []
            cur_stat = "Not Started"
            continue
            
        if "Disaster Recovery Projects" in l:
            if cur_name:
                extracted.append({"n": cur_name, "s": cur_stat, "d": "\n".join(cur_desc_list)})
            cur_name = None
            cur_desc_list = []
            cur_stat = "Design"
            continue
            
        matched = None
        if l in fund_map:
            matched = l
        elif l.endswith(" Project"):
             base = l[:-8]
             if base in fund_map:
                 matched = base
        
        if matched:
            if cur_name:
                extracted.append({"n": cur_name, "s": cur_stat, "d": "\n".join(cur_desc_list)})
            cur_name = matched
            cur_desc_list = []
        else:
            if cur_name:
                cur_desc_list.append(l)
                
    if cur_name:
         extracted.append({"n": cur_name, "s": cur_stat, "d": "\n".join(cur_desc_list)})

final_res = []
seen_ids = set()

for item in extracted:
    name = item["n"]
    status = item["s"]
    desc = item["d"].lower()
    
    if status == "Construction":
        if "completed" in desc and ("notice of completion" in desc or "construction was completed" in desc):
            status = "Completed"
            
    is_rel = False
    if "emergency" in desc or "fema" in desc or "emergency" in name.lower() or "fema" in name.lower():
        is_rel = True
        
    if is_rel:
        recs = list(fund_map.get(name, []))
        for fn in fund_names:
            if fn != name and fn.startswith(name) and ("FEMA" in fn or "CalOES" in fn):
                recs.extend(fund_map[fn])
        
        for r in recs:
            fid = r["Funding_ID"]
            if fid not in seen_ids:
                seen_ids.add(fid)
                final_res.append({
                    "Project_Name": r["Project_Name"],
                    "Funding_Source": r["Funding_Source"],
                    "Amount": r["Amount"],
                    "Status": status
                })

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-7451868806044347925': 'file_storage/function-call-7451868806044347925.json', 'var_function-call-16376562458933732175': 'file_storage/function-call-16376562458933732175.json', 'var_function-call-7662231611514557955': 'file_storage/function-call-7662231611514557955.json'}

exec(code, env_args)
