code = """import json, pandas as pd

path_etfs = var_call_XrHlNWKzMrgiQtx7cnfZcCrW
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

df_etf = pd.DataFrame(etfs)
symbols = df_etf['Symbol'].dropna().unique().tolist()

chunks = []
max_chunk = 80
for i in range(0, len(symbols), max_chunk):
    syms = symbols[i:i+max_chunk]
    parts = []
    for s in syms:
        t = '"' + s.replace('"','""') + '"'
        q = "SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM {} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(s, t)
        parts.append(q)
    chunks.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'chunks': chunks, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_XrHlNWKzMrgiQtx7cnfZcCrW': 'file_storage/call_XrHlNWKzMrgiQtx7cnfZcCrW.json', 'var_call_jWPZt9UPzSeXm5a2fEJh4H2f': 'file_storage/call_jWPZt9UPzSeXm5a2fEJh4H2f.json'}

exec(code, env_args)
