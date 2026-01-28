code = """import json

# Access the file paths from storage
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:5']

# Read the data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Get high funding records (> $50,000)
high_funding = []
for record in funding_records:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Step 2: Find capital projects in design phase
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        section = parts[1] if len(parts) > 1 else ''
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line:
                    if len(line) > 5:
                        design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Step 3: Count matches
funding_names = set(r['Project_Name'] for r in high_funding)
matches = 0
for proj in design_projects:
    for fund_name in funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matches += 1
            break

# Output
print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
