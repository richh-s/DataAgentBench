code = """import json
path = var_call_unWnvVZCxmBE1OLj05n70iIi
symbols = json.load(open(path, 'r'))
parts = []
for s in symbols:
    sym = s
    # build SELECT piece without using backslashes
    part = "SELECT '" + sym + "' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + ';'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json', 'var_call_HRvR8LlnRtRJNSMY9MC1q8G7': 'file_storage/call_HRvR8LlnRtRJNSMY9MC1q8G7.json', 'var_call_unWnvVZCxmBE1OLj05n70iIi': 'file_storage/call_unWnvVZCxmBE1OLj05n70iIi.json'}

exec(code, env_args)
