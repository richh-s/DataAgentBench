code = """import json
f_fund = var_functions.query_db:68
f_civic = var_functions.query_db:5

with open(f_fund) as f:
    funding = json.load(f)

with open(f_civic) as f:
    civic = json.load(f)

funding_names = []
for rec in funding:
    funding_names.append(rec['Project_Name'])

matching_lines = []

for doc in civic:
    if 'text' in doc:
        txt = doc['text']
        if 'Capital Improvement Projects (Design)' in txt or ('Capital' in txt and 'Design' in txt):
            for line in txt.split('\n'):
                line = line.strip()
                if line and len(line) < 80 and 'Updates' not in line and 'Schedule' not in line:
                    ll = line.lower()
                    if any(x in ll for x in ['road','avenue','park','canyon','beach','storm','bridge']):
                        matching_lines.append(line)

unique_lines = list(dict.fromkeys(matching_lines))
count = 0

for line in unique_lines:
    line_clean = ''.join(c for c in line.lower() if c.isalnum())
    for fname in funding_names:
        fname_clean = ''.join(c for c in fname.lower() if c.isalnum())
        if line_clean in fname_clean or fname_clean in line_clean:
            count += 1
            break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
