code = """import json

# Check available variables
available = [name for name in globals().keys() if 'query_db' in name]
print("Available variables containing 'query_db':")
for name in available:
    print(f"  {name}")

# Load publication data
try:
    pub_data_file = var_functions.query_db_20
    print(f"\nLoading pub data from file: {pub_data_file}")
    with open(pub_data_file, 'r') as f:
        pub_data = json.load(f)
    print(f"Loaded {len(pub_data)} publication records")
except Exception as e:
    print(f"Error loading publication data: {e}")
    pub_data = []

# Load CPC symbols
try:
    cpc_file = var_functions.query_db_24
    print(f"\nLoading CPC symbols from file: {cpc_file}")
    with open(cpc_file, 'r') as f:
        cpc_symbols = json.load(f)
    print(f"Loaded {len(cpc_symbols)} CPC symbols")
except Exception as e:
    print(f"Error loading CPC symbols: {e}")
    cpc_symbols = []

print("\n=== Data Summary ===")
print(f"Publication records: {len(pub_data)}")
print(f"CPC symbols: {len(cpc_symbols)}")

if pub_data:
    print(f"\nSample publication record:")
    print(json.dumps(pub_data[0])[:200])

if cpc_symbols:
    print(f"\nSample CPC symbols:")
    print(json.dumps(cpc_symbols[:3]))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}}

exec(code, env_args)
