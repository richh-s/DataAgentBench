code = """import json

# Get NASDAQ Capital Market symbols
nasdaq_result_key = 'var_functions.query_db:0'
result_file = locals()[nasdaq_result_key]
with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

nasdaq_symbols = set([stock['Symbol'] for stock in nasdaq_capital_stocks])
company_names = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_capital_stocks}

# Get available tables in stocktrade database
trade_result_key = 'var_functions.list_db:10'
result_file2 = locals()[trade_result_key]
with open(result_file2, 'r') as f:
    all_tables = json.load(f)

# Find intersection
available_symbols = list(nasdaq_symbols.intersection(all_tables))

print('__RESULT__:')
print(json.dumps({
    'nasdaq_symbols_count': len(nasdaq_symbols),
    'total_tables_count': len(all_tables),
    'available_symbols_count': len(available_symbols),
    'sample_available': available_symbols[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'num_symbols': 86, 'sample_symbols': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': ['ORSNU', 'MLND', 'ORGO', 'FTFT', 'MBNKP', 'HNNA', 'TGLS', 'EYEG', 'CFFA', 'FAMI', 'APEX', 'BCLI', 'MBCN', 'VRRM', 'BWEN', 'HQI', 'CPAAU', 'MMAC', 'EXPC', 'GLG'], 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json'}

exec(code, env_args)
