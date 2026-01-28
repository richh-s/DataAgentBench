code = """import json

# Load NYSE stocks data
nyse_file = locals()['var_functions.query_db:0']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create mapping of symbol to company name
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Get all NYSE symbols
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]

# Store results for stocks with more up days than down days
stock_performance = []

for i, symbol in enumerate(nyse_symbols):
    if i < 5:  # Test with first 5 stocks
        print(f"Processing {symbol}...")
        # Query will be executed via tool call, not here

print('__RESULT__:')
print(json.dumps({
    'test_mode': True,
    'symbols_to_process': nyse_symbols[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 234, 'first_10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:8': {'total_nyse_stocks': 234, 'available_tables': 2753, 'common_symbols': 234}, 'var_functions.execute_python:10': {'message': 'Data loaded successfully', 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:12': [{'count': '0'}], 'var_functions.query_db:14': [{'count': '0'}], 'var_functions.query_db:16': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}, {'Date': '2019-10-25', 'Open': '25.61000061035156', 'High': '25.68000030517578', 'Low': '25.559999465942383', 'Close': '25.670000076293945', 'Adj Close': '25.670000076293945', 'Volume': '1088300'}, {'Date': '2019-10-28', 'Open': '25.68000030517578', 'High': '25.68000030517578', 'Low': '25.549999237060547', 'Close': '25.59000015258789', 'Adj Close': '25.59000015258789', 'Volume': '1128400'}, {'Date': '2019-10-29', 'Open': '25.61000061035156', 'High': '25.61000061035156', 'Low': '25.5', 'Close': '25.56999969482422', 'Adj Close': '25.56999969482422', 'Volume': '497700'}, {'Date': '2019-10-30', 'Open': '25.530000686645508', 'High': '25.670000076293945', 'Low': '25.5', 'Close': '25.65999984741211', 'Adj Close': '25.65999984741211', 'Volume': '1517600'}], 'var_functions.execute_python:18': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'var_functions.execute_python:20': {'total_nyse_stocks': 234, 'valid_symbols_with_data': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:22': [{'count': '251', 'min_date': '2017-01-03', 'max_date': '2017-12-29'}], 'var_functions.execute_python:24': {'message': 'Prepared data for batch processing', 'total_symbols': 234, 'sample_mapping': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}}

exec(code, env_args)
