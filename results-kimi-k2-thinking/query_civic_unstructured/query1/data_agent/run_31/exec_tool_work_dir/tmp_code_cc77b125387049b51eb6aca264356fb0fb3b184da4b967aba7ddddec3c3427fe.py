code = """import json

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:5

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract project names
project_names = []
keywords = ['road', 'avenue', 'park', 'canyon', 'drive', 'beach', 'storm', 'bridge']

for doc in civic_docs:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        if 'Capital' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) < 70 and not line.startswith('('):
                    lower = line.lower()
                    if 'update' not in lower and 'schedule' not in lower:
                        for kw in keywords:
                            if kw in lower:
                                project_names.append(line)
                                break

# Remove duplicates
unique_projects = list(set(project_names))

# Filter funding > 50000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name']] = amount

# Match
matched = 0
for proj in unique_projects:
    proj_norm = proj.lower().replace(' ', '')
    for fund_name in funding_lookup.keys():
        fund_norm = fund_name.lower().replace(' ', '')
        if proj_norm in fund_norm or fund_norm in proj_norm:
            matched += 1
            break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
