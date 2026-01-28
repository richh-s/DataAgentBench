code = """import json
path = var_call_W602b8oE1IUyvpYg1x8SyP1w
with open(path,'r') as f:
    obj = json.load(f)
candidates = obj['candidates']

parts = []
for t in candidates:
    parts.append("SELECT '"+t+"' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \""+t+"\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
query = " UNION ALL ".join(parts)
final_query = "WITH m AS ("+query+") SELECT symbol, max_adj_close_2015 FROM m WHERE max_adj_close_2015 > 200 ORDER BY symbol;"

print('__RESULT__:')
print(json.dumps({'query': final_query}))"""

env_args = {'var_call_pyUpx70CiTUTPX4FbKRXqLqU': 'file_storage/call_pyUpx70CiTUTPX4FbKRXqLqU.json', 'var_call_6pETY1mJuNOhB4PdOukuBDhp': 'file_storage/call_6pETY1mJuNOhB4PdOukuBDhp.json', 'var_call_W602b8oE1IUyvpYg1x8SyP1w': 'file_storage/call_W602b8oE1IUyvpYg1x8SyP1w.json'}

exec(code, env_args)
