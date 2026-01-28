code = """import json

funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic = json.load(f)

# Filter funding for projects > $50,000
large_funding = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        large_funding.append(rec['Project_Name'])

# Find capital design projects in civic docs
design_projects = []

for doc in civic:
    if 'text' in doc and doc['text']:
        text = doc['text']
        if 'Capital' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Filter lines likely to be project names
                if line and len(line) > 8 and len(line) < 60 and not line.startswith('('):
                    lower = line.lower()
                    if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower:
                        design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Match with funding
matched = 0
for proj in unique_design:
    proj_clean = ''.join(c for c in proj.lower() if c.isalnum())
    
    for fund in large_funding:
        fund_clean = ''.join(c for c in fund.lower() if c.isalnum())
        
        if proj_clean in fund_clean or fund_clean in proj_clean:
            matched += 1
            break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
