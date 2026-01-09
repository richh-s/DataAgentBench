code = """import json, pandas as pd

# load tickers/company names (Capital Market)
path = var_call_7P2pKW2MvdjwPJAT38jWRKoj
with open(path, 'r', encoding='utf-8') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_tickers = set(cap_df['Symbol'].astype(str))

# load available trade tables
path2 = var_call_bmf0BnCD1Y3a4ithfN0awrMh
with open(path2, 'r', encoding='utf-8') as f:
    all_tables = json.load(f)
trade_tickers = set(all_tables)

use_tickers = sorted(list(cap_tickers & trade_tickers))

# chunk tickers for SQL length
chunks = [use_tickers[i:i+80] for i in range(0, len(use_tickers), 80)]

queries = []
for ch in chunks:
    parts = []
    for t in ch:
        # skip if invalid identifier (should be alnum/underscore); DuckDB table names here look safe
        parts.append(f"SELECT '{t}' AS Symbol, COUNT(*) AS cnt FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) > 0.2*Low")
    q = " UNION ALL ".join(parts)
    queries.append(q)

out = []
for q in queries:
    out.append(q)

print('__RESULT__:')
print(json.dumps({'tickers_n': len(use_tickers), 'union_queries_n': len(queries), 'queries': queries[:2]}))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json'}

exec(code, env_args)
