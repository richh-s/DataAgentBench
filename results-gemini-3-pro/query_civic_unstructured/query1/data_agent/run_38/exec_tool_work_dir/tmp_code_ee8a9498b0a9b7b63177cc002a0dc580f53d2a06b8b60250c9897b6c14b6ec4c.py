code = """import json
import pandas as pd

# Get file paths from storage
funding_path = locals()['var_function-call-5988651082647865980']
docs_path = locals()['var_function-call-9407752625735979853']

# Load funding data
# The file contains a JSON array of records
funding_data = pd.read_json(funding_path)

# Filter for funding > 50,000
high_funding_projects = set(funding_data[funding_data['Amount'] > 50000]['Project_Name'].str.strip().tolist())

# Load civic docs
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    capture_mode = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detect headers
        if "Capital Improvement Projects" in line and "Design" in line:
            capture_mode = True
            continue
        
        # Stop capturing if we hit another section
        if "Capital Improvement Projects" in line and ("Construction" in line or "Not Started" in line):
            capture_mode = False
            continue
        if "Disaster Recovery Projects" in line:
            capture_mode = False
            continue
        if "Agenda Item" in line or "Page " in line:
            continue
            
        if capture_mode:
            # Skip bullet points and metadata lines
            if line.startswith("(") or "Updates:" in line or "Project Schedule:" in line or "Complete Design:" in line or "Advertise:" in line or "Begin Construction:" in line:
                continue
            
            # Skip short lines
            if len(line) < 5:
                continue
            
            # This is likely a project name
            capital_design_projects.append(line)

# Clean extracted names
cleaned_projects = set()
for p in capital_design_projects:
    p = p.strip()
    # Remove leading non-alphanumeric if any
    cleaned_projects.add(p)

# Matching logic
matched_list = []

# Normalize for comparison
hf_norm = {name.lower().replace("project", "").strip(): name for name in high_funding_projects}

for cp in cleaned_projects:
    cp_norm = cp.lower().replace("project", "").strip()
    
    if cp in high_funding_projects:
        matched_list.append(cp)
    elif cp_norm in hf_norm:
        matched_list.append(hf_norm[cp_norm])
    else:
        # Check for near matches
        for hf_name in high_funding_projects:
            hf_n = hf_name.lower()
            cp_n = cp.lower()
            # If one contains the other and length is sufficient
            if (cp_n in hf_n or hf_n in cp_n) and len(cp_n) > 10:
                matched_list.append(hf_name)

# Deduplicate
matched_list = list(set(matched_list))

print("__RESULT__:")
print(json.dumps({"count": len(matched_list), "matched_projects": matched_list, "debug_extracted": list(cleaned_projects)}))"""

env_args = {'var_function-call-5988651082647865980': 'file_storage/function-call-5988651082647865980.json', 'var_function-call-9407752625735979853': 'file_storage/function-call-9407752625735979853.json'}

exec(code, env_args)
