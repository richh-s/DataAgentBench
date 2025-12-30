code = """import json
import re

# Load data
funding_data = json.load(open('var_function-call-2978529979761584874.json'))
civic_docs = json.load(open('var_function-call-18353548758763023349.json'))

# Combine text from all documents
full_text = "\\n".join([doc['text'] for doc in civic_docs])

# Regex to find project blocks
lines = full_text.split('\\n')
projects = []
current_project = {}

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue

    # Heuristic: A line is a project name if the NEXT line starts with (cid:190) or similar marker
    is_project_header = False
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
            is_project_header = True
    
    if is_project_header:
        # Save previous project if exists
        if current_project:
            projects.append(current_project)
        
        current_project = {
            "name": line,
            "text_block": ""
        }
    elif current_project:
        current_project["text_block"] += line + "\\n"

if current_project:
    projects.append(current_project)

# Analyze extracted projects
park_projects_2022 = []

for p in projects:
    text = p["text_block"].lower()
    name = p["name"]
    
    # Check if park related
    is_park = "park" in name.lower() or "park" in text or "playground" in name.lower() or "playground" in text
    
    if not is_park:
        continue
        
    # Check status and date (completed in 2022)
    # Search for completion keywords and 2022
    completed_in_2022 = False
    
    # Simple check: "completed" and "2022" in the same context?
    # Or specific phrases
    
    # Phrases found in preview: 
    # "Construction was completed November 2022"
    # "Construction was completed, November 2022"
    
    if "completed" in text and "2022" in text:
        # Be more specific to avoid false positives (e.g. started 2022, completed 2023)
        # Check if 2022 is associated with completion
        if re.search(r"completed.*2022", text) or re.search(r"completion.*2022", text):
            completed_in_2022 = True
            
    if completed_in_2022:
        park_projects_2022.append(name)

# Join with funding
total_funding = 0
matched_projects = []

for proj_name in park_projects_2022:
    clean_extracted_name = proj_name.strip()
    
    found = False
    for fund in funding_data:
        fund_name = fund['Project_Name'].strip()
        
        if fund_name.lower() == clean_extracted_name.lower():
            total_funding += int(fund['Amount'])
            matched_projects.append({'name': fund_name, 'amount': fund['Amount']})
            found = True
            break
            
    if not found:
        # Fuzzy match attempt: check if fund_name is in extracted name (sometimes extracted name has noise)
        for fund in funding_data:
            fund_name = fund['Project_Name'].strip()
            if fund_name.lower() in clean_extracted_name.lower() and len(fund_name) > 10:
                 # Check if the match is substantial
                total_funding += int(fund['Amount'])
                matched_projects.append({'name': fund_name, 'amount': fund['Amount'], 'match_type': 'fuzzy'})
                break

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects, "extracted_park_projects": park_projects_2022}))"""

env_args = {'var_function-call-2978529979761584874': 'file_storage/function-call-2978529979761584874.json', 'var_function-call-18353548758763023349': 'file_storage/function-call-18353548758763023349.json'}

exec(code, env_args)
