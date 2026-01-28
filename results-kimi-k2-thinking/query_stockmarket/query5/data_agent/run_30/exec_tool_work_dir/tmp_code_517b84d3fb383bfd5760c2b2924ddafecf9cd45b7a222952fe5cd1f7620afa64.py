code = """import json

# Read the NASDAQ Capital Market stocks
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Create symbol list and company name mapping
symbols = []
company_names = {}
for stock in nasdaq_capital_stocks:
    symbol = stock['Symbol']
    # Extract company name from description (usually before first period or 'specializes'/'focuses'/'operates')
    desc = stock['Company Description']
    company_name = desc
    if '.' in desc:
        company_name = desc.split('.')[0]
    elif ' specializes' in desc:
        company_name = desc.split(' specializes')[0]
    elif ' focuses' in desc:
        company_name = desc.split(' focuses')[0]
    elif ' operates' in desc:
        company_name = desc.split(' operates')[0]
    
    symbols.append(symbol)
    company_names[symbol] = company_name

print('Processing', len(symbols), 'NASDAQ Capital Market stocks')

# We'll build queries for each stock and track results
stock_volatility_data = []

# For now, let's just prepare the structure and show what we have
print('Sample symbols and companies:')
for i in range(min(5, len(symbols))):
    sym = symbols[i]
    print(f"  {sym}: {company_names[sym]}")

result = {
    'total_stocks': len(symbols),
    'sample_companies': list(company_names.items())[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:8': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:10': {'total_stocks': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:16': [{'high_vol_days': '13'}], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': {'total_symbols': 86, 'test_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB'], 'sample_company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, 'var_functions.query_db:22': [{'total_days': '252', 'high_vol_days': '13.0'}]}

exec(code, env_args)
