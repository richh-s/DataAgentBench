code = """# Load common symbols from previous execution
import json

exec24_data = locals()['var_functions.execute_python:24']
with open(exec24_data, 'r') as f:
    data = json.load(f)

common_symbols = data['common_symbols_list']
batch_size = 25

# Create batches
batches = [common_symbols[i:i+batch_size] for i in range(0, len(common_symbols), batch_size)]

# Function to create a query for a batch of symbols
def create_batch_query(symbols):
    queries = []
    for symbol in symbols:
        queries.append(f"SELECT '{symbol}' as Symbol FROM \"{symbol}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1")
    
    return " UNION ALL ".join(queries)

# Test with first batch
first_batch = batches[0]
query = create_batch_query(first_batch)

print('__RESULT__:')
print(json.dumps({
    'query_preview': query[:500],
    'symbols_in_batch': first_batch,
    'total_batches': len(batches)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': {'total_symbols': 1435, 'batches_count': 58, 'batch_size': 25, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT'], 'last_batch': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}}

exec(code, env_args)
