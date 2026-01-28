code = """import json
import os

# Read NYSE Arca ETFs list
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)
nyse_arca_etfs = [etf['Symbol'] for etf in nyse_arca_data]

# Prioritize known high-value ETF categories
high_price_candidates = []

# Check prominent index ETFs first
prominent_etfs = ['SPY', 'IVV', 'VOO', 'DIA', 'QQQ', 'VTI', 'VEA', 'VWO', 'EFA', 'EEM', 'IWM', 'IWB', 'IWF', 'IWD', 'IVW', 'IVE', 'IJH', 'IJR', 'IJT', 'ILF', 'EFA', 'ACWI']

# Filter to NYSE Arca ETFs
prominent_in_arca = [etf for etf in prominent_etfs if etf in nyse_arca_etfs]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'prominent_etfs_in_arca': len(prominent_in_arca),
    'sample_prominent': prominent_in_arca[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_stocktrade_tables': 2753, 'etfs_with_price_data': 1435, 'sample_etfs': ['GSY', 'EMLP', 'MMIN', 'SCHI', 'IAT', 'IJS', 'SIJ', 'RWM', 'ULE', 'DBEF']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_nyse_arca_etfs': 1435, 'etfs_with_data': 1435}, 'var_functions.query_db:18': [], 'var_functions.query_db:20': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:22': [{'max_adj_close': '125.2300033569336'}], 'var_functions.query_db:26': [{'max_adj_close': '110.42893981933594'}], 'var_functions.query_db:28': [{'max_adj_close': '193.5270538330078'}], 'var_functions.query_db:30': [{'max_adj_close': '66.95523071289062'}]}

exec(code, env_args)
