code = """import json
path = var_call_mrXAfVN5YNdsj9zErCOqiA2X
with open(path) as f:
    symbols = json.load(f)
# build DuckDB SQL over all these symbols to find those with Adj Close>200 in 2015
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS Symbol FROM '{s}' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200")
union_sql = " UNION " + " UNION ".join(parts) if parts else "SELECT NULL WHERE 0"
sql = "SELECT DISTINCT Symbol FROM (" + union_sql + ") ORDER BY Symbol;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_MRfF7pLULhPoqqn8IGTw7KE7': 'file_storage/call_MRfF7pLULhPoqqn8IGTw7KE7.json', 'var_call_xhCxceBifGPfBodEZxyokOVL': 'file_storage/call_xhCxceBifGPfBodEZxyokOVL.json', 'var_call_ei9gb6PNEaJhMhSzVOYvQ7Rn': 'file_storage/call_ei9gb6PNEaJhMhSzVOYvQ7Rn.json', 'var_call_mrXAfVN5YNdsj9zErCOqiA2X': 'file_storage/call_mrXAfVN5YNdsj9zErCOqiA2X.json'}

exec(code, env_args)
