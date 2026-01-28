code = """import json

civic_docs_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    t = text.lower()
    
    if 'park' in t and 'construction was completed' in t and '2022' in t:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if 'park' in line_clean.lower() and len(line_clean) > 5:
                if 'schedule' not in line_clean.lower():
                    for j in range(i, min(i+10, len(lines))):
                        if 'Construction was completed' in lines[j] and '2022' in lines[j]:
                            projects.append(line_clean)
                            break

unique = []
for p in projects:
    if p not in unique:
        unique.append(p)

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
