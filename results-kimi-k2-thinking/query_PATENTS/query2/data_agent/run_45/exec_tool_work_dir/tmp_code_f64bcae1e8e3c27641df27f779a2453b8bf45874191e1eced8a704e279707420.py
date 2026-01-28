code = """import json
from collections import defaultdict

# Get the file path
file_info = locals()['var_functions.query_db:26']
print('File info:', file_info)

# Load the German patents data
with open(file_info, 'r') as f:
    german_patents = json.load(f)

print('Found', len(german_patents), 'German patents')

# Debug first patent
d
first_patent = german_patents[0]
print('First patent grant date:', first_patent['grant_date'])
print('First patent CPC length:', len(first_patent['cpc']))
print('First patent CPC (raw):', first_patent['cpc'][:200])

# Test parsing
import json as js
try:
    cpc_data = js.loads(first_patent['cpc'])
    print('Successfully parsed CPC JSON')
    print('Number of CPC entries:', len(cpc_data))
    if cpc_data:
        print('First entry:', cpc_data[0])
except Exception as e:
    print('Error parsing CPC:', e)

result = {'status': 'debug_complete', 'count': len(german_patents)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'cpc_year_counts': {}, 'cpc_all_codes': {}, 'total_german_patents': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'country_code': 'US'}, {'country_code': 'DE'}, {'country_code': 'CU'}, {'country_code': 'EP'}, {'country_code': 'BR'}, {'country_code': 'AU'}, {'country_code': 'CN'}, {'country_code': 'SE'}, {'country_code': 'NL'}, {'country_code': 'RU'}, {'country_code': 'UA'}, {'country_code': 'DK'}, {'country_code': 'NO'}, {'country_code': 'GB'}, {'country_code': 'HU'}, {'country_code': 'AT'}, {'country_code': 'HR'}, {'country_code': 'ES'}, {'country_code': 'PL'}, {'country_code': 'GR'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'cpc_year_counts': {}, 'full_codes': {}, 'total_patents': 34}}

exec(code, env_args)
