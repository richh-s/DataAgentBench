code = """import json

# Load NYSE Arca ETF symbols and trading tables
nyse_arca_file = locals().get('var_functions.query_db:0')
tables_file = locals().get('var_functions.list_db:2')

with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)
with open(tables_file, 'r') as f:
    trade_tables = json.load(f)

# Filter for ETFs that have trading data
valid_etfs = [record['Symbol'] for record in nyse_arca_data if record['Symbol'] in trade_tables]

# Process in batches
BATCH_SIZE = 100
all_results = []

# Process first batch to start
batch_symbols = valid_etfs[:BATCH_SIZE]

# Build query for first batch
queries = []
for symbol in batch_symbols:
    query_part = "SELECT '" + symbol + "' as Symbol, MAX(\"Adj Close\") as max_adj_close FROM \"" + symbol + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    queries.append(query_part)

batch_query = " UNION ALL ".join(queries)

print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(valid_etfs),
    'batch_symbols': batch_symbols[:10],
    'batch_query_preview': batch_query[:300]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.query_db:30': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:46': [{'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:48': [{'Symbol': 'AAAU', 'max_adj_close': 'nan'}, {'Symbol': 'AADR', 'max_adj_close': '39.58057403564453'}, {'Symbol': 'ABEQ', 'max_adj_close': 'nan'}, {'Symbol': 'ACSG', 'max_adj_close': 'nan'}, {'Symbol': 'ACWF', 'max_adj_close': '23.251304626464844'}, {'Symbol': 'AFK', 'max_adj_close': '23.345184326171875'}, {'Symbol': 'AFLG', 'max_adj_close': 'nan'}, {'Symbol': 'AFMC', 'max_adj_close': 'nan'}, {'Symbol': 'AFSM', 'max_adj_close': 'nan'}, {'Symbol': 'AFTY', 'max_adj_close': '18.35982131958008'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}, {'Symbol': 'AGGP', 'max_adj_close': 'nan'}, {'Symbol': 'AGGY', 'max_adj_close': '43.77255630493164'}, {'Symbol': 'AGQ', 'max_adj_close': '51.709999084472656'}, {'Symbol': 'AGZ', 'max_adj_close': '105.05885314941406'}, {'Symbol': 'AIEQ', 'max_adj_close': 'nan'}, {'Symbol': 'AIIQ', 'max_adj_close': 'nan'}, {'Symbol': 'AMLP', 'max_adj_close': '11.749510765075684'}, {'Symbol': 'AMOM', 'max_adj_close': 'nan'}, {'Symbol': 'AMZA', 'max_adj_close': '89.12361907958984'}]}

exec(code, env_args)
