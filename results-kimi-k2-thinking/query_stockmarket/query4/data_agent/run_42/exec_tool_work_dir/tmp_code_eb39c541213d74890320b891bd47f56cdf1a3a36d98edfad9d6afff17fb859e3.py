code = """import json

# Load NYSE non-ETF stocks
nyse_path = locals()['var_functions.query_db:40']
with open(nyse_path, 'r') as f:
    nyse_stocks = json.load(f)

symbols = [stock['Symbol'] for stock in nyse_stocks]
company_names = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

print(f"Need to analyze {len(symbols)} NYSE non-ETF stocks")
print("Sample symbols:", symbols[:5])
print("Sample company:", company_names[symbols[0]])

result = {
    'total_stocks': len(symbols),
    'sample_symbols': symbols[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}], 'var_functions.query_db:14': [{'test': 'AAPL'}], 'var_functions.execute_python:24': {'nyse_count': 234, 'tables_count': 2753, 'matching_count': 234, 'matching_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:26': [{'total_days': '0', 'up_days': '0', 'down_days': '0'}], 'var_functions.query_db:28': [{'total_days': '251', 'up_days': '143', 'down_days': '101'}], 'var_functions.query_db:36': [{'symbol': 'AIN', 'total_days': '251', 'up_days': '143', 'down_days': '101'}], 'var_functions.query_db:38': [{'symbol': 'AIV', 'total_days': '251', 'up_days': '118', 'down_days': '128'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:44': [{'symbol': 'AJRD', 'total_days': '251', 'up_days': '123', 'down_days': '123'}]}

exec(code, env_args)
