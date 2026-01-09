code = """import json, pandas as pd
from pathlib import Path

p = Path(var_call_5rlnM7Pvk7TR2Co1NWSE5ph4)
rows = json.loads(p.read_text())
df = pd.DataFrame(rows)
tickers = sorted(df['Symbol'].dropna().unique().tolist())
print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'n': len(tickers)}))"""

env_args = {'var_call_5rlnM7Pvk7TR2Co1NWSE5ph4': 'file_storage/call_5rlnM7Pvk7TR2Co1NWSE5ph4.json'}

exec(code, env_args)
