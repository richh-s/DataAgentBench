code = """import json
import re

# Read the files
civic_docs = json.load(open('/tmp/tmp1.json'))
funding_data = json.load(open('/tmp/tmp2.json'))

# Build funding lookup
funding_lookup = {}
for f in funding_data:
    funding_lookup[f['Project_Name']] = int(f['Amount'])

print('Funding lookup built')

# Find projects mentioning Spring 2022
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line:
                # Find project name before this line
                for j in range(i-1, max(0, i-3), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) > 15:
                        spring_projects.append(prev)
                        break

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_projects))
print('Spring 2022 projects found:', len(unique_projects))

# Match with funding
total = 0
matches = []
for proj in unique_projects:
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        total += amount
        matches.append({'project': proj, 'funding': amount})
    else:
        # Check partial matches
        for funded in funding_lookup:
            if proj.lower() in funded.lower():
                amount = funding_lookup[funded]
                total += amount
                matches.append({'project': proj, 'funding': amount, 'matched_to': funded})
                break

output = {
    'count': len(matches),
    'total_funding': total,
    'matched_projects': matches
}

print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
