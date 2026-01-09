code = """import json, pandas as pd

# load nyse non-etf symbols
p = var_call_fssuB9N5FSr9mC6JQ02Vi5f3
if isinstance(p, str) and p.endswith('.json'):
    with open(p,'r') as f:
        nyse = json.load(f)
else:
    nyse = p
nyse_df = pd.DataFrame(nyse)
nyse_symbols = set(nyse_df['Symbol'].astype(str))

# load available trade tables symbols
tp = var_call_iNc1jtCKZc3PmhFsHF5mVkiw
if isinstance(tp, str) and tp.endswith('.json'):
    with open(tp,'r') as f:
        trade_syms = set(json.load(f))
else:
    trade_syms = set(tp)

symbols = sorted(nyse_symbols.intersection(trade_syms))

# limit to reasonable batch size for parallel queries
# but we need all to find top 5; do iterative in chunks
chunks = [symbols[i:i+80] for i in range(0, len(symbols), 80)]
print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'n_chunks': len(chunks), 'first_chunk': chunks[0][:10]}))"""

env_args = {'var_call_iNc1jtCKZc3PmhFsHF5mVkiw': 'file_storage/call_iNc1jtCKZc3PmhFsHF5mVkiw.json', 'var_call_fssuB9N5FSr9mC6JQ02Vi5f3': 'file_storage/call_fssuB9N5FSr9mC6JQ02Vi5f3.json'}

exec(code, env_args)
