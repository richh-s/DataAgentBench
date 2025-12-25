code = """import json, pandas as pd

ema_groups = var_call_sXki7wQRAZ8ioFODBVpz9gmG
with open(var_call_lCy1gnBmr0jviCz4yLbfPX5O, 'r') as f:
    defs = json.load(f)

df_defs = pd.DataFrame(defs)

rows = []
for r in ema_groups:
    g = r['group']
    title = None
    # match exact symbol equal to group
    m = df_defs[df_defs['symbol'] == g]
    if not m.empty:
        title = m.iloc[0]['titleFull']
    rows.append({'cpc_group_code': g, 'titleFull': title, 'best_year': r['best_year'], 'ema': r['best_ema']})

rows_sorted = sorted(rows, key=lambda x: x['ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(rows_sorted))"""

env_args = {'var_call_YuWLwZPaOOAsTRTZactsHp86': 'file_storage/call_YuWLwZPaOOAsTRTZactsHp86.json', 'var_call_lCy1gnBmr0jviCz4yLbfPX5O': 'file_storage/call_lCy1gnBmr0jviCz4yLbfPX5O.json', 'var_call_sXki7wQRAZ8ioFODBVpz9gmG': [{'group': 'C04', 'best_year': 1020, 'best_ema': 45.0}, {'group': 'B29', 'best_year': 1020, 'best_ema': 15.0}, {'group': 'F02', 'best_year': 1120, 'best_ema': 9.1}, {'group': 'E02', 'best_year': 1020, 'best_ema': 6.0}, {'group': 'B41', 'best_year': 1020, 'best_ema': 3.0}, {'group': 'F04', 'best_year': 1120, 'best_ema': 2.0}, {'group': 'F41', 'best_year': 1020, 'best_ema': 2.0}, {'group': 'F42', 'best_year': 1020, 'best_ema': 2.0}, {'group': 'C09', 'best_year': 1020, 'best_ema': 2.0}, {'group': 'B66', 'best_year': 1020, 'best_ema': 1.0}, {'group': 'B63', 'best_year': 1020, 'best_ema': 1.0}, {'group': 'B60', 'best_year': 1020, 'best_ema': 1.0}, {'group': 'Y02', 'best_year': 1020, 'best_ema': 1.0}]}

exec(code, env_args)
