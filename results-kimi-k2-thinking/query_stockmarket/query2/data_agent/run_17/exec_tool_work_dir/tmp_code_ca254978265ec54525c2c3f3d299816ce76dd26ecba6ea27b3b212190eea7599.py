code = """import json
import os

# Load the valid symbols
with open(locals()['var_functions.execute_python:10'], 'r') as f:
    data = json.load(f)

symbols = data['valid_symbols']

# Create a Python script that will query each symbol
# We'll do this in batches to handle the 1400+ symbols

ef_above_200 = []
batch_size = 50

print('__RESULT__:')
print(f"Will process {len(symbols)} symbols in batches of {batch_size}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'message': 'Will check each symbol for adjusted close > $200 in 2015', 'total_symbols_to_check': 1435}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'test_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:18': ['AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:20': [], 'var_functions.execute_python:24': {'high_value_candidates': ['GLD', 'DIA', 'SPY', 'IAU', 'SLV', 'USO', 'UCO', 'SPXL', 'UPRO', 'UDOW', 'GDX', 'GDXJ', 'GLDM', 'LQD'], 'all_symbols_count': 1435}, 'var_functions.query_db:26': [{'max_adj_close': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:32': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:34': [{'max_adj_close': '22.93797874450684'}], 'var_functions.query_db:36': [{'max_adj_close': '121.58584594726562'}], 'var_functions.query_db:38': [{'max_adj_close': '24.036970138549805'}], 'var_functions.query_db:40': [{'max_adj_close': '12.619999885559082'}], 'var_functions.query_db:46': [{'max_adj_close': '37.28549957275391'}], 'var_functions.query_db:50': [{'max_adj_close': '97.26858520507812'}], 'var_functions.query_db:52': [{'max_adj_close': '45.316165924072266'}], 'var_functions.query_db:54': [{'max_adj_close': '46.619998931884766'}], 'var_functions.query_db:56': [{'max_adj_close': '624.0791625976562'}], 'var_functions.query_db:58': [{'max_adj_close': '230.2828063964844'}], 'var_functions.query_db:60': [{'max_adj_close': '21.189502716064453'}], 'var_functions.query_db:62': [{'max_adj_close': '51.709999084472656'}]}

exec(code, env_args)
