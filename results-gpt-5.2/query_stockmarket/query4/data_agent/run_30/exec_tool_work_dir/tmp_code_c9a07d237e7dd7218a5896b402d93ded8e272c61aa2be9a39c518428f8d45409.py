code = """import json, pandas as pd

# Load NYSE non-ETF symbols from stockinfo result file
path_info = var_call_4yJxBgN7c7oIup6a2mx3hC8o
with open(path_info, 'r') as f:
    info = json.load(f)
df_info = pd.DataFrame(info)

# Load available trade tables list
path_tbl = var_call_6kpaJecmr7U1o7D0tLDOguVk
with open(path_tbl, 'r') as f:
    tbls = set(json.load(f))

symbols = sorted(set(df_info['Symbol']).intersection(tbls))

# take a manageable subset? We'll query all in chunks later; here just output symbol list for next step
out = json.dumps({"n_symbols": len(symbols), "symbols": symbols})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_4yJxBgN7c7oIup6a2mx3hC8o': 'file_storage/call_4yJxBgN7c7oIup6a2mx3hC8o.json', 'var_call_6kpaJecmr7U1o7D0tLDOguVk': 'file_storage/call_6kpaJecmr7U1o7D0tLDOguVk.json'}

exec(code, env_args)
