code = """import json

# Load available tables from storage
tables_key = 'var_functions.list_db:12'
tables_data = locals().get(tables_key, [])

# Handle file path case
if isinstance(tables_data, str) and tables_data.endswith('.json'):
    with open(tables_data, 'r') as f:
        tables_data = json.load(f)

# Available tables in stocktrade database
available_tables = set(tables_data)

# Load NYSE Arca ETFs
symbols_key = 'var_functions.query_db:6'
symbols_data = locals().get(symbols_key, [])
if isinstance(symbols_data, str) and symbols_data.endswith('.json'):
    with open(symbols_data, 'r') as f:
        symbols_data = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in symbols_data]

# Find intersection (ETFs that have data tables)
etfs_with_data = [sym for sym in nyse_arca_etfs if sym in available_tables]

print(f"Total NYSE Arca ETFs: {len(nyse_arca_etfs)}")
print(f"ETFs with price data: {len(etfs_with_data)}")
print(f"Sample ETFs to check: {etfs_with_data[:10]}")

print("__RESULT__:")
print(json.dumps({
    "total_nyse_arca_etfs": len(nyse_arca_etfs),
    "etfs_with_data": len(etfs_with_data),
    "sample_etfs": etfs_with_data[:10]
}))"""

env_args = {'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'status': 'ready_to_check', 'count': 1435, 'symbols_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'Date': '2015-03-02', 'Open': '210.77999877929688', 'High': '212.05999755859372', 'Low': '210.72000122070312', 'Close': '211.9900054931641', 'Adj Close': '190.98098754882807', 'Volume': '87491400'}, {'Date': '2015-03-03', 'Open': '211.47000122070312', 'High': '212.0500030517578', 'Low': '210.0800018310547', 'Close': '211.1199951171875', 'Adj Close': '190.19715881347656', 'Volume': '110325800'}, {'Date': '2015-03-04', 'Open': '210.3999938964844', 'High': '210.4900054931641', 'Low': '209.05999755859372', 'Close': '210.22999572753903', 'Adj Close': '189.39535522460935', 'Volume': '114497200'}, {'Date': '2015-03-05', 'Open': '210.6199951171875', 'High': '210.8000030517578', 'Low': '209.8500061035156', 'Close': '210.4600067138672', 'Adj Close': '189.60255432128903', 'Volume': '76873000'}]}

exec(code, env_args)
