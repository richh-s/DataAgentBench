code = """import json, pandas as pd

# Load stockinfo result (may be file path)
info_src = var_call_zlYRMan0HPetvjLjgeuO6agi
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        info = json.load(f)
else:
    info = info_src

df_info = pd.DataFrame(info)
syms = df_info['Symbol'].dropna().unique().tolist()

# Load list of trade tables
trade_src = var_call_ZApv5rHSEBFqhwGyKtTJeGFr
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        tables = json.load(f)
else:
    tables = trade_src

tables_set = set(tables)
syms = [s for s in syms if s in tables_set]

# limit to tickers that look like common stocks (exclude warrants/units/rights etc.)
# keep 1-5 uppercase letters only
import re
syms = [s for s in syms if re.fullmatch(r'[A-Z]{1,5}', s or '')]

# chunk tickers for SQL length
chunks = [syms[i:i+120] for i in range(0, len(syms), 120)]

print('__RESULT__:')
print(json.dumps({'symbols': syms, 'chunks': chunks}))"""

env_args = {'var_call_zlYRMan0HPetvjLjgeuO6agi': 'file_storage/call_zlYRMan0HPetvjLjgeuO6agi.json', 'var_call_ZApv5rHSEBFqhwGyKtTJeGFr': 'file_storage/call_ZApv5rHSEBFqhwGyKtTJeGFr.json'}

exec(code, env_args)
