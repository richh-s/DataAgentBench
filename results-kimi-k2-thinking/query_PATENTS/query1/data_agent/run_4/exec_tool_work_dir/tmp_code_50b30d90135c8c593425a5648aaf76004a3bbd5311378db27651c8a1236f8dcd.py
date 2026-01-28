code = """import json

# Get level 5 CPC symbols from the query result
level5_symbols = []

# Try to load from file first
try:
    level5_file = '/tmp/tmpj9t1b8_a.json'
    with open(level5_file, 'r') as f:
        level5_data = json.load(f)
    level5_symbols = [item['symbol'] for item in level5_data]
    print(f"Loaded {len(level5_symbols)} level 5 CPC symbols from file")
except:
    # Fallback to using the variable
    try:
        level5_data = var_functions.query_db_58
        level5_symbols = [item['symbol'] for item in level5_data]
        print(f"Loaded {len(level5_symbols)} level 5 CPC symbols from variable")
    except:
        # Use the sample data
        level5_data = var_functions.query_db_40
        level5_symbols = [item['symbol'] for item in level5_data]
        print(f"Loaded {len(level5_symbols)} level 5 CPC symbols from sample")

# Create a set for fast lookup
level5_set = set(level5_symbols)
print(f"Total level 5 CPC symbols: {len(level5_set)}")
print(f"Sample symbols: {sorted(list(level5_set))[:10]}")

result = {
    'level5_symbols_count': len(level5_set),
    'sample_symbols': sorted(list(level5_set))[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'error': 'no_publication_files'}, 'var_functions.query_db:48': [{'total_patents': '277813'}], 'var_functions.query_db:50': [], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'error': 'no_files'}}

exec(code, env_args)
