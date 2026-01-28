code = """import json
data = json.load(open(var_call_UlwTYnxK8aLPvZD04YhbL5xk, 'r'))
symbols = [rec['Symbol'] for rec in data]
info = {'n_symbols': len(symbols), 'first_20': symbols[:20]}
print('__RESULT__:')
print(json.dumps(info))"""

env_args = {'var_call_Ad4UsH2M8L6uC8cGxj7jUQRQ': 'file_storage/call_Ad4UsH2M8L6uC8cGxj7jUQRQ.json', 'var_call_SiXzvTbfmBNhOMQ5JDOIG3NS': 'file_storage/call_SiXzvTbfmBNhOMQ5JDOIG3NS.json', 'var_call_UlwTYnxK8aLPvZD04YhbL5xk': 'file_storage/call_UlwTYnxK8aLPvZD04YhbL5xk.json'}

exec(code, env_args)
