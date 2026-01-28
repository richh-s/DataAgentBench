code = """import json, pandas as pd

path = var_call_xUmnKzx0Unz6nHN1uFwG0Ltg
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
tickers = df['Symbol'].dropna().unique().tolist()

# DuckDB identifier quoting with double quotes; escape any embedded quotes (unlikely)
quoted = [f'"{t.replace("\"","\"\"")}"' for t in tickers]
res = {
    'tickers': tickers,
    'quoted_list_sql': ','.join(quoted),
    'n': len(tickers)
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_xUmnKzx0Unz6nHN1uFwG0Ltg': 'file_storage/call_xUmnKzx0Unz6nHN1uFwG0Ltg.json'}

exec(code, env_args)
