code = """import json
path = var_call_W602b8oE1IUyvpYg1x8SyP1w
with open(path,'r') as f:
    obj = json.load(f)
candidates = obj['candidates']

# Build a DuckDB query that checks 2015 max Adj Close per ticker, and filters > 200
# Use UNION ALL of per-table aggregations
parts = []
for t in candidates:
    # Quote table name with double quotes
    parts.append(f"SELECT '{t}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
query = "\nUNION ALL\n".join(parts)
final_query = f"WITH m AS ({query}) SELECT symbol, max_adj_close_2015 FROM m WHERE max_adj_close_2015 > 200 ORDER BY symbol;"

print('__RESULT__:')
print(json.dumps({'query': final_query}))"""

env_args = {'var_call_pyUpx70CiTUTPX4FbKRXqLqU': 'file_storage/call_pyUpx70CiTUTPX4FbKRXqLqU.json', 'var_call_6pETY1mJuNOhB4PdOukuBDhp': 'file_storage/call_6pETY1mJuNOhB4PdOukuBDhp.json', 'var_call_W602b8oE1IUyvpYg1x8SyP1w': 'file_storage/call_W602b8oE1IUyvpYg1x8SyP1w.json'}

exec(code, env_args)
