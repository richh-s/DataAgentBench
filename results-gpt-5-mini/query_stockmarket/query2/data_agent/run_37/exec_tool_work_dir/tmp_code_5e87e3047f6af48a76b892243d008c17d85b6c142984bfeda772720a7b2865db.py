code = """import json
symbols = var_call_bFVjO27fud3o5M6hrpsjwweI
parts = []
for s in symbols:
    parts.append("SELECT '{s}' AS Symbol, (SELECT MAX(\"Adj Close\") FROM \"{s}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31') AS max_adj".format(s=s))
if parts:
    final_sql = "SELECT Symbol, max_adj FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) WHERE max_adj IS NOT NULL AND max_adj > 200 ORDER BY Symbol;"
else:
    final_sql = "SELECT NULL AS Symbol, NULL AS max_adj WHERE 1=0;"
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_uaaUjkgCkmEkiZqaNlFP7iBq': 'file_storage/call_uaaUjkgCkmEkiZqaNlFP7iBq.json', 'var_call_V3UlhusiiMVsL0D2qHUs1Des': 'file_storage/call_V3UlhusiiMVsL0D2qHUs1Des.json', 'var_call_bFVjO27fud3o5M6hrpsjwweI': 'file_storage/call_bFVjO27fud3o5M6hrpsjwweI.json'}

exec(code, env_args)
