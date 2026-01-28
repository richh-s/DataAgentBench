code = """# Simple approach - just load and check variables
import json

# Check what variables are available
print("Checking for variables with 'functions.query_db' in name...")

pub_data = None
cpc_symbols = None

# Try to access the publication data
for name in list(globals().keys()):
    if 'query_db:20' in name:
        print(f"Found variable: {name}")
        value = globals()[name]
        print(f"Type: {type(value)}")
        if isinstance(value, str) and value.endswith('.json'):
            try:
                with open(value, 'r') as f:
                    pub_data = json.load(f)
                print(f"Loaded pub_data with {len(pub_data)} records")
            except Exception as e:
                print(f"Error loading from file: {e}")
        else:
            pub_data = value
            print(f"Set pub_data with {len(pub_data)} records")
        break

# Try to access CPC symbols
for name in list(globals().keys()):
    if 'query_db:24' in name:
        print(f"Found variable: {name}")
        value = globals()[name]
        print(f"Type: {type(value)}")
        if isinstance(value, str) and value.endswith('.json'):
            try:
                with open(value, 'r') as f:
                    cpc_symbols = json.load(f)
                print(f"Loaded cpc_symbols with {len(cpc_symbols)} records")
            except Exception as e:
                print(f"Error loading from file: {e}")
        else:
            cpc_symbols = value
            print(f"Set cpc_symbols with {len(cpc_symbols)} records")
        break

print("=== SUMMARY ===")
print(f"Publication data loaded: {pub_data is not None}")
print(f"CPC symbols loaded: {cpc_symbols is not None}")

if pub_data:
    print(f"Sample publication record: {pub_data[0]}")
if cpc_symbols:
    print(f"Sample CPC symbol: {cpc_symbols[0]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}}

exec(code, env_args)
