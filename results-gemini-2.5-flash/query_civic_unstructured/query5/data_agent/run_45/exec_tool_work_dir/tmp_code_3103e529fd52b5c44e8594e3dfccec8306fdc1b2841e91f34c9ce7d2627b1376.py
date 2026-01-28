code = """import json
import re

with open(locals()['var_function-call-9214184878544642466'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    lines = text.split('\n')
    current_project_type = None
    current_project_name = None
    
    for line in lines:
        line = line.strip()
        
        if "Capital Improvement Projects" in line:
            current_project_type = "capital"
            current_project_name = None # Reset project name when new section starts
            continue
        elif "Disaster Recovery Projects" in line:
            current_project_type = "disaster"
            current_project_name = None # Reset project name when new section starts
            continue
            
        # Try to identify a project name if we are in a project section
        # A project name is often a line that starts with a capital letter and isn't a keyword/header
        if current_project_type and line and not line.startswith(("(", "Page", "Agenda Item", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:", "Updates:", "Project Schedule:", "Estimated Schedule:", "Project Description:", "Public Works Commission", "Item")):
            # Heuristic: If the line contains 'Project' but not 'Capital' or 'Disaster', it might be a project name.
            # Or, if it looks like a title and is followed by project details (cid:190)
            if re.match(r'^[A-Z][a-zA-Z0-9_ -]+$', line) or (re.search(r'Project', line) and "Capital" not in line and "Disaster" not in line):
                current_project_name = line
                continue

        # If a project name is identified, look for its start date
        if current_project_name and "Begin Construction:" in line:
            start_date_match = re.search(r'Begin Construction: (.*?)$', line)
            if start_date_match:
                start_date = start_date_match.group(1).strip()
                projects_data.append({
                    "Project_Name": current_project_name,
                    "type": current_project_type,
                    "st": start_date
                })
                current_project_name = None # Reset after finding its schedule to avoid false positives

# Filter for disaster projects that started in 2022
disaster_projects_2022 = [
    p for p in projects_data 
    if p["type"] == "disaster" and p["st"] and "2022" in p["st"]
]

# Extract project names for the next step
project_names_2022_disaster = [p["Project_Name"] for p in disaster_projects_2022]

print("__RESULT__:")
print(json.dumps(project_names_2022_disaster))"""

env_args = {'var_function-call-9214184878544642466': 'file_storage/function-call-9214184878544642466.json'}

exec(code, env_args)
