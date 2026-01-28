code = """import json
import pandas as pd

# Load symbols from storage
symbols_key = 'var_functions.query_db:6'
symbols_data = locals().get(symbols_key, [])

# Handle file path case
if isinstance(symbols_data, str) and symbols_data.endswith('.json'):
    with open(symbols_data, 'r') as f:
        symbols_data = json.load(f)

symbols = [item['Symbol'] for item in symbols_data]
print(f"Total NYSE Arca ETFs to check: {len(symbols)}")

# Store qualifying ETFs
qualifying_etfs = []

# Process in batches to be efficient
results_summary = {
    'total_checked': 0,
    'total_qualifying': 0,
    'qualifying_symbols': [],
    'errors': []
}

print("__RESULT__:")
print(json.dumps({
    "status": "ready_to_check", 
    "count": len(symbols), 
    "symbols_sample": symbols[:20]
}))"""

env_args = {'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json'}

exec(code, env_args)
