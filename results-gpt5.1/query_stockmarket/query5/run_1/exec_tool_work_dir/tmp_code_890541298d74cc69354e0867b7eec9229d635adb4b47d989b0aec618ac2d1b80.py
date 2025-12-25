code = """import json, pandas as pd
syms = pd.read_json(var_call_pM2FV6lLgafSuYB8s9TzJY44)
symlist = syms['Symbol'].tolist()
chunks = [symlist[i:i+300] for i in range(0, len(symlist), 300)]
result = json.dumps(chunks)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_uQPVZnU823CE2SOlAj7hnl1Z': 'file_storage/call_uQPVZnU823CE2SOlAj7hnl1Z.json', 'var_call_pM2FV6lLgafSuYB8s9TzJY44': 'file_storage/call_pM2FV6lLgafSuYB8s9TzJY44.json'}

exec(code, env_args)
