code = """import json
import re

# Read funding data
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data (filtered for emergency/FEMA)
civic_file = locals()['var_functions.query_db:10']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('__RESULT__:')
result = {
    'funding_count': len(funding_data),
    'civic_count': len(civic_data),
    'sample_funding': funding_data[:3],
    'sample_civic_preview': civic_data[0]['text'][:500] if civic_data else 'No data'
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.execute_python:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
