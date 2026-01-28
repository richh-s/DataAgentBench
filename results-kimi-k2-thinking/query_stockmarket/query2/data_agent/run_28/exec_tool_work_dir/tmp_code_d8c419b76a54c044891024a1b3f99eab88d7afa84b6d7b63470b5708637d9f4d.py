code = """import json

# Load common symbols
exec24_path = locals()['var_functions.execute_python:24']
with open(exec24_path, 'r') as f:
    data = json.load(f)

common_symbols = data['common_symbols_list']

# Take first 50 symbols and create a simple query
first_50 = common_symbols[:50]

query_parts = []
for symbol in first_50:
    # Build query for each symbol
    part = "SELECT '" + symbol + "' as Symbol, MAX(\"Adj Close\") as Max_Adj_Close FROM \"" + symbol + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    query_parts.append(part)

combined_query = " UNION ALL ".join(query_parts)

print('__RESULT__:')
print(json.dumps({
    'symbols_count': len(first_50),
    'query_preview': combined_query[:200] + '...' if len(combined_query) > 200 else combined_query,
    'total_length': len(combined_query)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': {'total_symbols': 1435, 'batches_count': 58, 'batch_size': 25, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT'], 'last_batch': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'Symbol': 'SPY', 'Max_Adj_Close': '193.3121490478516'}], 'var_functions.execute_python:42': {'total_symbols': 1435, 'batch_size': 25, 'total_batches': 58}, 'var_functions.query_db:44': [{'Symbol': 'GLD', 'Max_Adj_Close': '125.2300033569336'}], 'var_functions.query_db:46': [], 'var_functions.execute_python:48': {'total_symbols': 1435, 'total_batches': 72, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'batch_count': 72}, 'var_functions.query_db:54': [{'Symbol': 'IVV', 'Max_Adj_Close': '193.5270538330078'}, {'Symbol': 'VOO', 'Max_Adj_Close': '177.17626953125'}, {'Symbol': 'QQQ', 'Max_Adj_Close': '110.42893981933594'}, {'Symbol': 'DIA', 'Max_Adj_Close': '163.6190185546875'}], 'var_functions.query_db:56': [{'Symbol': 'IWB', 'Max_Adj_Close': '108.6298828125'}, {'Symbol': 'IWM', 'Max_Adj_Close': '120.37349700927734'}, {'Symbol': 'IWF', 'Max_Adj_Close': '97.2972412109375'}, {'Symbol': 'IWD', 'Max_Adj_Close': '93.8613052368164'}, {'Symbol': 'IWO', 'Max_Adj_Close': '153.2022705078125'}], 'var_functions.query_db:58': [{'Symbol': 'TQQQ', 'Max_Adj_Close': '21.189502716064453'}, {'Symbol': 'UPRO', 'Max_Adj_Close': '24.036970138549805'}, {'Symbol': 'UDOW', 'Max_Adj_Close': '37.28549957275391'}, {'Symbol': 'SPXL', 'Max_Adj_Close': '22.93797874450684'}, {'Symbol': 'TNA', 'Max_Adj_Close': '48.85812377929688'}], 'var_functions.execute_python:60': {'candidates_found': 16, 'candidates': ['GLD', 'IAU', 'SLV', 'USO', 'UNG', 'LQD', 'HYG', 'VNQ', 'IYR', 'RWR', 'SCHH', 'EFA', 'EFA', 'VEA', 'VTI', 'VT'], 'all_symbols_count': 1435}, 'var_functions.query_db:62': [{'Symbol': 'VNQ', 'Max_Adj_Close': '71.3005142211914'}, {'Symbol': 'IYR', 'Max_Adj_Close': '68.42395782470703'}, {'Symbol': 'SCHH', 'Max_Adj_Close': '36.98344039916992'}, {'Symbol': 'RWR', 'Max_Adj_Close': '82.26422882080078'}, {'Symbol': 'TLT', 'Max_Adj_Close': '121.58584594726562'}, {'Symbol': 'IEF', 'Max_Adj_Close': '99.8505401611328'}, {'Symbol': 'EFA', 'Max_Adj_Close': '59.14651870727539'}, {'Symbol': 'VEA', 'Max_Adj_Close': '36.54500198364258'}], 'var_functions.query_db:66': [{'Symbol': 'GOEX', 'Max_Adj_Close': '15.534685134887695'}, {'Symbol': 'GURU', 'Max_Adj_Close': '26.802734375'}, {'Symbol': 'BIBL', 'Max_Adj_Close': 'nan'}, {'Symbol': 'CWS', 'Max_Adj_Close': 'nan'}, {'Symbol': 'FPX', 'Max_Adj_Close': '54.537410736083984'}, {'Symbol': 'PNQI', 'Max_Adj_Close': '82.94065856933594'}, {'Symbol': 'QQEW', 'Max_Adj_Close': '44.25756072998047'}, {'Symbol': 'QQXT', 'Max_Adj_Close': '43.08406448364258'}, {'Symbol': 'QTEC', 'Max_Adj_Close': '43.26129913330078'}, {'Symbol': 'SKYY', 'Max_Adj_Close': '30.62405204772949'}], 'var_functions.query_db:68': [{'Symbol': 'ICF', 'Max_Adj_Close': '89.69170379638672'}, {'Symbol': 'VIG', 'Max_Adj_Close': '74.69651794433594'}, {'Symbol': 'VYM', 'Max_Adj_Close': '60.23244094848633'}, {'Symbol': 'DVY', 'Max_Adj_Close': '67.666748046875'}, {'Symbol': 'SCHD', 'Max_Adj_Close': '36.06608200073242'}]}

exec(code, env_args)
