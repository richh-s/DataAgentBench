code = """import json
with open(var_call_xUOaxmbbff9vQrRDvVe48yow, 'r') as f:
    stockinfo_results = json.load(f)
with open(var_call_D0rlb06yrhA5kxJcpmoUdIgJ, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [r['Symbol'] for r in stockinfo_results]
common = sorted([s for s in etf_symbols if s in trade_tables])

parts = []
for s in common:
    part = 'SELECT {0!r} AS Symbol, "Adj Close" FROM "{0}" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\''.format(s)
    parts.append(part)

if parts:
    sql = 'SELECT Symbol, MAX("Adj Close") AS max_adj FROM (\n' + '\nUNION ALL\n'.join(parts) + '\n) AS t GROUP BY Symbol HAVING MAX("Adj Close") > 200 ORDER BY Symbol;'
else:
    sql = '-- No common symbols found between stockinfo ETFs and trade tables.'

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_xUOaxmbbff9vQrRDvVe48yow': 'file_storage/call_xUOaxmbbff9vQrRDvVe48yow.json', 'var_call_D0rlb06yrhA5kxJcpmoUdIgJ': 'file_storage/call_D0rlb06yrhA5kxJcpmoUdIgJ.json'}

exec(code, env_args)
