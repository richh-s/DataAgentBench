code = """# Access the correct variable name
# Let's load the available data first
import json

# Try to access the variables - they should be stored with these names
pub_data = None
cpc_symbols = None

# Check if we have the data loaded
if 'var_functions.query_db_20' in globals():
    pub_data_file = var_functions.query_db_20
    print(f"Publication data file: {pub_data_file}")
    if isinstance(pub_data_file, str) and pub_data_file.endswith('.json'):
        with open(pub_data_file, 'r') as f:
            pub_data = json.load(f)
    else:
        pub_data = pub_data_file
else:
    print("Publication data not found")

if 'var_functions.query_db_24' in globals():
    cpc_file = var_functions.query_db_24
    print(f"CPC symbols file: {cpc_file}")
    if isinstance(cpc_file, str) and cpc_file.endswith('.json'):
        with open(cpc_file, 'r') as f:
            cpc_symbols = json.load(f)
    else:
        cpc_symbols = cpc_file
else:
    print("CPC symbols not found")

print(f"Pub data type: {type(pub_data)}")
print(f"CPC symbols type: {type(cpc_symbols)}")

if pub_data:
    print(f"Number of publication records: {len(pub_data)}")
    print(f"First record: {pub_data[0]}")

if cpc_symbols:
    print(f"Number of CPC symbols: {len(cpc_symbols)}")
    print(f"First few symbols: {cpc_symbols[:5]}")

# Store results for next steps
result = {
    'has_pub_data': pub_data is not None,
    'has_cpc_symbols': cpc_symbols is not None,
    'pub_records_count': len(pub_data) if pub_data else 0,
    'cpc_symbols_count': len(cpc_symbols) if cpc_symbols else 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
