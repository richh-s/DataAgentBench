code = """import json
import os

# Get the list of NASDAQ Capital Market symbols
stockinfo_path = locals()['var_functions.query_db:0']
stocktrade_tables_path = locals()['var_functions.list_db:5']

with open(stockinfo_path, 'r') as f:
    stock_records = json.load(f)

with open(stocktrade_tables_path, 'r') as f:
    trade_tables = json.load(f)

# Create symbol to company mapping and get available symbols
symbol_to_company = {record['Symbol']: record['Company Description'] for record in stock_records}
nasdaq_capital_symbols = [record['Symbol'] for record in stock_records if record['Market Category'] == 'S']

# Filter for symbols that exist in trade database
available_symbols = [sym for sym in nasdaq_capital_symbols if sym in trade_tables]

print("__RESULT__:")
print(json.dumps({
    'total_symbols': len(available_symbols),
    'symbol_to_company': symbol_to_company,
    'symbols': available_symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nasdaq_capital_symbols': 86, 'available_in_trade_db': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:10': {'symbol': 'AGMH', 'total_days': 252, 'high_vol_days': 13}, 'var_functions.execute_python:12': {'total_symbols_to_process': 86, 'first_20_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:14': {'total_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
