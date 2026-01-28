code = """import json
# load symbol list from previous result file
with open(var_call_Gmrvj9ea7v46kRfuBSfS9yXm, 'r') as f:
    etf_symbols = json.load(f)
# load stocktrade table list
with open(var_call_20NHNe69ryX0z8aharn7rbQK, 'r') as f:
    trade_tables = json.load(f)

# compute intersection
trade_set = set(trade_tables)
symbols_to_check = [s for s in etf_symbols if s in trade_set]

import json
print('__RESULT__:')
print(json.dumps(symbols_to_check))"""

env_args = {'var_call_0P2qHEebXBBE5ncXpuNKLpGw': 'file_storage/call_0P2qHEebXBBE5ncXpuNKLpGw.json', 'var_call_Gmrvj9ea7v46kRfuBSfS9yXm': 'file_storage/call_Gmrvj9ea7v46kRfuBSfS9yXm.json', 'var_call_20NHNe69ryX0z8aharn7rbQK': 'file_storage/call_20NHNe69ryX0z8aharn7rbQK.json'}

exec(code, env_args)
