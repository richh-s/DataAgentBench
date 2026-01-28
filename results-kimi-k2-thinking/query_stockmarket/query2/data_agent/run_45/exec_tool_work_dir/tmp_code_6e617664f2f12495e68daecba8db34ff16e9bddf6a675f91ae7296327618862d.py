code = """import json

# Read the list of tables from stocktrade database
file_path = locals()['var_functions.list_db:8']

with open(file_path, 'r') as f:
    all_tickers = json.load(f)

# Read the NYSE Arca ETFs list
etfs_file_path = locals()['var_functions.query_db:0']
with open(etfs_file_path, 'r') as f:
    etfs_data = json.load(f)

nyse_arca_etfs = [etf['Symbol'] for etf in etfs_data]

# Find intersection - ETFs that have data in stocktrade database
available_etfs = [ticker for ticker in nyse_arca_etfs if ticker in all_tickers]

print('Total NYSE Arca ETFs:', len(nyse_arca_etfs))
print('Total tables in stocktrade_db:', len(all_tickers))
print('NYSE Arca ETFs with price data:', len(available_etfs))
print('Sample available ETFs:', available_etfs[:10])

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etfs': len(nyse_arca_etfs),
    'total_tables': len(all_tickers),
    'available_etfs': len(available_etfs),
    'sample_available': available_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'etf_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_count': 1435}, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
