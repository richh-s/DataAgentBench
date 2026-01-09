code = """import json, pandas as pd

with open(var_call_7P2pKW2MvdjwPJAT38jWRKoj, 'r', encoding='utf-8') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_tickers = set(cap_df['Symbol'].astype(str))

with open(var_call_bmf0BnCD1Y3a4ithfN0awrMh, 'r', encoding='utf-8') as f:
    all_tables = json.load(f)
trade_tickers = set(all_tables)

use_tickers = sorted(list(cap_tickers & trade_tickers))

# confirm missing ones that were in earlier union attempt (hardcoded list)
attempt = ['KERN']
missing = [t for t in attempt if t not in trade_tickers]

print('__RESULT__:')
print(json.dumps({'use_tickers_n': len(use_tickers), 'kern_in_trade': 'KERN' in trade_tickers, 'missing_from_trade': missing, 'sample_last10': use_tickers[-10:]}))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json', 'var_call_kFjbYZ0s15AJ39Vk9DSBz8tr': [{'Symbol': 'AGMH', 'cnt': '13'}], 'var_call_OGK4qMhQNVQY6NfHK9uE4rjV': {'a': 1}, 'var_call_OaUTqaJ748bgeupqPoS5SImr': {'tickers_n': 86, 'chunks': 2, 'first_query_len': 9773}}

exec(code, env_args)
