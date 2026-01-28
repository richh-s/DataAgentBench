code = """import json, pandas as pd

# load symbols/company list
p = var_call_WEHmWuq38xwH8o3YmUPIUsUm
if isinstance(p, str):
    with open(p, 'r') as f:
        recs = json.load(f)
else:
    recs = p
info = pd.DataFrame(recs)

# load available trade tables
p2 = var_call_YDYetXoUvp7hZkrB8iyZiWtm
if isinstance(p2, str):
    with open(p2, 'r') as f:
        tables = json.load(f)
else:
    tables = p2
trade_set = set(tables)

symbols = [s for s in info['Symbol'].tolist() if s in trade_set]

out = json.dumps({"n_symbols": len(symbols), "symbols": symbols[:50]})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WEHmWuq38xwH8o3YmUPIUsUm': 'file_storage/call_WEHmWuq38xwH8o3YmUPIUsUm.json', 'var_call_YDYetXoUvp7hZkrB8iyZiWtm': 'file_storage/call_YDYetXoUvp7hZkrB8iyZiWtm.json'}

exec(code, env_args)
