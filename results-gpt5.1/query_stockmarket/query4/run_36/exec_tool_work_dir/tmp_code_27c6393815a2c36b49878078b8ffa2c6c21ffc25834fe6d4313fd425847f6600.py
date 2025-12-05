code = """import json, pandas as pd
syms = pd.read_json(var_call_ztnt8JUGoRdERZNfcvJ5OBJW)
info = pd.read_json(var_call_vZUxSHU43cF35TunCMYlWLQL)
nyse_syms = set(info['Symbol'])
common = [s for s in syms[0].tolist() if s in nyse_syms]
result = json.dumps(common)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_ztnt8JUGoRdERZNfcvJ5OBJW': 'file_storage/call_ztnt8JUGoRdERZNfcvJ5OBJW.json', 'var_call_vZUxSHU43cF35TunCMYlWLQL': 'file_storage/call_vZUxSHU43cF35TunCMYlWLQL.json'}

exec(code, env_args)
