code = """import json

# Load data
symbols_file = locals()['var_functions.query_db:0']
trade_tables_file = locals()['var_functions.list_db:2']

with open(symbols_file, 'r') as f:
    symbols_data = json.load(f)

# Create symbol to company name mapping
symbol_info = {}
for rec in symbols_data:
    symbol_info[rec['Symbol']] = rec['Company Description']

print('Total NYSE non-ETF symbols:', len(symbol_info))
print('First 5 symbols:', list(symbol_info.keys())[:5])
print('__RESULT__:')
print(json.dumps({'count': len(symbol_info), 'example': list(symbol_info.items())[0]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_non_etf': 234, 'present_in_trade_db': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:8': [{'Symbol': 'AEFC', 'Company': 'None'}, {'Symbol': 'AIN', 'Company': 'None'}, {'Symbol': 'AIV', 'Company': 'None'}, {'Symbol': 'AIZP', 'Company': 'None'}, {'Symbol': 'AJRD', 'Company': 'None'}], 'var_functions.query_db:10': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'High': '15.701873779296877', 'Low': '14.988152503967283', 'Close': '15.107105255126951', 'Adj Close': '8.918145179748535', 'Volume': '2292200'}, {'Date': '1987-10-01', 'Open': '15.107105255126951', 'High': '15.345012664794922', 'Low': '14.988152503967283', 'Close': '15.345012664794922', 'Adj Close': '9.05859375', 'Volume': '468200'}, {'Date': '1987-10-02', 'Open': '15.345012664794922', 'High': '15.701873779296877', 'Low': '15.107105255126951', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '371600'}, {'Date': '1987-10-05', 'Open': '15.701873779296877', 'High': '15.701873779296877', 'Low': '15.226058959960938', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '121300'}, {'Date': '1987-10-06', 'Open': '15.58292007446289', 'High': '15.58292007446289', 'Low': '15.226058959960938', 'Close': '15.463966369628906', 'Adj Close': '9.128814697265623', 'Volume': '159300'}]}

exec(code, env_args)
