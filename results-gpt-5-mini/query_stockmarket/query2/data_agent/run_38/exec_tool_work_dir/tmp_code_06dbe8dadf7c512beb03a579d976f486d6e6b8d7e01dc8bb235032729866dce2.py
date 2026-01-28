code = """import json
path_info = var_call_iy1Wl4j8WobUxW4UkYuf7dP0
path_tables = var_call_sq3YAjllLjEkNwyEI3gkbR7h
with open(path_info, 'r') as f:
    info = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)

tables_set = set(tables)
symbols = [r['Symbol'] for r in info if r.get('Symbol') and r['Symbol'] in tables_set]
parts = []
for s in symbols:
    s_literal = "'" + s.replace("'", "''") + "'"
    tbl = chr(34) + s.replace('"', '""') + chr(34)
    adj = chr(34) + 'Adj Close' + chr(34)
    part = 'SELECT ' + s_literal + ' AS Symbol, MAX(' + adj + ') AS max_adj FROM ' + tbl + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)

if parts:
    sql = 'SELECT Symbol, max_adj FROM (\n' + '\nUNION ALL\n'.join(parts) + '\n) t WHERE max_adj > 200 ORDER BY Symbol;'
else:
    sql = 'SELECT NULL as Symbol, NULL as max_adj WHERE 1=0;'

out = {'query': sql, 'num_symbols_considered': len(symbols)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iy1Wl4j8WobUxW4UkYuf7dP0': 'file_storage/call_iy1Wl4j8WobUxW4UkYuf7dP0.json', 'var_call_sq3YAjllLjEkNwyEI3gkbR7h': 'file_storage/call_sq3YAjllLjEkNwyEI3gkbR7h.json'}

exec(code, env_args)
