code = """import json, pandas as pd
syms = pd.read_json(var_call_CTYMQvDXtw1Bh42e8BN63JEV)
symlist = syms['Symbol'].tolist()
chunks = [symlist[i:i+200] for i in range(0, len(symlist), 200)]
result = json.dumps({'chunks': chunks})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_glTYOB3jibACn8eNGTwIGZeQ': 'file_storage/call_glTYOB3jibACn8eNGTwIGZeQ.json', 'var_call_CTYMQvDXtw1Bh42e8BN63JEV': 'file_storage/call_CTYMQvDXtw1Bh42e8BN63JEV.json'}

exec(code, env_args)
