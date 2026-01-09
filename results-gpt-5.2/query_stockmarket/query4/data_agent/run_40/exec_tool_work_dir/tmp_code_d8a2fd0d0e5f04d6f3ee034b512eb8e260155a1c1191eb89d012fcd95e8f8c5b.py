code = """import json, pandas as pd

# Load NYSE non-ETF symbols from stockinfo query
p = var_call_Fl3OJ3xCnJbTqSpNsuIdopir
with open(p,'r') as f:
    recs = json.load(f)
df = pd.DataFrame(recs)
syms = df['Symbol'].dropna().unique().tolist()

# Load available tables in trade DB
p2 = var_call_QHyGuxLLn4WvSGr1RDAQ51ca
with open(p2,'r') as f:
    tables = set(json.load(f))

# intersection: only those with price tables
syms2 = [s for s in syms if s in tables]

out = {'n_nyse_non_etf': int(len(syms)), 'n_with_trade_table': int(len(syms2)), 'symbols': syms2}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QHyGuxLLn4WvSGr1RDAQ51ca': 'file_storage/call_QHyGuxLLn4WvSGr1RDAQ51ca.json', 'var_call_Fl3OJ3xCnJbTqSpNsuIdopir': 'file_storage/call_Fl3OJ3xCnJbTqSpNsuIdopir.json'}

exec(code, env_args)
