code = """import json
with open(var_call_sivacHuiSgcyyLES4JY2Pmbh, 'r') as f:
    stockinfo_records = json.load(f)
symbols = [r['Symbol'] for r in stockinfo_records]
result = {'has_SPY': 'SPY' in symbols, 'total_etfs': len(symbols)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json'}

exec(code, env_args)
