code = """import json
symbols = var_call_61D5Hts0AV2zfEZjgSlbihxP
if isinstance(symbols, str):
    with open(symbols, 'r') as f:
        symbols = json.load(f)
symbols = [s for s in symbols if s]
parts = []
for s in symbols:
    part = 'SELECT "{}" AS symbol, MAX("Adj Close") AS max_adj FROM "{}" WHERE Date >= \"2015-01-01\" AND Date <= \"2015-12-31\"'.format(s, s)
    parts.append(part)
union_sql = '\nUNION ALL\n'.join(parts)
full_sql = 'SELECT symbol, max_adj FROM (\n' + union_sql + '\n) AS t WHERE max_adj > 200;'
print('__RESULT__:')
print(json.dumps(full_sql))"""

env_args = {'var_call_Day7OVVdk4ENSW1nwiqCArEm': 'file_storage/call_Day7OVVdk4ENSW1nwiqCArEm.json', 'var_call_RBlOD3WsjJAEM6XkSVpae7va': 'file_storage/call_RBlOD3WsjJAEM6XkSVpae7va.json', 'var_call_61D5Hts0AV2zfEZjgSlbihxP': 'file_storage/call_61D5Hts0AV2zfEZjgSlbihxP.json'}

exec(code, env_args)
