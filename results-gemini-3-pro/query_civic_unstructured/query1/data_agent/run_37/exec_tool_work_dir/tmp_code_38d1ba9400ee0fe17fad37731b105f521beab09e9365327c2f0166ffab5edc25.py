code = """import json

# Load Funding Data
with open('var_function-call-2838577088197188033.json', 'r') as f:
    funding_data = json.load(f)

# Create a set of high-funding project names for easy lookup
# Normalize by stripping whitespace and maybe lowercasing for comparison
high_funding_projects = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    high_funding_projects[name.lower()] = name

# Load Civic Docs Data
with open('var_function-call-11182446621266237343.json', 'r') as f:
    civic_docs = json.load(f)

doc_text = civic_docs[0]['text']

# Parse the text
lines = doc_text.split('\n')
design_projects = []
in_design_section = False
in_construction_section = False

# We want lines that look like project names under "Capital Improvement Projects (Design)"
# We stop at "Capital Improvement Projects (Construction)"

# Possible headers
design_header = "Capital Improvement Projects (Design)"
construction_header = "Capital Improvement Projects (Construction)"
not_started_header = "Capital Improvement Projects (Not Started)"
disaster_header = "Disaster Recovery Projects" # Just in case

project_names_extracted = []

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
        
    if design_header in line:
        in_design_section = True
        continue
    
    if construction_header in line or not_started_header in line or disaster_header in line:
        if in_design_section:
            in_design_section = False
            break
            
    if in_design_section:
        # Heuristic to identify project name:
        # 1. Not a bullet point (starts with (cid:) or similar garbage)
        # 2. Not "Updates:", "Project Schedule:", "Page x of y", "Agenda Item"
        # 3. Next meaningful line starts with a marker like (cid: or Updates
        
        if line.startswith("(cid:") or line.startswith("Updates:") or line.startswith("Project Schedule:") or \
           line.startswith("Page ") or line.startswith("Agenda Item") or line.lower().startswith("prepared by") or \
           line.lower().startswith("approved by") or line.lower().startswith("date prepared"):
            continue
            
        # Check if it's a date or unrelated text
        if "Complete Design" in line or "Advertise" in line or "Begin Construction" in line:
            continue
            
        # Likely a project name
        # Verify by looking ahead? 
        # For now, just append and we filter later
        project_names_extracted.append(line)

# Now match with funding data
matched_projects = []
unmatched_projects = []

for proj in project_names_extracted:
    proj_norm = proj.lower()
    found = False
    
    # Try exact match
    if proj_norm in high_funding_projects:
        matched_projects.append(high_funding_projects[proj_norm])
        found = True
    else:
        # Try fuzzy match
        # Check if one contains the other
        for db_proj_lower, db_proj_original in high_funding_projects.items():
            if db_proj_lower in proj_norm or proj_norm in db_proj_lower:
                matched_projects.append(db_proj_original)
                found = True
                break
                
    if not found:
        unmatched_projects.append(proj)

# Remove duplicates in matched_projects (in case multiple extracted lines map to same DB entry? Unlikely but safe)
matched_projects = list(set(matched_projects))

print("__RESULT__:")
print(json.dumps({
    "count": len(matched_projects),
    "matches": matched_projects,
    "unmatched": unmatched_projects,
    "extracted": project_names_extracted
}))"""

env_args = {'var_function-call-2838577088197188033': 'file_storage/function-call-2838577088197188033.json', 'var_function-call-2838577088197188526': 'file_storage/function-call-2838577088197188526.json', 'var_function-call-7878716980368608955': ['civic_docs'], 'var_function-call-11182446621266237343': 'file_storage/function-call-11182446621266237343.json'}

exec(code, env_args)
