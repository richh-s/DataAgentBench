code = """import json

# Load the data
civic_docs = json.load(open('/tmp/tmpq0c3uww8.json'))
funding_data = json.load(open('/tmp/tmphv6u7l7_.json'))

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and 'park' in line.lower():
                if 'Project' in line or 'Improvements' in line:
                    for j in range(i+1, min(i+15, len(lines))):
                        if '2022' in lines[j] and 'completed' in lines[j].lower():
                            park_projects.append(line)
                            break

# Remove duplicates
park_projects = list(set(park_projects))

# Build funding lookup
funding_lookup = {}
for f in funding_data:
    funding_lookup[f['Project_Name']] = int(f['Amount'])

# Calculate total funding
total = 0
for proj in park_projects:
    if proj in funding_lookup:
        total += funding_lookup[proj]

result = str(total)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
