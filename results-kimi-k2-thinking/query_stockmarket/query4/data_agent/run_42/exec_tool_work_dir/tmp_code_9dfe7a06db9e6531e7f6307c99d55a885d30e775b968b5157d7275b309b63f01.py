code = """import json

# Get analysis results from previous query  
analysis_result = locals()['var_functions.query_db:62']

# Handle both list and file path cases
if isinstance(analysis_result, str):
    with open(analysis_result, 'r') as f:
        stock_analysis = json.load(f)
else:
    stock_analysis = analysis_result

print(f"Found {len(stock_analysis)} stocks with more up days than down days")

# Get NYSE companies data
nyse_result = locals()['var_functions.query_db:58']
if isinstance(nyse_result, str):
    with open(nyse_result, 'r') as f:
        nyse_companies = json.load(f)
else:
    nyse_companies = nyse_result

# Create company name lookup
company_names = {}
for item in nyse_companies:
    company_names[item['Symbol']] = item['company_name']

# Add company names and calculate differences
for stock in stock_analysis:
    symbol = stock['symbol']
    stock['company_name'] = company_names.get(symbol, 'Unknown Company')
    stock['diff'] = int(stock['up_days']) - int(stock['down_days'])

print("Current ranking:")
for s in stock_analysis:
    print(f"{s['symbol']}: {s['up_days']} up vs {s['down_days']} down ({s['diff']}) - {s['company_name'][:50]}...")

# Check if we have top 5
if len(stock_analysis) >= 5:
    top_5 = stock_analysis[:5]
    print("\\nTOP 5 STOCKS:")
    for i, stock in enumerate(top_5, 1):
        print(f"{i}. {stock['company_name']}")

result = {
    'stocks': stock_analysis,
    'count': len(stock_analysis)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}], 'var_functions.query_db:14': [{'test': 'AAPL'}], 'var_functions.execute_python:24': {'nyse_count': 234, 'tables_count': 2753, 'matching_count': 234, 'matching_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:26': [{'total_days': '0', 'up_days': '0', 'down_days': '0'}], 'var_functions.query_db:28': [{'total_days': '251', 'up_days': '143', 'down_days': '101'}], 'var_functions.query_db:36': [{'symbol': 'AIN', 'total_days': '251', 'up_days': '143', 'down_days': '101'}], 'var_functions.query_db:38': [{'symbol': 'AIV', 'total_days': '251', 'up_days': '118', 'down_days': '128'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:44': [{'symbol': 'AJRD', 'total_days': '251', 'up_days': '123', 'down_days': '123'}], 'var_functions.execute_python:46': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:48': 'file_storage/functions.execute_python:48.json', 'var_functions.query_db:50': [{'symbol': 'AL', 'total_days': '251', 'up_days': '131', 'down_days': '117'}], 'var_functions.execute_python:52': {'count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:54': {'count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:56': [{'symbol': 'AMP', 'total_days': '251', 'up_days': '141', 'down_days': '110'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': [{'symbol': 'AMN', 'total_days': '251', 'up_days': '134', 'down_days': '111'}], 'var_functions.query_db:62': [{'symbol': 'AIN', 'total_days': '251', 'up_days': '143', 'down_days': '101'}, {'symbol': 'AMP', 'total_days': '251', 'up_days': '141', 'down_days': '110'}, {'symbol': 'CRM', 'total_days': '251', 'up_days': '137', 'down_days': '113'}, {'symbol': 'AMN', 'total_days': '251', 'up_days': '134', 'down_days': '111'}, {'symbol': 'AL', 'total_days': '251', 'up_days': '131', 'down_days': '117'}, {'symbol': 'AMT', 'total_days': '251', 'up_days': '128', 'down_days': '123'}]}

exec(code, env_args)
