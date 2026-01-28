code = """import json
import re

# Load the data
with open(str(var_functions.query_db:2), 'r') as f:
    funding = json.load(f)

with open(str(var_functions.query_db:6), 'r') as f:
    civic = json.load(f)

# Count funding records > 50000
count_funding = sum(1 for item in funding if float(item['Amount']) > 50000)

# Extract unique lines from civic docs that might be project names
project_names = set()
for doc in civic:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 15 and 'Page' not in line and 'Agenda' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                if 'RECOMMENDED' not in line.upper():
                    project_names.add(line)

# Count capital design projects (crude estimate)
capital_design_count = len([p for p in project_names if 'Design' in p or any(x in p for x in ['Road', 'Park', 'Drain', 'Bridge'])])

# Simple match count
fund_names = {item['Project_Name'] for item in funding if float(item['Amount']) > 50000}
clean_fund_names = {re.sub(r'\s*\([^)]*\)\s*$', '', name).strip() for name in fund_names}

match_count = 0
for project in project_names:
    clean_project = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    if project in fund_names or clean_project in clean_fund_names:
        match_count += 1

result = {
    'funding_over_50k': count_funding,
    'potential_projects': len(project_names),
    'matches': match_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
