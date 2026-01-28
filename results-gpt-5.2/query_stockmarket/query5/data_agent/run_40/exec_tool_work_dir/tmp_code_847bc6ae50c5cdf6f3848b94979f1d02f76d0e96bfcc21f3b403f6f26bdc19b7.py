code = """import json, pandas as pd
from pathlib import Path

# Load tickers list from file if needed
src = var_call_Zn1ziHBgt0lm454JT5C7GiNT
if isinstance(src, str) and Path(src).exists():
    records = json.loads(Path(src).read_text())
else:
    records = src

df = pd.DataFrame(records)
# ensure unique symbols
symbols = sorted(df['Symbol'].dropna().unique().tolist())

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'company_map': dict(zip(df['Symbol'], df['company_name'])), 'n': len(symbols)}))"""

env_args = {'var_call_Zn1ziHBgt0lm454JT5C7GiNT': 'file_storage/call_Zn1ziHBgt0lm454JT5C7GiNT.json'}

exec(code, env_args)
