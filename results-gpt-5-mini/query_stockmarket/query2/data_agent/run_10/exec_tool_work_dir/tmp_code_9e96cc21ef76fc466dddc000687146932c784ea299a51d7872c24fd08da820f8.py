code = """import json
# Load the stockinfo symbols (file path provided in var_call_JJXAp8DK6M2yHvYQPNfOY1bj)
with open(var_call_JJXAp8DK6M2yHvYQPNfOY1bj, 'r') as f:
    stockinfo_records = json.load(f)
stockinfo_syms = [r['Symbol'] for r in stockinfo_records]

# Load the stocktrade table list
with open(var_call_Cvbmm6EWb3LxORAAoWskYzKl, 'r') as f:
    trade_tables = json.load(f)

# Intersection
trade_set = set(trade_tables)
stockinfo_set = set(stockinfo_syms)
common = sorted(list(stockinfo_set & trade_set))

out = {
    'num_etfs_in_stockinfo': len(stockinfo_syms),
    'num_tables_in_trade_db': len(trade_tables),
    'num_common_symbols': len(common),
    'has_SPY': 'SPY' in common,
    'sample_common_first_20': common[:20]
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_JJXAp8DK6M2yHvYQPNfOY1bj': 'file_storage/call_JJXAp8DK6M2yHvYQPNfOY1bj.json', 'var_call_Cvbmm6EWb3LxORAAoWskYzKl': 'file_storage/call_Cvbmm6EWb3LxORAAoWskYzKl.json'}

exec(code, env_args)
