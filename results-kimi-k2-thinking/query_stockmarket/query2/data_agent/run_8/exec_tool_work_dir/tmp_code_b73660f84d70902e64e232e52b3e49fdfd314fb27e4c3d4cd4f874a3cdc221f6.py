code = """import json

# Get the list of ETFs from storage
etfs_key = 'var_functions.execute_python:20'
etfs_info = locals().get(etfs_key, {})

# Get full list of ETFs to check
symbols_key = 'var_functions.query_db:6'
symbols_data = locals().get(symbols_key, [])
if isinstance(symbols_data, str) and symbols_data.endswith('.json'):
    with open(symbols_data, 'r') as f:
        symbols_data = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in symbols_data]

print(f"Need to check {len(nyse_arca_etfs)} ETFs for 2015 prices > $200")
print("This will take multiple queries...")

print("__RESULT__:")
print(json.dumps({
    "total_etfs" : len(nyse_arca_etfs),
    "ready" : True,
    "first_5": nyse_arca_etfs[:5]
}))"""

env_args = {'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'status': 'ready_to_check', 'count': 1435, 'symbols_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'Date': '2015-03-02', 'Open': '210.77999877929688', 'High': '212.05999755859372', 'Low': '210.72000122070312', 'Close': '211.9900054931641', 'Adj Close': '190.98098754882807', 'Volume': '87491400'}, {'Date': '2015-03-03', 'Open': '211.47000122070312', 'High': '212.0500030517578', 'Low': '210.0800018310547', 'Close': '211.1199951171875', 'Adj Close': '190.19715881347656', 'Volume': '110325800'}, {'Date': '2015-03-04', 'Open': '210.3999938964844', 'High': '210.4900054931641', 'Low': '209.05999755859372', 'Close': '210.22999572753903', 'Adj Close': '189.39535522460935', 'Volume': '114497200'}, {'Date': '2015-03-05', 'Open': '210.6199951171875', 'High': '210.8000030517578', 'Low': '209.8500061035156', 'Close': '210.4600067138672', 'Adj Close': '189.60255432128903', 'Volume': '76873000'}], 'var_functions.execute_python:20': {'total_nyse_arca_etfs': 1435, 'etfs_with_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:22': {'action': 'checking_prices', 'etfs_to_check': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}}

exec(code, env_args)
