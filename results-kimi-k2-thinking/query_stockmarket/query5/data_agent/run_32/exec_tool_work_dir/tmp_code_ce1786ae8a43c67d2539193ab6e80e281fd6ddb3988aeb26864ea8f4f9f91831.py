code = """import json
import os

# Load NASDAQ Capital Market stocks
nasdaq_file = locals()['var_functions.query_db:0']
with open(nasdaq_file, 'r') as f:
    nasdaq_stocks = json.load(f)

# Load available tables in stocktrade_database
tables_file = locals()['var_functions.list_db:6']
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Create mapping and find intersection
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}
nasdaq_symbols = list(symbol_to_company.keys())

# Find available symbols (intersection)
available_symbols = []
for symbol in nasdaq_symbols:
    if symbol in all_tables:
        available_symbols.append(symbol)

print("NASDAQ Capital stocks:", len(nasdaq_symbols))
print("Available in trade DB:", len(available_symbols))
print("Sample symbols:", available_symbols[:10])

# Save results to file for next steps
result = {
    'symbols': available_symbols,
    'company_map': symbol_to_company
}

# Write to temp file
with open('/tmp/nasdaq_symbols.json', 'w') as f:
    json.dump(result, f)

print("__RESULT__:")
print(json.dumps({
    "total_nasdaq_capital": len(nasdaq_symbols),
    "available_in_db": len(available_symbols),
    "sample": available_symbols[:5],
    "file_path": "/tmp/nasdaq_symbols.json"
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:4': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:9': {'total_nasdaq_capital_stocks': 86, 'total_tables_in_db': 2753, 'available_symbols': 86, 'sample_symbols': ['HCCOU', 'IDEX', 'PECK', 'XBIOW', 'MNCLU', 'MMAC', 'PBFS', 'AMHC', 'PFIE', 'AGMH']}, 'var_functions.execute_python:12': {'type': "<class 'dict'>", 'data_keys': ['total_nasdaq_capital_stocks', 'total_tables_in_db', 'available_symbols', 'sample_symbols']}, 'var_functions.query_db:14': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:20': {'result_data_type': "<class 'dict'>"}, 'var_functions.query_db:22': [{'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}], 'var_functions.execute_python:24': {'count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json'}

exec(code, env_args)
