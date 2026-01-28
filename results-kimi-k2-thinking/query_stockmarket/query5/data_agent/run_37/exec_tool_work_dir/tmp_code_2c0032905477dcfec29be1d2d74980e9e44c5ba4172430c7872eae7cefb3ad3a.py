code = """import json

# Get all NASDAQ Capital Market symbols
nasdaq_file = locals()['var_functions.query_db:22']
with open(nasdaq_file, 'r') as f:
    nasdaq_stocks = json.load(f)

symbol_to_company = {}
for stock in nasdaq_stocks:
    symbol = stock['Symbol']
    # Extract first sentence for company name
    desc = stock['Company Description']
    if ' specializes in ' in desc:
        company_name = desc.split(' specializes in ')[0]
    elif ' is ' in desc:
        company_name = desc.split(' is ')[0]
    elif ' focuses on ' in desc:
        company_name = desc.split(' focuses on ')[0]
    else:
        company_name = desc
    symbol_to_company[symbol] = company_name

# Get the table names available in stocktrade database
trade_tables_file = locals()['var_functions.list_db:10']
with open(trade_tables_file, 'r') as f:
    available_tables = json.load(f)

# Filter to only symbols that exist in stocktrade database
valid_symbols = []
for symbol in symbol_to_company:
    if symbol in available_tables:
        valid_symbols.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'total_valid_symbols': len(valid_symbols),
    'sample_valid_symbols': valid_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'num_symbols': 86, 'sample_symbols': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': ['ORSNU', 'MLND', 'ORGO', 'FTFT', 'MBNKP', 'HNNA', 'TGLS', 'EYEG', 'CFFA', 'FAMI', 'APEX', 'BCLI', 'MBCN', 'VRRM', 'BWEN', 'HQI', 'CPAAU', 'MMAC', 'EXPC', 'GLG'], 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'nasdaq_symbols_count': 86, 'total_tables_count': 2753, 'available_symbols_count': 86, 'sample_available': ['CFBK', 'SSNT', 'OTEL', 'VVPR', 'MMAC', 'SNSS', 'FTFT', 'ITI', 'BIOC', 'QRHC', 'WHLM', 'PBFS', 'CEMI', 'SES', 'AGMH', 'HQI', 'BOSC', 'TGLS', 'MNPR', 'PFIE']}, 'var_functions.execute_python:14': ['ALACU', 'CPAH', 'VMD', 'CVV', 'MBCN', 'SES', 'NVEE', 'BOSC', 'BLFS', 'LACQ', 'EYEG', 'HNNA', 'VTIQW', 'BWEN', 'ANDA', 'SSNT', 'QRHC', 'XBIOW', 'FNCB', 'PLIN', 'POPE', 'HCCOU', 'CFFA', 'GRNVU', 'NXTD', 'HQI', 'OPTT', 'CBAT', 'CPAAU', 'WHLR', 'SHSP', 'MNPR', 'OTEL', 'BIOC', 'PFIE', 'VVPR', 'WHLM', 'CLRB', 'DZSI', 'ISNS', 'CFBK', 'HRTX', 'ORSNU', 'BCLI', 'PBFS', 'EXPC', 'BHAT', 'VRRM', 'TMSR', 'FAMI', 'VERB', 'CORV', 'IGIC', 'AGMH', 'MLND', 'XPEL', 'MMAC', 'IOTS', 'MNCLU', 'GLG', 'PCSB', 'STKS', 'BKYI', 'ORGO', 'CCCL', 'MCEP', 'FTFT', 'GDYN', 'IDEX', 'PBTS', 'PEIX', 'FSBW', 'ELSE', 'BOTJ', 'GTEC', 'PECK', 'MBNKP', 'CDMOP', 'CUBA', 'CEMI', 'TGLS', 'OPOF', 'APEX', 'ITI', 'AMHC', 'SNSS'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_symbols': 86, 'sample_data': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'], ['BCLI', 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.'], ['BHAT', 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.'], ['BIOC', 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'], ['BKYI', 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'], ['BLFS', 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.']]}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_nasdaq_capital_stocks': 86, 'available_in_trade_db': 86}, 'var_functions.execute_python:26': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_symbols': 86, 'batches': 9, 'sample_batches': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], ['BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB'], ['CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI']]}}

exec(code, env_args)
