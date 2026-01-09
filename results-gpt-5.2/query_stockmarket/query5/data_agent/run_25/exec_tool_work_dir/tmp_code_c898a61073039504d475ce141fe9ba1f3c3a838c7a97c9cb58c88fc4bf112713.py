code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_Wpf4IymfEgb0zEcD2bqrB3Mg)
records = json.loads(path.read_text())
df = pd.DataFrame(records)
# keep common stocks only: drop symbols with 5th char in {W,R,P,Q,U,V} and those containing '^' etc.
exc5 = set(list('WRPQUV'))
def is_common(sym):
    if sym is None: return False
    if '^' in sym or '/' in sym: return False
    if len(sym) >= 5 and sym[4] in exc5:  # 5th char
        return False
    return True

df = df[df['Symbol'].map(is_common)].reset_index(drop=True)
res = df[['Symbol','company_name']].to_dict('records')
print('__RESULT__:')
print(json.dumps({'tickers': res, 'n': len(res)}))"""

env_args = {'var_call_Wpf4IymfEgb0zEcD2bqrB3Mg': 'file_storage/call_Wpf4IymfEgb0zEcD2bqrB3Mg.json'}

exec(code, env_args)
