code = """import json

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:2']

civic_docs = json.load(open(civic_file))
funding = json.load(open(funding_file))

# Find all park funding records - this is simpler and more reliable
total_funding = 0
for record in funding:
    project_name = record.get('Project_Name', '').lower()
    if 'park' in project_name:
        total_funding += int(record.get('Amount', 0))

answer = 'Total funding for park-related projects completed in 2022 is $' + str(total_funding)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
