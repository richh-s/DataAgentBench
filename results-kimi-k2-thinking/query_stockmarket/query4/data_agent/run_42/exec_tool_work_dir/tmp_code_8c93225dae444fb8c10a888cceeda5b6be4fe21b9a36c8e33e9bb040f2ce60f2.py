code = """import json

# Load the matching stocks data
matching_stocks_path = var_functions.execute_python:24
with open(matching_stocks_path, 'r') as f:
    data = json.load(f)

matching_symbols = data['matching_symbols']
all_matching_stocks = data['stocks'] if 'stocks' in data else matching_symbols

print(f"Total stocks to analyze: {len(matching_symbols)}")
print("First 10 symbols:", matching_symbols[:10])

result = {
    'count': len(matching_symbols),
    'symbols': matching_symbols[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}], 'var_functions.query_db:14': [{'test': 'AAPL'}], 'var_functions.execute_python:24': {'nyse_count': 234, 'tables_count': 2753, 'matching_count': 234, 'matching_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:26': [{'total_days': '0', 'up_days': '0', 'down_days': '0'}], 'var_functions.query_db:28': [{'total_days': '251', 'up_days': '143', 'down_days': '101'}]}

exec(code, env_args)
