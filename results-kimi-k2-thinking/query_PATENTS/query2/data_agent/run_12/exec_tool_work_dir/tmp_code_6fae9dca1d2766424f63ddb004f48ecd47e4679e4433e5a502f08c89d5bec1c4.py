code = """import json
from collections import defaultdict

# Load German patent data
result_value = locals()['var_functions.query_db:30']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = result_value

print('Total German patents:', len(german_patents))

# Check if we have data
if len(german_patents) == 0:
    print('No German patents found')
else:
    print('First record grant_date:', german_patents[0].get('grant_date'))
    print('Sample CPC field:', str(german_patents[0].get('cpc'))[:100])

# Now let's get CPC definitions from the other database
print('Will query CPC definitions next')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
