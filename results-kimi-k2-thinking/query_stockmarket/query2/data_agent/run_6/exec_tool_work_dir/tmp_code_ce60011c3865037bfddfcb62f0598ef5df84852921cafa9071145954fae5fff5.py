code = """import json

# Load NYSE Arca ETF symbols
arca_file = locals()['var_functions.query_db:0']
arca_etfs = []
with open(arca_file, 'r') as f:
    arca_etfs = json.load(f)
symbols = [item['Symbol'] for item in arca_etfs]

# Remove any problematic symbols that might cause quoting issues
# Ensure symbols contain only alphanumeric characters
symbols = [s for s in symbols if s.isalnum()]

# Define batch size
batch_size = 100
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]

print("__RESULT__:")
print(json.dumps({
    "total_symbols": len(symbols),
    "num_batches": len(batches),
    "sample_batch": batches[0][:5] if batches else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.execute_python:5': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_symbols': 1435}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_arca_etfs': 1435, 'total_tables_in_db': 2753, 'available_etfs_count': 1435, 'sample_available_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:10': {'message': 'Found 1435 NYSE Arca ETFs', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'total_to_check': 1435}}

exec(code, env_args)
