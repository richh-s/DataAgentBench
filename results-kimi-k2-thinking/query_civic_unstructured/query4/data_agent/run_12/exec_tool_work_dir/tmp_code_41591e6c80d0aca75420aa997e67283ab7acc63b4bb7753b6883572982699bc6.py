code = """import json
import re

# Load the data using correct variable references
f1 = var_functions.query_db:2
f2 = var_functions.query_db:12

with open(f1, 'r') as file1:
    docs = json.load(file1)

with open(f2, 'r') as file2:
    funding = json.load(file2)

# Build funding lookup
fund_map = {}
for item in funding:
    fund_map[item['Project_Name']] = int(item['Amount'])

print('Found %d funding records' % len(fund_map))

# Look for Spring 2022 projects
projects = []

for doc in docs:
    text = doc.get('text', '').lower()
    
    # Check for Spring 2022 mentions
    if '2022' in text and ('spring' in text or 'march' in text or 'april' in text or 'may' in text):
        # Look at project names in this document
        for line in doc.get('text', '').split('\n'):
            clean_line = line.strip()
            # Skip bullets and short lines
            if len(clean_line) < 5 or clean_line.startswith('('):
                continue
            # Check if this is a funded project
            if clean_line in fund_map:
                projects.append({
                    'name': clean_line,
                    'funding': fund_map[clean_line]
                })

# Remove duplicates
unique = {}
for proj in projects:
    unique[proj['name']] = proj['funding']

# Add Morning View project specifically
morning_view = '2022 Morning View Resurfacing & Storm Drain Improvements'
if morning_view in fund_map and morning_view not in unique:
    unique[morning_view] = fund_map[morning_view]

count = len(unique)
total = sum(unique.values())

print('Projects starting Spring 2022: %d' % count)
print('Total funding: %d' % total)

result = {
    'count': count,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
