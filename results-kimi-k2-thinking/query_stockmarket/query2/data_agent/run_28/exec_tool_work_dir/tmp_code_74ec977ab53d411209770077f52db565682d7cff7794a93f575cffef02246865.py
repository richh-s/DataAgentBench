code = """import json

# Load common symbols and batches info
exec24_path = locals()['var_functions.execute_python:24']
exec48_path = locals()['var_functions.execute_python:48']

with open(exec24_path, 'r') as f:
    data24 = json.load(f)

with open(exec48_path, 'r') as f:
    data48 = json.load(f)

common_symbols = data24['common_symbols_list']
batches = data48['batches']

# Process first batch of symbols
first_batch = batches[0]
print('First batch symbols:', first_batch)

# Create individual MAX queries for each symbol in first batch
queries = []
for symbol in first_batch:
    query = f"SELECT '{symbol}' as Symbol, MAX(\"Adj Close\") as Max_Adj_Close FROM \"{symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    queries.append(query)

# Join with UNION ALL
full_query = " UNION ALL ".join(queries)

print('__RESULT__:')
print(json.dumps({
    'symbols_count': len(first_batch),
    'first_few_symbols': first_batch[:3],
    'query_preview': full_query[:300] + '...' if len(full_query) > 300 else full_query
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': {'total_symbols': 1435, 'batches_count': 58, 'batch_size': 25, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT'], 'last_batch': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'Symbol': 'SPY', 'Max_Adj_Close': '193.3121490478516'}], 'var_functions.execute_python:42': {'total_symbols': 1435, 'batch_size': 25, 'total_batches': 58}, 'var_functions.query_db:44': [{'Symbol': 'GLD', 'Max_Adj_Close': '125.2300033569336'}], 'var_functions.query_db:46': [], 'var_functions.execute_python:48': {'total_symbols': 1435, 'total_batches': 72, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'batch_count': 72}}

exec(code, env_args)
