code = """import json

# Load data from files
civic_docs = json.load(open('/tmp/tmp7.json'))
funding_data = json.load(open('/tmp/tmp8.json'))

# Build funding lookup
funding = {}
for rec in funding_data:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding[name] = funding.get(name, 0) + amount

# Find 2022 projects in civic docs
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if '2022' in line and len(line) > 10:
            projects_2022.append(line)

# Deduplicate
unique = list(dict.fromkeys(projects_2022))

# Match funding
count = 0
total = 0

for proj in unique:
    if proj in funding:
        count += 1
        total += funding[proj]
    else:
        # Try by first word
        first = proj.split()[0] if proj.split() else ''
        for funded in funding:
            if funded.startswith(first) and len(first) > 5:
                count += 1
                total += funding[funded]
                break

# Add funding records with 2022
for funded_name, amount in funding.items():
    if '2022' in funded_name:
        if 'Morning View' in funded_name or 'Annual' in funded_name:
            if funded_name not in unique:
                count += 1
                total += amount

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
