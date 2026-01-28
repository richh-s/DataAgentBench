code = """import json

# Read NYSE Arca ETFs
nyse_arka_path = locals()['var_functions.query_db:24']
with open(nyse_arka_path, 'r') as f:
    nyse_arka_etfs = json.load(f)

# Read all tables from stocktrade database
all_tables_path = locals()['var_functions.list_db:30']
with open(all_tables_path, 'r') as f:
    all_tables = json.load(f)

# Extract symbols from NYSE Arca ETFs
nyse_arka_symbols = set([item['Symbol'] for item in nyse_arka_etfs])
all_table_symbols = set(all_tables)

# Find intersection
common_symbols = sorted(list(nyse_arka_symbols.intersection(all_table_symbols)))

print(f"NYSE Arca ETFs: {len(nyse_arka_symbols)}")
print(f"Tables in stocktrade: {len(all_table_symbols)}")
print(f"Common (ETFs with price data): {len(common_symbols)}")
print('__RESULT__:')
print(json.dumps(common_symbols))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': ['AMOM', 'EWN', 'EVX', 'GMF', 'TIP', 'FLTB', 'EEMX', 'FRI', 'KOLD', 'GIGB'], 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}, {'Date': '1993-02-03', 'Open': '44.40625', 'High': '44.84375', 'Low': '44.375', 'Close': '44.8125', 'Adj Close': '26.822998046875', 'Volume': '529400'}, {'Date': '1993-02-04', 'Open': '44.96875', 'High': '45.09375', 'Low': '44.46875', 'Close': '45.0', 'Adj Close': '26.93523979187012', 'Volume': '531500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:39': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}, {'Adj Close': '192.83792114257807', 'Date': '2015-05-18'}, {'Adj Close': '192.8120574951172', 'Date': '2015-06-23'}, {'Adj Close': '192.77456665039065', 'Date': '2015-05-19'}, {'Adj Close': '192.73838806152344', 'Date': '2015-05-22'}, {'Adj Close': '192.67564392089844', 'Date': '2015-06-22'}], 'var_functions.query_db:28': [], 'var_functions.list_db:30': 'file_storage/functions.list_db:30.json', 'var_functions.execute_python:32': 1435, 'var_functions.query_db:34': [{'Adj Close': '125.2300033569336', 'Date': '2015-01-22'}, {'Adj Close': '124.4000015258789', 'Date': '2015-01-27'}, {'Adj Close': '124.2300033569336', 'Date': '2015-01-21'}, {'Adj Close': '124.2300033569336', 'Date': '2015-01-23'}, {'Adj Close': '124.1999969482422', 'Date': '2015-01-20'}, {'Adj Close': '123.4499969482422', 'Date': '2015-01-30'}, {'Adj Close': '123.41999816894533', 'Date': '2015-01-28'}, {'Adj Close': '122.98999786376952', 'Date': '2015-01-26'}, {'Adj Close': '122.5199966430664', 'Date': '2015-01-16'}, {'Adj Close': '122.41999816894533', 'Date': '2015-02-02'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
