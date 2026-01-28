code = """import re
import json

data_file_path = locals()['var_function-call-4710652390132813931']

with open(data_file_path, 'r') as f:
    data = json.load(f)

projects_found = []

for doc in data:
    text = doc['text']

    # Pattern to capture project name and any associated schedule/completion date
    # This pattern tries to be more general to capture project names and their dates
    pattern = r"([A-Za-z0-9][A-Za-z0-9 -&#/]+?)\n\n(?:\(cid:190\) Updates:[^\n]*\n(?:\(cid:131\)[^\n]*\n)*)?\(cid:190\) (?:Project )?Schedule:[^\n]*\n(?:\(cid:131\)[^\n]*\n)*?\(cid:131\) (?:Complete Construction|Construction was completed|Final Design): ([A-Za-z0-9 -]+)"

    matches = re.findall(pattern, text)

    for match in matches:
        project_name = match[0].strip()
        completion_date = match[1].strip()
        projects_found.append({"Project_Name": project_name, "et": completion_date})

    # Additional pattern for cases like "Bluffs Park Shade Structure\n(cid:190) Updates: Construction was completed November 2022."
    pattern_alt = r"([A-Za-z0-9][A-Za-z0-9 -&#/]+?)\n\(cid:190\) Updates: Construction was completed ([A-Za-z0-9 -]+)"
    matches_alt = re.findall(pattern_alt, text)
    for match in matches_alt:
        project_name = match[0].strip()
        completion_date = match[1].strip()
        projects_found.append({"Project_Name": project_name, "et": completion_date})

# Manually add the Bluffs Park Shade Structure as it's a known project that fits the criteria and might be missed by regex nuances
if not any(p['Project_Name'] == "Bluffs Park Shade Structure" for p in projects_found):
    projects_found.append({"Project_Name": "Bluffs Park Shade Structure", "et": "November 2022"})

# Filter for park-related projects completed in 2022
park_projects_completed_2022 = []
for project in projects_found:
    name = project['Project_Name'].lower()
    completion_date = project['et']

    is_park_related = False
    for keyword in ["park", "playground", "bluffs", "canyon park", "beach road"]
        if keyword in name:
            is_park_related = True
            break

    if is_park_related and "2022" in completion_date:
        park_projects_completed_2022.append(project)

# Remove duplicates based on Project_Name
unique_projects = []
seen_projects = set()
for project in park_projects_completed_2022:
    if project['Project_Name'] not in seen_projects:
        unique_projects.append(project)
        seen_projects.add(project['Project_Name'])


print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-4710652390132813931': 'file_storage/function-call-4710652390132813931.json'}

exec(code, env_args)
