code = """import json

# Load common symbols from previous result
common_symbols = locals()['var_functions.execute_python:38']

# Load company names from NASDAQ Capital data
nasdaq_cap_file = locals()['var_functions.query_db:30']
with open(nasdaq_cap_file, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

company_names = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_cap_stocks}

print('Loaded', len(common_symbols), 'common symbols')
print('Loaded', len(company_names), 'company descriptions')
print('Sample common symbols:', common_symbols[:5])
print('__RESULT__:')
print(json.dumps({'common_symbols_count': len(common_symbols), 'sample_symbols': common_symbols[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.list_db:7': ['stockinfo'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:24': 'file_storage/functions.list_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'var_functions.execute_python:38': ['WHLR', 'AGMH', 'IOTS', 'CLRB', 'XBIOW', 'ITI', 'GTEC', 'GDYN', 'HQI', 'APEX', 'SSNT', 'MNPR', 'HRTX', 'FTFT', 'SNSS', 'POPE', 'PBFS', 'TGLS', 'FAMI', 'MNCLU', 'PEIX', 'HCCOU', 'PBTS', 'ANDA', 'ALACU', 'OTEL', 'VMD', 'CBAT', 'HNNA', 'ISNS', 'CFFA', 'MBNKP', 'OPOF', 'BCLI', 'CVV', 'VRRM', 'AMHC', 'LACQ', 'PECK', 'CORV', 'NXTD', 'BHAT', 'MLND', 'BOTJ', 'VVPR', 'CPAAU', 'BLFS', 'CEMI', 'CFBK', 'TMSR', 'SES', 'NVEE', 'ELSE', 'DZSI', 'OPTT', 'ORGO', 'MCEP', 'BIOC', 'FSBW', 'WHLM', 'GLG', 'CCCL', 'BOSC', 'MMAC', 'BWEN', 'GRNVU', 'PCSB', 'VERB', 'VTIQW', 'ORSNU', 'QRHC', 'PFIE', 'MBCN', 'FNCB', 'CPAH', 'BKYI', 'EXPC', 'XPEL', 'CUBA', 'PLIN', 'EYEG', 'IGIC', 'CDMOP', 'SHSP', 'IDEX', 'STKS']}

exec(code, env_args)
