code = """import json, pandas as pd

# load ETF list (NYSE Arca)
path_etfs = var_call_XrHlNWKzMrgiQtx7cnfZcCrW
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

df_etf = pd.DataFrame(etfs)

# Build per-symbol max Adj Close in 2015
symbols = df_etf['Symbol'].dropna().unique().tolist()

# query each symbol table for 2015 max adj close > 200
# do it in batches to reduce overhead by generating UNION ALL query chunks
from math import ceil

chunks = []
max_chunk = 80  # keep SQL length manageable

for i in range(0, len(symbols), max_chunk):
    syms = symbols[i:i+max_chunk]
    parts = []
    for s in syms:
        # quote table names for special chars
        t = '"' + s.replace('"','""') + '"'
        parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM {t} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
    chunks.append(' UNION ALL '.join(parts))

# execute queries sequentially via python's ability? can't call query_db here.
# Instead, output the generated SQL chunks so caller can execute with query_db.

print('__RESULT__:')
print(json.dumps({'chunks': chunks, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_XrHlNWKzMrgiQtx7cnfZcCrW': 'file_storage/call_XrHlNWKzMrgiQtx7cnfZcCrW.json', 'var_call_jWPZt9UPzSeXm5a2fEJh4H2f': 'file_storage/call_jWPZt9UPzSeXm5a2fEJh4H2f.json'}

exec(code, env_args)
