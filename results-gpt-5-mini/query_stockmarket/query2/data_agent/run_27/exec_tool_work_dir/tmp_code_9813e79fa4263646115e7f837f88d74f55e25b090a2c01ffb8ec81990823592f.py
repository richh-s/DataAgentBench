code = """import json
path = var_call_unWnvVZCxmBE1OLj05n70iIi
symbols = json.load(open(path, 'r'))
parts = []
for s in symbols:
    # escape double quotes in table name by wrapping with double quotes; assume no double quotes in symbol
    dq = '"' + s + '"'
    part = ("SELECT * FROM (SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj FROM {dq} "
            "WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') WHERE max_adj > 200").format(sym=s, dq=dq)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) if parts else "SELECT NULL as symbol, NULL as max_adj WHERE 0=1"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json', 'var_call_HRvR8LlnRtRJNSMY9MC1q8G7': 'file_storage/call_HRvR8LlnRtRJNSMY9MC1q8G7.json', 'var_call_unWnvVZCxmBE1OLj05n70iIi': 'file_storage/call_unWnvVZCxmBE1OLj05n70iIi.json'}

exec(code, env_args)
