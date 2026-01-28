code = """import json

# Load NASDAQ Capital Market stocks from the query result
nasdaq_cap_file = locals()['var_functions.query_db:32']
with open(nasdaq_cap_file, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

# Extract symbols and company descriptions
nasdaq_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]
company_names = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_cap_stocks}

# Load all tickers from trade database
trade_file = locals()['var_functions.list_db:24']
with open(trade_file, 'r') as f:
    all_trade_stocks = json.load(f)

# Find intersection
nasdaq_symbols_set = set(nasdaq_symbols)
trade_symbols_set = set(all_trade_stocks)
common_symbols = list(nasdaq_symbols_set.intersection(trade_symbols_set))

print('Total NASDAQ Capital Market stocks:', len(nasdaq_symbols))
print('Total stocks in trade database:', len(all_trade_stocks))
print('Common stocks with trade data:', len(common_symbols))
print('__RESULT__:')
print(json.dumps(common_symbols[:100]))  # Return first 100 for preview"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.list_db:7': ['stockinfo'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:24': 'file_storage/functions.list_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}

exec(code, env_args)
