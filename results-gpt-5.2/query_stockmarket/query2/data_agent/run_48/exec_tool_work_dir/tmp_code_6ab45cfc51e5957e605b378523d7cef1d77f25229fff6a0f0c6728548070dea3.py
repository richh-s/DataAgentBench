code = """import json, pandas as pd

# load ETF list (NYSE ARCA)
path_etfs = var_call_FUvH3fPlMC7f1SsXJdXrJGAD
with open(path_etfs, 'r') as f:
    etfs = json.load(f)
df_etfs = pd.DataFrame(etfs)

# load available price tables
path_tbls = var_call_IHbpJReSGBxSJZJQN1U6OsBu
with open(path_tbls, 'r') as f:
    tbls = json.load(f)
set_tbls = set(tbls)

# intersect
symbols = sorted(set(df_etfs['symbol']).intersection(set_tbls))

# build a query that checks max Adj Close in 2015 for each symbol
# Use parameterized via UNION ALL with read each table; quote identifiers with double quotes
parts = []
for sym in symbols:
    parts.append(f"SELECT '{sym}' AS symbol, max(\"Adj Close\") AS max_adj_close_2015 FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

query = "\nUNION ALL\n".join(parts)

out = {
    'symbols': symbols,
    'union_query': query,
    'n_symbols': len(symbols)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FUvH3fPlMC7f1SsXJdXrJGAD': 'file_storage/call_FUvH3fPlMC7f1SsXJdXrJGAD.json', 'var_call_IHbpJReSGBxSJZJQN1U6OsBu': 'file_storage/call_IHbpJReSGBxSJZJQN1U6OsBu.json'}

exec(code, env_args)
