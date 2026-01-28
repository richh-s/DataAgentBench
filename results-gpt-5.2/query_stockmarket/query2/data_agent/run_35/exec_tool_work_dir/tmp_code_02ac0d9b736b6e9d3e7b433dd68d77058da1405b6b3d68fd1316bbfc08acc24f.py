code = """import json
path_info = var_call_pyUpx70CiTUTPX4FbKRXqLqU
with open(path_info,'r') as f:
    info = json.load(f)
symbols = [r['symbol'] for r in info]

# build IN list
in_list = ",".join(["'"+s.replace("'","''")+"'" for s in symbols])
query = (
"SELECT t.table_name AS symbol,\n"
"       (SELECT MAX(\"Adj Close\") FROM \"" + "'||t.table_name||'" + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31') AS max_adj_close_2015\n"
"FROM information_schema.tables t\n"
"WHERE t.table_schema='main' AND t.table_name IN ("+in_list+")\n"
"ORDER BY symbol;"
)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_pyUpx70CiTUTPX4FbKRXqLqU': 'file_storage/call_pyUpx70CiTUTPX4FbKRXqLqU.json', 'var_call_6pETY1mJuNOhB4PdOukuBDhp': 'file_storage/call_6pETY1mJuNOhB4PdOukuBDhp.json', 'var_call_W602b8oE1IUyvpYg1x8SyP1w': 'file_storage/call_W602b8oE1IUyvpYg1x8SyP1w.json', 'var_call_DHqufiDMf0ruq0xzpDs4vxNc': 'file_storage/call_DHqufiDMf0ruq0xzpDs4vxNc.json'}

exec(code, env_args)
