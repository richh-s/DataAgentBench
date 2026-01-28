code = """import json

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:2']

civic_docs = json.load(open(civic_file))
funding = json.load(open(funding_file))

# Calculate total funding for park projects
total_funding = 0
for record in funding:
    if 'park' in record.get('Project_Name', '').lower():
        total_funding += int(record.get('Amount', 0))

print('__RESULT__:')
print(json.dumps(total_funding))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
