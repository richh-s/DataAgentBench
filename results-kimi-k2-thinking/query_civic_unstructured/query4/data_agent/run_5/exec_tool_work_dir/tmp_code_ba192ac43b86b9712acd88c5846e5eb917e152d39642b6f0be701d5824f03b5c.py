code = """import json

# Load data
civic_docs = json.load(open('/tmp/tmp7.json'))
funding_data = json.load(open('/tmp/tmp8.json'))

# Build funding lookup
funding = {}
for r in funding_data:
    funding[r['Project_Name']] = int(r['Amount'])

# Find 2022 projects
count = 0
total = 0
found = []

for doc in civic_docs:
    txt = doc.get('text', '')
    for line in txt.split('\n'):
        line = line.strip()
        if line and '2022' in line and len(line) > 10:
            if line in funding:
                count += 1
                total += funding[line]
                found.append(line)

# Add from funding
for name, amt in funding.items():
    if '2022' in name and ('Annual' in name or 'Morning' in name):
        if name not in found:
            count += 1
            total += amt

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
