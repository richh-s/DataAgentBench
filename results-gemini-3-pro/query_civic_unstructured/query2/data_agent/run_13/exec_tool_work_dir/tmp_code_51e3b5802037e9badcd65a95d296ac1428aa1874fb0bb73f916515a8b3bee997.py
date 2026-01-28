code = """import json
import re

# Get file paths from variables
funding_path = locals()['var_function-call-2978529979761584874']
civic_path = locals()['var_function-call-18353548758763023349']

# Load data
funding_data = json.load(open(funding_path))
civic_docs = json.load(open(civic_path))

# Combine text from all documents
# Use chr(10) for newline to avoid escaping hell
newline = chr(10)
full_text = newline.join([doc['text'] for doc in civic_docs])

# Split lines
lines = [line.strip() for line in full_text.split(newline) if line.strip()]

projects = []
current_project = {}

for i, line in enumerate(lines):
    # Check if this line is a marker
    if line.startswith("(cid:190)") or line.startswith("Updates:") or line.startswith("Project Description:"):
        # Then the PREVIOUS line was likely the project name
        # We need to find the previous non-marker line that hasn't been used?
        # Actually, simpler: Iterate. If we hit a marker, the previous line `lines[i-1]` is the name.
        # But we must ensure `lines[i-1]` is not a marker itself.
        
        if i > 0:
            potential_name = lines[i-1]
            # Verify potential name is not a marker and not part of previous block
            if not (potential_name.startswith("(cid:190)") or potential_name.startswith("Updates:") or potential_name.startswith("Project Description:")):
                # This is a new project header.
                # Save previous project
                if current_project and current_project.get('name') != potential_name:
                    projects.append(current_project)
                    current_project = {}
                
                if not current_project:
                    current_project = {
                        "name": potential_name,
                        "text_block": ""
                    }
    
    # Add content to current project
    if current_project:
        current_project["text_block"] += line + newline

if current_project:
    projects.append(current_project)

# Analyze extracted projects
park_projects_2022 = []

for p in projects:
    text = p["text_block"].lower()
    name = p["name"]
    
    # Check if park related
    # "park" or "playground" or "recreation" or "green space"
    is_park = "park" in name.lower() or "park" in text or "playground" in name.lower() or "playground" in text
    
    if not is_park:
        continue
        
    # Check completed in 2022
    # Patterns to catch: "completed November 2022", "completed, November 2022", "complete construction: ... 2022"
    # Also "Status: Completed" and date in 2022? (The text doesn't seem to have structured fields)
    
    completed_in_2022 = False
    
    # Regex designed to be flexible
    # Look for "completed" ... "2022" within a reasonable distance (e.g. same line or sentence)
    # or specific phrases
    
    if re.search(r"completed.{0,50}2022", text) or \
       re.search(r"complete construction.{0,50}2022", text):
        completed_in_2022 = True
            
    if completed_in_2022:
        park_projects_2022.append(name)

# Deduplicate names
unique_park_projects = list(set(park_projects_2022))

# Join with funding
total_funding = 0
matched_projects = []
matched_funding_ids = set()

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
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects, "extracted_park_projects": unique_park_projects}))"""

env_args = {'var_function-call-2978529979761584874': 'file_storage/function-call-2978529979761584874.json', 'var_function-call-18353548758763023349': 'file_storage/function-call-18353548758763023349.json', 'var_function-call-17154176344544213090': {'total_funding': 214000, 'matched_projects': [{'name': 'Marie Canyon Green Streets', 'amount': '50000', 'extracted_name': 'Marie Canyon Green Streets'}, {'name': 'Birdview Avenue Improvements', 'amount': '79000', 'extracted_name': 'Birdview Avenue Improvements (CalOES Project)'}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'amount': '85000', 'extracted_name': 'Birdview Avenue Improvements (CalOES Project)'}], 'extracted_park_projects': ['Marie Canyon Green Streets', 'Metro.', 'Birdview Avenue Improvements (CalOES Project)', '(cid:190) Updates: Project is currently under construction']}}

exec(code, env_args)
