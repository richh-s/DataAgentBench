code = """# Access the correct variable names with colons
# The storage keys use format like "var_functions.query_db:20"
import json
import pandas as pd
import re

# Check if we can access the variables
global_vars = list(globals().keys())
print("Available global variables:")
for var in global_vars[:20]:  # Print first 20 to avoid too much output
    print(f"  {var}")

# The correct way to access is using the string keys directly
# Let's try to load the data properly
pub_data = []
cpc_symbols = []

# Try to access the preview data first
preview_key = 'functions.query_db:20'
cpc_key = 'functions.query_db:24'

if preview_key in globals():
    pub_data = globals()[preview_key]
    print(f"Got publication data from {preview_key}, type: {type(pub_data)}")
    if isinstance(pub_data, str) and pub_data.endswith('.json'):
        with open(pub_data, 'r') as f:
            pub_data = json.load(f)
            print(f"Loaded {len(pub_data)} pub records from file")
else:
    print(f"Key {preview_key} not found in globals")

if cpc_key in globals():
    cpc_symbols = globals()[cpc_key]
    print(f"Got CPC symbols from {cpc_key}, type: {type(cpc_symbols)}")
    if isinstance(cpc_symbols, str) and cpc_symbols.endswith('.json'):
        with open(cpc_symbols, 'r') as f:
            cpc_symbols = json.load(f)
            print(f"Loaded {len(cpc_symbols)} CPC symbols from file")
else:
    print(f"Key {cpc_key} not found in globals")

# If still not found, try the var_ prefix versions
try:
    if not pub_data and 'var_functions.query_db:20' in globals():
        pub_data_var = globals()['var_functions.query_db:20']
        print(f"Got pub data via var_ prefix: {type(pub_data_var)}")
        if isinstance(pub_data_var, str) and pub_data_var.endswith('.json'):
            with open(pub_data_var, 'r') as f:
                pub_data = json.load(f)
        else:
            pub_data = pub_data_var
    
    if not cpc_symbols and 'var_functions.query_db:24' in globals():
        cpc_symbols_var = globals()['var_functions.query_db:24']
        print(f"Got CPC symbols via var_ prefix: {type(cpc_symbols_var)}")
        if isinstance(cpc_symbols_var, str) and cpc_symbols_var.endswith('.json'):
            with open(cpc_symbols_var, 'r') as f:
                cpc_symbols = json.load(f)
        else:
            cpc_symbols = cpc_symbols_var
except Exception as e:
    print(f"Error accessing data: {e}")

print(f"\nFinal data loaded:")
print(f"Publication records: {len(pub_data) if pub_data else 0}")
print(f"CPC symbols: {len(cpc_symbols) if cpc_symbols else 0}")

if pub_data:
    print(f"Sample pub record: {pub_data[0]}")

if cpc_symbols:
    print(f"Sample CPC symbols: {cpc_symbols[:3]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}}

exec(code, env_args)
