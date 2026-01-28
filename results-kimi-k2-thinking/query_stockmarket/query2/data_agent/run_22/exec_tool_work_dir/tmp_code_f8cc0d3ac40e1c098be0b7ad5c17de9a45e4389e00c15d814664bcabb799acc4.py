code = """import json
import time

# Get file paths
nyse_arca_file = locals().get('var_functions.query_db:0', '')
all_tables_file = locals().get('var_functions.list_db:2', '')

# Load data if not already in memory
if nyse_arca_file and not isinstance(nyse_arca_file, list):
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = nyse_arca_file if isinstance(nyse_arca_file, list) else []

if all_tables_file and not isinstance(all_tables_file, list):
    with open(all_tables_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_file if isinstance(all_tables_file, list) else []

# Get NYSE Arca symbols
nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]
common_symbols = [sym for sym in nyse_arca_symbols if sym in all_tables]

result = {
    'count': len(common_symbols),
    'sample': common_symbols[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}}

exec(code, env_args)
