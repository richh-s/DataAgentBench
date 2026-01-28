code = """import json
with open(var_call_aCAbdB3jQgRTH8mqdp5wsMj6, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_tJA9EW3OouFCqMIGZNLFpvYc, 'r') as f:
    trade_tables = json.load(f)

symbols_info = [r['Symbol'] for r in stockinfo]
available_symbols = [s for s in symbols_info if s in trade_tables]

if not available_symbols:
    sql = "SELECT '' as symbol, 0 as cnt WHERE 0=1;"
else:
    parts = []
    for sym in available_symbols:
        part = "SELECT '{sym}' AS symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"{sym}\"".format(sym=sym)
        parts.append(part)
    union_sql = "\nUNION ALL\n".join(parts)
    sql = "SELECT symbol, cnt FROM (\n" + union_sql + "\n) ORDER BY cnt DESC, symbol ASC LIMIT 5;"

result = {'sql': sql, 'num_symbols': len(available_symbols)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aCAbdB3jQgRTH8mqdp5wsMj6': 'file_storage/call_aCAbdB3jQgRTH8mqdp5wsMj6.json', 'var_call_tJA9EW3OouFCqMIGZNLFpvYc': 'file_storage/call_tJA9EW3OouFCqMIGZNLFpvYc.json'}

exec(code, env_args)
