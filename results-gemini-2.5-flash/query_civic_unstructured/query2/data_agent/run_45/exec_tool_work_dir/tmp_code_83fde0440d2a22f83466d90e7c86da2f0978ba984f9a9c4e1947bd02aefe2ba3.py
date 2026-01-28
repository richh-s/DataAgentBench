code = """import re
import json

data_file_path = locals()['var_function-call-4710652390132813931']

with open(data_file_path, 'r') as f:
    data = json.load(f)

park_projects_completed_2022 = []

for doc in data:
    text = doc['text']

    # Pattern to capture project name and completion date within Project Schedule
    # Escaping parentheses for (cid:190) and (cid:131)
    pattern1 = r"([A-Za-z0-9][A-Za-z0-9 -&#/]+?)\\n\\n\\(cid:190\\) Updates:[^\\n]*\\n(?:\\(cid:131\\)[^\\n]*\\n)*\\(cid:190\\) Project Schedule:[^\\n]*\\n(?:\\(cid:131\\)[^\\n]*\\n)*\\(cid:131\\) Complete Construction: ([A-Za-z0-9 -]+?2022)"

    matches1 = re.findall(pattern1, text)
    for project_name, completion_date in matches1:
        park_projects_completed_2022.append({"Project_Name": project_name.strip(), "et": completion_date.strip()})

    # Pattern for projects like "Bluffs Park Shade Structure\n(cid:190) Updates: Construction was completed November 2022."
    pattern2 = r"([A-Za-z0-9][A-Za-z0-9 -&#/]+?)\\n\\(cid:190\\) Updates: Construction was completed ([A-Za-z0-9 -]+?2022)"
    matches2 = re.findall(pattern2, text)
    for project_name, completion_date in matches2:
        park_projects_completed_2022.append({"Project_Name": project_name.strip(), "et": completion_date.strip()})

# Filter for park-related projects and ensure unique names
final_park_projects = []
seen_project_names = set()

for project in park_projects_completed_2022:
    project_name = project['Project_Name'].lower()
    if any(keyword in project_name for keyword in ["park", "playground", "bluffs", "canyon park"]):
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
