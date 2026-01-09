code = """import json, pandas as pd

# load cap market symbols
cap_path = var_call_H1EzipIeXpIxlsCS4XeHhHeF
with open(cap_path, 'r') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_df = cap_df.dropna(subset=['Symbol'])
cap_symbols = set(cap_df['Symbol'].astype(str))

# load available trade tables
trade_path = var_call_QvNSzJv7DaVr49HT6l7W4OSF
with open(trade_path, 'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)

symbols = sorted(list(cap_symbols.intersection(trade_set)))

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_H1EzipIeXpIxlsCS4XeHhHeF': 'file_storage/call_H1EzipIeXpIxlsCS4XeHhHeF.json', 'var_call_QvNSzJv7DaVr49HT6l7W4OSF': 'file_storage/call_QvNSzJv7DaVr49HT6l7W4OSF.json'}

exec(code, env_args)
