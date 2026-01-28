code = """import json
with open(var_call_d6OF5lNHFpCkdROe3WXhSEIn, 'r') as f:
    etf_list = json.load(f)
with open(var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_list]
trade_set = set(trade_tables)
common_symbols = [s for s in etf_symbols if s in trade_set]
selects = []
for s in common_symbols:
    lit = s.replace("'", "''")
    sel = '(SELECT "{}" AS Symbol FROM "{}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1)'.format(lit, s)
    selects.append(sel)
if selects:
    sql = '\nUNION ALL\n'.join(selects) + '\nORDER BY Symbol;'
else:
    sql = ''
out = {'sql': sql, 'candidate_count': len(common_symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d6OF5lNHFpCkdROe3WXhSEIn': 'file_storage/call_d6OF5lNHFpCkdROe3WXhSEIn.json', 'var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p': 'file_storage/call_pWaf7Rt5WZqXxRrWb0Xhaa1p.json'}

exec(code, env_args)
