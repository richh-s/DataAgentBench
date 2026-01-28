code = """import json

# Load the list of NYSE Arca ETFs from stockinfo
arca_file = locals()['var_functions.query_db:0']
arca_etfs = []
with open(arca_file, 'r') as f:
    arca_etfs = json.load(f)

# Create a mapping for easy lookup
symbols = [item['Symbol'] for item in arca_etfs]

# Check individual prominent ETFs first as a test
test_symbols = ['DIA', 'SPY', 'QQQ', 'IWM', 'VTI', 'EFA', 'EEM', 'AGG', 'GLD', 'TLT'] 

# Filter to only include those in our NYSE Arca list
test_symbols = [s for s in test_symbols if s in symbols]

print("__RESULT__:")
print(json.dumps({
    "test_symbols": test_symbols,
    "total_nyse_arca_etfs": len(symbols),
    "sample_symbols": symbols[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.execute_python:5': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_symbols': 1435}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_arca_etfs': 1435, 'total_tables_in_db': 2753, 'available_etfs_count': 1435, 'sample_available_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:10': {'message': 'Found 1435 NYSE Arca ETFs', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'total_to_check': 1435}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'num_batches': 15, 'sample_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': []}

exec(code, env_args)
