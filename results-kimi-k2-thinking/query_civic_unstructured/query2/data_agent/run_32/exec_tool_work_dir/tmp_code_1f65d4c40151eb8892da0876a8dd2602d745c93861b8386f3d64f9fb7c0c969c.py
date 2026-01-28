code = """import json, pandas as pd
f_path = locals()['var_functions.query_db:4']
c_path = locals()['var_functions.query_db:5']

with open(f_path, 'r') as f:
    funding_data = json.load(f)
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

completed_park_projects_2022 = set()
for doc in civic_docs:
    txt = doc.get('text', '')
    parts = txt.splitlines()
    for i in range(len(parts)):
        cur = parts[i].strip()
        if '2022' in cur and ('completed' in cur.lower() or 'completion' in cur.lower()):
            for j in range(i-1, -1, -1):
                prev = parts[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('('):
                    low = prev.lower()
                    if any(x in low for x in ['project schedule', 'updates:', 'to:', 'from:', 'subject:']):
                        continue
                    if 'park' in low or 'playground' in low or 'bluff' in low:
                        completed_park_projects_2022.add(prev)
                        break

project_names = list(completed_park_projects_2022)
funding_total = 0
for proj in project_names:
    proj_lower = proj.lower()
    for _, row in funding_df.iterrows():
        funding_lower = row['Project_Name'].lower()
        if proj_lower in funding_lower or funding_lower in proj_lower:
            funding_total += row['Amount']

result = {'total_funding': int(funding_total)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
