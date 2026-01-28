code = """import json
import re

# Load data
funding_data = json.load(open('var_function-call-2978529979761584874.json'))
civic_docs = json.load(open('var_function-call-18353548758763023349.json'))

# Combine text from all documents
full_text = "\n".join([doc['text'] for doc in civic_docs])

# Regex to find project blocks
# Pattern: Project Name (end of line) -> followed by (cid:190) lines
# We will iterate line by line to be more robust

lines = full_text.split('\n')
projects = []
current_project = {}
capture_mode = False

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue

    # Heuristic: A line is a project name if the NEXT line starts with (cid:190) or similar marker 
    # The markers in the preview look like "(cid:190)" or just "Updates:" if the char is lost.
    # In the preview string: "(cid:190)" appears.
    
    # Check if next line starts with marker
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
        current_project["text_block"] += line + "\n"

# Add the last project
if current_project:
    projects.append(current_project)

# Analyze extracted projects
park_projects_2022 = []

for p in projects:
    text = p["text_block"].lower()
    name = p["name"]
    
    # Check if park related
    # Keywords: "park", "playground"
    is_park = "park" in name.lower() or "park" in text or "playground" in name.lower() or "playground" in text
    
    if not is_park:
        continue
        
    # Check status and date
    # Look for "completed" and "2022"
    # Patterns: "Construction was completed November 2022", "Complete Construction: April 2023"
    
    completed_in_2022 = False
    
    # Regex for completion
    # Matches "completed <date>" or "complete construction: <date>"
    completion_patterns = [
        r"completed\W+([a-zA-Z]+\W+2022)",
        r"complete construction:?\W+([a-zA-Z]+\W+2022)",
        r"completion.*2022"
    ]
    
    for pat in completion_patterns:
        if re.search(pat, text):
            completed_in_2022 = True
            break
            
    if completed_in_2022:
        park_projects_2022.append(name)

# Join with funding
total_funding = 0
matched_projects = []

for proj_name in park_projects_2022:
    # Find matching funding record
    # normalize names for comparison
    # exact match might fail due to whitespace or casing
    
    # Strategy: Check if Funding Project_Name is in Extracted Name or vice versa
    # The hint says "The Project_Name in the Funding SQLite table matches the project names that can be extracted"
    # So we should try exact match or close match.
    
    # Let's clean the extracted name first
    clean_extracted_name = proj_name.strip()
    
    found = False
    for fund in funding_data:
        fund_name = fund['Project_Name'].strip()
        
        # Try direct match or containment
        if fund_name.lower() == clean_extracted_name.lower():
            total_funding += int(fund['Amount'])
            matched_projects.append({'name': fund_name, 'amount': fund['Amount']})
            found = True
            break
            
    if not found:
        # Try to match if the funding name is contained in the extracted line (which might have extra chars)
        # or vice versa
        pass 
        # For now, let's see what we get with exact/stripped match.

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects, "extracted_park_projects": park_projects_2022}))"""

env_args = {'var_function-call-2978529979761584874': 'file_storage/function-call-2978529979761584874.json', 'var_function-call-18353548758763023349': 'file_storage/function-call-18353548758763023349.json'}

exec(code, env_args)
