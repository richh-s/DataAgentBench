code = """import json

# Load the German patent data
result_value = locals()['var_functions.query_db:30']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = result_value

print('Total German patents loaded:', len(german_patents))

if len(german_patents) > 0:
    print('First patent grant date:', german_patents[0].get('grant_date'))
    cpc_sample = str(german_patents[0].get('cpc', ''))[:150]
    print('Sample CPC:', cpc_sample)
    
print('\n---')
print('Need to query CPC definitions for titles')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
