code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-16421974567631203467'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

projects = []
current_section = "Unknown"
current_project = None

# Helper to normalize strings for comparison
def normalize(s):
    return s.strip().lower()

# Process text line by line
# We'll concatenate all text first or process document by document
full_text = "\n".join([doc['text'] for doc in civic_docs])
lines = full_text.split('\n')

# Iterate
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Check for Section Headers
    # Headers in sample: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", etc.
    # We suspect "Disaster Recovery Projects" exists.
    if "Capital Improvement Projects" in line:
        current_section = "Capital"
    elif "Disaster Recovery Projects" in line:
        current_section = "Disaster"
    
    # Check for Project Start
    # A project usually starts with a name line, followed by "(cid:190) Updates:" or "(cid:190) Project Description:"
    # We look ahead to confirm
    is_project_start = False
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        # Look for the special bullet point or "Updates:"
        if next_line.startswith("(cid:190)") or "Updates:" in next_line or "Project Description:" in next_line:
            # Also exclude lines that are clearly headers or page numbers
            if "Agenda Item" not in line and "Page" not in line and "Public Works" not in line:
                is_project_start = True
    
    if is_project_start:
        # Save previous project
        if current_project:
            projects.append(current_project)
        
        current_project = {
            "name": line,
            "section": current_section,
            "text": "",
            "st": None,
            "is_disaster": False
        }
        
        # Check if name implies disaster
        if any(x in line for x in ["FEMA", "CalOES", "CalJPIA", "Disaster"]):
            current_project["is_disaster"] = True
        
        # Check section
        if current_section == "Disaster":
            current_project["is_disaster"] = True

    elif current_project:
        current_project["text"] += line + "\n"
        # Extract fields
        # Look for "Begin Construction: <date>" or "Start: <date>"
        # In the sample: "(cid:131) Begin Construction: Fall 2023"
        # We look for "Begin Construction" line
        if "Begin Construction" in line:
            # Extract the part after colon
            parts = line.split(":")
            if len(parts) > 1:
                date_str = parts[1].strip()
                current_project["st"] = date_str
        elif "Construction Start" in line:
             parts = line.split(":")
             if len(parts) > 1:
                date_str = parts[1].strip()
                current_project["st"] = date_str
        
        # Check for disaster keywords in text
        if "FEMA" in line or "CalOES" in line or "Disaster" in line:
             current_project["is_disaster"] = True

# Append last project
if current_project:
    projects.append(current_project)

# Filter Projects
# 1. Started in 2022
# 2. Disaster related

target_projects = []
for p in projects:
    st = p.get("st", "")
    if st and "2022" in st:
        if p["is_disaster"]:
            target_projects.append(p)

# Now Sum Funding
# We need to match target_projects names with Funding table Project_Name
total_funding = 0
matched_funding_ids = set()

# Normalize target names
target_names = [normalize(p["name"]) for p in target_projects]

print(f"DEBUG: Found {len(target_projects)} target projects.")
for p in target_projects:
    print(f"DEBUG: Project: {p['name']}, Start: {p['st']}")

for record in funding_data:
    f_name = normalize(record["Project_Name"])
    f_amount = float(record["Amount"])
    
    # Check if this funding record matches any target project
    # Direct match or partial match?
    # The Description says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents"
    # So we should expect exact or close match.
    # However, Funding table has "Project (FEMA)" variants.
    # If the text project "Project" is disaster and started in 2022, do we count "Project" and "Project (FEMA)"?
    # Yes, all funding for that project.
    
    # Check if f_name is in target_names
    # OR if f_name contains one of the target names (e.g. "Project (FEMA)" contains "Project")
    # OR if one of the target names contains f_name
    
    match = False
    for t_name in target_names:
        # Check exact match
        if f_name == t_name:
            match = True
            break
        # Check if funding name is a variant of text name (e.g. text="X", funding="X (FEMA)")
        if t_name in f_name: 
            match = True
            break
        # Check if text name is a variant of funding name (unlikely but possible)
        if f_name in t_name:
            match = True
            break
            
    if match:
        if record["Funding_ID"] not in matched_funding_ids:
            total_funding += f_amount
            matched_funding_ids.add(record["Funding_ID"])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects_found": [p["name"] for p in target_projects]}))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json'}

exec(code, env_args)
