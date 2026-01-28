code = """import json

# Load the common symbols from previous result
common_symbols_result = locals()['var_functions.execute_python:24']

# Since it's a file path, read it
import json
with open(common_symbols_result, 'r') as f:
    data = json.load(f)

common_symbols = sorted(data['common_symbols_list'])

# Create batches for DuckDB queries
batch_size = 25
batches = []
for i in range(0, len(common_symbols), batch_size):
    batch = common_symbols[i:i+batch_size]
    batches.append(batch)

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(common_symbols),
    'batches_count': len(batches),
    'batch_size': batch_size,
    'first_batch': batches[0],
    'last_batch': batches[-1]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
