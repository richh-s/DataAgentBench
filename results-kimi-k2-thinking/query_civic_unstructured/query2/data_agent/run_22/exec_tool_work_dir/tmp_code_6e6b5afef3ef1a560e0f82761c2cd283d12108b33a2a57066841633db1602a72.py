code = """import json

civic = json.load(open('var_functions.query_db_64'))
funding = json.load(open('var_functions.query_db_8'))

# Extract park projects completed in 2022
projects = []

for doc in civic:
    t = doc.get('text', '')
    # Check for Bluffs Park Shade Structure completed Nov 2022
    if 'Bluffs Park Shade' in t and 'completed' in t.lower() and '2022' in t:
        projects.append('Bluffs Park Shade Structure')
    # Check for Broad Beach Road Water Quality Repair completed Nov 2022
    if 'Broad Beach Road Water Quality' in t and 'completed' in t.lower() and '2022' in t:
        projects.append('Broad Beach Road Water Quality Repair')

# Remove duplicates
projects = list(set(projects))

# Calculate total funding
total = 0
for p in projects:
    pl = p.lower()
    for f in funding:
        fm = f['Project_Name'].lower()
        if pl == fm:
            total += int(f['Amount'])

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
