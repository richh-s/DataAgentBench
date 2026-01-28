code = """import json

# Load the data directly
civic_docs = []
funding_records = []

# The previous queries should have stored data we can access
# Let's check what we have access to
import os
print('Current directory files:', os.listdir('.')[:10])

# Try to load from common file patterns
for fname in os.listdir('.'):
    if 'civic' in fname.lower() and fname.endswith('.json'):
        print(f'Loading civic docs from {fname}')
        with open(fname, 'r') as f:
            civic_docs = json.load(f)
    if 'funding' in fname.lower() and fname.endswith('.json'):
        print(f'Loading funding from {fname}')
        with open(fname, 'r') as f:
            funding_records = json.load(f)

print(f'Loaded {len(civic_docs)} civic docs, {len(funding_records)} funding records')

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

print(f'Funding lookup has {len(funding_lookup)} projects')

# Now find Spring 2022 projects
spring_2022_count = 0
total_funding_amount = 0
matched_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Look for project names in this document
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Basic project name detection
            if len(line) > 10 and len(line) < 150:
                if any(kw in line for kw in ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation']):
                    if not line.startswith('(') and not line.startswith('To:'):
                        # Check if this project has funding
                        if line in funding_lookup:
                            if line not in [p['name'] for p in matched_projects]:
                                amount = funding_lookup[line]
                                matched_projects.append({'name': line, 'funding': amount})
                                spring_2022_count += 1
                                total_funding_amount += amount
                        else:
                            # Try partial match
                            for fund_name in funding_lookup:
                                if line.lower() in fund_name.lower() or fund_name.lower() in line.lower():
                                    if fund_name not in [p['name'] for p in matched_projects]:
                                        amount = funding_lookup[fund_name]
                                        matched_projects.append({'name': fund_name, 'funding': amount})
                                        spring_2022_count += 1
                                        total_funding_amount += amount
                                    break

result = {
    'project_count': spring_2022_count,
    'total_funding': total_funding_amount
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
