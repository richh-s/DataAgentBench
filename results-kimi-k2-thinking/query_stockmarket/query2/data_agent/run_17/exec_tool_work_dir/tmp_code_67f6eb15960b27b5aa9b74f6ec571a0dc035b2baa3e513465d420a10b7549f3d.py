code = """import json

# Load the high value candidates we identified
with open(locals()['var_functions.execute_python:24'], 'r') as f:
    data = json.load(f)

candidates = data['high_value_candidates']

print('__RESULT__:')
print(json.dumps(candidates))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'message': 'Will check each symbol for adjusted close > $200 in 2015', 'total_symbols_to_check': 1435}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'test_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:18': ['AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:20': [], 'var_functions.execute_python:24': {'high_value_candidates': ['GLD', 'DIA', 'SPY', 'IAU', 'SLV', 'USO', 'UCO', 'SPXL', 'UPRO', 'UDOW', 'GDX', 'GDXJ', 'GLDM', 'LQD'], 'all_symbols_count': 1435}, 'var_functions.query_db:26': [{'max_adj_close': '125.2300033569336'}]}

exec(code, env_args)
