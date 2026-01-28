code = """import json
import pandas as pd

f_path = locals()['var_functions.query_db:4']
c_path = locals()['var_functions.query_db:5']

with open(f_path) as f:
    funding_raw = json.load(f)
with open(c_path) as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_raw)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

park_2022 = set()
for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        cur = lines[i].strip()
        if '2022' in cur and ('completed' in cur.lower() or 'completion' in cur.lower()):
            for j in range(i-1, -1, -1):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('('):
                    low = prev.lower()
                    has_skip = any(x in low for x in ['project schedule', 'updates:', 'to:'])
                    if not has_skip:
                        if 'park' in low or 'playground' in low or 'bluff' in low:
                            park_2022.add(prev)
                            break

park_list = list(park_2022)
total_funding = 0
matched_names = []
for p in park_list:
    p_low = p.lower()
    for _, r in funding_df.iterrows():
        n_low = r['Project_Name'].lower()
        common = p_low in n_low or n_low in p_low
        if common:
            total_funding += r['Amount']
            matched_names.append(r['Project_Name'])

print('__RESULT__:')
print(str(total_funding))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
