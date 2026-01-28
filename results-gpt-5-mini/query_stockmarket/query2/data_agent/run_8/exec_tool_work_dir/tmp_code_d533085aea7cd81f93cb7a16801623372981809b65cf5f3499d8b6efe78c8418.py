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
parts = []
for sym in common_syms:
    parts.append("SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS maxadj FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym, sym))
sql = "\nUNION ALL\n".join(parts) + ';'
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_Lb6wOudI1vGIvlWeFmRfaMcq': 'file_storage/call_Lb6wOudI1vGIvlWeFmRfaMcq.json', 'var_call_DT0diiPjDs1dAAdc2zRjJVxt': 'file_storage/call_DT0diiPjDs1dAAdc2zRjJVxt.json'}

exec(code, env_args)
