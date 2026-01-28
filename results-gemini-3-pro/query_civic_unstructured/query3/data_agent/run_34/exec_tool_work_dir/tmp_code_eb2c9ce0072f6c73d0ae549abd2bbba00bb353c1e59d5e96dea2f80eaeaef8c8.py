code = """import json

civic_docs_path = locals()['var_function-call-7662231611514557955']
funding_path = locals()['var_function-call-16376562458933732175']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

funding_map = {}
all_funding_names = set()
for f in funding:
    name = f['Project_Name']
    all_funding_names.add(name)
    if name not in funding_map:
        funding_map[name] = []
    funding_map[name].append(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    curr_proj_name = None
    curr_proj_desc = []
    
    def save_project(p_name, p_desc, p_status):
        if not p_name: return
        full_desc = "\n".join(p_desc).lower()
        
        final_status = p_status
        if p_status == "Construction":
            if "completed" in full_desc and ("notice of completion" in full_desc or "construction was completed" in full_desc):
                 final_status = "Completed"
        
        keywords = ['emergency', 'fema']
        is_relevant = False
        for kw in keywords:
            if kw in full_desc or kw in p_name.lower():
                is_relevant = True
                break
        
        if is_relevant:
            extracted_projects.append({
                "name": p_name,
                "status": final_status,
                "description": full_desc
            })

    for line in lines:
        line_clean = line.strip()
        if not line_clean: continue
        
        if "Capital Improvement Projects (Design)" in line_clean:
            save_project(curr_proj_name, curr_proj_desc, current_status)
            curr_proj_name = None
            curr_proj_desc = []
            current_status = "Design"
            continue
        elif "Capital Improvement Projects (Construction)" in line_clean:
            save_project(curr_proj_name, curr_proj_desc, current_status)
            curr_proj_name = None
            curr_proj_desc = []
            current_status = "Construction"
            continue
        elif "Capital Improvement Projects (Not Started)" in line_clean:
            save_project(curr_proj_name, curr_proj_desc, current_status)
            curr_proj_name = None
            curr_proj_desc = []
            current_status = "Not Started"
            continue
        elif "Disaster Recovery Projects" in line_clean:
            save_project(curr_proj_name, curr_proj_desc, current_status)
            curr_proj_name = None
            curr_proj_desc = []
            current_status = "Design"
            continue
        
        match = None
        if line_clean in funding_map:
            match = line_clean
        elif line_clean.endswith(" Project"):
             stripped = line_clean[:-8]
             if stripped in funding_map:
                 match = stripped
        
        if match:
            save_project(curr_proj_name, curr_proj_desc, current_status)
            curr_proj_name = match
            curr_proj_desc = []
            if current_status is None:
                current_status = "Design"
        else:
            if curr_proj_name:
                curr_proj_desc.append(line_clean)
    
    save_project(curr_proj_name, curr_proj_desc, current_status)

results = []
seen_funding_ids = set()

for p in extracted_projects:
    p_name = p['name']
    p_status = p['status']
    
    f_recs = list(funding_map.get(p_name, []))
    
    for fname in all_funding_names:
        if fname == p_name: continue
        if fname.startswith(p_name):
             remainder = fname[len(p_name):]
             if "FEMA" in remainder or "CalOES" in remainder:
                 f_recs.extend(funding_map[fname])
    
    for fr in f_recs:
        fid = fr['Funding_ID']
        if fid not in seen_funding_ids:
            seen_funding_ids.add(fid)
            results.append({
                "Project_Name": fr['Project_Name'],
                "Funding_Source": fr['Funding_Source'],
                "Amount": fr['Amount'],
                "Status": p_status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7451868806044347925': 'file_storage/function-call-7451868806044347925.json', 'var_function-call-16376562458933732175': 'file_storage/function-call-16376562458933732175.json', 'var_function-call-7662231611514557955': 'file_storage/function-call-7662231611514557955.json'}

exec(code, env_args)
