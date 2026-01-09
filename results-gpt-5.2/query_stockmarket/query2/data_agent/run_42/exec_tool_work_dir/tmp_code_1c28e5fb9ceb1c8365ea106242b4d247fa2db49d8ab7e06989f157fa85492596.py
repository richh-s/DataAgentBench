code = """import json, pandas as pd

# load symbols from file
path = var_call_Gx0fPAIHRtr9SkCxfjDwil6o
with open(path, 'r') as f:
    symbols = [r['symbol'] for r in json.load(f)]

# load available trade tables list from file
path2 = var_call_x46B2WTQq6zbsoWLQaJw9Uiv
with open(path2, 'r') as f:
    tables = set(json.load(f))

symbols_in_trade = [s for s in symbols if s in tables]

# build union-all max(adj close) query for 2015
parts = []
for s in symbols_in_trade:
    # quote table name for duckdb (double quotes)
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

result = {"etfs": [], "total": 0}
if parts:
    union_query = "\nUNION ALL\n".join(parts)
    final_query = f"SELECT symbol, max_adj_close FROM ({union_query}) t WHERE max_adj_close > 200 ORDER BY symbol;"
    out = {"final_query": final_query, "n_symbols": len(symbols_in_trade)}
else:
    out = {"final_query": None, "n_symbols": 0}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Gx0fPAIHRtr9SkCxfjDwil6o': 'file_storage/call_Gx0fPAIHRtr9SkCxfjDwil6o.json', 'var_call_x46B2WTQq6zbsoWLQaJw9Uiv': 'file_storage/call_x46B2WTQq6zbsoWLQaJw9Uiv.json'}

exec(code, env_args)
