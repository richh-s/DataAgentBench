code = """import json

# Load ETF symbols and table list
etf_file = locals().get('var_functions.query_db:0')
tables_file = locals().get('var_functions.list_db:2')

with open(etf_file, 'r') as f:
    etf_list = json.load(f)

with open(tables_file, 'r') as f:
    table_names = json.load(f)

# Filter symbols that exist as tables
symbols_to_check = []
for etf in etf_list:
    sym = etf['Symbol']
    if sym in table_names:
        symbols_to_check.append(sym)

# Create batch queries
BATCH_SIZE = 150
queries = []
for i in range(0, len(symbols_to_check), BATCH_SIZE):
    batch = symbols_to_check[i:i+BATCH_SIZE]
    parts = []
    for sym in batch:
        parts.append("SELECT ''" + sym + "'' as Symbol, MAX(\"Adj Close\") as max_price FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
    union_part = " UNION ALL ".join(parts)
    full_query = "SELECT Symbol, max_price FROM (" + union_part + ") WHERE max_price > 200"
    queries.append(full_query)

result = {
    'total_symbols': len(symbols_to_check),
    'num_queries': len(queries),
    'batch_size': BATCH_SIZE
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.query_db:30': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:46': [{'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:48': [{'Symbol': 'AAAU', 'max_adj_close': 'nan'}, {'Symbol': 'AADR', 'max_adj_close': '39.58057403564453'}, {'Symbol': 'ABEQ', 'max_adj_close': 'nan'}, {'Symbol': 'ACSG', 'max_adj_close': 'nan'}, {'Symbol': 'ACWF', 'max_adj_close': '23.251304626464844'}, {'Symbol': 'AFK', 'max_adj_close': '23.345184326171875'}, {'Symbol': 'AFLG', 'max_adj_close': 'nan'}, {'Symbol': 'AFMC', 'max_adj_close': 'nan'}, {'Symbol': 'AFSM', 'max_adj_close': 'nan'}, {'Symbol': 'AFTY', 'max_adj_close': '18.35982131958008'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}, {'Symbol': 'AGGP', 'max_adj_close': 'nan'}, {'Symbol': 'AGGY', 'max_adj_close': '43.77255630493164'}, {'Symbol': 'AGQ', 'max_adj_close': '51.709999084472656'}, {'Symbol': 'AGZ', 'max_adj_close': '105.05885314941406'}, {'Symbol': 'AIEQ', 'max_adj_close': 'nan'}, {'Symbol': 'AIIQ', 'max_adj_close': 'nan'}, {'Symbol': 'AMLP', 'max_adj_close': '11.749510765075684'}, {'Symbol': 'AMOM', 'max_adj_close': 'nan'}, {'Symbol': 'AMZA', 'max_adj_close': '89.12361907958984'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'Symbol': 'DIA'}, {'Symbol': 'IVV'}, {'Symbol': 'IWM'}, {'Symbol': 'SPY'}, {'Symbol': 'VTI'}], 'var_functions.execute_python:56': {'total_nyse_arca_etfs': 1435, 'valid_etfs_with_data': 1435}, 'var_functions.query_db:58': [{'Symbol': 'SPY', 'max_adj_close': '193.3121490478516'}, {'Symbol': 'IVV', 'max_adj_close': '193.5270538330078'}, {'Symbol': 'VTI', 'max_adj_close': '100.54161834716795'}, {'Symbol': 'QQQ', 'max_adj_close': '110.42893981933594'}], 'var_functions.query_db:60': []}

exec(code, env_args)
