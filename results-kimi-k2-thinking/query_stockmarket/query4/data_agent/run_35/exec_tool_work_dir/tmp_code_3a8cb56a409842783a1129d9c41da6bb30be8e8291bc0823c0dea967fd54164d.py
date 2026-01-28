code = """import json
import os

# Load NYSE non-ETF stock data
stockinfo_path = locals().get('var_functions.query_db:0')
if isinstance(stockinfo_path, str) and stockinfo_path.endswith('.json'):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = locals().get('var_functions.query_db:0', [])

# Create a dictionary mapping symbols to company names
symbol_to_name = {stock['Symbol']: stock['Company Description'] for stock in stockinfo_data}
nyse_symbols = list(symbol_to_name.keys())

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'sample_symbols': nyse_symbols[:10],
    'sample_names': {sym: symbol_to_name[sym] for sym in nyse_symbols[:5]}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_count': 234, 'available_count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_available': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:8': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}, {'Date': '2017-01-10', 'Open': '45.5', 'High': '45.95000076293945', 'Low': '45.5', 'Close': '45.70000076293945', 'Adj Close': '43.9408073425293', 'Volume': '161700'}, {'Date': '2017-01-11', 'Open': '45.79999923706055', 'High': '46.650001525878906', 'Low': '45.54999923706055', 'Close': '46.29999923706055', 'Adj Close': '44.51770782470703', 'Volume': '104600'}, {'Date': '2017-01-12', 'Open': '46.25', 'High': '46.25', 'Low': '45.0', 'Close': '45.75', 'Adj Close': '43.9888801574707', 'Volume': '59700'}, {'Date': '2017-01-13', 'Open': '46.04999923706055', 'High': '46.70000076293945', 'Low': '46.04999923706055', 'Close': '46.70000076293945', 'Adj Close': '44.90231704711914', 'Volume': '96900'}, {'Date': '2017-01-17', 'Open': '46.5', 'High': '46.75', 'Low': '46.20000076293945', 'Close': '46.650001525878906', 'Adj Close': '44.8542366027832', 'Volume': '111100'}]}

exec(code, env_args)
