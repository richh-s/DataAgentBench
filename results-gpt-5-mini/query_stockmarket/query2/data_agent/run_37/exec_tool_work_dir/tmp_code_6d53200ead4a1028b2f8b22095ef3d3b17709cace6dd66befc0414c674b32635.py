code = """import json
stockinfo_path = var_call_uaaUjkgCkmEkiZqaNlFP7iBq
trade_tables_path = var_call_V3UlhusiiMVsL0D2qHUs1Des
with open(stockinfo_path, 'r') as f:
    stockinfo = json.load(f)
with open(trade_tables_path, 'r') as f:
    trade_tables = json.load(f)
symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
symbols_trade = trade_tables
symbols = sorted([s for s in symbols_stockinfo if s in symbols_trade])
parts = []
for s in symbols:
    part = "SELECT '{sym}' AS Symbol, (SELECT MAX(\"Adj Close\") FROM \"{sym}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31') AS max_adj".format(sym=s)
    parts.append(part)
if parts:
    union_sql = "\nUNION ALL\n".join(parts)
    final_sql = "SELECT Symbol, max_adj FROM (\n" + union_sql + "\n) WHERE max_adj IS NOT NULL AND max_adj > 200 ORDER BY Symbol;"
else:
    final_sql = "SELECT NULL AS Symbol, NULL AS max_adj WHERE 1=0;"
print("__RESULT__:")
print(json.dumps(final_sql))"""

env_args = {'var_call_uaaUjkgCkmEkiZqaNlFP7iBq': 'file_storage/call_uaaUjkgCkmEkiZqaNlFP7iBq.json', 'var_call_V3UlhusiiMVsL0D2qHUs1Des': 'file_storage/call_V3UlhusiiMVsL0D2qHUs1Des.json'}

exec(code, env_args)
