code = """import json

# Load the data
funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Get projects with funding > 50000
funding_projects = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        funding_projects.append(rec['Project_Name'])

# Extract capital design project names from civic docs
design_projects = []

for doc in civic_docs:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 8 and len(line) < 60:
                    lower = line.lower()
                    if 'road' in lower or 'park' in lower or 'canyon' in lower:
                        design_projects.append(line)

# Remove duplicate project names
unique_design = []
seen = set()
for proj in design_projects:
    if proj not in seen:
        seen.add(proj)
        unique_design.append(proj)

# Match projects by simple string comparison
matched = 0
for proj in unique_design:
    for fund in funding_projects:
        if proj.lower().replace(' ', '') in fund.lower().replace(' ', '') or fund.lower().replace(' ', '') in proj.lower().replace(' ', ''):
            matched += 1
            break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
