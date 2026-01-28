code = """import json
with open(var_call_WaEvCHYDu8q5PYvnJxAh1X2s, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_C9yV3KAORv9nL5ONxiYWO0Ud, 'r') as f:
    trade_tables = json.load(f)
symbols = [r['Symbol'] for r in stockinfo]
available_symbols = [s for s in symbols if s in trade_tables]
selects = []
for s in available_symbols:
    sel = "SELECT '%s' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"%s\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX(\"Adj Close\") > 200" % (s, s)
    selects.append(sel)
if selects:
    sql = '\nUNION ALL\n'.join(selects) + '\nORDER BY symbol;'
else:
    sql = ''
result = {'symbols_count_checked': len(available_symbols), 'symbols_checked_count': len(available_symbols), 'sql': sql}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7unxnarEaWwSx7trThvVwizq': ['stockinfo'], 'var_call_WaEvCHYDu8q5PYvnJxAh1X2s': 'file_storage/call_WaEvCHYDu8q5PYvnJxAh1X2s.json', 'var_call_C9yV3KAORv9nL5ONxiYWO0Ud': 'file_storage/call_C9yV3KAORv9nL5ONxiYWO0Ud.json'}

exec(code, env_args)
