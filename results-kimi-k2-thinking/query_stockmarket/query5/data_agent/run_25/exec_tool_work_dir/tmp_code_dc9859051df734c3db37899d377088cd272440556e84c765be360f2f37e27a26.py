code = """import json

# Read the full result from the file
result_path = locals()['var_functions.query_db:2']
with open(result_path, 'r') as f:
    stockinfo_data = json.load(f)

# Check the structure and see if Market Category field exists
if stockinfo_data:
    first_row = stockinfo_data[0]
    print('__RESULT__:')
    print(json.dumps({
        'first_row_keys': list(first_row.keys()),
        'sample_data': stockinfo_data[:5]
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No data found'}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 86, 'capital_market_count': 0, 'sample_stocks': []}}

exec(code, env_args)
