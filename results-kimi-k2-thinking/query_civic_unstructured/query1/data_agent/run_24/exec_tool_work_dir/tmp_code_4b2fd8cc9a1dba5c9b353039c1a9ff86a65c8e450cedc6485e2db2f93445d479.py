code = """import json

# Read the data directly from the stored storage
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:64

# Since these are JSON file paths, let's read them
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Filter for funding > $50,000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Step 2: Extract design capital projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        part = text.split('Capital Improvement Projects (Design)', 1)[1]
        for line in part.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and line[0].isalpha():
                if 'To:' not in line and 'From:' not in line and len(line) > 5:
                    design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Count matches
matched = 0
funding_names = [r['Project_Name'] for r in high_funding]

for proj in unique_design:
    for fund_name in funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:80': ['civic_docs']}

exec(code, env_args)
