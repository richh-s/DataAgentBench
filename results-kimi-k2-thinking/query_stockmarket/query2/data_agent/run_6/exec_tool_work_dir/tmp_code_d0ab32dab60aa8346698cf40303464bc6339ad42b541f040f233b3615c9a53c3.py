code = """import json

# Get NYSE Arca ETFs
arca_file = locals()['var_functions.query_db:0']
arca_etfs = []
with open(arca_file, 'r') as f:
    arca_etfs = json.load(f)
symbols = [item['Symbol'] for item in arca_etfs]

# Get all available tables
tables_file = locals()['var_functions.list_db:6']
tables = []
with open(tables_file, 'r') as f:
    tables = json.load(f)

# Filter to only tables that are also in NYSE Arca ETFs
valid_symbols = [s for s in symbols if s in tables]

print("__RESULT__:")
print(json.dumps({
    "total_etfs": len(valid_symbols),
    "batch_size": 50,
    "num_batches": (len(valid_symbols) + 49) // 50,
    "sample_symbols": valid_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.execute_python:5': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_symbols': 1435}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_arca_etfs': 1435, 'total_tables_in_db': 2753, 'available_etfs_count': 1435, 'sample_available_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:10': {'message': 'Found 1435 NYSE Arca ETFs', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'total_to_check': 1435}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'num_batches': 15, 'sample_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.execute_python:20': {'test_symbols': ['DIA', 'SPY', 'IWM', 'VTI', 'EFA', 'EEM', 'AGG', 'GLD'], 'total_nyse_arca_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:22': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}], 'var_functions.execute_python:24': {'etf_count': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
