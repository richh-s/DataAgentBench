code = """import json, pandas as pd

ema = var_call_x8TQi7XwKje60ksRKDBl3W3X
path = var_call_92u4sXiEitQKiogPZYz7kn5L
with open(path) as f:
    defs = json.load(f)

df_ema = pd.DataFrame(ema)
df_defs = pd.DataFrame(defs)

# level field may be string
try:
    df_defs['level'] = df_defs['level'].astype(float)
except:
    pass

# join on prefix match: definition symbol equals level4 code prefix (before any subgroup digits)
# but our level4 codes like C04B2235 - likely symbol 'C04B' at level 4; adjust

def map_symbol(code):
    # take first 4 chars e.g. C04B, B41F
    return code[:4]

df_ema['symbol'] = df_ema['code_level4'].map(map_symbol)

merged = pd.merge(df_ema, df_defs[df_defs['level']==4.0][['symbol','titleFull']], on='symbol', how='left')

result = []
for _, r in merged.iterrows():
    result.append({
        'cpc_group_code_level4': r['code_level4'],
        'cpc_symbol_level4': r['symbol'],
        'titleFull': r.get('titleFull') or '',
        'best_year': int(r['best_year']),
        'best_ema': r['best_ema']
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RK9mtT0CJ3Sjr4waejsYnD9b': 'file_storage/call_RK9mtT0CJ3Sjr4waejsYnD9b.json', 'var_call_x8TQi7XwKje60ksRKDBl3W3X': [{'code_level4': 'C04B2235', 'best_year': 2019, 'best_ema': 32.0}, {'code_level4': 'C04B35', 'best_year': 2019, 'best_ema': 12.0}, {'code_level4': 'E02F9', 'best_year': 2019, 'best_ema': 3.0}, {'code_level4': 'E02F3', 'best_year': 2019, 'best_ema': 3.0}, {'code_level4': 'F41H11', 'best_year': 2019, 'best_ema': 2.0}, {'code_level4': 'F42B3', 'best_year': 2019, 'best_ema': 2.0}, {'code_level4': 'B41F21', 'best_year': 2019, 'best_ema': 2.0}, {'code_level4': 'C09K11', 'best_year': 2019, 'best_ema': 2.0}, {'code_level4': 'C04B40', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'B41F22', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'B60S9', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'B66C23', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'F02D15', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'F02D13', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'F02D41', 'best_year': 2019, 'best_ema': 1.0}, {'code_level4': 'Y02T10', 'best_year': 2019, 'best_ema': 1.0}], 'var_call_92u4sXiEitQKiogPZYz7kn5L': 'file_storage/call_92u4sXiEitQKiogPZYz7kn5L.json'}

exec(code, env_args)
