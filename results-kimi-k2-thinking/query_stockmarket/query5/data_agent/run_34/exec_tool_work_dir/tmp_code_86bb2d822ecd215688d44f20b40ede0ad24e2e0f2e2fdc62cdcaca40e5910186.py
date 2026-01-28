code = """import json

# Read NASDAQ Capital Market companies
nasdaq_file = locals()['var_functions.query_db:0']
with open(nasdaq_file, 'r') as f:
    nasdaq_companies = json.load(f)

# Read available tables in stocktrade_database
tables_file = locals()['var_functions.list_db:6']
with open(tables_file, 'r') as f:
    trade_tables = json.load(f)

# Create mapping of tickers to company names
company_map = {company['Symbol']: company['Company Description'] for company in nasdaq_companies}

# Find intersection
tickers = list(company_map.keys())
available_tickers = [ticker for ticker in tickers if ticker in trade_tables]

print('__RESULT__:')
print(json.dumps({
    'available_tickers': available_tickers,
    'total_nasdaq': len(tickers),
    'available_count': len(available_tickers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
