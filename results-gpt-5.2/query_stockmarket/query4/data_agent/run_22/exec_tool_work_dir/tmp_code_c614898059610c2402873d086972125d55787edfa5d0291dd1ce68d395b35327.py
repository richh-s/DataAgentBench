code = """import json, pandas as pd

# Load NYSE non-ETF symbols from SQLite query result (may be file path)
nyse_src = var_call_5822wOwfcLaYYadreBI7KG5c
if isinstance(nyse_src, str):
    with open(nyse_src, 'r') as f:
        nyse = json.load(f)
else:
    nyse = nyse_src

trade_src = var_call_YYdJVoiG0lczBGplEQymgbJz
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_src

nyse_syms = {r['Symbol'] for r in nyse}
available = set(trade_tables)
syms = sorted(list(nyse_syms & available))

print('__RESULT__:')
print(json.dumps({'symbols': syms, 'n': len(syms)}))"""

env_args = {'var_call_DBOLZOLuaoEswnulCgSfwgzw': ['stockinfo'], 'var_call_5822wOwfcLaYYadreBI7KG5c': 'file_storage/call_5822wOwfcLaYYadreBI7KG5c.json', 'var_call_YYdJVoiG0lczBGplEQymgbJz': 'file_storage/call_YYdJVoiG0lczBGplEQymgbJz.json'}

exec(code, env_args)
