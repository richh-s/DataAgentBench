code = """import json
import pandas as pd

funding_path = locals()['var_functions.query_db:4']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if line_clean and len(line_clean) > 10:
            if any(keyword in line_clean.lower() for keyword in ['park', 'playground', 'bluff']):
                current_project = line_clean
            if current_project:
                if '2022' in line_clean and ('completed' in line_clean.lower() or 'completion' in line_clean.lower()):
                    if 'construction was completed' in line_clean.lower() or 'notice of completion' in line_clean.lower():
                        park_projects.append(current_project)

park_projects = list(set(park_projects))

park_funding_total = 0
for project in park_projects:
    for _, row in df_funding.iterrows():
        funding_name = row['Project_Name'].lower()
        project_name = project.lower()
        if project_name in funding_name or funding_name in project_name:
            park_funding_total += row['Amount']

result = {
    'completed_2022_park_projects': park_projects,
    'project_count': len(park_projects),
    'total_funding': park_funding_total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
