code = """import json
import os

# Load ETF symbols from the file
symbols_file = locals().get('var_functions.query_db:8')
with open(symbols_file, 'r') as f:
    etf_list = json.load(f)

etf_symbols = [item['Symbol'] for item in etf_list]
batch_size = 50
batches = [etf_symbols[i:i + batch_size] for i in range(0, len(etf_symbols), batch_size)]

print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(etf_symbols),
    'num_batches': len(batches),
    'batch_size': batch_size,
    'first_batch': batches[0][:5] if batches else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 1435, 'sample': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_symbols': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
