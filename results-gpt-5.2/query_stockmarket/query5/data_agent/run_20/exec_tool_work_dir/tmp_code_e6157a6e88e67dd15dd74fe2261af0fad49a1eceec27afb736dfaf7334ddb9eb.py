code = """import json, pandas as pd

# load tickers list (NASDAQ Capital Market)
cap_path = var_call_7SNvE0OkxU00aUqhUS9kukBQ
with open(cap_path, 'r') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_tickers = set(cap_df['Symbol'].astype(str))

# load available trade tables
trade_path = var_call_2AnqwOtdJ9I5uRxdMdLLmqG7
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

# intersect
tickers = sorted(cap_tickers.intersection(trade_tables))

# build a single UNION ALL query for 2019 with the condition (High-Low) > 0.2*Low
# guard against Low <= 0 or NULL
parts = []
for t in tickers:
    parts.append(f"SELECT '{t}' AS Symbol, COUNT(*) AS cnt FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2")

query = "\nUNION ALL\n".join(parts)
# print query length for debug? no

out = json.dumps({"tickers": tickers, "union_query": query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_7SNvE0OkxU00aUqhUS9kukBQ': 'file_storage/call_7SNvE0OkxU00aUqhUS9kukBQ.json', 'var_call_2AnqwOtdJ9I5uRxdMdLLmqG7': 'file_storage/call_2AnqwOtdJ9I5uRxdMdLLmqG7.json'}

exec(code, env_args)
