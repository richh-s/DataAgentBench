code = """import json

# Try to get the file path
result_data = locals()['var_functions.query_db:18']
print('Result type:', type(result_data))
print('Result value:', str(result_data)[:200])

# Check if it's a file path string
if isinstance(result_data, str) and 'var_functions' in result_data:
    try:
        f = open(result_data, 'r')
        nyse_stocks = json.load(f)
        f.close()
        print('Successfully loaded from file')
    except:
        print('Failed to load from file')
        nyse_stocks = []
else:
    nyse_stocks = result_data if isinstance(result_data, list) else []

print('Total stocks:', len(nyse_stocks))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'symbols': [], 'metadata': []}, 'var_functions.query_db:14': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
