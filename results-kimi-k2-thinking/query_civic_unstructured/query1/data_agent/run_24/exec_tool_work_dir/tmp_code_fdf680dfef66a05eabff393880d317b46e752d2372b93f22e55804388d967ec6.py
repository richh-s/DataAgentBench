code = """import json

# Get data from files
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Filter funding > 50k
high_funding_names = set(r['Project_Name'] for r in funding if int(r['Amount']) > 50000)

# Extract design projects
from pprint import pprint
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)', 1)[1]
        for line in section.split('\n')[2:30]:
            line = line.strip()
            if line and not line.startswith('(') and ':' not in line:
                if 'To:' not in line and 'From:' not in line:
                    design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches
matches = 0
for proj in design_projects:
    for fund_name in high_funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matches += 1
            break

# Print result in required format
result = str(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
