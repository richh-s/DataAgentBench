code = """import json
p = var_call_qO5UOjJhgUd3ljUq9Cpo6Q7e
with open(p) as f:
    data = json.load(f)
symbols = [rec['Symbol'] for rec in data]
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_NOrOeolxry3KNh5kwmiCZwYH': 'file_storage/call_NOrOeolxry3KNh5kwmiCZwYH.json', 'var_call_mt89zRyxGP2HAtEkz4Dmna3z': 'file_storage/call_mt89zRyxGP2HAtEkz4Dmna3z.json', 'var_call_qO5UOjJhgUd3ljUq9Cpo6Q7e': 'file_storage/call_qO5UOjJhgUd3ljUq9Cpo6Q7e.json', 'var_call_pzgIXutuSg5PSbl8pUosa5yX': {'count': 234, 'first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
