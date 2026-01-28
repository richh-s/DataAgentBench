code = """import json
p1 = var_call_Lb6wOudI1vGIvlWeFmRfaMcq
p2 = var_call_DT0diiPjDs1dAAdc2zRjJVxt
with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    trade_tables = json.load(f)
stockinfo_syms = [rec['Symbol'] for rec in stockinfo]
trade_syms = list(trade_tables)
common_syms = sorted(list(set(stockinfo_syms).intersection(set(trade_syms))))
print("__RESULT__:")
print(json.dumps(common_syms))"""

env_args = {'var_call_Lb6wOudI1vGIvlWeFmRfaMcq': 'file_storage/call_Lb6wOudI1vGIvlWeFmRfaMcq.json', 'var_call_DT0diiPjDs1dAAdc2zRjJVxt': 'file_storage/call_DT0diiPjDs1dAAdc2zRjJVxt.json'}

exec(code, env_args)
