code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

park_projects_info = []

project_section_pattern = re.compile(
    r'(?m)^([A-Z][a-zA-Z0-9&\\s\\-]+(?:Park|Playground|Project)?(?: \\(FEMA Project\\))?)\n'  # Project Name
    r'((?:(?!^[A-Z][a-zA-Z0-9&\\s\\-]+(?:Park|Playground|Project)?(?: \\(FEMA Project\\))?).)*)', # Details block
    re.DOTALL
)

for doc in civic_docs:
    text = doc['text']
    for project_name_raw, details_raw in project_section_pattern.findall(text):
        project_name = project_name_raw.strip()
        details = details_raw.strip()

        if 'Park' in project_name or 'Playground' in project_name:
            park_projects_info.append({'Project_Name': project_name, 'Details': details})

completed_park_projects_2022 = []

for project in park_projects_info:
    details = project['Details']
    # Check for keywords indicating completion and the year 2022
    if re.search(r'completed', details, re.IGNORECASE) and re.search(r'2022', details):
        # Refine the 2022 check to ensure it's related to completion/end date
        if re.search(r'(?:completed|Complete Construction|Complete Design|November|December).*?2022', details, re.IGNORECASE):
            completed_park_projects_2022.append(project['Project_Name'])

unique_completed_park_projects_2022 = list(set(completed_park_projects_2022))

print("__RESULT__:")
print(json.dumps(unique_completed_park_projects_2022)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test']}

exec(code, env_args)
