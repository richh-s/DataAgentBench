code = """import json
path_info = var_call_8UvW6KsMY3Sq7CHGXoSaQiC8
path_trade = var_call_HRvR8LlnRtRJNSMY9MC1q8G7
info = json.load(open(path_info, 'r'))
trade_tables = set(json.load(open(path_trade, 'r')))
symbols_info = [rec['Symbol'] for rec in info]
symbols = [s for s in symbols_info if s in trade_tables]
parts = []
qadj = chr(34) + 'Adj Close' + chr(34)
for s in symbols:
    dq = chr(34) + s + chr(34)
    part = "SELECT * FROM (SELECT '{sym}' AS symbol, MAX({qadj}) AS max_adj FROM {dq} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') WHERE max_adj > 200".format(sym=s, qadj=qadj, dq=dq)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) if parts else "SELECT NULL as symbol, NULL as max_adj WHERE 0=1"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json', 'var_call_HRvR8LlnRtRJNSMY9MC1q8G7': 'file_storage/call_HRvR8LlnRtRJNSMY9MC1q8G7.json'}

exec(code, env_args)
