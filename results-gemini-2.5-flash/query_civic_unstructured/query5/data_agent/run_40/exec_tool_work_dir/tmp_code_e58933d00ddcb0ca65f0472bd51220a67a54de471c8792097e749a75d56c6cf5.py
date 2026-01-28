code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022 = []

for doc in documents:
    text = doc['text']
    # Regex to find project names, types, and start dates
    # This regex looks for "type: disaster" and then "st: 2022" within the project description
    # It also tries to capture the project name before the type/start date information.
    matches = re.findall(r'(.*?)\n\s+\(cid:190\)\s+Updates:.*?\n\s+\(cid:190\)\s+Project Schedule:.*?type:\s*(disaster).*?st:\s*(2022.*?)\n', text, re.DOTALL)
    for match in matches:
        project_name = match[0].strip()
        start_date = match[2].strip()

        # More robust check for "2022" in the start date, considering various formats
        if "2022" in start_date:
            disaster_projects_2022.append(project_name)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json'}

exec(code, env_args)
