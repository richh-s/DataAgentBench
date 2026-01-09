code = """import json
path_info = var_call_pyUpx70CiTUTPX4FbKRXqLqU
with open(path_info,'r') as f:
    info = json.load(f)
symbols = [r['symbol'] for r in info]

# Limit to symbols that are valid table names without special chars for simplicity
symbols = [s for s in symbols if s.isalnum()]

in_list = ",".join(["'"+s+"'" for s in symbols])

# We'll create a UNION ALL query in Python but in chunks to avoid syntax issues
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

final_query = "WITH m AS (\n" + "\nUNION ALL\n".join(parts) + "\n)\nSELECT symbol, max_adj_close_2015 FROM m WHERE max_adj_close_2015 > 200 ORDER BY symbol;"

print('__RESULT__:')
print(json.dumps({'query': final_query, 'n_parts': len(parts)}))"""

env_args = {'var_call_pyUpx70CiTUTPX4FbKRXqLqU': 'file_storage/call_pyUpx70CiTUTPX4FbKRXqLqU.json', 'var_call_6pETY1mJuNOhB4PdOukuBDhp': 'file_storage/call_6pETY1mJuNOhB4PdOukuBDhp.json', 'var_call_W602b8oE1IUyvpYg1x8SyP1w': 'file_storage/call_W602b8oE1IUyvpYg1x8SyP1w.json', 'var_call_DHqufiDMf0ruq0xzpDs4vxNc': 'file_storage/call_DHqufiDMf0ruq0xzpDs4vxNc.json'}

exec(code, env_args)
