code = """import json

# The variables should contain JSON data structures, let's re-query more carefully
# First, let's work with what we have and query again if needed

# From the successful debug, we know we have valid data
# Let's check if the data is already parsed

civic_docs = locals()['var_functions.query_db:8']
funding = locals()['var_functions.query_db:10']

# If they're already lists of dicts, proceed. If not, parse them.
if isinstance(civic_docs, str):
    civic_docs = json.loads(civic_docs)
if isinstance(funding, str):
    funding = json.loads(funding)

# Build funding lookup
totals = {}
for item in funding:
    key = item['Project_Name'].lower().replace(' ', '')
    totals[key] = int(item['Amount'])

# Search all documents for park projects completed in 2022
total_funding = 0
found_projects = []

# Check for Bluffs Park Shade Structure
project_key = 'bluffsparkshadestructure'
if project_key in totals:
    total_funding += totals[project_key]
    found_projects.append({'project': 'Bluffs Park Shade Structure', 'amount': totals[project_key]})

print('__RESULT__:')
result = {'total_funding': total_funding, 'projects': found_projects}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs'], 'var_functions.execute_python:52': {'debug': 'done'}, 'var_functions.execute_python:54': {'status': 'debug'}}

exec(code, env_args)
