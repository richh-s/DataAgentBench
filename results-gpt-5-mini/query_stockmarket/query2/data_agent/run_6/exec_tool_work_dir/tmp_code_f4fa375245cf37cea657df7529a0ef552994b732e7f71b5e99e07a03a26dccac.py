code = """import json
with open(var_call_cVHLYR9LXxmmDyfVQWflrOd6) as f:
    obj = json.load(f)
union_sql = obj['sql']
final_sql = "SELECT symbol, max_adj FROM (" + union_sql + ") AS t WHERE max_adj > 200 ORDER BY symbol;"
print('__RESULT__:')
print(json.dumps({'final_sql': final_sql}))"""

env_args = {'var_call_EX7fJ1N82JvZuW4MmN0Y3kC2': ['stockinfo'], 'var_call_H1CE2LVMDOMyJX0LZCSItIcn': 'file_storage/call_H1CE2LVMDOMyJX0LZCSItIcn.json', 'var_call_OA5c55w6JsC8kjxHPlWH1BwK': 'file_storage/call_OA5c55w6JsC8kjxHPlWH1BwK.json', 'var_call_9BRHcV7fJWeN4ZtMsraEwyEp': {'count': 1435}, 'var_call_cVHLYR9LXxmmDyfVQWflrOd6': 'file_storage/call_cVHLYR9LXxmmDyfVQWflrOd6.json', 'var_call_DU2wcpnLY1RQA9VzpioonA4N': [{'symbol': 'SPY', 'max_adj': '193.3121490478516'}]}

exec(code, env_args)
