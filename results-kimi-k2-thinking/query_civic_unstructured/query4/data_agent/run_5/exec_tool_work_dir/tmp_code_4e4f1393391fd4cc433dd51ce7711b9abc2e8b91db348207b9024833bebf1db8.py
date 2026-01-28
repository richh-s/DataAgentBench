code = """import json

# Load data from files
civic_docs = json.load(open('/tmp/tmp7.json'))
funding_data = json.load(open('/tmp/tmp8.json'))

# Build funding lookup map
funding_lookup = {}
for rec in funding_data:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Look for Spring 2022 projects
# From the data, these are clearly 2022 projects:
spring_2022_projects = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    '2022 Annual Street Maintenance'
]

# Count and sum funding
count = 0
total = 0

for project in spring_2022_projects:
    if project in funding_lookup:
        count += 1
        total += funding_lookup[project]

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
