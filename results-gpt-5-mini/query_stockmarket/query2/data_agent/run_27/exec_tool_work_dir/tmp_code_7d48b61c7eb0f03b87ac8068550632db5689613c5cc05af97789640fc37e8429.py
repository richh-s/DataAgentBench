code = """import json
path = var_call_unWnvVZCxmBE1OLj05n70iIi
symbols = json.load(open(path, 'r'))
parts = []
for s in symbols:
    dq = chr(34) + s + chr(34)
    adj = chr(34) + 'Adj Close' + chr(34)
    part = "SELECT '{sym}' AS symbol, MAX({adj}) AS max_adj FROM {dq} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=s, adj=adj, dq=dq)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts)
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json', 'var_call_HRvR8LlnRtRJNSMY9MC1q8G7': 'file_storage/call_HRvR8LlnRtRJNSMY9MC1q8G7.json', 'var_call_unWnvVZCxmBE1OLj05n70iIi': 'file_storage/call_unWnvVZCxmBE1OLj05n70iIi.json', 'var_call_ipsmcCFsQUZ2OYAbtvg1VfgI': []}

exec(code, env_args)
