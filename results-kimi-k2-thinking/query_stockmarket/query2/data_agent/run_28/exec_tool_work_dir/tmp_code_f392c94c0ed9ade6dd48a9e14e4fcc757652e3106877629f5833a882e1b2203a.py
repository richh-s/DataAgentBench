code = """import json

# Load common symbols 
exec24_path = locals()['var_functions.execute_python:24']
with open(exec24_path, 'r') as f:
    data = json.load(f)

common_symbols = data['common_symbols_list']

# Create batches of symbols for querying
batch_size = 20
batches = []
for i in range(0, len(common_symbols), batch_size):
    batches.append(common_symbols[i:i+batch_size])

# Store batch info
with open('/tmp/batches_info.json', 'w') as f:
    json.dump({
        'total_symbols': len(common_symbols),
        'batch_size': batch_size,
        'total_batches': len(batches),
        'batches': batches
    }, f)

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(common_symbols),
    'total_batches': len(batches),
    'first_batch': batches[0],
    'batch_count': len(batches)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': {'total_symbols': 1435, 'batches_count': 58, 'batch_size': 25, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT'], 'last_batch': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'Symbol': 'SPY', 'Max_Adj_Close': '193.3121490478516'}], 'var_functions.execute_python:42': {'total_symbols': 1435, 'batch_size': 25, 'total_batches': 58}, 'var_functions.query_db:44': [{'Symbol': 'GLD', 'Max_Adj_Close': '125.2300033569336'}], 'var_functions.query_db:46': []}

exec(code, env_args)
