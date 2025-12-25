code = """import json, pandas as pd, os
# load NASDAQ Capital Market symbols
stockinfo_file = var_call_dkrKcwQT9rg1LAxzgWcAreHK
with open(stockinfo_file, 'r') as f:
    stockinfo = json.load(f)
stockinfo_df = pd.DataFrame(stockinfo)
nasdaq_cap_symbols = sorted(set(stockinfo_df['Symbol']))
# load all available trade tables symbols
symbols_file = var_call_UIhvbxgEIqIepnIVxvgXtPOU
with open(symbols_file, 'r') as f:
    all_trade_symbols = json.load(f)
# intersect
target_symbols = sorted(set(nasdaq_cap_symbols).intersection(all_trade_symbols))
result = json.dumps(target_symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_s2uPdYaejgejFzJOxR2KtJjm': 'file_storage/call_s2uPdYaejgejFzJOxR2KtJjm.json', 'var_call_dkrKcwQT9rg1LAxzgWcAreHK': 'file_storage/call_dkrKcwQT9rg1LAxzgWcAreHK.json', 'var_call_UIhvbxgEIqIepnIVxvgXtPOU': 'file_storage/call_UIhvbxgEIqIepnIVxvgXtPOU.json'}

exec(code, env_args)
