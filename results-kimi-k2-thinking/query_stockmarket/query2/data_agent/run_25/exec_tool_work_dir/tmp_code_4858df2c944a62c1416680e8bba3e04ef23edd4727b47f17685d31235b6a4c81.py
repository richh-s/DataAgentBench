code = """import json

# Load the list of tables/tickers from stocktrade database
with open(locals()['var_functions.list_db:5'], 'r') as f:
    all_trade_tickers = json.load(f)

# Load the NYSE Arca ETFs from stockinfo
with open(locals()['var_functions.query_db:0'], 'r') as f:
    nyse_arca_data = json.load(f)

nyse_arca_tickers = [item['Symbol'] for item in nyse_arca_data]

# Find intersection - NYSE Arca ETFs that have price data
trade_tickers_set = set(all_trade_tickers)
nyse_arca_tickers_set = set(nyse_arca_tickers)
common_tickers = trade_tickers_set.intersection(nyse_arca_tickers_set)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_tickers),
    'total_trade_tables': len(all_trade_tickers),
    'common_tickers_count': len(common_tickers),
    'first_10_common_tickers': list(common_tickers)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
