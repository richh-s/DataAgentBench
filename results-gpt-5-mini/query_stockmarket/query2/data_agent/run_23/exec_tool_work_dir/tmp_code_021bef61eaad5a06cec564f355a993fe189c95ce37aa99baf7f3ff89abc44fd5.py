code = """import json
with open(var_call_L8lDGwg5aCrUUSHmMM5cQmvn, 'r') as f:
    common = json.load(f)

chunk_size = 100
sql_chunks = []
for i in range(0, len(common), chunk_size):
    chunk = common[i:i+chunk_size]
    parts = []
    for s in chunk:
        # use single quotes around symbol literal, double quotes around identifiers
        parts.append("SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31'".format(s=s))
    sql = 'SELECT Symbol, max_adj FROM (\n' + '\nUNION ALL\n'.join(parts) + '\n) t WHERE max_adj > 200 ORDER BY Symbol;'
    sql_chunks.append(sql)

print('__RESULT__:')
print(json.dumps(sql_chunks))"""

env_args = {'var_call_xUOaxmbbff9vQrRDvVe48yow': 'file_storage/call_xUOaxmbbff9vQrRDvVe48yow.json', 'var_call_D0rlb06yrhA5kxJcpmoUdIgJ': 'file_storage/call_D0rlb06yrhA5kxJcpmoUdIgJ.json', 'var_call_L8lDGwg5aCrUUSHmMM5cQmvn': 'file_storage/call_L8lDGwg5aCrUUSHmMM5cQmvn.json', 'var_call_VsYrBy8yyQKMEhCVkaGgn0R2': 1435}

exec(code, env_args)
