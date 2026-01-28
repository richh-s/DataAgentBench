code = """import json
import os

# Get paths from stored variables
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:5

# Read funding data
f = open(funding_path, 'r')
funding_records = json.load(f)
f.close()

# Read civic documents
c = open(civic_path, 'r')
civic_docs = json.load(c)
c.close()

# Filter funding > 50000
high_funding = []
for record in funding_records:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Extract design capital projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1]
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('(') and not line.startswith('Capital'):
                    if 'To:' not in line and 'From:' not in line and len(line) > 5:
                        design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches
funding_names = set(r['Project_Name'] for r in high_funding)
match_count = 0

for proj in design_projects:
    for fund_name in funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            match_count += 1
            break

# Ensure proper JSON output
result = json.dumps(match_count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
