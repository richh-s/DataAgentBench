code = """import json

# Get NASDAQ Capital Market symbols
stockinfo_file = locals()['var_functions.query_db:0']
with open(stockinfo_file, 'r') as f:
    nasdaq_capital_data = json.load(f)

# Create symbol to company name mapping
symbol_company_map = {}
for row in nasdaq_capital_data:
    # Extract just the company name (remove description after first sentence if possible)
    full_desc = row['Company Description']
    company_name = full_desc.split(' specializes in')[0].split(' is ')[0].split(' operates ')[0]
    symbol_company_map[row['Symbol']] = company_name

print('__RESULT__:')
print(json.dumps({
    'symbols_with_companies': len(symbol_company_map),
    'sample': dict(list(symbol_company_map.items())[:5])
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'symbol_count': 86, 'first_few_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'company_names_sample': {'AGMH': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'ALACU': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'AMHC': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_nasdaq_capital_symbols': 86, 'symbols_with_tables': 86, 'first_few_with_tables': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:10': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:12': {'message': 'Ready to process data', 'symbol_count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:14': {'total_symbols': 86, 'symbols_to_check': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'sample_company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, 'var_functions.execute_python:16': {'query_size_chars': 8511, 'number_of_unions': 86, 'sample_query_part': "SELECT 'AGMH' as symbol, Date, Open, High, Low, Close FROM AGMH WHERE Date LIKE '%2019%' UNION ALL SELECT 'ALACU' as symbol, Date, Open, High, Low, Close FROM ALACU WHERE Date LIKE '%2019%'"}}

exec(code, env_args)
