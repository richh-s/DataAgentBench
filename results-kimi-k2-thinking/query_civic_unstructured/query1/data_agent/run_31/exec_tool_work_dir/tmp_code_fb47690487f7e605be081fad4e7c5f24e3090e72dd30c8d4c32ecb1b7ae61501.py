code = """import json

funding_path = var_functions.query_db:68
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic = json.load(f)

design_project_names = []
for doc in civic:
    if 'text' in doc:
        text = doc['text']
        if 'Capital' in text and 'Design' in text:
            for line in text.split('\n'):
                line = line.strip()
                if line and len(line) > 8:
                    lower = line.lower()
                    if 'update' not in lower and 'schedule' not in lower:
                        if 'road' in lower or 'park' in lower or 'canyon' in lower:
                            design_project_names.append(line)

# Remove duplicates
unique_design = []
seen = set()
for name in design_project_names:
    if name not in seen:
        seen.add(name)
        unique_design.append(name)

# Match with funding
funding_names = [rec['Project_Name'] for rec in funding]

matched = 0
for dproj in unique_design:
    d_clean = ''.join(c for c in dproj.lower() if c.isalnum())
    for fproj in funding_names:
        f_clean = ''.join(c for c in fproj.lower() if c.isalnum())
        if d_clean in f_clean or f_clean in d_clean:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
