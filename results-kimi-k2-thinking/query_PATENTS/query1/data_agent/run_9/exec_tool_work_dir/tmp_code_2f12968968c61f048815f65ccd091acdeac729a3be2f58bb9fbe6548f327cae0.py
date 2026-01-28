code = """import json

pub_data = []
cpc_symbols = []

# Load data from files
try:
    pub_file = var_functions.query_db_20
    with open(pub_file, 'r') as f:
        pub_data = json.load(f)
except Exception as e:
    print("Error loading pub data:", str(e))

try:
    cpc_file = var_functions.query_db_24
    with open(cpc_file, 'r') as f:
        cpc_symbols = json.load(f)
except Exception as e:
    print("Error loading cpc data:", str(e))

print("Publication records:", len(pub_data))
print("CPC symbols:", len(cpc_symbols))

if pub_data:
    first_rec = pub_data[0]
    print("Sample pub record keys:", list(first_rec.keys()))
    print("Sample cpc field (truncated):", str(first_rec.get('cpc', ''))[:100])
    print("Sample date:", first_rec.get('publication_date', 'N/A'))

if cpc_symbols:
    print("Sample CPC symbol:", cpc_symbols[0])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}}

exec(code, env_args)
