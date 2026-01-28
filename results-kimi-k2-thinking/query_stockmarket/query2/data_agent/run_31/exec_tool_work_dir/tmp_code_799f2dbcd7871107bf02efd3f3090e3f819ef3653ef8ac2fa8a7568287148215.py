code = """import json

# Get the candidate ETFs to check
candidates = ["AGG", "DDM", "DIA", "EEM", "EFA", "FXE", "GLD", "IVV", "IWM", "MVV", "QLD", "ROM", "SAA", "SPXL", "SPY", "SSO", "UPRO", "URE", "USO", "UUP", "UWM", "VEA", "VOO", "VTI", "VWO"]

# Build a list of SQL queries
def build_query(symbol):
    return f'SELECT "{symbol}" as symbol, COUNT(*) as days_above_200 FROM "{symbol}" WHERE Date LIKE \'2015-%\' AND "Adj Close" > 200'

queries = [build_query(symbol) for symbol in candidates]

# Join queries with UNION ALL to run them all at once
full_query = " UNION ALL ".join(queries) + " ORDER BY days_above_200 DESC"

print('__RESULT__:')
print(json.dumps({'query': full_query, 'total_candidates': len(candidates)}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'file_path': 'file_storage/functions.query_db:8.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:16': {'total_symbols': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_nyse_arca_etfs': 1435, 'tables_in_trade_db': 2753, 'available_for_query': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:24': [{'count': '0'}], 'var_functions.query_db:26': [{'count': '0'}], 'var_functions.execute_python:30': {'total_nyse_arca_etfs': 1435, 'high_value_candidates': 25, 'candidates': ['AGG', 'DDM', 'DIA', 'EEM', 'EFA', 'FXE', 'GLD', 'IVV', 'IWM', 'MVV', 'QLD', 'ROM', 'SAA', 'SPXL', 'SPY', 'SSO', 'UPRO', 'URE', 'USO', 'UUP', 'UWM', 'VEA', 'VOO', 'VTI', 'VWO']}}

exec(code, env_args)
