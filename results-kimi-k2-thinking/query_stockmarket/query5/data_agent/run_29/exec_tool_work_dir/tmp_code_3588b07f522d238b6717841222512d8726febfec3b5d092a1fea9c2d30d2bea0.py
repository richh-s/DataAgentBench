code = """import json

# Read the NASDAQ Capital stocks data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Read the list of all trade tables
with open(locals()['var_functions.list_db:2'], 'r') as f:
    all_trade_tables = json.load(f)

# Find intersection
nasdaq_symbols = set(stock['Symbol'] for stock in nasdaq_capital_stocks)
trade_symbols = set(all_trade_tables)
valid_symbols = list(nasdaq_symbols.intersection(trade_symbols))

# Create company name mapping
company_map = {stock['Symbol']: stock['Company Description'].split('.')[0] for stock in nasdaq_capital_stocks}

print('__RESULT__:')
print(json.dumps({
    'valid_symbols_count': len(valid_symbols),
    'sample_symbols': valid_symbols[:10],
    'company_map_sample': {k: company_map[k] for k in list(company_map.keys())[:10]}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'nasdaq_capital_count': 86, 'trade_tables_count': 2753, 'valid_symbols_count': 86, 'sample_valid_symbols': ['CCCL', 'ELSE', 'BOTJ', 'CPAH', 'AMHC', 'MNPR', 'CPAAU', 'XBIOW', 'PECK', 'OTEL']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [{'Date': '2019-01-02', 'Open': '1.8200000524520876', 'High': '2.3499999046325684', 'Low': '1.7000000476837158', 'Close': '1.8899999856948853', 'Adj Close': '1.8899999856948853', 'Volume': '17102800'}, {'Date': '2019-01-03', 'Open': '1.7999999523162842', 'High': '1.8899999856948853', 'Low': '1.3799999952316284', 'Close': '1.3799999952316284', 'Adj Close': '1.3799999952316284', 'Volume': '2197600'}, {'Date': '2019-01-04', 'Open': '1.3600000143051147', 'High': '1.899999976158142', 'Low': '1.3600000143051147', 'Close': '1.6399999856948853', 'Adj Close': '1.6399999856948853', 'Volume': '7201200'}, {'Date': '2019-01-07', 'Open': '1.590000033378601', 'High': '1.6399999856948853', 'Low': '1.440000057220459', 'Close': '1.5800000429153442', 'Adj Close': '1.5800000429153442', 'Volume': '1078600'}, {'Date': '2019-01-08', 'Open': '1.559999942779541', 'High': '1.6100000143051147', 'Low': '1.440000057220459', 'Close': '1.5199999809265137', 'Adj Close': '1.5199999809265137', 'Volume': '574900'}]}

exec(code, env_args)
