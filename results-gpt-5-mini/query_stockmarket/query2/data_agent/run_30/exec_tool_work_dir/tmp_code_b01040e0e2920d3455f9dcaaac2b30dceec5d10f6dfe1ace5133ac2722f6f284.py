code = """import json
with open(var_call_tLRo1zbYbAD3E4yZphgT3t81, 'r') as f:
    symbols = json.load(f)
# Build SQL in batches to avoid extremely long single query; but we'll build one full UNION ALL
parts = []
for s in symbols:
    parts.append(f'SELECT "{s}" AS Symbol, MAX("Adj Close") AS max_adj FROM "{s}" WHERE Date >= \"2015-01-01\" AND Date <= \"2015-12-31\"')
sql = ' UNION ALL '.join(parts) + ';'
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_WOv0WK9BUMSQ1XblNAD7pZeX': 'file_storage/call_WOv0WK9BUMSQ1XblNAD7pZeX.json', 'var_call_dGvngHc8WSA2MSh6aOM8h4Ao': 'file_storage/call_dGvngHc8WSA2MSh6aOM8h4Ao.json', 'var_call_tLRo1zbYbAD3E4yZphgT3t81': 'file_storage/call_tLRo1zbYbAD3E4yZphgT3t81.json', 'var_call_57TPV3exQbPNq7FZpfwU18oy': []}

exec(code, env_args)
