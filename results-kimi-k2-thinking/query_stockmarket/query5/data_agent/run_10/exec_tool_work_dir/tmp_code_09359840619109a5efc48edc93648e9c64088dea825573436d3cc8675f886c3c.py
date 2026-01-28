code = """import json

# Get the NASDAQ Capital Market tickers
nasdaq_tickers = locals()['var_functions.execute_python:24']
print("Number of NASDAQ Capital Market tickers:", len(nasdaq_tickers))
print("Sample:", nasdaq_tickers[:10])

# Get the list of tables from stocktrade database
tables_result = locals()['var_functions.list_db:18']
print("Type of tables result:", type(tables_result))

# Parse tables result
if isinstance(tables_result, str):
    if '.json' in tables_result:
        with open(tables_result, 'r') as f:
            all_tables = json.load(f)
    else:
        all_tables = json.loads(tables_result)
else:
    all_tables = tables_result

print("Total tables in stocktrade database:", len(all_tables))
print("Sample tables:", all_tables[:10])

# Find intersection
existing_tickers = [ticker for ticker in nasdaq_tickers if ticker in all_tables]
print("Found", len(existing_tickers), "tickers with data")
print("Sample existing tickers:", existing_tickers[:10])

print('__RESULT__:')
print(json.dumps(existing_tickers))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'num_companies': 0, 'sample': []}, 'var_functions.query_db:12': [{'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Market Category': 'G'}, {'Market Category': 'Q'}, {'Market Category': 'S'}], 'var_functions.query_db:14': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:24': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
