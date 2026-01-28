code = """import json
# Load large results from file paths
with open(var_call_LRt0exprHfOJ1inMQRTPA5Sp, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_CrVKZQBqTmnPuAKFQp6jscWu, 'r') as f:
    trade_tables = json.load(f)
symbols_stockinfo = [r['Symbol'] for r in stockinfo_records]
available_symbols = sorted([s for s in symbols_stockinfo if s in trade_tables])
output = {'count': len(available_symbols), 'sample_symbols': available_symbols[:50]}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_hR1ujv8iGbULDzfr7OEeOW0w': 'file_storage/call_hR1ujv8iGbULDzfr7OEeOW0w.json', 'var_call_CrVKZQBqTmnPuAKFQp6jscWu': 'file_storage/call_CrVKZQBqTmnPuAKFQp6jscWu.json', 'var_call_LRt0exprHfOJ1inMQRTPA5Sp': 'file_storage/call_LRt0exprHfOJ1inMQRTPA5Sp.json'}

exec(code, env_args)
