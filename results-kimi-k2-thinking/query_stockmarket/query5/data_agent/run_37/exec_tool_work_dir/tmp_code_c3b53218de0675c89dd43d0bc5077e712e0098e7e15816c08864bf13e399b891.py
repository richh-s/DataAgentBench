code = """import json

# Get NASDAQ Capital Market symbols and company names
nasdaq_capital_file = locals()['var_functions.query_db:18']
with open(nasdaq_capital_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Create a dictionary of symbol to company name
company_names = {}
symbols_list = []
for stock in nasdaq_capital_stocks:
    symbol = stock['Symbol']
    company_names[symbol] = stock['company_name']
    symbols_list.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols_list),
    'sample_data': list(company_names.items())[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'num_symbols': 86, 'sample_symbols': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': ['ORSNU', 'MLND', 'ORGO', 'FTFT', 'MBNKP', 'HNNA', 'TGLS', 'EYEG', 'CFFA', 'FAMI', 'APEX', 'BCLI', 'MBCN', 'VRRM', 'BWEN', 'HQI', 'CPAAU', 'MMAC', 'EXPC', 'GLG'], 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'nasdaq_symbols_count': 86, 'total_tables_count': 2753, 'available_symbols_count': 86, 'sample_available': ['CFBK', 'SSNT', 'OTEL', 'VVPR', 'MMAC', 'SNSS', 'FTFT', 'ITI', 'BIOC', 'QRHC', 'WHLM', 'PBFS', 'CEMI', 'SES', 'AGMH', 'HQI', 'BOSC', 'TGLS', 'MNPR', 'PFIE']}, 'var_functions.execute_python:14': ['ALACU', 'CPAH', 'VMD', 'CVV', 'MBCN', 'SES', 'NVEE', 'BOSC', 'BLFS', 'LACQ', 'EYEG', 'HNNA', 'VTIQW', 'BWEN', 'ANDA', 'SSNT', 'QRHC', 'XBIOW', 'FNCB', 'PLIN', 'POPE', 'HCCOU', 'CFFA', 'GRNVU', 'NXTD', 'HQI', 'OPTT', 'CBAT', 'CPAAU', 'WHLR', 'SHSP', 'MNPR', 'OTEL', 'BIOC', 'PFIE', 'VVPR', 'WHLM', 'CLRB', 'DZSI', 'ISNS', 'CFBK', 'HRTX', 'ORSNU', 'BCLI', 'PBFS', 'EXPC', 'BHAT', 'VRRM', 'TMSR', 'FAMI', 'VERB', 'CORV', 'IGIC', 'AGMH', 'MLND', 'XPEL', 'MMAC', 'IOTS', 'MNCLU', 'GLG', 'PCSB', 'STKS', 'BKYI', 'ORGO', 'CCCL', 'MCEP', 'FTFT', 'GDYN', 'IDEX', 'PBTS', 'PEIX', 'FSBW', 'ELSE', 'BOTJ', 'GTEC', 'PECK', 'MBNKP', 'CDMOP', 'CUBA', 'CEMI', 'TGLS', 'OPOF', 'APEX', 'ITI', 'AMHC', 'SNSS'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
