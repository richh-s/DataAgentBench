code = """import json, re

funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:34']

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'park' in line.lower() and len(line) > 8 and len(line) < 100:
            if 'schedule' not in line.lower() and 'updates' not in line.lower():
                for j in range(i, min(i+8, len(lines))):
                    if 'Construction was completed' in lines[j] and '2022' in lines[j]:
                        if line not in park_projects_2022:
                            park_projects_2022.append(line)
                        break

# Deduplicate
unique = []
for p in park_projects_2022:
    if p not in unique:
        unique.append(p)

print('__RESULT__:')
print(json.dumps({'projects': unique, 'count': len(unique)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
