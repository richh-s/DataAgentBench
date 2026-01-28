code = """import json

# Load the CPC data from the previous query
cpc_level5_data = locals()['var_functions.query_db:16']

# Extract all level 5 CPC symbols
level5_symbols = [record['symbol'] for record in cpc_level5_data]

print('Found ' + str(len(level5_symbols)) + ' level 5 CPC symbols (sample):')
print(level5_symbols[:20])

# Also need to get the complete CPC year counts data from previous analysis
full_analysis_data = locals()['var_functions.execute_python:14']

# Check if it's a file path or actual data
if isinstance(full_analysis_data, str):
    with open(full_analysis_data, 'r') as f:
        full_analysis = json.load(f)
else:
    full_analysis = full_analysis_data

print('\nFull analysis data keys: ' + str(full_analysis.keys()))
print('Years available: ' + str(full_analysis.get('years', [])))
print('Total base CPC codes: ' + str(full_analysis.get('total_base_codes', 0)))
print('Total combinations: ' + str(full_analysis.get('total_combinations', 0)))

result = {
    'level5_symbols': level5_symbols,
    'total_level5': len(level5_symbols),
    'years': full_analysis.get('years', []),
    'cpc_year_counts': full_analysis.get('cpc_year_counts', {})
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
