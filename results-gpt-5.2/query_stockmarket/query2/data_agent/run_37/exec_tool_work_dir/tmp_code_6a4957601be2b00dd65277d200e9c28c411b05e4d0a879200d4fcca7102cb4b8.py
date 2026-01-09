code = """import json, pandas as pd

# Load NYSE Arca ETFs list
p = var_call_sk5XKsNrqckiS1jjOTMbwfDa
with open(p, 'r') as f:
    etfs = json.load(f)

etf_symbols = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

# Load all available price tables in DuckDB
p2 = var_call_wUZv4P1r1qG7d8sTKMa3SlIi
with open(p2, 'r') as f:
    tables = json.load(f)

tables_set = set(tables)

symbols_in_both = [s for s in etf_symbols if s in tables_set]

print('__RESULT__:')
print(json.dumps({'symbols_in_both': symbols_in_both, 'missing_price_table': [s for s in etf_symbols if s not in tables_set], 'n_etfs_arca': len(etf_symbols), 'n_in_both': len(symbols_in_both)}))"""

env_args = {'var_call_sk5XKsNrqckiS1jjOTMbwfDa': 'file_storage/call_sk5XKsNrqckiS1jjOTMbwfDa.json', 'var_call_wUZv4P1r1qG7d8sTKMa3SlIi': 'file_storage/call_wUZv4P1r1qG7d8sTKMa3SlIi.json'}

exec(code, env_args)
