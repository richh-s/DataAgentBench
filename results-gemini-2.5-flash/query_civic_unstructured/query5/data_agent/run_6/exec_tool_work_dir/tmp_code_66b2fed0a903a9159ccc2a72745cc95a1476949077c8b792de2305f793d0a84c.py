code = """import json
import re

def extract_project_info(text):
    projects = []
    # Regex to find project blocks
    project_blocks = re.findall(r"([A-Za-z0-9][A-Za-z0-9\s&,-_]+Project)(?:\n|\s)*?\(cid:190) Updates:([^\n]*(?:\n(?!\(cid:190) Project Schedule:)[^\n]*)*)(?:\n|\s)*?\(cid:190) Project Schedule:([^\n]*(?:\n(?!\(cid:190) Updates:)[^\n]*)*)", text)
    
    for name, updates, schedule_info in project_blocks:
        project_name = name.strip()
        project_type = "capital" # Default type
        if "Disaster Recovery Projects" in text or "FEMA" in updates or "CalOES" in updates or "(FEMA Project)" in project_name or "(CalJPIA Project)" in project_name or "(CalOES Project)" in project_name:
            project_type = "disaster"
        
        start_time = None
        if "Begin Construction: " in schedule_info:
            start_time_match = re.search(r"Begin Construction:\s*([^\n]+)", schedule_info)
            if start_time_match:
                start_time = start_time_match.group(1).strip()
        elif "Advertise: " in schedule_info:
            advertise_time_match = re.search(r"Advertise:\s*([^\n]+)", schedule_info)
            if advertise_time_match:
                # If construction start is not available, consider advertise date as a proxy for project start
                start_time = advertise_time_match.group(1).strip()
        elif "Project Schedule:" in schedule_info:
            # Try to find a date within the schedule_info as a fallback
            date_match = re.search(r"\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b", schedule_info)
            if date_match:
                start_time = date_match.group(0)

        projects.append({
            "Project_Name": project_name,
            "type": project_type,
            "st": start_time
        })

    return projects


file_path = locals()['var_function-call-6524522295671191307']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data:
    projects_in_doc = extract_project_info(doc['text'])
    all_projects.extend(projects_in_doc)


# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)


project_names = [project['Project_Name'] for project in disaster_projects_2022]

# Remove duplicates from project_names
unique_project_names = list(set(project_names))

print("__RESULT__:")
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json'}

exec(code, env_args)
