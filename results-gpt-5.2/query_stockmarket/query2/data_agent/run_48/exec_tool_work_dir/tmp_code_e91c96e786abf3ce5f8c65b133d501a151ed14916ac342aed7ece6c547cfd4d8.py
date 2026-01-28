code = """import json, pandas as pd

path_etfs = var_call_FUvH3fPlMC7f1SsXJdXrJGAD
with open(path_etfs, 'r') as f:
    etfs = json.load(f)
df_etfs = pd.DataFrame(etfs)

path_tbls = var_call_IHbpJReSGBxSJZJQN1U6OsBu
with open(path_tbls, 'r') as f:
    tbls = json.load(f)
set_tbls = set(tbls)

symbols = sorted(set(df_etfs['symbol']).intersection(set_tbls))

out = {'n_symbols': len(symbols), 'first10': symbols[:10]}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FUvH3fPlMC7f1SsXJdXrJGAD': 'file_storage/call_FUvH3fPlMC7f1SsXJdXrJGAD.json', 'var_call_IHbpJReSGBxSJZJQN1U6OsBu': 'file_storage/call_IHbpJReSGBxSJZJQN1U6OsBu.json'}

exec(code, env_args)
