code = """import json
import os

# Load common symbols
exec24_path = locals()['var_functions.execute_python:24']
with open(exec24_path, 'r') as f:
    data = json.load(f)

common_symbols = data['common_symbols_list']

# Create SQL queries for all symbols - individual queries to avoid failures
all_queries = []
for symbol in common_symbols:
    query = f"SELECT '{symbol}' as Symbol, MAX(\"Adj Close\") as Max_Adj_Close FROM \"{symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    all_queries.append(query)

# Split into batches of 10 to avoid query size limits
batch_size = 10
query_batches = [all_queries[i:i+batch_size] for i in range(0, len(all_queries), batch_size)]

# Save query batches to file
with open('/tmp/query_batches.json', 'w') as f:
    json.dump(query_batches, f)

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(common_symbols),
    'total_batches': len(query_batches),
    'queries_per_batch': batch_size,
    'first_batch_sample': query_batches[0][:3]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': {'total_symbols': 1435, 'batches_count': 58, 'batch_size': 25, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT'], 'last_batch': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'Symbol': 'SPY', 'Max_Adj_Close': '193.3121490478516'}], 'var_functions.execute_python:42': {'total_symbols': 1435, 'batch_size': 25, 'total_batches': 58}, 'var_functions.query_db:44': [{'Symbol': 'GLD', 'Max_Adj_Close': '125.2300033569336'}], 'var_functions.query_db:46': [], 'var_functions.execute_python:48': {'total_symbols': 1435, 'total_batches': 72, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'batch_count': 72}, 'var_functions.query_db:54': [{'Symbol': 'IVV', 'Max_Adj_Close': '193.5270538330078'}, {'Symbol': 'VOO', 'Max_Adj_Close': '177.17626953125'}, {'Symbol': 'QQQ', 'Max_Adj_Close': '110.42893981933594'}, {'Symbol': 'DIA', 'Max_Adj_Close': '163.6190185546875'}], 'var_functions.query_db:56': [{'Symbol': 'IWB', 'Max_Adj_Close': '108.6298828125'}, {'Symbol': 'IWM', 'Max_Adj_Close': '120.37349700927734'}, {'Symbol': 'IWF', 'Max_Adj_Close': '97.2972412109375'}, {'Symbol': 'IWD', 'Max_Adj_Close': '93.8613052368164'}, {'Symbol': 'IWO', 'Max_Adj_Close': '153.2022705078125'}], 'var_functions.query_db:58': [{'Symbol': 'TQQQ', 'Max_Adj_Close': '21.189502716064453'}, {'Symbol': 'UPRO', 'Max_Adj_Close': '24.036970138549805'}, {'Symbol': 'UDOW', 'Max_Adj_Close': '37.28549957275391'}, {'Symbol': 'SPXL', 'Max_Adj_Close': '22.93797874450684'}, {'Symbol': 'TNA', 'Max_Adj_Close': '48.85812377929688'}], 'var_functions.execute_python:60': {'candidates_found': 16, 'candidates': ['GLD', 'IAU', 'SLV', 'USO', 'UNG', 'LQD', 'HYG', 'VNQ', 'IYR', 'RWR', 'SCHH', 'EFA', 'EFA', 'VEA', 'VTI', 'VT'], 'all_symbols_count': 1435}, 'var_functions.query_db:62': [{'Symbol': 'VNQ', 'Max_Adj_Close': '71.3005142211914'}, {'Symbol': 'IYR', 'Max_Adj_Close': '68.42395782470703'}, {'Symbol': 'SCHH', 'Max_Adj_Close': '36.98344039916992'}, {'Symbol': 'RWR', 'Max_Adj_Close': '82.26422882080078'}, {'Symbol': 'TLT', 'Max_Adj_Close': '121.58584594726562'}, {'Symbol': 'IEF', 'Max_Adj_Close': '99.8505401611328'}, {'Symbol': 'EFA', 'Max_Adj_Close': '59.14651870727539'}, {'Symbol': 'VEA', 'Max_Adj_Close': '36.54500198364258'}]}

exec(code, env_args)
