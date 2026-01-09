code = """import json, pandas as pd

cap_path = var_call_7SNvE0OkxU00aUqhUS9kukBQ
with open(cap_path, 'r') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_tickers = set(cap_df['Symbol'].astype(str))

trade_path = var_call_2AnqwOtdJ9I5uRxdMdLLmqG7
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

tickers = sorted(cap_tickers.intersection(trade_tables))

def q_ident(name: str) -> str:
    return '"' + name.replace('"','""') + '"'

parts = []
for t in tickers:
    parts.append(
        "SELECT '" + t + "' AS Symbol, COUNT(*) AS cnt FROM " + q_ident(t) +
        " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2"
    )

union_query = " UNION ALL ".join(parts)

print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'union_query': union_query}))"""

env_args = {'var_call_7SNvE0OkxU00aUqhUS9kukBQ': 'file_storage/call_7SNvE0OkxU00aUqhUS9kukBQ.json', 'var_call_2AnqwOtdJ9I5uRxdMdLLmqG7': 'file_storage/call_2AnqwOtdJ9I5uRxdMdLLmqG7.json', 'var_call_wYm17yQ11FpKXHjYZX7ZcS4u': 'file_storage/call_wYm17yQ11FpKXHjYZX7ZcS4u.json'}

exec(code, env_args)
