code = """import json

path_civic = locals()["var_function-call-17911160366985572279"]
path_fund = locals()["var_function-call-5314689848264008089"]

with open(path_civic, "r") as f:
    civic = json.load(f)
with open(path_fund, "r") as f:
    fund = json.load(f)

extracted = []
NL = chr(10)
CID = chr(40) + "cid:"

for doc in civic:
    txt = doc.get("text", "")
    parts = txt.split("Capital Improvement Projects " + chr(40))
    
    for part in parts[1:]: 
        if part.startswith("Design" + chr(41)):
            status = "design"
        elif part.startswith("Construction" + chr(41)):
            status = "construction"
        elif part.startswith("Not Started" + chr(41)):
            status = "not started"
        else:
            status = "unknown"
            
        subparts = part.split(NL + CID)
        
        for k in range(len(subparts) - 1):
            prev_lines = subparts[k].split(NL)
            prev_lines = [l.strip() for l in prev_lines if l.strip()]
            if not prev_lines:
                continue
            name = prev_lines[-1]
            
            body_chunk = subparts[k+1]
            body_lines = body_chunk.split(NL)
            
            if k < len(subparts) - 2:
                idx = -1
                for x in range(len(body_lines)-1, -1, -1):
                    if body_lines[x].strip():
                        idx = x
                        break
                if idx != -1:
                    body_lines = body_lines[:idx]
            
            full_text = NL.join(body_lines).lower()
            
            p_status = status
            if p_status == "construction":
                if "construction was completed" in full_text or "notice of completion" in full_text:
                    p_status = "completed"
            
            extracted.append({
                "name": name,
                "status": p_status,
                "text": full_text
            })

results = []
seen = set()

for p in extracted:
    p_name = p["name"].strip()
    p_txt = p["text"]
    
    is_rel = "emergency" in p_txt or "fema" in p_txt
    
    matches = []
    for f in fund:
        fn = f.get("Project_Name", "").strip()
        if fn == p_name:
            matches.append(f)
        elif fn.startswith(p_name) and (chr(40) + "FEMA" in fn or chr(40) + "CalOES" in fn):
            matches.append(f)
            
    is_rel_fund = any("FEMA" in m["Project_Name"] for m in matches)
    
    if is_rel or is_rel_fund:
        for m in matches:
            key = (m["Project_Name"], m["Funding_Source"], m["Amount"], p["status"])
            if key not in seen:
                results.append({
                    "Project_Name": m["Project_Name"],
                    "Funding_Source": m["Funding_Source"],
                    "Amount": m["Amount"],
                    "Status": p["status"]
                })
                seen.add(key)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5314689848264011546': 'file_storage/function-call-5314689848264011546.json', 'var_function-call-5314689848264008089': 'file_storage/function-call-5314689848264008089.json', 'var_function-call-17911160366985572279': 'file_storage/function-call-17911160366985572279.json'}

exec(code, env_args)
