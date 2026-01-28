code = """import json

# Strategy: Process in smaller batches to avoid timeouts and manage memory
# Batch size for processing
BATCH_SIZE = 50

# Load NYSE Arca ETF symbols
nyse_arca_file = locals().get('var_functions.query_db:0', '')
if nyse_arca_file and not isinstance(nyse_arca_file, list):
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = nyse_arca_file if isinstance(nyse_arca_file, list) else []

# Get all available tables
all_tables_file = locals().get('var_functions.list_db:2', '')
if all_tables_file and not isinstance(all_tables_file, list):
    with open(all_tables_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_file if isinstance(all_tables_file, list) else []

# Filter ETFs that have corresponding tables
nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs if etf['Symbol'] in all_tables]
print('__RESULT__:')
print(json.dumps({
    'total_symbols_to_check': len(nyse_arca_symbols),
    'batch_size': BATCH_SIZE,
    'batches': (len(nyse_arca_symbols) + BATCH_SIZE - 1) // BATCH_SIZE
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
