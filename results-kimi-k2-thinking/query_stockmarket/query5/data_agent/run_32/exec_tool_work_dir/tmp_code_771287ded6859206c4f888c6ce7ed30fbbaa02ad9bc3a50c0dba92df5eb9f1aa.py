code = """import json
import os

# Load all NASDAQ Capital Market data
nasdaq_file = locals()['var_functions.query_db:0']
with open(nasdaq_file, 'r') as f:
    nasdaq_stocks = json.load(f)

# Create a clean company name mapping (extract just the company name before first period)
symbol_to_company = {}
for stock in nasdaq_stocks:
    symbol = stock['Symbol']
    desc = stock.get('Company Description', '')
    # Extract company name (text before first period)
    company_name = desc.split('.')[0].strip() if desc else symbol
    symbol_to_company[symbol] = company_name

print(f"Total NASDAQ Capital Market stocks: {len(symbol_to_company)}")
print(f"Sample: {list(symbol_to_company.items())[:5]}")

print("__RESULT__:")
print(json.dumps({
    "total_stocks": len(symbol_to_company),
    "symbols": list(symbol_to_company.keys())
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:4': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:9': {'total_nasdaq_capital_stocks': 86, 'total_tables_in_db': 2753, 'available_symbols': 86, 'sample_symbols': ['HCCOU', 'IDEX', 'PECK', 'XBIOW', 'MNCLU', 'MMAC', 'PBFS', 'AMHC', 'PFIE', 'AGMH']}, 'var_functions.execute_python:12': {'type': "<class 'dict'>", 'data_keys': ['total_nasdaq_capital_stocks', 'total_tables_in_db', 'available_symbols', 'sample_symbols']}, 'var_functions.query_db:14': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:20': {'result_data_type': "<class 'dict'>"}, 'var_functions.query_db:22': [{'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}], 'var_functions.execute_python:24': {'count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.execute_python:30': {'total_nasdaq_capital': 86, 'available_in_db': 86, 'sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'file_path': '/tmp/nasdaq_symbols.json'}, 'var_functions.execute_python:32': {'total_symbols': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'symbol': 'AGMH', 'total_days': 252, 'high_volatility_days': 13, 'company': 'AGM Group Holdings Inc'}}

exec(code, env_args)
