code = """import json
import pandas as pd

# Load funding data
funding_data = pd.read_json('var_function-call-5988651082647865980')

# Filter for funding > 50,000
high_funding_projects = set(funding_data[funding_data['Amount'] > 50000]['Project_Name'].str.strip().tolist())

# Load civic docs
with open('var_function-call-9407752625735979853', 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
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
            if line.startswith("(") or line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Complete Design:") or line.startswith("Advertise:") or line.startswith("Begin Construction:") or line.startswith("Final Design:"):
                continue
            
            # Skip short lines (dates, etc)
            if len(line) < 5:
                continue
            
            # This is likely a project name
            capital_design_projects.append(line)

# Clean extracted names
cleaned_projects = set()
for p in capital_design_projects:
    # Remove any trailing details if stuck to the name
    p = p.strip()
    cleaned_projects.add(p)

# Matching logic
match_count = 0
matched_list = []

# Normalize for comparison
hf_norm = {name.lower().replace("project", "").strip(): name for name in high_funding_projects}

for cp in cleaned_projects:
    cp_norm = cp.lower().replace("project", "").strip()
    
    if cp in high_funding_projects:
        match_count += 1
        matched_list.append(cp)
    elif cp_norm in hf_norm:
        match_count += 1
        matched_list.append(hf_norm[cp_norm])
    else:
        # Check for near matches
        pass

# Deduplicate matched list in case of multiple matches pointing to same funding record
matched_list = list(set(matched_list))

print("__RESULT__:")
print(json.dumps({"count": len(matched_list), "matched_projects": matched_list, "debug_extracted": list(cleaned_projects)}))"""

env_args = {'var_function-call-5988651082647865980': 'file_storage/function-call-5988651082647865980.json', 'var_function-call-9407752625735979853': 'file_storage/function-call-9407752625735979853.json'}

exec(code, env_args)
