code = """import json, pandas as pd

# load symbols list
p = var_call_DqrJ20Dt6kRZ0Xf4cm1RtXQg
with open(p, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# keep likely common stocks: symbols without special NASDAQ suffixes (W, U, R, etc.)
# We'll still allow dots/hyphens? Most are plain.
import re

def is_common(sym):
    return re.fullmatch(r"[A-Z]{1,5}", sym) is not None

symbols = [s for s in df['Symbol'].dropna().unique().tolist() if is_common(s)]

out = json.dumps({'n_total': int(df['Symbol'].nunique()), 'n_common': len(symbols), 'symbols': symbols[:200]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DqrJ20Dt6kRZ0Xf4cm1RtXQg': 'file_storage/call_DqrJ20Dt6kRZ0Xf4cm1RtXQg.json'}

exec(code, env_args)
