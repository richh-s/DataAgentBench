code = """import json

# Read the results from the query
query_result_path = locals()['var_functions.query_db:30']
with open(query_result_path, 'r') as f:
    results = json.load(f)

# Read the symbol descriptions
nasdaq_data_path = locals()['var_functions.execute_python:16']
with open(nasdaq_data_path, 'r') as f:
    nasdaq_data = json.load(f)

symbol_to_desc = nasdaq_data['symbol_to_desc']

# Get top 5
top_5 = results[:5]
print("Top 5 symbols:", top_5)

# Map to company descriptions and extract company names
company_info = []
for item in top_5:
    symbol = item['Symbol']
    high_vol_days = item['HighVolDays']
    company_desc = symbol_to_desc.get(symbol, "Description not found")
    
    # Extract company name (first sentence or up to first period)
    company_name = company_desc
    if '.' in company_desc:
        company_name = company_desc.split('.')[0] + '.'
    
    company_info.append({
        'symbol': symbol,
        'high_vol_days': high_vol_days,
        'company_description': company_desc,
        'company_name': company_name
    })

print("Company info extracted:")
for info in company_info:
    print(f"{info['symbol']}: {info['high_vol_days']} days - {info['company_name']}")

result = company_info

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'Symbol': 'PECK', 'HighVolDays': '19'}], 'var_functions.query_db:24': [{'Symbol': 'CBAT', 'HighVolDays': '23'}, {'Symbol': 'FAMI', 'HighVolDays': '23'}, {'Symbol': 'AGMH', 'HighVolDays': '13'}, {'Symbol': 'BHAT', 'HighVolDays': '10'}, {'Symbol': 'BOSC', 'HighVolDays': '3'}], 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.query_db:30': [{'Symbol': 'SES', 'HighVolDays': '51'}, {'Symbol': 'GLG', 'HighVolDays': '42'}, {'Symbol': 'TMSR', 'HighVolDays': '40'}, {'Symbol': 'FAMI', 'HighVolDays': '23'}, {'Symbol': 'CBAT', 'HighVolDays': '23'}, {'Symbol': 'PECK', 'HighVolDays': '19'}, {'Symbol': 'WHLR', 'HighVolDays': '15'}, {'Symbol': 'MCEP', 'HighVolDays': '14'}, {'Symbol': 'AGMH', 'HighVolDays': '13'}, {'Symbol': 'BHAT', 'HighVolDays': '10'}]}

exec(code, env_args)
