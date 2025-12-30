code = """import json

k_fund = "var_function-call-15202175332951554163"
k_docs = "var_function-call-15202175332951553736"

with open(locals()[k_fund], "r") as f:
    funds = json.load(f)

with open(locals()[k_docs], "r") as f:
    docs = json.load(f)

extracted = []

for d in docs:
    txt = d.get("text", "")
    # Use splitlines to avoid backslash n issues
    lines = txt.splitlines()
    
    section = ""
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            section = line
            i += 1
            continue
            
        is_proj = False
        if i + 1 < len(lines):
            nxt = lines[i+1].strip()
            # Check keywords in next line
            if "Updates:" in nxt or "Project Description:" in nxt or "Project Updates:" in nxt:
                is_proj = True
        
        if is_proj and line:
            name = line
            
            # Extract block
            blk_parts = []
            j = i + 1
            while j < len(lines):
                sub = lines[j].strip()
                if "Capital Improvement Projects" in sub or "Disaster Recovery Projects" in sub:
                    break
                
                if j + 1 < len(lines):
                    snxt = lines[j+1].strip()
                    if ("Updates:" in snxt or "Project Description:" in snxt or "Project Updates:" in snxt) and sub:
                        break
                
                blk_parts.append(sub)
                j += 1
            
            blk = " ".join(blk_parts)
            
            # Check relevancy
            full = (name + " " + blk).lower()
            if "emergency" in full or "fema" in full:
                # Status
                st = "Unknown"
                sec_low = (section or "").lower()
                blk_low = blk.lower()
                
                if "design" in sec_low:
                    st = "design"
                elif "not started" in sec_low:
                    st = "not started"
                elif "construction" in sec_low:
                    if "completed" in blk_low and "currently under construction" not in blk_low:
                        st = "completed"
                    elif "notice of completion" in blk_low:
                        st = "completed"
                    else:
                        st = "construction"
                
                extracted.append({"n": name, "s": st})
            
            i = j
        else:
            i += 1

# Join
res = []
f_dict = {x["Project_Name"]: x for x in funds}
f_dict_l = {x["Project_Name"].lower(): x for x in funds}

for item in extracted:
    n = item["n"]
    match = f_dict.get(n)
    if not match:
        match = f_dict_l.get(n.lower())
    
    if match:
        # Check dups
        seen = False
        for r in res:
            if r["Project_Name"] == match["Project_Name"]:
                seen = True
                break
        if not seen:
            res.append({
                "Project_Name": match["Project_Name"],
                "Funding_Source": match["Funding_Source"],
                "Amount": match["Amount"],
                "Status": item["s"]
            })

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json'}

exec(code, env_args)
