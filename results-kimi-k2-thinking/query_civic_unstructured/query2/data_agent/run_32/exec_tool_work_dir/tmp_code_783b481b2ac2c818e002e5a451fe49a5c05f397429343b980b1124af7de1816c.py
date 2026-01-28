code = """import json, pandas as pd

funding_path = locals()['var_functions.query_db:4']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path) as f:
    funding_raw = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

df_funding = pd.DataFrame(funding_raw)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

park_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if '2022' in line and 'completed' in line.lower():
            for j in range(i-1, max(0, i-6), -1):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('('):
                    low = prev.lower()
                    if 'park' in low or 'playground' in low or 'bluff' in low:
                        if 'project schedule' not in low and 'updates:' not in low:
                            park_projects_2022.append(prev)
                            break

park_projects_2022 = list(set(park_projects_2022))

matched = []
total = 0
for p in park_projects_2022:
    for _, r in df_funding.iterrows():
        p_low, r_low = p.lower(), r['Project_Name'].lower()
        if p_low in r_low or r_low in p_low:
            total += r['Amount']
            matched.append(r['Project_Name'])

print('__RESULT__:')
print(json.dumps({'total_funding': int(total), 'project_count': len(set(matched))}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
