code = """import json
with open(var_call_L8lDGwg5aCrUUSHmMM5cQmvn, 'r') as f:
    common = json.load(f)

parts = []
for s in common:
    # Build SQL part without using backslash escapes
    part = "SELECT '{sym}' AS Symbol, \"Adj Close\" FROM \"{sym}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31'".format(sym=s)
    parts.append(part)

if parts:
    sql = "SELECT Symbol, MAX(\"Adj Close\") AS max_adj FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) AS t GROUP BY Symbol HAVING MAX(\"Adj Close\") > 200 ORDER BY Symbol;"
else:
    sql = "-- no symbols"

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_xUOaxmbbff9vQrRDvVe48yow': 'file_storage/call_xUOaxmbbff9vQrRDvVe48yow.json', 'var_call_D0rlb06yrhA5kxJcpmoUdIgJ': 'file_storage/call_D0rlb06yrhA5kxJcpmoUdIgJ.json', 'var_call_L8lDGwg5aCrUUSHmMM5cQmvn': 'file_storage/call_L8lDGwg5aCrUUSHmMM5cQmvn.json'}

exec(code, env_args)
