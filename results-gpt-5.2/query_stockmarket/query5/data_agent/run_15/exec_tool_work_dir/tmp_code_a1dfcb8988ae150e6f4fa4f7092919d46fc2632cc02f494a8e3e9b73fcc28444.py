code = """import json, pandas as pd

# Load capital market tickers
with open(var_call_7P2pKW2MvdjwPJAT38jWRKoj, 'r', encoding='utf-8') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_tickers = set(cap_df['Symbol'].astype(str))

# Load available trade tables
with open(var_call_bmf0BnCD1Y3a4ithfN0awrMh, 'r', encoding='utf-8') as f:
    all_tables = json.load(f)
trade_tickers = set(all_tables)

use_tickers = sorted(list(cap_tickers & trade_tickers))

# Create union-all SQL in manageable size
chunks = [use_tickers[i:i+60] for i in range(0, len(use_tickers), 60)]
queries = []
for ch in chunks:
    parts = [f"SELECT '{t}' AS Symbol, COUNT(*)::BIGINT AS cnt FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) > 0.2*Low" for t in ch]
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'tickers_n': len(use_tickers), 'chunks': len(chunks), 'first_chunk_len': len(chunks[0]) if chunks else 0, 'first_query_preview': queries[0][:500] if queries else ''}))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json', 'var_call_kFjbYZ0s15AJ39Vk9DSBz8tr': [{'Symbol': 'AGMH', 'cnt': '13'}]}

exec(code, env_args)
