code = """import json

pub_data = []
cpc_symbols = []

# Load publication data
try:
    pub_file_path = var_functions.query_db_20
    with open(pub_file_path, 'r') as f:
        pub_data = json.load(f)
    print("Loaded publication data:", len(pub_data), "records")
except Exception as e:
    print("Error with publication data:", str(e))

# Load CPC symbols
try:
    cpc_file_path = var_functions.query_db_24
    with open(cpc_file_path, 'r') as f:
        cpc_symbols = json.load(f)
    print("Loaded CPC symbols:", len(cpc_symbols), "symbols")
except Exception as e:
    print("Error with CPC data:", str(e))

# Check data structure
if pub_data:
    sample = pub_data[0]
    print("Sample keys:", list(sample.keys()))
    print("Sample CPC (first 150 chars):", str(sample.get('cpc', ''))[:150])
    print("Sample date:", sample.get('publication_date', 'N/A'))

if cpc_symbols:
    print("Sample CPC symbol:", cpc_symbols[0])

result = {
    'pub_records': len(pub_data),
    'cpc_symbols': len(cpc_symbols),
    'sample_pub': pub_data[0] if pub_data else None,
    'sample_cpc': cpc_symbols[0] if cpc_symbols else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}}

exec(code, env_args)
