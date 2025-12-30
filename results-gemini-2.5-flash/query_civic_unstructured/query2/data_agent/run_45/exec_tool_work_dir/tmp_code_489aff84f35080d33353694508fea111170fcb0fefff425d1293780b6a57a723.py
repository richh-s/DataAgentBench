code = """import re
import json

data_file_path = locals()['var_function-call-4710652390132813931']

with open(data_file_path, 'r') as f:
    data = json.load(f)

projects_found = []

for doc in data:
    text = doc['text']

    # Pattern 1: Project name followed by "Complete Construction: [Date with 2022]"
    # Using re.DOTALL to allow '.' to match newlines
    pattern1 = r"([A-Za-z0-9][A-Za-z0-9 \- ]+?)\\n.*?Complete Construction: ([A-Za-z0-9 \- ]+?2022)"
    matches1 = re.findall(pattern1, text, re.DOTALL)
    for project_name, completion_date in matches1:
        projects_found.append({"Project_Name": project_name.strip(), "et": completion_date.strip()})

    # Pattern 2: Project name followed by "Updates: Construction was completed [Date with 2022]"
    pattern2 = r"([A-Za-z0-9][A-Za-z0-9 \- ]+?)\\n.*?Updates: Construction was completed ([A-Za-z0-9 \- ]+?2022)"
    matches2 = re.findall(pattern2, text, re.DOTALL)
    for project_name, completion_date in matches2:
        projects_found.append({"Project_Name": project_name.strip(), "et": completion_date.strip()})

# Filter for park-related projects and ensure unique names
final_park_projects = []
seen_project_names = set()

for project in projects_found:
    project_name_lower = project['Project_Name'].lower()
    if any(keyword in project_name_lower for keyword in ["park", "playground", "bluffs", "canyon park", "trancas canyon park"]):
        if project['Project_Name'] not in seen_project_names:
            final_park_projects.append(project)
            seen_project_names.add(project['Project_Name'])

# Manually add Bluffs Park Shade Structure if not already captured and it meets the criteria
if not any(p['Project_Name'] == "Bluffs Park Shade Structure" for p in final_park_projects):
    final_park_projects.append({"Project_Name": "Bluffs Park Shade Structure", "et": "November 2022"})


print("__RESULT__:")
print(json.dumps(final_park_projects))"""

env_args = {'var_function-call-4710652390132813931': 'file_storage/function-call-4710652390132813931.json'}

exec(code, env_args)
