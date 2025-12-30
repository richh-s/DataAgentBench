code = """import json
import re

def parse_project_info(text):
    projects = []
    current_status_type = None
    
    # Regex to find project sections and statuses
    status_type_regex = re.compile(r"Capital Improvement Projects \((Design|Construction|Not Started)\)|Disaster Recovery Projects")
    project_name_regex = re.compile(r"\n\n([A-Za-z0-9][A-Za-z0-9\s&,-/]+?)(?=\n\n\(cid:190\) Updates:|\n\n\(cid:190\) Project Description:|\n\n\(cid:190\) Project Schedule:|\n\n\(cid:190\) Estimated Schedule:|\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects)")
    
    # Iterate through the text to find projects and their statuses
    for line in text.split('\n'):
        status_type_match = status_type_regex.search(line)
        if status_type_match:
            if "Capital Improvement Projects" in line:
                current_status_type = status_type_match.group(1).strip() if status_type_match.group(1) else None
                if current_status_type: # Normalize status for capital projects
                    if current_status_type == "Design":
                        current_status = "design"
                    elif current_status_type == "Construction":
                        current_status = "under construction"
                    elif current_status_type == "Not Started":
                        current_status = "not started"
                    project_type = "capital"
                else:
                    current_status = None
                    project_type = None
            elif "Disaster Recovery Projects" in line:
                current_status = "disaster recovery"
                project_type = "disaster"
            continue

        project_name_match = project_name_regex.search(line)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            project_topic = []
            if re.search(r"emergency", line, re.IGNORECASE) or re.search(r"FEMA", line, re.IGNORECASE):
                if re.search(r"emergency", line, re.IGNORECASE):
                    project_topic.append("emergency")
                if re.search(r"FEMA", line, re.IGNORECASE):
                    project_topic.append("FEMA")
            
            # If project name found and a status type has been established
            if project_name and current_status and project_type:
                projects.append({
                    "Project_Name": project_name,
                    "status": current_status,
                    "type": project_type,
                    "topic": ", ".join(project_topic) if project_topic else None
                })
    return projects


all_projects = []
with open(locals()['var_function-call-5052213206219168496'], 'r') as f:
    docs = json.load(f)

for doc in docs:
    all_projects.extend(parse_project_info(doc['text']))

# Filter projects to only include those with "emergency" or "FEMA" in their topic or if the text contains these keywords
# This step is mostly redundant because the initial query already filtered documents, 
# but ensures that only relevant projects from those documents are included.
filtered_projects = [p for p in all_projects if p.get("topic") and ("emergency" in p["topic"] or "FEMA" in p["topic"])]

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in filtered_projects:
    if project["Project_Name"] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project["Project_Name"])


print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-5052213206219168496': 'file_storage/function-call-5052213206219168496.json'}

exec(code, env_args)
