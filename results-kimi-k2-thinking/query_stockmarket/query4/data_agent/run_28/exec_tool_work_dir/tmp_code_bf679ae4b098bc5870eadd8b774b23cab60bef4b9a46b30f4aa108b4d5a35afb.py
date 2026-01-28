code = """import json

db_list_key = 'var_functions.list_db:8'

# Load the list of all tables from stocktrade database
with open(locals()[db_list_key], 'r') as f:
    all_symbols = json.load(f)

print('Total symbols in stocktrade database:', len(all_symbols))
print('First 10 symbols:', all_symbols[:10])

result = json.dumps({
    'total_symbols': len(all_symbols),
    'sample_symbols': all_symbols[:10]
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Listing Exchange': 'A', 'count': '28'}, {'Listing Exchange': 'N', 'count': '234'}, {'Listing Exchange': 'P', 'count': '1444'}, {'Listing Exchange': 'Q', 'count': '710'}, {'Listing Exchange': 'Z', 'count': '336'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_stocks': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:22': [{'Date': '2017-01-03', 'Open': '69.29000091552734', 'High': '70.86000061035156', 'Low': '69.0', 'Close': '70.54000091552734', 'Adj Close': '70.54000091552734', 'Volume': '8112200'}, {'Date': '2017-01-04', 'Open': '71.08000183105469', 'High': '73.06999969482422', 'Low': '70.76000213623047', 'Close': '72.80000305175781', 'Adj Close': '72.80000305175781', 'Volume': '9289500'}, {'Date': '2017-01-05', 'Open': '72.80999755859375', 'High': '73.66000366210938', 'Low': '72.52999877929688', 'Close': '72.79000091552734', 'Adj Close': '72.79000091552734', 'Volume': '4695600'}, {'Date': '2017-01-06', 'Open': '72.88999938964844', 'High': '74.12999725341797', 'Low': '72.55000305175781', 'Close': '73.80000305175781', 'Adj Close': '73.80000305175781', 'Volume': '4466100'}, {'Date': '2017-01-09', 'Open': '74.05000305175781', 'High': '74.44000244140625', 'Low': '73.51000213623047', 'Close': '73.95999908447266', 'Adj Close': '73.95999908447266', 'Volume': '3933100'}]}

exec(code, env_args)
