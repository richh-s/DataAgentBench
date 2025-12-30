code = """import json

# Load Funding
with open(locals()['var_function-call-16421974567631203467'], 'r') as f:
    funding_data = json.load(f)

# Load Docs
with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = "\n".join([d.get('text', '') for d in civic_docs])
lines = full_text.splitlines()

projects = []
current_project = None
current_section = None

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Section Detection
    if "Capital Improvement Projects" in line:
        current_section = "Capital"
    elif "Disaster Recovery Projects" in line:
        current_section = "Disaster"
    
    # Project Detection
    # Look ahead for "Updates:" or "Project Description:"
    is_new_project = False
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        if "Updates:" in next_line or "Project Description:" in next_line:
            # Avoid some false positives
            if len(line) < 100 and "Page" not in line and "Agenda" not in line:
                is_new_project = True
    
    if is_new_project:
        if current_project:
            projects.append(current_project)
        current_project = {
            "name": line,
            "section": current_section,
            "text": "",
            "st": None,
            "is_disaster": False
        }
        # Check keywords in name
        if "FEMA" in line or "CalOES" in line or "Disaster" in line:
            current_project["is_disaster"] = True
        if current_section == "Disaster":
            current_project["is_disaster"] = True
            
    elif current_project:
        current_project["text"] += line + "\n"
        # Extract st
        # Check for "Begin Construction: <date>"
        if "Begin Construction" in line:
            parts = line.split(":")
            if len(parts) > 1:
                current_project["st"] = parts[1].strip()
        
        # Check for disaster keywords in text
        if "FEMA" in line or "CalOES" in line:
            current_project["is_disaster"] = True

if current_project:
    projects.append(current_project)

# Filter
# Started in 2022
target_projects = []
for p in projects:
    st = p.get("st", "")
    if st and "2022" in st:
        if p["is_disaster"]:
            target_projects.append(p)

# Sum Funding
total_funding = 0
matched_records = []
target_names = [p["name"].lower() for p in target_projects]

print("DEBUG: Target Projects (Disaster & Started 2022):")
for p in target_projects:
    print(f" - {p['name']} (Start: {p['st']})")

for rec in funding_data:
    f_name = rec["Project_Name"].lower()
    # Match logic
    matched = False
    for t_name in target_names:
        if t_name in f_name or f_name in t_name:
            matched = True
            break
    
    if matched:
        # Also, check if funding source confirms disaster? Not strictly required if project is identified as disaster.
        # But wait, if text name is "Road Repair" (started 2022, disaster section)
        # And funding has "Road Repair" and "Road Repair (FEMA)".
        # Both match "Road Repair".
        # We should count both.
        total_funding += float(rec["Amount"])
        matched_records.append(rec["Project_Name"])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_records}))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json'}

exec(code, env_args)
