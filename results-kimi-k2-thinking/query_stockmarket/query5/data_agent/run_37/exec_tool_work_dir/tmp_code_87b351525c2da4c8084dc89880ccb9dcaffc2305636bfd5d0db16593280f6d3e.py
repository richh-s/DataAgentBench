code = """import json

# Get the lists
nasdaq_result_key = 'var_functions.query_db:0'
result_file = locals()[nasdaq_result_key]
with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

nasdaq_symbols = set([stock['Symbol'] for stock in nasdaq_capital_stocks])
company_names = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_capital_stocks}

trade_result_key = 'var_functions.list_db:10'
result_file2 = locals()[trade_result_key]
with open(result_file2, 'r') as f:
    all_tables = json.load(f)

# Process 5 symbols at a time for efficiency
symbols_to_process = list(nasdaq_symbols.intersection(all_tables))
print('__RESULT__:')
print(json.dumps(symbols_to_process))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'num_symbols': 86, 'sample_symbols': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': ['ORSNU', 'MLND', 'ORGO', 'FTFT', 'MBNKP', 'HNNA', 'TGLS', 'EYEG', 'CFFA', 'FAMI', 'APEX', 'BCLI', 'MBCN', 'VRRM', 'BWEN', 'HQI', 'CPAAU', 'MMAC', 'EXPC', 'GLG'], 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'nasdaq_symbols_count': 86, 'total_tables_count': 2753, 'available_symbols_count': 86, 'sample_available': ['CFBK', 'SSNT', 'OTEL', 'VVPR', 'MMAC', 'SNSS', 'FTFT', 'ITI', 'BIOC', 'QRHC', 'WHLM', 'PBFS', 'CEMI', 'SES', 'AGMH', 'HQI', 'BOSC', 'TGLS', 'MNPR', 'PFIE']}}

exec(code, env_args)
