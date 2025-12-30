code = """import json
import re

def extract_project_info_robust(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    # Check if the document as a whole implies a disaster context
    global_disaster_context = "Disaster Recovery Projects" in text

    for i, line in enumerate(lines):
        line = line.strip()
        
        # Attempt to identify a project name, which typically ends with 'Project'
        # and is often followed by '(cid:190) Updates:' or similar structure.
        project_name_match = re.match(r'^(.*?Project)(\s+\(.*?\))?$', line)
        
        if project_name_match:
            if current_project and current_project["Project_Name"] is not None: # Finalize previous project
                projects.append(current_project)
            
            project_name = project_name_match.group(1).strip()
            current_project = {
                "Project_Name": project_name,
                "type": "capital",
                "st": None
            }
            # Check if project name itself indicates disaster
            if "(FEMA Project)" in project_name or "(CalJPIA Project)" in project_name or "(CalOES Project)" in project_name:
                current_project["type"] = "disaster"
            
            continue

        if current_project:
            # Look for project type indicators within the project's detail lines
            if current_project["type"] == "capital" and ("FEMA" in line or "CalOES" in line):
                current_project["type"] = "disaster"

            # Look for Project Schedule and then start time
            if "(cid:190) Project Schedule:" in line:
                # Scan next few lines for 'Begin Construction:' or 'Advertise:' or a year/season
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

    # Apply global disaster context if not specifically identified
    for project in projects:
        if project["type"] == "capital" and global_disaster_context:
            project["type"] = "disaster"

    return projects

file_path = locals()['var_function-call-6524522302801542169']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data:
    projects_in_doc = extract_project_info_robust(doc['text'])
    all_projects.extend(projects_in_doc)

disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022.append(project)

unique_project_names = list(set([project['Project_Name'] for project in disaster_projects_2022]))

# Filter out names that are too short or seem like generic headings
unique_project_names = [name for name in unique_project_names if len(name) > 10 and not name.isupper()]

print("__RESULT__:")
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json'}

exec(code, env_args)
