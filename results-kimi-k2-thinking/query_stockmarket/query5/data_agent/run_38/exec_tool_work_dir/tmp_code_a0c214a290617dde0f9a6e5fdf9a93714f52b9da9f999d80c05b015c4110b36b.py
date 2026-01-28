code = """import json

# Load the full list of tickers
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

# Create a mapping of ticker to company name
company_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
tickers = list(company_map.keys())

print('__RESULT__:')
print(json.dumps({
    'tickers': tickers,
    'count': len(tickers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_capital_market': 86, 'total_trade_tables': 2753, 'common_tickers_count': 86, 'sample_common': ['PLIN', 'FAMI', 'MBCN', 'NXTD', 'MNCLU', 'PFIE', 'NVEE', 'IOTS', 'XBIOW', 'EXPC']}, 'var_functions.query_db:10': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:12': ['PLIN', 'FAMI', 'MBCN', 'NXTD', 'MNCLU', 'PFIE', 'NVEE', 'IOTS', 'XBIOW', 'EXPC']}

exec(code, env_args)
