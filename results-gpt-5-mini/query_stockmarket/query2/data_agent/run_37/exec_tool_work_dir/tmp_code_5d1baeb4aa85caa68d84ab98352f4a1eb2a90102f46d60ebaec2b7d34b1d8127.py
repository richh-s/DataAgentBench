code = """import json
symbols = var_call_bFVjO27fud3o5M6hrpsjwweI
chunksize = 150
sqls = []
for i in range(0, len(symbols), chunksize):
    chunk = symbols[i:i+chunksize]
    parts = []
    for s in chunk:
        # use single quotes around the symbol literal
        parts.append("SELECT '{s}' AS Symbol, (SELECT MAX(\"Adj Close\") FROM \"{s}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31') AS max_adj".format(s=s))
    sql = "SELECT Symbol, max_adj FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) WHERE max_adj IS NOT NULL AND max_adj > 200 ORDER BY Symbol;"
    sqls.append(sql)
print("__RESULT__:")
print(json.dumps(sqls))"""

env_args = {'var_call_uaaUjkgCkmEkiZqaNlFP7iBq': 'file_storage/call_uaaUjkgCkmEkiZqaNlFP7iBq.json', 'var_call_V3UlhusiiMVsL0D2qHUs1Des': 'file_storage/call_V3UlhusiiMVsL0D2qHUs1Des.json', 'var_call_bFVjO27fud3o5M6hrpsjwweI': 'file_storage/call_bFVjO27fud3o5M6hrpsjwweI.json', 'var_call_emu3k5XzAEDrGhgqRlRw7GFc': [{'max_adj': '193.3121490478516'}], 'var_call_I0cJEmOL701eCITt4TLqJdHq': [{'max_adj': '177.17626953125'}]}

exec(code, env_args)
