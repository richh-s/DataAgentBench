code = """import json

civic_docs_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Construction was completed' in text and '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if 'park' in line_clean.lower():
                if 'Bluffs Park Shade Structure' in line_clean:
                    projects_2022.append(line_clean)
                elif 'park' in line_clean.lower() and len(line_clean) < 50:
                    if i+1 < len(lines):
                        next_line = lines[i+1]
                        if 'Construction was completed' in next_line and '2022' in next_line:
                            projects_2022.append(line_clean)

# Remove duplicates
unique = []
for p in projects_2022:
    if p not in unique:
        unique.append(p)

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
