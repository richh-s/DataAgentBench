code = """import json
import os

# Load NYSE Arca ETF symbols
symbols_file = locals().get('var_functions.query_db:24')
with open(symbols_file, 'r') as f:
    etf_list = json.load(f)

symbols = [item['Symbol'] for item in etf_list]

# Build a union query for first 10 symbols as a test case
query_parts = []
for symbol in symbols[:10]:
    part = 'SELECT "' + symbol + '" as Symbol FROM "' + symbol + '" WHERE "Adj Close" > 200 AND Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' LIMIT 1'
    query_parts.append(part)

union_query = ' UNION '.join(query_parts) + ';'

print('__RESULT__:')
print(json.dumps({
    'query_sample': union_query[:300],
    'length': len(union_query)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 1435, 'sample': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_symbols': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'num_batches': 29, 'batch_size': 50, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_etfs': 1435, 'batch_size': 100, 'num_batches': 15, 'first_batch_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.execute_python:28': {'total_nyse_arca_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
