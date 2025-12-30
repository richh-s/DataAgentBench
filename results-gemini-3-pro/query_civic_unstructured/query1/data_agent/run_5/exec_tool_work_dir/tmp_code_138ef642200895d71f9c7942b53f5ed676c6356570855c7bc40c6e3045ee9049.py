code = """import json

# Load funding results
with open(locals()['var_function-call-2752695128907644383'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-10485844614487521069'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding for > 50,000
funded_projects = {}
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        pass

design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Use splitlines
    lines = text.splitlines()
    
    in_section = False
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check start of section
        if "Capital Improvement Projects (Design)" in line:
            in_section = True
            continue
            
        # Check end of section
        if in_section:
            if "Capital Improvement Projects (" in line and "Design" not in line:
                in_section = False
            if "Disaster Recovery Projects" in line:
                in_section = False
            # Check for other section headers that might appear
            if line.startswith("Capital Improvement Projects") and "Design" not in line:
                 in_section = False
            
            if not in_section:
                continue
                
            # Extraction logic
            # Look ahead for "Updates:" or equivalent
            # scan next 1-3 non-empty lines
            is_project = False
            lookahead_count = 0
            for j in range(i + 1, len(lines)):
                next_l = lines[j].strip()
                if not next_l:
                    continue
                lookahead_count += 1
                if lookahead_count > 3:
                    break
                
                if "Updates:" in next_l or "Project Description:" in next_l or "Project Updates:" in next_l:
                    is_project = True
                    break
                # If we hit another likely header or something, stop
                if "(cid:190)" in next_l: # The bullet point usually starts the updates line
                     if "Updates" in next_l or "Project Description" in next_l:
                         is_project = True
                     # Sometimes just a bullet point? In the sample it was `(cid:190) Updates:`
                     break
            
            if is_project:
                # This line is likely the project name
                # Clean it
                p_name = line
                # Ignore short lines or headers (like "Page 1 of 6")
                if len(p_name) > 3 and "Page " not in p_name and "Agenda Item" not in p_name:
                    design_projects.add(p_name)

# Matching
matches = []
normalized_funding = {k.lower(): k for k in funded_projects.keys()}

for dp in design_projects:
    dp_norm = dp.lower()
    
    matched_name = None
    
    # 1. Exact match
    if dp_norm in normalized_funding:
        matched_name = normalized_funding[dp_norm]
    else:
        # 2. Startswith / Contained (Fuzzy)
        # Check if funding name starts with dp (e.g. "Name" vs "Name (FEMA)")
        # Check if dp starts with funding name (unlikely)
        # Check if dp is contained in funding name
        for fname_norm, original_name in normalized_funding.items():
            if fname_norm.startswith(dp_norm) or dp_norm in fname_norm:
                 matched_name = original_name
                 break
                 
    if matched_name:
        matches.append(matched_name)

unique_matches = sorted(list(set(matches)))

print("__RESULT__:")
print(json.dumps({"count": len(unique_matches), "matches": unique_matches, "extracted_projects": list(design_projects)}))"""

env_args = {'var_function-call-2752695128907644383': 'file_storage/function-call-2752695128907644383.json', 'var_function-call-2752695128907641442': 'file_storage/function-call-2752695128907641442.json', 'var_function-call-10485844614487521069': 'file_storage/function-call-10485844614487521069.json', 'var_function-call-5225985024774178468': {'count': 1, 'matches': ['Trancas Canyon Park Playground Resurfacing'], 'extracted_projects': ['Marie Canyon Green Streets', 'Trancas Canyon Park Playground']}}

exec(code, env_args)
