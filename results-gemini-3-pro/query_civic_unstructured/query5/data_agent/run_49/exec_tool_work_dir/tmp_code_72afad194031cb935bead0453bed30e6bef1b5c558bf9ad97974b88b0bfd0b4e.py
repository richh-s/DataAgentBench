code = """import json

# Load Funding
with open(locals()['var_function-call-16421974567631203467'], 'r') as f:
    funding_data = json.load(f)

# Load Docs
with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

projects = []
# Parse each doc
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    current_section = None
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects" in line:
            current_section = "Capital"
        elif "Disaster Recovery Projects" in line:
            current_section = "Disaster"
            
        # Check new project
        is_new = False
        if i + 1 < len(lines):
            nxt = lines[i+1].strip()
            if "Updates:" in nxt or "Project Description:" in nxt:
                # Basic heuristic
                if len(line) < 150 and "Page" not in line:
                    is_new = True
        
        if is_new:
            if current_project:
                projects.append(current_project)
            current_project = {
                "name": line,
                "section": current_section,
                "st": None,
                "is_disaster": False
            }
            if current_section == "Disaster":
                current_project["is_disaster"] = True
            if "FEMA" in line or "CalOES" in line:
                current_project["is_disaster"] = True
        
        elif current_project:
            # Check fields
            if "Begin Construction" in line:
                # Expected format: (bullet) Begin Construction: Date
                parts = line.split(":")
                if len(parts) > 1:
                    current_project["st"] = parts[1].strip()
            
            if "FEMA" in line or "CalOES" in line or "Disaster" in line:
                current_project["is_disaster"] = True
    
    if current_project:
        projects.append(current_project)

# Filter
target_projects = []
for p in projects:
    st = p.get("st")
    if st and "2022" in st:
        if p["is_disaster"]:
            target_projects.append(p)

# Match
total = 0
matched_ids = set()
matched_names = []

for p in target_projects:
    p_name_norm = p["name"].lower().replace("project", "").strip()
    
    for rec in funding_data:
        f_name_norm = rec["Project_Name"].lower().replace("project", "").strip()
        
        # Check match
        # Use simple substring match
        if p_name_norm in f_name_norm or f_name_norm in p_name_norm:
            if rec["Funding_ID"] not in matched_ids:
                total += float(rec["Amount"])
                matched_ids.add(rec["Funding_ID"])
                matched_names.append(rec["Project_Name"])

print("__RESULT__:")
print(json.dumps({"total": total, "projects": [p["name"] for p in target_projects], "matched": matched_names}))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json'}

exec(code, env_args)
