code = """import re
import json

def extract_project_info(text):
    projects = []
    lines = text.split('\\n') # Split by actual newline character
    current_type = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if "Capital Improvement Projects" in line:
            if "(Design)" in line:
                current_type = "capital_design"
            elif "(Construction)" in line:
                current_type = "capital_construction"
            elif "(Not Started)" in line:
                current_type = "capital_not_started"
            else:
                current_type = "capital"
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"

        if "(cid:190) Project Schedule:" in line or "(cid:190) Estimated Schedule:" in line:
            project_name = None
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith("(cid:190)") and not re.search(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:|Agenda Item #|Page \\d of \\d)$', prev_line):
                    project_name = prev_line
                    fema_match = re.search(r'^(.*)\\s+\\((FEMA|CalJPIA|CalOES) Project\\)$', project_name)
                    if fema_match:
                        project_name = fema_match.group(1).strip()
                    break

            if project_name and current_type:
                st = ""
                k = i + 1
                while k < len(lines) and lines[k].strip().startswith("(cid:131)"):
                    schedule_line = lines[k].strip()
                    if "Begin Construction:" in schedule_line:
                        st_match = re.search(r"Begin Construction:\\s*(.*)", schedule_line)
                        if st_match:
                            st = st_match.group(1).strip()
                            break
                    elif "Complete Construction:" in schedule_line:
                        st_match = re.search(r"Complete Construction:\\s*(.*)", schedule_line)
                        if st_match and not st:
                            st = st_match.group(1).strip()
                    k += 1
                
                if re.search(r"Project is delayed", line):
                    st = "delayed"

                projects.append({
                    "Project_Name": project_name,
                    "type": current_type,
                    "st": st
                })
            i += 1
        elif "(cid:190) Updates:" in line and "Construction was completed" in line:
            project_name = None
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith("(cid:190)") and not re.search(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:|Agenda Item #|Page \\d of \\d)$', prev_line):
                    project_name = prev_line
                    fema_match = re.search(r'^(.*)\\s+\\((FEMA|CalJPIA|CalOES) Project\\)$', project_name)
                    if fema_match:
                        project_name = fema_match.group(1).strip()
                    break
            if project_name and current_type:
                st_match = re.search(r"Construction was completed, (.*)", line)
                if st_match:
                    st = st_match.group(1).strip()
                    projects.append({
                        "Project_Name": project_name,
                        "type": current_type,
                        "st": st
                    })
            i += 1
        elif "(cid:190) Updates: Project is currently under construction" in line:
            project_name = None
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith("(cid:190)") and not re.search(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:|Agenda Item #|Page \\d of \\d)$', prev_line):
                    project_name = prev_line
                    fema_match = re.search(r'^(.*)\\s+\\((FEMA|CalJPIA|CalOES) Project\\)$', project_name)
                    if fema_match:
                        project_name = fema_match.group(1).strip()
                    break
            if project_name and current_type:
                projects.append({
                    "Project_Name": project_name,
                    "type": current_type,
                    "st": "under construction"
                })
            i += 1
        else:
            i += 1
    return projects

file_path = locals()[\'var_function-call-9117459986810486534\']
with open(file_path, \'r\') as f:
    documents = json.load(f)

all_projects = []
for doc in documents[\'query_db_response\'][\'results\']:\
    all_projects.extend(extract_project_info(doc[\'text\']))

disaster_projects_2022_names = []
for project in all_projects:
    if project[\'type\'] == \'disaster\' and project[\'st\'] and \'2022\' in project[\'st\']:\
        disaster_projects_2022_names.append(project[\'Project_Name\'])

print("__RESULT__:")
print(json.dumps(list(set(disaster_projects_2022_names))))"""

env_args = {'var_function-call-9117459986810486534': 'file_storage/function-call-9117459986810486534.json'}

exec(code, env_args)
