code = """import json, pandas as pd
with open(var_call_7P2pKW2MvdjwPJAT38jWRKoj, 'r', encoding='utf-8') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)

with open(var_call_bmf0BnCD1Y3a4ithfN0awrMh, 'r', encoding='utf-8') as f:
    all_tables = json.load(f)

cap_tickers = set(cap_df['Symbol'].astype(str))
trade_tickers = set(all_tables)
use_tickers = sorted(list(cap_tickers & trade_tickers))

chunks = [use_tickers[i:i+60] for i in range(0, len(use_tickers), 60)]
queries = []
for ch in chunks:
    parts = []
    for t in ch:
        parts.append("SELECT '" + t + "' AS Symbol, COUNT(*)::BIGINT AS cnt FROM \"" + t + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) > 0.2*Low")
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'tickers_n': len(use_tickers), 'chunks': len(chunks), 'first_query_len': len(queries[0]) if queries else 0}))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json', 'var_call_kFjbYZ0s15AJ39Vk9DSBz8tr': [{'Symbol': 'AGMH', 'cnt': '13'}], 'var_call_OGK4qMhQNVQY6NfHK9uE4rjV': {'a': 1}}

exec(code, env_args)
