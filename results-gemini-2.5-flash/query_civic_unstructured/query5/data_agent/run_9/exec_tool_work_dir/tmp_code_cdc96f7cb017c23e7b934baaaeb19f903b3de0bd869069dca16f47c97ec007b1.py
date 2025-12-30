code = """import re
import json

def extract_project_info(text):
    projects = []
    lines = text.split('\n')
    current_type = None
    project_name = None

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        if "Capital Improvement Projects" in stripped_line:
            if "Disaster Recovery Projects" not in stripped_line: # Avoid misclassifying if both are on the same line
                current_type = "capital"
            else:
                current_type = "disaster" # Assume disaster takes precedence if both are there
        elif "Disaster Recovery Projects" in stripped_line:
            current_type = "disaster"
        
        # Look for project names (lines that don't start with (cid:190) and are not section headers)
        # and are followed by project details
        if current_type and not stripped_line.startswith("(cid:190)") and not re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:|Agenda Item #|Page \d of \d|Public Works Commission|Agenda Report|Item \d\.\w\.)$' ,stripped_line) and len(stripped_line) > 5:
            # Heuristic: A project name is often a non-empty line that isn't a known header/footer
            # and is followed by lines starting with (cid:190)
            if i + 1 < len(lines) and lines[i+1].strip().startswith("(cid:190)"):
                project_name = stripped_line
                # Clean up project name, removing suffixes like (FEMA Project)
                fema_match = re.search(r'^(.*)\s+\((FEMA|CalJPIA|CalOES) Project\)$', project_name)
                if fema_match:
                    project_name = fema_match.group(1).strip()
                
                st = ""
                # Look for schedule information in subsequent lines
                for j in range(i + 1, len(lines)):
                    schedule_line = lines[j].strip()
                    if not schedule_line.startswith("(cid:190)"):
                        break # Stop if we hit a new project or section
                    
                    if "Begin Construction:" in schedule_line:
                        st_match = re.search(r"Begin Construction:\s*(.*)", schedule_line)
                        if st_match:
                            st = st_match.group(1).strip()
                            break
                    elif "Complete Construction:" in schedule_line:
                        st_match = re.search(r"Complete Construction:\s*(.*)", schedule_line)
                        if st_match and not st: # Only use if no 'Begin Construction' was found
                            st = st_match.group(1).strip()
                    elif "Construction was completed," in schedule_line:
                        st_match = re.search(r"Construction was completed,\s*(.*)", schedule_line)
                        if st_match:
                            st = st_match.group(1).strip()
                            break
                    elif "Updates: Project is currently under construction" in schedule_line:
                        st = "under construction"
                        break
                
                if project_name and current_type:
                    projects.append({
                        "Project_Name": project_name,
                        "type": current_type,
                        "st": st
                    })

    return projects

file_path = locals()['var_function-call-9117459986810486534']
with open(file_path, 'r') as f:
    documents_data = json.load(f)

all_projects = []
# Access the list of documents correctly
for doc in documents_data['query_db_response']['results']:
    all_projects.extend(extract_project_info(doc['text']))

disaster_projects_2022_names = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022_names.append(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(list(set(disaster_projects_2022_names))))"""

env_args = {'var_function-call-9117459986810486534': 'file_storage/function-call-9117459986810486534.json'}

exec(code, env_args)
