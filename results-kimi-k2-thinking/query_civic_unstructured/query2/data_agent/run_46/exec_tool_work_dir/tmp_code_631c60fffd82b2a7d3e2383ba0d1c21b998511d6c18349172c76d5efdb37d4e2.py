code = """import json

# Access data from storage - results should already be parsed lists
civic_docs_data = locals()['var_functions.query_db:64']
funding_data = locals()['var_functions.query_db:10']

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    normalized_name = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[normalized_name] = int(item['Amount'])

# Verify Bluffs Park Shade Structure was completed in 2022
all_text = ''
for doc in civic_docs_data:
    all_text += doc.get('text', '')

# Check if mentioned as completed in 2022 or November 2022
is_completed_2022 = 'Bluffs Park Shade Structure' in all_text and ('2022' in all_text or 'November 2022' in all_text)

# Get funding amount
project_name = 'bluffsparkshadestructure'
approved_funding = funding_lookup.get(project_name, 0)

print('__RESULT__:')
result = {
    'total_funding': approved_funding if is_completed_2022 else 0,
    'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': approved_funding, 'completed_2022': is_completed_2022}]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs'], 'var_functions.execute_python:52': {'debug': 'done'}, 'var_functions.execute_python:54': {'status': 'debug'}, 'var_functions.execute_python:58': {'status': 'debug_info_recorded'}, 'var_functions.execute_python:62': {'debug': 'path_identification'}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
