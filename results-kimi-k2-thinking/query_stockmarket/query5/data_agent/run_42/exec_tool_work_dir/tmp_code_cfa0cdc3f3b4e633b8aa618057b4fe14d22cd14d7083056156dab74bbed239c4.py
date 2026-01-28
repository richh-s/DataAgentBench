code = """import json

# Load the list of all tables from stocktrade_database
all_tables_file = locals()['var_functions.list_db:5']
with open(all_tables_file, 'r') as f:
    all_tables = json.load(f)

# Load the list of NASDAQ Capital Market tickers
nasdaq_tickers_file = locals()['var_functions.query_db:0']
with open(nasdaq_tickers_file, 'r') as f:
    stock_data = json.load(f)

nasdaq_tickers = [stock['Symbol'] for stock in stock_data]
company_names = {stock['Symbol']: stock['Company Description'] for stock in stock_data}

# Find which tickers exist as tables in the database
existing_tickers = [ticker for ticker in nasdaq_tickers if ticker in all_tables]

print('__RESULT__:')
print(json.dumps({
    'existing_tickers': existing_tickers,
    'count_existing': len(existing_tickers),
    'total_nasdaq_tickers': len(nasdaq_tickers),
    'company_names': company_names
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
