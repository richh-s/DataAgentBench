code = """import json
with open(var_call_f1r85XmWDTSl5Ddo53iy59CI, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_6Z6sS3PLvRX8NaXWX42bHpQu, 'r') as f:
    tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo if 'Symbol' in rec and rec.get('Listing Exchange') == 'N' and (rec.get('ETF') is None or rec.get('ETF') != 'Y')]
available = [s for s in symbols if s in tables]
selects = []
for s in available:
    sel = "SELECT '{}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down FROM {} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(s, s)
    selects.append(sel)

sql = '\nUNION ALL\n'.join(selects) if selects else ''
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_f1r85XmWDTSl5Ddo53iy59CI': 'file_storage/call_f1r85XmWDTSl5Ddo53iy59CI.json', 'var_call_6Z6sS3PLvRX8NaXWX42bHpQu': 'file_storage/call_6Z6sS3PLvRX8NaXWX42bHpQu.json'}

exec(code, env_args)
