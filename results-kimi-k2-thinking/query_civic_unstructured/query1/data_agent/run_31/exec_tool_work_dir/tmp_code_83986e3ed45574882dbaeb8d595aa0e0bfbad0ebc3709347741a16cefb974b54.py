code = """import json

f_fund = var_functions.query_db:68
f_civic = var_functions.query_db:5

with open(f_fund) as f:
    funding = json.load(f)

with open(f_civic) as f:
    civic = json.load(f)

# Get funding project names
funding_names = [rec['Project_Name'] for rec in funding]

# Extract capital design projects
design_projects = []

for doc in civic:
    if 'text' in doc:
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) < 80 and 'Updates:' not in line and 'Schedule:' not in line:
                    lower = line.lower()
                    if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower or 'bridge' in lower or 'avenue' in lower or 'beach' in lower:
                        design_projects.append(line)

# Remove duplicates
seen = set()
unique_design = []
for proj in design_projects:
    if proj not in seen:
        seen.add(proj)
        unique_design.append(proj)

# Match projects
count = 0
for proj in unique_design:
    proj_clean = ''.join(c for c in proj.lower() if c.isalnum())
    for fund in funding_names:
        fund_clean = ''.join(c for c in fund.lower() if c.isalnum())
        if proj_clean in fund_clean or fund_clean in proj_clean:
            count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
