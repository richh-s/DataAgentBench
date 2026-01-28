code = """import json

data1 = json.load(open('var_functions.query_db_36'))
data2 = json.load(open('var_functions.query_db_8'))

# Look for Bluffs Park Shade Structure
park_completed = []
for doc in data1:
    if 'Bluffs Park Shade' in doc['text']:
        park_completed.append('Bluffs Park Shade Structure')
        break
    if 'Broad Beach Road Water Quality' in doc['text']:
        park_completed.append('Broad Beach Road Water Quality Repair')
        break

# Find matching funding
total = 0
for record in data2:
    proj = record['Project_Name']
    if 'Bluffs Park Shade' in proj or 'Broad Beach Road Water Quality' in proj:
        total += int(record['Amount'])

print('__RESULT__:')
print(str(total))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
