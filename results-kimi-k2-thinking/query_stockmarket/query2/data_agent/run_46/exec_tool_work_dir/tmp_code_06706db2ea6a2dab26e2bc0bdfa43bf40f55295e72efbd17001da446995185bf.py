code = """import json
import os

# Get the available ETFs list from the previous result
available_etfs_file = locals()['var_functions.execute_python:8']
# Since execute_python result is stored directly as JSON, read it appropriately
try:
    with open(available_etfs_file, 'r') as f:
        available_data = json.load(f)
    available_etfs = available_data['sample_available_etfs'][:20]  # Start with a smaller batch
except:
    # If it's not a file path but a direct result, use it directly
    # Actually, execute_python stores the result itself, so we need to access the previous result
    # Let me just use the count from the previous output and create a manageable batch
    etfs_file = locals()['var_functions.query_db:5']
    with open(etfs_file, 'r') as f:
        etfs_data = json.load(f)
    available_etfs = [item['Symbol'] for item in etfs_data][:20]  # Start with 20 ETFs

print('__RESULT__:')
print(json.dumps({
    'etfs_to_check': available_etfs,
    'count': len(available_etfs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_nyse_arca_etfs': 1435, 'available_etfs_count': 1435, 'sample_available_etfs': ['AOR', 'IBDL', 'SBM', 'IIGD', 'XTL', 'DIV', 'IVV', 'LGLV', 'HEWC', 'URTH']}}

exec(code, env_args)
