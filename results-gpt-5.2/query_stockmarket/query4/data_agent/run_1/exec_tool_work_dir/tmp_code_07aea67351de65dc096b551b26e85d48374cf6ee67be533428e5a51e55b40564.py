code = """import json, pandas as pd

# load symbols + company names from stockinfo query
info = var_call_pMsh5yuKRacB6eyqcaS4pm30
if isinstance(info, str):
    with open(info, 'r') as f:
        info = json.load(f)
info_df = pd.DataFrame(info)

# load available trade tables
tabs = var_call_LRg6M8X1BFvDc4y8td0zwKSz
if isinstance(tabs, str):
    with open(tabs, 'r') as f:
        tabs = json.load(f)
trade_set = set(tabs)

# restrict to symbols that have a trade table
cand = info_df[info_df['Symbol'].isin(trade_set)].copy()

# prioritize likely common stocks by excluding symbols with special characters (preferred/warrants etc.)
cand = cand[~cand['Symbol'].str.contains(r'[^A-Z]')].copy()

symbols = cand['Symbol'].tolist()

print('__RESULT__:')
print(json.dumps({'n_candidates': len(symbols), 'symbols': symbols[:500]}))"""

env_args = {'var_call_pMsh5yuKRacB6eyqcaS4pm30': 'file_storage/call_pMsh5yuKRacB6eyqcaS4pm30.json', 'var_call_LRg6M8X1BFvDc4y8td0zwKSz': 'file_storage/call_LRg6M8X1BFvDc4y8td0zwKSz.json'}

exec(code, env_args)
