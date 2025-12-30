code = """import json
import re

def extract_project_info_line_by_line(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    # Overall text check for disaster type if not found in project block
    is_global_disaster_context = "Disaster Recovery Projects" in text

    for i, line in enumerate(lines):
        project_name_match = re.search(r'^([A-Za-z0-9][A-Za-z0-9\s&,-_]+Project)$|'
                                       r'^([A-Za-z0-9][A-Za-z0-9\s&,-_]+Project)\s+\(', line)
        if project_name_match:
            project_name = project_name_match.group(1) or project_name_match.group(2)
            current_project = {
                "Project_Name": project_name.strip(),
                "type": "capital",
                "st": None,
                "details": []  # To store relevant lines for type/schedule analysis
            }
            # Check for disaster keywords in the project name itself
            if "(FEMA Project)" in project_name or "(CalJPIA Project)" in project_name or "(CalOES Project)" in project_name:
                current_project["type"] = "disaster"
            projects.append(current_project)
            continue

        if current_project:
            current_project["details"].append(line)
            
            # Look for project type indicators in details
            if "FEMA" in line or "CalOES" in line:
                current_project["type"] = "disaster"

            # Look for schedule information
            if "(cid:190) Project Schedule:" in line:
                # Look for start time in the next few lines after schedule header
                for j in range(i + 1, min(i + 5, len(lines))):
                    schedule_line = lines[j]
                    begin_construction_match = re.search(r"Begin Construction:\s*([^\n]+)", schedule_line)
                    if begin_construction_match:
                        current_project["st"] = begin_construction_match.group(1).strip()
                        break
                    advertise_match = re.search(r"Advertise:\s*([^\n]+)", schedule_line)
                    if advertise_match:
                        current_project["st"] = advertise_match.group(1).strip()
                        break
                    date_match = re.search(r"\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b", schedule_line)
                    if date_match:
                        current_project["st"] = date_match.group(0).strip()
                        break
    
    # Final check for disaster type if not identified in project block
    for project in projects:
        if project["type"] == "capital" and is_global_disaster_context:
            project["type"] = "disaster"
        # Remove details as they are no longer needed
        del project["details"]

    return projects

file_path = locals()['var_function-call-6524522302801542169']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data:
    projects_in_doc = extract_project_info_line_by_line(doc['text'])
    all_projects.extend(projects_in_doc)

disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022.append(project)

unique_project_names = list(set([project['Project_Name'] for project in disaster_projects_2022]))

print("__RESULT__:")
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json'}

exec(code, env_args)
