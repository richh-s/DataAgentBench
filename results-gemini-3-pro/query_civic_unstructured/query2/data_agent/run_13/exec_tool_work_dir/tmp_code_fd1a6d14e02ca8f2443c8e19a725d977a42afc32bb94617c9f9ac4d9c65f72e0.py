code = """import json
import re

# Get file paths from variables
funding_path = locals()['var_function-call-2978529979761584874']
civic_path = locals()['var_function-call-18353548758763023349']

# Load data
funding_data = json.load(open(funding_path))
civic_docs = json.load(open(civic_path))

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

    is_project_header = False
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
            is_project_header = True
    
    if is_project_header:
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
        
    # Check completed in 2022
    completed_in_2022 = False
    if re.search(r"completed.*2022", text) or re.search(r"completion.*2022", text):
        completed_in_2022 = True
            
    if completed_in_2022:
        park_projects_2022.append(name)

# Join with funding
total_funding = 0
matched_projects = []

# Create a set of already matched funding IDs to avoid double counting if fuzzy matching overlaps
matched_funding_ids = set()

for proj_name in park_projects_2022:
    clean_extracted_name = proj_name.strip()
    
    found = False
    # Exact match first
    for fund in funding_data:
        if fund['Funding_ID'] in matched_funding_ids:
            continue
            
        fund_name = fund['Project_Name'].strip()
        if fund_name.lower() == clean_extracted_name.lower():
            total_funding += int(fund['Amount'])
            matched_projects.append({'name': fund_name, 'amount': fund['Amount']})
            matched_funding_ids.add(fund['Funding_ID'])
            found = True
            break
            
    if not found:
        # Fuzzy match
        for fund in funding_data:
            if fund['Funding_ID'] in matched_funding_ids:
                continue
                
            fund_name = fund['Project_Name'].strip()
            # If fund name is a substring of extracted name or vice versa
            # Ensure length is sufficient to avoid accidental matches
            if (fund_name.lower() in clean_extracted_name.lower() and len(fund_name) > 10) or \
               (clean_extracted_name.lower() in fund_name.lower() and len(clean_extracted_name) > 10):
                total_funding += int(fund['Amount'])
                matched_projects.append({'name': fund_name, 'amount': fund['Amount'], 'match_type': 'fuzzy'})
                matched_funding_ids.add(fund['Funding_ID'])
                found = True # One match per extracted project? 
                # Actually a project might have multiple funding sources/records?
                # The Funding table has Project_Name. It's possible there are multiple records for one project.
                # But usually Funding_ID is unique.
                # The logic above stops after first match per extracted project.
                # If a project has multiple funding records, we should sum all of them.
                # Let's adjust: Find ALL funding records matching the project name.
                break 

# Refined matching logic: Iterate over unique extracted projects, find ALL matching funding records.
# Reset totals
total_funding = 0
matched_projects = []
matched_funding_ids = set()

unique_park_projects = set(park_projects_2022)

for proj_name in unique_park_projects:
    clean_extracted_name = proj_name.strip()
    
    # Find all matching funding records
    for fund in funding_data:
        if fund['Funding_ID'] in matched_funding_ids:
            continue
            
        fund_name = fund['Project_Name'].strip()
        
        match = False
        if fund_name.lower() == clean_extracted_name.lower():
            match = True
        elif (fund_name.lower() in clean_extracted_name.lower() and len(fund_name) > 10) or \
             (clean_extracted_name.lower() in fund_name.lower() and len(clean_extracted_name) > 10):
            match = True
            
        if match:
            total_funding += int(fund['Amount'])
            matched_projects.append({'name': fund_name, 'amount': fund['Amount'], 'extracted_name': clean_extracted_name})
            matched_funding_ids.add(fund['Funding_ID'])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects, "extracted_park_projects": list(unique_park_projects)}))"""

env_args = {'var_function-call-2978529979761584874': 'file_storage/function-call-2978529979761584874.json', 'var_function-call-18353548758763023349': 'file_storage/function-call-18353548758763023349.json'}

exec(code, env_args)
