code = """import json, pandas as pd

# Load NYSE Arca ETFs list
path = var_call_nOWlEQHUrbqOHXmVXSYbHeRt
with open(path, 'r') as f:
    etfs = json.load(f)

tickers = [r['Symbol'] for r in etfs]

# Build union query for max Adj Close in 2015 per ticker
# DuckDB identifiers may need quoting; use double quotes around table and column with space.
queries = []
for t in tickers:
    # skip tickers with characters that will break identifier quoting
    if '"' in t:
        continue
    queries.append(f"SELECT '{t}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'")

union_sql = " UNION ALL ".join(queries)
result = {
    "sql": union_sql,
    "n": len(queries)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qJiDwOwNX2pGcodn9dgo9XsI': ['stockinfo'], 'var_call_nOWlEQHUrbqOHXmVXSYbHeRt': 'file_storage/call_nOWlEQHUrbqOHXmVXSYbHeRt.json', 'var_call_7z5eVmmDQejMlywaWhpIlzRp': 'file_storage/call_7z5eVmmDQejMlywaWhpIlzRp.json'}

exec(code, env_args)
