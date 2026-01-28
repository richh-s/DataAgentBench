code = """import json
p1 = var_call_zMD84XMnjkH9UlsG24xJ8ZSe
p2 = var_call_KyzReNveROt475cBa6fObcUY
# Load possibly file-path stored results
if isinstance(p1, str):
    with open(p1, 'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = p1
if isinstance(p2, str):
    with open(p2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = p2
symbols_stockinfo = set([rec['Symbol'] for rec in stockinfo if rec.get('Symbol')])
trade_tables_set = set(trade_tables)
symbols = sorted(symbols_stockinfo & trade_tables_set)
# Build SQL
selects = []
for s in symbols:
    sel = ("SELECT '{}' AS symbol, "
           "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_days, "
           "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_days "
           "FROM \"{}\" "
           "WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'").format(s, s)
    selects.append(sel)
sql = ' UNION ALL '.join(selects)
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_uXvZcerR4ZItvITwGgYWUY3A': 'file_storage/call_uXvZcerR4ZItvITwGgYWUY3A.json', 'var_call_KyzReNveROt475cBa6fObcUY': 'file_storage/call_KyzReNveROt475cBa6fObcUY.json', 'var_call_zMD84XMnjkH9UlsG24xJ8ZSe': 'file_storage/call_zMD84XMnjkH9UlsG24xJ8ZSe.json'}

exec(code, env_args)
