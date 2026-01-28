code = """import json
with open(var_call_aCAbdB3jQgRTH8mqdp5wsMj6, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_tJA9EW3OouFCqMIGZNLFpvYc, 'r') as f:
    trade_tables = json.load(f)

symbols_info = [r['Symbol'] for r in stockinfo]
available_symbols = [s for s in symbols_info if s in trade_tables]

parts = []
for sym in available_symbols:
    # safe symbol
    s = sym.replace("'", "''")
    part = (
        "SELECT '{s}' AS symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * NULLIF(\"Low\",0) AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"{s}\"".format(s=s)
    )
    parts.append(part)
union_sql = "\nUNION ALL\n".join(parts)
sql = "SELECT symbol, cnt FROM (\n" + union_sql + "\n) ORDER BY cnt DESC, symbol ASC LIMIT 5;"

out = {'sql': sql, 'num_symbols': len(available_symbols)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aCAbdB3jQgRTH8mqdp5wsMj6': 'file_storage/call_aCAbdB3jQgRTH8mqdp5wsMj6.json', 'var_call_tJA9EW3OouFCqMIGZNLFpvYc': 'file_storage/call_tJA9EW3OouFCqMIGZNLFpvYc.json', 'var_call_aSp5DOh5raQx05jOOLGTzCz5': {'num_stockinfo_symbols': 86, 'num_available': 86, 'available_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
