code = """import json, pandas as pd

funding_path = locals()['var_functions.query_db:4']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

completed_park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            for j in range(i-1, max(0, i-6), -1):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) > 10 and not prev_line.startswith('('):
                    if any(keyword in prev_line.lower() for keyword in ['park', 'playground', 'bluff']):
                        completed_park_projects.append(prev_line)
                        break

completed_park_projects = list(set(completed_park_projects))

total_funding = 0
for project in completed_park_projects:
    for _, row in df_funding.iterrows():
        if project.lower() in row['Project_Name'].lower() or row['Project_Name'].lower() in project.lower():
            total_funding += row['Amount']

print('__RESULT__:')
print(json.dumps({'projects': completed_park_projects, 'total_funding': total_funding, 'count': len(completed_park_projects)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
