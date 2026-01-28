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

# Extract design projects from civic docs
design_projects = set()

# Use chr(10) for newline to avoid escaping issues
NEWLINE = chr(10)

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Normalize text newlines
    # Just split by newline character directly, assuming python handles it or just split
    lines = text.splitlines()
    
    # Find the section "Capital Improvement Projects (Design)"
    section_header = "Capital Improvement Projects (Design)"
    
    in_section = False
    
    # Iterate lines to find section
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if section_header in line:
            in_section = True
            continue
            
        if in_section:
            # Check for end of section headers
            if "Capital Improvement Projects (" in line and "Design" not in line:
                in_section = False
                break
            if "Disaster Recovery Projects" in line:
                in_section = False
                break
            if "Public Works Commission" in line:
                in_section = False
                break
                
            # Logic to extract project name
            # If current line is not empty, and next line has "Updates:" or "Project Description:"
            if line:
                if i + 1 < len(lines):
                    next_line = lines[i+1]
                    if "Updates:" in next_line or "Project Description:" in next_line or "Project Updates:" in next_line:
                        # Clean project name
                        p_name = line
                        if len(p_name) > 3 and "Page" not in p_name:
                            design_projects.add(p_name)

# Matching logic
matches = []
normalized_funding = {k.lower(): k for k in funded_projects.keys()}

for dp in design_projects:
    dp_norm = dp.lower()
    
    matched_name = None
    
    if dp_norm in normalized_funding:
        matched_name = normalized_funding[dp_norm]
    else:
        # Fuzzy match: starts with or contained
        for fname_norm, original_name in normalized_funding.items():
            if fname_norm.startswith(dp_norm) or dp_norm in fname_norm:
                matched_name = original_name
                break
    
    if matched_name:
        matches.append(matched_name)

unique_matches = sorted(list(set(matches)))

print("__RESULT__:")
print(json.dumps({"count": len(unique_matches), "matches": unique_matches, "extracted_projects": list(design_projects)}))"""

env_args = {'var_function-call-2752695128907644383': 'file_storage/function-call-2752695128907644383.json', 'var_function-call-2752695128907641442': 'file_storage/function-call-2752695128907641442.json', 'var_function-call-10485844614487521069': 'file_storage/function-call-10485844614487521069.json'}

exec(code, env_args)
