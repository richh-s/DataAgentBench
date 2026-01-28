code = """import json

# Load NYSE Arca symbols from stockinfo
try:
    nyse_arca_file = locals().get('var_functions.query_db:0')
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_data = json.load(f)
    nyse_arca_symbols = [record['Symbol'] for record in nyse_arca_data]
except:
    nyse_arca_symbols = []

# Load available trading tables
try:
    tables_file = locals().get('var_functions.list_db:2')
    with open(tables_file, 'r') as f:
        trade_tables = json.load(f)
except:
    trade_tables = []

# Filter for ETFs that have trading data
valid_etfs = [symbol for symbol in nyse_arca_symbols if symbol in trade_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'valid_etfs_with_data': len(valid_etfs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.query_db:30': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:46': [{'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:48': [{'Symbol': 'AAAU', 'max_adj_close': 'nan'}, {'Symbol': 'AADR', 'max_adj_close': '39.58057403564453'}, {'Symbol': 'ABEQ', 'max_adj_close': 'nan'}, {'Symbol': 'ACSG', 'max_adj_close': 'nan'}, {'Symbol': 'ACWF', 'max_adj_close': '23.251304626464844'}, {'Symbol': 'AFK', 'max_adj_close': '23.345184326171875'}, {'Symbol': 'AFLG', 'max_adj_close': 'nan'}, {'Symbol': 'AFMC', 'max_adj_close': 'nan'}, {'Symbol': 'AFSM', 'max_adj_close': 'nan'}, {'Symbol': 'AFTY', 'max_adj_close': '18.35982131958008'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}, {'Symbol': 'AGGP', 'max_adj_close': 'nan'}, {'Symbol': 'AGGY', 'max_adj_close': '43.77255630493164'}, {'Symbol': 'AGQ', 'max_adj_close': '51.709999084472656'}, {'Symbol': 'AGZ', 'max_adj_close': '105.05885314941406'}, {'Symbol': 'AIEQ', 'max_adj_close': 'nan'}, {'Symbol': 'AIIQ', 'max_adj_close': 'nan'}, {'Symbol': 'AMLP', 'max_adj_close': '11.749510765075684'}, {'Symbol': 'AMOM', 'max_adj_close': 'nan'}, {'Symbol': 'AMZA', 'max_adj_close': '89.12361907958984'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'Symbol': 'DIA'}, {'Symbol': 'IVV'}, {'Symbol': 'IWM'}, {'Symbol': 'SPY'}, {'Symbol': 'VTI'}]}

exec(code, env_args)
