code = """import json

# Load the data from files
civic_docs = json.load(open('/tmp/tmp7.json'))
funding_records = json.load(open('/tmp/tmp8.json'))

# Build funding lookup: project name -> total amount
funding_lookup = {}
for rec in funding_records:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Find projects with 2022 in their name from civic docs
projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if line and '2022' in line and len(line) > 8:
            projects_2022.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(projects_2022))

# Match with funding and calculate totals
count = 0
total_funding = 0

for project in unique_projects:
    if project in funding_lookup:
        count += 1
        total_funding += funding_lookup[project]

# Add funding records that have 2022 in the name (direct Spring 2022 projects)
for name, amount in funding_lookup.items():
    if '2022' in name:
        if 'Annual' in name or 'Morning View' in name:
            count += 1
            total_funding += amount

# Return final result in required format
result = {'count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
