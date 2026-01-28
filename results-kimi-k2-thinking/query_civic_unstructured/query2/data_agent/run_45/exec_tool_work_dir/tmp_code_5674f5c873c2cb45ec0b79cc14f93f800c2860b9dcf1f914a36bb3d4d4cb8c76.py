code = """import json

# Load the data from the files
civic_file = open('/tmp/tmpq0c3uww8.json', 'r').read()
funding_file = open('/tmp/tmphv6u7l7_.json', 'r').read()

civic_docs = json.loads(civic_file)
funding_data = json.loads(funding_file)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and 'park' in line.lower() and 'Project' in line:
                for j in range(i+1, min(i+15, len(lines))):
                    if '2022' in lines[j] and 'completed' in lines[j].lower():
                        park_projects_2022.append(line)
                        break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Build funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Calculate total funding
total_funding = 0
for project in park_projects_2022:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
    else:
        p_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            f_lower = fund_name.lower()
            if p_lower in f_lower or f_lower in p_lower:
                total_funding += amount
                break

print('__RESULT__:')
print(total_funding)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
