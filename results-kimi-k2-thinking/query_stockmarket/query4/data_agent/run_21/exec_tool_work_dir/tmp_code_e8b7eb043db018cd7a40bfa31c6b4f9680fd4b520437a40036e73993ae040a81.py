code = """import json

# Get NYSE stocks data
nyse_var = 'var_functions.query_db:7'
with open(locals()[nyse_var], 'r') as f:
    nyse_stocks = json.load(f)

# Create mapping of symbol to company name
symbol_to_name = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(symbol_to_name),
    'sample': {k: symbol_to_name[k] for k in list(symbol_to_name.keys())[:3]}
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.execute_python:5': 2753, 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:10': {'total_nyse_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}, {'Date': '2018-08-16', 'Open': '11.779999732971191', 'High': '11.800000190734863', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '428400'}, {'Date': '2018-08-17', 'Open': '11.800000190734863', 'High': '11.81999969482422', 'Low': '11.770000457763672', 'Close': '11.81999969482422', 'Adj Close': '11.81999969482422', 'Volume': '52400'}, {'Date': '2018-08-20', 'Open': '11.880000114440918', 'High': '11.90999984741211', 'Low': '11.850000381469728', 'Close': '11.899999618530272', 'Adj Close': '11.899999618530272', 'Volume': '28700'}, {'Date': '2018-08-21', 'Open': '11.920000076293944', 'High': '11.949999809265137', 'Low': '11.890000343322754', 'Close': '11.93000030517578', 'Adj Close': '11.93000030517578', 'Volume': '30600'}], 'var_functions.query_db:18': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'Close': '47.150001525878906'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'Close': '48.150001525878906'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'Close': '47.75'}, {'Date': '2017-01-06', 'Open': '47.75', 'Close': '46.59999847412109'}, {'Date': '2017-01-09', 'Open': '46.5', 'Close': '45.54999923706055'}]}

exec(code, env_args)
