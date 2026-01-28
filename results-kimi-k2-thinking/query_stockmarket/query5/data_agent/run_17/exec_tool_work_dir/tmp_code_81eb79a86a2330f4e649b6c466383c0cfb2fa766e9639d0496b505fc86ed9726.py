code = """import json

# Load the NASDAQ Capital Market stocks
stockinfo_result = locals()['var_functions.query_db:6']

if isinstance(stockinfo_result, str) and stockinfo_result.endswith('.json'):
    with open(stockinfo_result, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = stockinfo_result

# Create dictionary mapping symbol to company name
symbol_to_company = {item['Symbol']: item['Company Description'].split(',')[0].split(' specializes')[0].split(' is a')[0].split(' operates')[0].split(' provides')[0] for item in stockinfo_data}

print("__RESULT__:")
print(json.dumps({"symbol_mapping": symbol_to_company, "count": len(symbol_to_company)}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:4': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}], 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)
