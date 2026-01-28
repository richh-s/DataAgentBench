code = """import json

# Get the file path from storage
file_path = locals()['var_functions.execute_python:24']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

common_symbols = data['common_symbols_list']

# Create batch queries
def create_query_for_batch(symbols):
    conditions = []
    for i, symbol in enumerate(symbols):
        # Check for valid table names (some may contain special characters)
        clean_symbol = symbol.replace('-', '_').replace('.', '_')
        conditions.append(
            f"SELECT '{symbol}' as Symbol FROM \"{symbol}\" "
            f"WHERE \"Adj Close\" > 200 AND "
            f"Date >= '2015-01-01' AND Date <= '2015-12-31'"
        )
    return " UNION ALL ".join(conditions)

# Test with first 5 symbols
test_symbols = common_symbols[:5]
test_query = create_query_for_batch(test_symbols)

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(common_symbols),
    'test_query': test_query,
    'test_symbols': test_symbols
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': {'total_symbols': 1435, 'batches_count': 58, 'batch_size': 25, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT'], 'last_batch': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}}

exec(code, env_args)
