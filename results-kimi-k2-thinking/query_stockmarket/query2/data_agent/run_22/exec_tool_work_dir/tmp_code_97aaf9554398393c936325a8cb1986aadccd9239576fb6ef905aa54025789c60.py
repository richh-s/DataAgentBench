code = """import json

# Load ETF symbols and trading tables
nyse_arca_file = locals().get('var_functions.query_db:0')
tables_file = locals().get('var_functions.list_db:2')

with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)
with open(tables_file, 'r') as f:
    trade_tables = json.load(f)

# Filter for ETFs that have trading data
valid_symbols = []
for item in nyse_arca_data:
    symbol = item['Symbol']
    if symbol in trade_tables:
        valid_symbols.append(symbol)

# Create 15 batches of ~96 symbols each (1435 total)
BATCHES = 15
batch_size = len(valid_symbols) // BATCHES + 1

batches = []
for i in range(0, len(valid_symbols), batch_size):
    batches.append(valid_symbols[i:i+batch_size])

# Build queries for all batches
all_queries = []
for batch in batches:
    parts = []
    for symbol in batch:
        q = f"SELECT '{symbol}' as Symbol, MAX(\"Adj Close\") as max_price FROM \"{symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        parts.append(q)
    union_part = " UNION ALL ".join(parts)
    full_query = f"SELECT Symbol, max_price FROM ({union_part}) WHERE max_price > 200"
    all_queries.append(full_query)

result = {
    'total_etfs': len(valid_symbols),
    'num_batches': len(batches),
    'queries_generated': len(all_queries)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.query_db:30': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:46': [{'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:48': [{'Symbol': 'AAAU', 'max_adj_close': 'nan'}, {'Symbol': 'AADR', 'max_adj_close': '39.58057403564453'}, {'Symbol': 'ABEQ', 'max_adj_close': 'nan'}, {'Symbol': 'ACSG', 'max_adj_close': 'nan'}, {'Symbol': 'ACWF', 'max_adj_close': '23.251304626464844'}, {'Symbol': 'AFK', 'max_adj_close': '23.345184326171875'}, {'Symbol': 'AFLG', 'max_adj_close': 'nan'}, {'Symbol': 'AFMC', 'max_adj_close': 'nan'}, {'Symbol': 'AFSM', 'max_adj_close': 'nan'}, {'Symbol': 'AFTY', 'max_adj_close': '18.35982131958008'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}, {'Symbol': 'AGGP', 'max_adj_close': 'nan'}, {'Symbol': 'AGGY', 'max_adj_close': '43.77255630493164'}, {'Symbol': 'AGQ', 'max_adj_close': '51.709999084472656'}, {'Symbol': 'AGZ', 'max_adj_close': '105.05885314941406'}, {'Symbol': 'AIEQ', 'max_adj_close': 'nan'}, {'Symbol': 'AIIQ', 'max_adj_close': 'nan'}, {'Symbol': 'AMLP', 'max_adj_close': '11.749510765075684'}, {'Symbol': 'AMOM', 'max_adj_close': 'nan'}, {'Symbol': 'AMZA', 'max_adj_close': '89.12361907958984'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'Symbol': 'DIA'}, {'Symbol': 'IVV'}, {'Symbol': 'IWM'}, {'Symbol': 'SPY'}, {'Symbol': 'VTI'}], 'var_functions.execute_python:56': {'total_nyse_arca_etfs': 1435, 'valid_etfs_with_data': 1435}, 'var_functions.query_db:58': [{'Symbol': 'SPY', 'max_adj_close': '193.3121490478516'}, {'Symbol': 'IVV', 'max_adj_close': '193.5270538330078'}, {'Symbol': 'VTI', 'max_adj_close': '100.54161834716795'}, {'Symbol': 'QQQ', 'max_adj_close': '110.42893981933594'}], 'var_functions.query_db:60': [], 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:86': [{'Symbol': 'AGZ', 'max_adj_close': '105.05885314941406'}, {'Symbol': 'GLD', 'max_adj_close': '125.2300033569336'}, {'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}], 'var_functions.query_db:88': [{'Symbol': 'DRN', 'max_adj_close': '23.39595031738281'}, {'Symbol': 'UPRO', 'max_adj_close': '24.036970138549805'}, {'Symbol': 'TQQQ', 'max_adj_close': '21.189502716064453'}, {'Symbol': 'SPXL', 'max_adj_close': '22.93797874450684'}, {'Symbol': 'SQQQ', 'max_adj_close': '507.2368774414063'}], 'var_functions.query_db:90': [{'Symbol': 'SSO', 'max_adj_close': '66.95523071289062'}, {'Symbol': 'QLD', 'max_adj_close': '41.19669723510742'}, {'Symbol': 'DDM', 'max_adj_close': '22.4426212310791'}, {'Symbol': 'MVV', 'max_adj_close': '27.161584854125977'}, {'Symbol': 'UYM', 'max_adj_close': '53.07555389404297'}], 'var_functions.query_db:92': [], 'var_functions.execute_python:94': {'total_etfs': 1435, 'valid_symbols': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:98': {'total_nyse_arca_etfs': 1435, 'etfs_with_data': 1435, 'first_20_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:100': [{'Date': '2015-01-15', 'Open': '500.4800109863281', 'High': '528.7999877929688', 'Low': '497.6000061035156', 'Close': '527.0399780273438', 'Adj Close': '507.2368774414063', 'Volume': '389800'}, {'Date': '2015-01-06', 'Open': '500.7999877929688', 'High': '529.760009765625', 'Low': '498.0799865722656', 'Close': '522.719970703125', 'Adj Close': '503.0791015625', 'Volume': '345600'}, {'Date': '2015-01-16', 'Open': '529.280029296875', 'High': '531.8400268554688', 'Low': '506.239990234375', 'Close': '508.4800109863281', 'Adj Close': '489.3742370605469', 'Volume': '314600'}, {'Date': '2015-01-14', 'Open': '514.0800170898438', 'High': '520.3200073242188', 'Low': '499.6799926757813', 'Close': '507.2000122070313', 'Adj Close': '488.1423645019531', 'Volume': '407200'}, {'Date': '2015-01-05', 'Open': '488.1600036621094', 'High': '506.8800048828125', 'Low': '486.3999938964844', 'Close': '504.1600036621094', 'Adj Close': '485.2165222167969', 'Volume': '234100'}], 'var_functions.query_db:102': [{'Symbol': 'SQQQ', 'max_price': '507.2368774414063'}], 'var_functions.execute_python:106': {'total_etfs': 1435, 'batches': 15, 'first_query_part': 'SELECT Symbol, max_price FROM (SELECT  + sym +  as Symbol, MAX(Adj Close) as max_price FROM "AAAU" W'}, 'var_functions.query_db:108': [], 'var_functions.query_db:110': [], 'var_functions.query_db:112': [], 'var_functions.execute_python:114': {'total_nyse_arca_etfs': 1435, 'valid_symbols_with_data': 1435, 'batches_needed': 10, 'batch_size': 150}, 'var_functions.execute_python:118': {'total_etfs': 1435, 'status': 'ready to process'}, 'var_functions.query_db:122': [{'Symbol': 'SQQQ', 'max_price': '507.2368774414063'}, {'Symbol': 'UPRO', 'max_price': '24.036970138549805'}, {'Symbol': 'TQQQ', 'max_price': '21.189502716064453'}, {'Symbol': 'SPXL', 'max_price': '22.93797874450684'}, {'Symbol': 'QLD', 'max_price': '41.19669723510742'}, {'Symbol': 'DDM', 'max_price': '22.4426212310791'}, {'Symbol': 'SSO', 'max_price': '66.95523071289062'}, {'Symbol': 'MVV', 'max_price': '27.161584854125977'}, {'Symbol': 'EWV', 'max_price': '68.61780548095703'}, {'Symbol': 'BIB', 'max_price': '104.69000244140624'}], 'var_functions.query_db:124': 'file_storage/functions.query_db:124.json'}

exec(code, env_args)
