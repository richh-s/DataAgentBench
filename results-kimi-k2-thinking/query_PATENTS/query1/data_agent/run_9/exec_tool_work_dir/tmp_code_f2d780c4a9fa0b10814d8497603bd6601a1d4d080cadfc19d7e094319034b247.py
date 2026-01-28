code = """# Access the correct variable names without f-string issues
import json
import pandas as pd
import re

# Check available variables
all_vars = list(globals().keys())
print("Available variables:")
var_count = 0
for var in all_vars:
    if var.startswith('var_') or var.startswith('functions.query_db'):
        print(f"  {var}")
        var_count += 1
        if var_count > 30:  # Limit output
            break

# Try to load data from the file paths
data_loaded = False

# Try different possible keys
candidate_keys = [
    'var_functions.query_db:20',
    'var_functions.query_db:24',
    'functions.query_db:20',
    'functions.query_db:24',
    'var_functions.query_db_20',
    'var_functions.query_db_24'
]

pub_data = []
cpc_symbols = []

for key in candidate_keys:
    try:
        if key in globals():
            value = globals()[key]
            print(f"Found key {key}: {type(value)}")
            
            if isinstance(value, str) and value.endswith('.json'):
                with open(value, 'r') as f:
                    loaded = json.load(f)
                print(f"Loaded {len(loaded)} items from {key}")
                
                if 'cpc' in str(loaded[0]) and 'publication_date' in str(loaded[0]):
                    pub_data = loaded
                    print(f"Set as pub_data: {len(pub_data)} records")
                elif 'symbol' in str(loaded[0]):
                    cpc_symbols = loaded
                    print(f"Set as cpc_symbols: {len(cpc_symbols)} records")
            else:
                # It's already the data
                if 'cpc' in str(value[0]) and 'publication_date' in str(value[0]):
                    pub_data = value
                    print(f"Set as pub_data: {len(pub_data)} records")
                elif 'symbol' in str(value[0]):
                    cpc_symbols = value
                    print(f"Set as cpc_symbols: {len(cpc_symbols)} records")
    except Exception as e:
        print(f"Error with {key}: {e}")

print(f"\nResults:")
print(f"pub_data: {len(pub_data)} records")
print(f"cpc_symbols: {len(cpc_symbols)} records")

if pub_data:
    print(f"Sample pub record: {pub_data[0]}")

if cpc_symbols:
    print(f"Sample cpc record: {cpc_symbols[0]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}}

exec(code, env_args)
