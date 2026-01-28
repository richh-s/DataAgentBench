code = """import json

# Load data
with open(locals()['var_function-call-13773859182325991137']) as f:
    sqlite_projects = json.load(f)

with open(locals()['var_function-call-15526337120589505523']) as f:
    mongo_docs = json.load(f)

funded_names = set(p['Project_Name'] for p in sqlite_projects)

design_projects_text = []

for doc in mongo_docs:
    text = doc['text']
    start_idx = text.find("Capital Improvement Projects (Design)")
    if start_idx == -1:
        continue
    
    # Find end
    next_sections = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = len(text)
    for ns in next_sections:
        idx = text.find(ns, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        if "Capital Improvement Projects" in line: continue
        if line.startswith("Page"): continue
        if line.startswith("Agenda Item"): continue
        if line.startswith("(cid"): continue
        if line.startswith("Updates:"): continue
        if line.startswith("Project Schedule"): continue
        if line.startswith("Estimated Schedule"): continue
        
        # Check next few lines for updates marker
        is_project = False
        for j in range(i+1, min(i+10, len(lines))):
            next_line = lines[j].strip()
            if not next_line: continue
            if next_line.startswith("(cid") or "Updates" in next_line or "Project Description" in next_line:
                is_project = True
                break
            # If we encounter another header-like line, stop
            if "Capital Improvement" in next_line:
                break
        
        if is_project:
            if line not in design_projects_text:
                design_projects_text.append(line)

print("DEBUG_EXTRACTED:", design_projects_text)

count = 0
matched_list = []
for d_proj in design_projects_text:
    d_norm = d_proj.lower().strip()
    match_found = False
    
    # Normalize d_proj: remove common suffices for better matching?
    # e.g. "Clover Heights Storm Drainage Improvements" -> "Clover Heights Storm Drain"
    
    for f_proj in funded_names:
        f_norm = f_proj.lower().strip()
        
        if d_norm == f_norm:
            match_found = True
        elif d_norm in f_norm or f_norm in d_norm:
            # Check for false positives with short strings?
            # e.g. "Project A" in "Project A Phase 2" -> OK
            # e.g. "Park" in "Trancas Canyon Park" -> Maybe too generic?
            # But the extracted names are full titles.
            match_found = True
            
        if match_found:
            break
            
    if match_found:
        count += 1
        matched_list.append(d_proj)

print("DEBUG_MATCHED:", matched_list)

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-13773859182325991137': 'file_storage/function-call-13773859182325991137.json', 'var_function-call-13773859182325990970': 'file_storage/function-call-13773859182325990970.json', 'var_function-call-15526337120589505523': 'file_storage/function-call-15526337120589505523.json'}

exec(code, env_args)
