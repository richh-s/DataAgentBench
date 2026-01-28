code = """import json
import re

# Read the result from previous query
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    data = json.load(f)

# Look at a few records to understand structure
print('__RESULT__:')
print(json.dumps({
    'num_records': len(data),
    'sample_patent_info': data[0]['Patents_info'],
    'sample_citation': data[0].get('citation', 'No citation field')[:500] if data[0].get('citation') else 'No citation',
    'sample_cpc': data[0].get('cpc', 'No CPC field')[:500] if data[0].get('cpc') else 'No CPC'
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
