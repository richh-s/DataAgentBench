code = """import json

funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path) as f:
    funding_data = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Get funding projects over $50,000
large_funding = {}
for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        large_funding[rec['Project_Name']] = amount

# Extract capital design projects from civic docs
capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 8 < len(line) < 60 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
                lower = line.lower()
                if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower:
                    capital_projects.append(line)

# Remove duplicates
unique_projects = list(set(capital_projects))

# Match with funding data
matched = 0
for proj in unique_projects:
    proj_clean = proj.lower().replace(' ', '').replace('(', '').replace(')', '')
    proj_clean = ''.join(c for c in proj_clean if c.isalnum())
    
    for fund_name in large_funding.keys():
        fund_clean = fund_name.lower().replace(' ', '').replace('(', '').replace(')', '')
        fund_clean = ''.join(c for c in fund_clean if c.isalnum())
        
        if proj_clean in fund_clean or fund_clean in proj_clean:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
