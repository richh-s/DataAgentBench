code = """import json
import os

# Get file paths from previous queries
civic_path = var_functions.query_db:60
funding_path = var_functions.query_db:61

# Load data
with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

# Build funding map
funding_lookup = {}
for rec in funding:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amt

# Look for projects that started in Spring 2022
# From civic docs preview, we see patterns like "2022 Morning View"
spring_2022_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Find lines with 2022 that look like project names
    for line in text.split('\n'):
        line = line.strip()
        if '2022' in line and len(line) > 10 and not line.startswith('('):
            if 'Morning View' in line or 'Annual' in line:
                spring_2022_names.append(line)

# Remove duplicates
unique_names = list(dict.fromkeys(spring_2022_names))

# Count funding for matching projects
count = 0
total = 0
matches = []

for name in unique_names:
    if name in funding_lookup:
        count += 1
        total += funding_lookup[name]
        matches.append({'name': name, 'funding': funding_lookup[name]})

# Also include direct funding records for 2022 projects
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name:
        if 'Morning View' in funded_name or 'Annual' in funded_name:
            # Check if not already counted
            if not any(m['name'] == funded_name for m in matches):
                count += 1
                total += amount
                matches.append({'name': funded_name, 'funding': amount})

result = {'count': count, 'total_funding': total, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
