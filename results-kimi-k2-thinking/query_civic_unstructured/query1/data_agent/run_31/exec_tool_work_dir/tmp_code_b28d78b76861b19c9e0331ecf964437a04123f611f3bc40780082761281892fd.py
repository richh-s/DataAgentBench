code = """import json

# Load data
with open(var_functions.query_db:68) as f:
    funding = json.load(f)

with open(var_functions.query_db:5) as f:
    civic = json.load(f)

# Filter funding > 50000
large_funding = [item for item in funding if int(item['Amount']) > 50000]

# Extract design projects
all_design = []
for doc in civic:
    if 'text' in doc and 'Capital' in doc['text'] and 'Design' in doc['text']:
        for line in doc['text'].split('\n'):
            ll = line.strip().lower()
            if 'road' in ll or 'park' in ll or 'canyon' in ll:
                all_design.append(line.strip())

# Remove duplicates
unique_design = []
seen = set()
for proj in all_design:
    if proj not in seen:
        seen.add(proj)
        unique_design.append(proj)

# Match projects
matched = 0
for proj in unique_design:
    proj_clean = ''.join(c for c in proj.lower() if c.isalnum())
    for fund in large_funding:
        fund_clean = ''.join(c for c in fund['Project_Name'].lower() if c.isalnum())
        if proj_clean in fund_clean or fund_clean in proj_clean:
            if len(proj_clean) > 10:  # Avoid short matches
                matched += 1
                break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
