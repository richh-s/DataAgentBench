code = """import json, pandas as pd

path_info = var_call_1azq8avYekP4AJfnP0YbucJf
with open(path_info, 'r') as f:
    info = json.load(f)
df_info = pd.DataFrame(info)

path_tbls = var_call_1WDp8YTpSz1oSWbHEA5yX3HS
with open(path_tbls, 'r') as f:
    tbls = set(json.load(f))

symbols = [s for s in df_info['Symbol'].tolist() if s in tbls]

out = json.dumps({'n_symbols': len(symbols), 'symbols': symbols})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_1azq8avYekP4AJfnP0YbucJf': 'file_storage/call_1azq8avYekP4AJfnP0YbucJf.json', 'var_call_1WDp8YTpSz1oSWbHEA5yX3HS': 'file_storage/call_1WDp8YTpSz1oSWbHEA5yX3HS.json'}

exec(code, env_args)
