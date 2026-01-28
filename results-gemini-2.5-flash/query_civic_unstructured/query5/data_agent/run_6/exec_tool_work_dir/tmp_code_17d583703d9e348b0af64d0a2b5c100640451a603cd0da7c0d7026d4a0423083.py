code = """import json
import re

def extract_project_info_simplified_parse(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    global_disaster_context = "Disaster Recovery Projects" in text

    for i, line in enumerate(lines):
        line = line.strip()

        if "Project" in line and len(line) > 10 and not line.isupper() and "(cid:190)" not in line:
            if current_project and current_project["Project_Name"] is not None: # Finalize previous project
                projects.append(current_project)
            
            project_name = line # Take the entire line as the project name for now
            current_project = {
                "Project_Name": project_name,
                "type": "capital",
                "st": None
            }
            if "FEMA Project" in project_name or "CalJPIA Project" in project_name or "CalOES Project" in project_name:
                current_project["type"] = "disaster"
            continue

        if current_project:
            if current_project["type"] == "capital" and ("FEMA" in line or "CalOES" in line or "Disaster Recovery" in line):
                current_project["type"] = "disaster"

            if "(cid:190) Project Schedule:" in line:
                for j in range(i + 1, min(i + 5, len(lines))):
                    schedule_detail_line = lines[j].strip()
                    
                    begin_construction_match = re.search(r'Begin Construction:\s*([^\n]+)', schedule_detail_line)
                    if begin_construction_match:
                        current_project["st"] = begin_construction_match.group(1).strip()
                        break
                    
                    advertise_match = re.search(r'Advertise:\s*([^\n]+)', schedule_detail_line)
                    if advertise_match:
                        current_project["st"] = advertise_match.group(1).strip()
                        break
                    
                    date_match = re.search(r'\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b', schedule_detail_line)
                    if date_match:
                        current_project["st"] = date_match.group(0).strip()
                        break
    
    if current_project and current_project["Project_Name"] is not None: # Add the last project
        projects.append(current_project)

    for project in projects:
        if project["type"] == "capital" and global_disaster_context:
            project["type"] = "disaster"

    return projects

file_path = locals()['var_function-call-6524522302801542169']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data:
    projects_in_doc = extract_project_info_simplified_parse(doc['text'])
    all_projects.extend(projects_in_doc)

disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022.append(project)

unique_project_names = list(set([project['Project_Name'] for project in disaster_projects_2022]))

unique_project_names = [name for name in unique_project_names if len(name) > 10 and not name.isupper() and "Agenda Item" not in name]

print("__RESULT__:")
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json', 'var_function-call-17434838567716078401': ['Funding'], 'var_function-call-7943208518371631309': 'file_storage/function-call-7943208518371631309.json'}

exec(code, env_args)
