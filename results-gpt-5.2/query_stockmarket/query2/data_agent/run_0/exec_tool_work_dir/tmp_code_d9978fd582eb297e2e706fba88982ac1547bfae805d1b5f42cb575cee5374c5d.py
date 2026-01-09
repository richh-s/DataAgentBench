code = """import json, pandas as pd

# Load NYSE Arca ETFs list from file
path = var_call_bavIZzqXN7oDpRfSFpYuYorR
with open(path, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

# Load available trade tables list
path2 = var_call_OZ4dLgiitANHzlGBCgnXcXoE
with open(path2, 'r') as f:
    tables = set(json.load(f))

# Keep tickers that have a table and are valid SQL identifiers (some have #)
valid = [t for t in tickers if t in tables and t.replace('_','').isalnum()]
invalid = [t for t in tickers if t not in valid]

out = {
    'total_arca_etfs': len(tickers),
    'valid_with_trade_table': len(valid),
    'excluded_nonqueryable_or_missing_table': invalid[:50],
    'excluded_count': len(invalid)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MDAuedzCPOgAQD2J4pERdoeB': ['stockinfo'], 'var_call_bavIZzqXN7oDpRfSFpYuYorR': 'file_storage/call_bavIZzqXN7oDpRfSFpYuYorR.json', 'var_call_OZ4dLgiitANHzlGBCgnXcXoE': 'file_storage/call_OZ4dLgiitANHzlGBCgnXcXoE.json'}

exec(code, env_args)
