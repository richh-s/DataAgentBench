code = """import json, pandas as pd

# Load NYSE Arca ETFs from storage file
path = var_call_NZ0JfUmxkUXZtZhMlGbm0tDu
with open(path, 'r', encoding='utf-8') as f:
    etfs = json.load(f)

# Load available price tables list (preview already list; may be file)
tables = var_call_aTsh1In8HMrOaUxRKitJk4wo
if isinstance(tables, str):
    with open(tables, 'r', encoding='utf-8') as f:
        tables = json.load(f)

tables_set = set(tables)

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol') in tables_set})

# chunk tickers for query length
chunks = [tickers[i:i+200] for i in range(0, len(tickers), 200)]

queries = []
for chunk in chunks:
    parts = []
    for t in chunk:
        # quote table name for DuckDB; also double-quote column "Adj Close"
        parts.append(f"SELECT '{t}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
    queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'queries': queries, 'n_chunks': len(chunks)}))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json'}

exec(code, env_args)
