code = """import json, pandas as pd

with open(var_call_7P2pKW2MvdjwPJAT38jWRKoj, 'r', encoding='utf-8') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_tickers = set(cap_df['Symbol'].astype(str))

with open(var_call_bmf0BnCD1Y3a4ithfN0awrMh, 'r', encoding='utf-8') as f:
    all_tables = json.load(f)
trade_tickers = set(all_tables)

use_tickers = sorted(list(cap_tickers & trade_tickers))

# only valid table identifiers (letters/numbers/underscore)
import re
use_tickers = [t for t in use_tickers if re.fullmatch(r'[A-Za-z0-9_]+', t)]

chunks = [use_tickers[i:i+60] for i in range(0, len(use_tickers), 60)]
queries = []
for ch in chunks:
    parts = []
    for t in ch:
        parts.append('SELECT ' + "'" + t + "'" + ' AS Symbol, COUNT(*)::BIGINT AS cnt FROM ' + '"' + t + '"' + " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) > 0.2*Low")
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'tickers_n': len(use_tickers), 'chunks': len(chunks), 'q1_preview': queries[0][:300]}))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json', 'var_call_kFjbYZ0s15AJ39Vk9DSBz8tr': [{'Symbol': 'AGMH', 'cnt': '13'}], 'var_call_OGK4qMhQNVQY6NfHK9uE4rjV': {'a': 1}, 'var_call_OaUTqaJ748bgeupqPoS5SImr': {'tickers_n': 86, 'chunks': 2, 'first_query_len': 9773}, 'var_call_JHYRHuDoX4u0Y4SWiCXqAyhD': {'use_tickers_n': 86, 'kern_in_trade': False, 'missing_from_trade': ['KERN'], 'sample_last10': ['TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_EiO3AuR7kdL9AHjoE79ZZLWd': 'file_storage/call_EiO3AuR7kdL9AHjoE79ZZLWd.json'}

exec(code, env_args)
