code = """import json
with open(var_call_VSBCcFT8Su5uJNbSN9uv1sFU, 'r') as f:
    data = json.load(f)
symbols = data.get('symbols_to_check', [])
parts = []
for s in symbols:
    part = '''SELECT '{}' AS symbol, MAX("Adj Close") AS max_adj FROM "{}" WHERE "Date">='2015-01-01' AND "Date"<='2015-12-31' '''.format(s, s)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts)
full_sql = 'SELECT symbol, max_adj FROM (\n' + sql + '\n) WHERE max_adj > 200 ORDER BY symbol;'
print('__RESULT__:')
print(json.dumps({'sql': full_sql}))"""

env_args = {'var_call_81ZiPdIF1G7CPi99Rtt3w4pr': 'file_storage/call_81ZiPdIF1G7CPi99Rtt3w4pr.json', 'var_call_ONhfeFX5gPfa2gDRgYKNP6U1': 'file_storage/call_ONhfeFX5gPfa2gDRgYKNP6U1.json', 'var_call_VSBCcFT8Su5uJNbSN9uv1sFU': 'file_storage/call_VSBCcFT8Su5uJNbSN9uv1sFU.json'}

exec(code, env_args)
