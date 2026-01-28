code = """import json, pandas as pd

# load NYSE Arca ETFs from sqlite result (may be file path)
info = var_call_uUZ3gTLYPwMqJRcEG8uHFBPs
if isinstance(info, str):
    with open(info, 'r') as f:
        info = json.load(f)
info_df = pd.DataFrame(info)

# load available price tables
tbls = var_call_2n0dNz7RWhjCVuzhtGi8QDlJ
if isinstance(tbls, str):
    with open(tbls, 'r') as f:
        tbls = json.load(f)
price_tbls = set(tbls)

# candidate tickers with price tables
candidates = sorted(set(info_df['symbol']).intersection(price_tbls))

# build per-ticker UNION ALL query to compute max Adj Close in 2015
parts = []
for sym in candidates:
    parts.append(
        f"SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 "
        f"FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    )

query = "\nUNION ALL\n".join(parts) if parts else "SELECT NULL AS symbol, NULL AS max_adj_close_2015 WHERE 1=0"

# store query to pass back
out = json.dumps({'candidate_count': len(candidates), 'union_query': query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_uUZ3gTLYPwMqJRcEG8uHFBPs': 'file_storage/call_uUZ3gTLYPwMqJRcEG8uHFBPs.json', 'var_call_2n0dNz7RWhjCVuzhtGi8QDlJ': 'file_storage/call_2n0dNz7RWhjCVuzhtGi8QDlJ.json'}

exec(code, env_args)
