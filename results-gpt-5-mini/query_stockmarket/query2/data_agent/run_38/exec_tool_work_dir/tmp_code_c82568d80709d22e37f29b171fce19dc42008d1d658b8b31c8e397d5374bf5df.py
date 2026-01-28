code = """import json
path_info = var_call_iy1Wl4j8WobUxW4UkYuf7dP0
path_tables = var_call_sq3YAjllLjEkNwyEI3gkbR7h
with open(path_info, 'r') as f:
    info = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)
symbols = [r['Symbol'] for r in info if r.get('Symbol')]
# keep only those symbols that have a table in stocktrade_database
tables_set = set(tables)
symbols = [s for s in symbols if s in tables_set]
parts = []
for s in symbols:
    parts.append("SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(s=s))
if parts:
    sql = "SELECT Symbol, max_adj FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) t WHERE max_adj > 200 ORDER BY Symbol;"
else:
    sql = "SELECT NULL as Symbol, NULL as max_adj WHERE 1=0;"
out = {"query": sql, "num_symbols_considered": len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_iy1Wl4j8WobUxW4UkYuf7dP0': 'file_storage/call_iy1Wl4j8WobUxW4UkYuf7dP0.json', 'var_call_sq3YAjllLjEkNwyEI3gkbR7h': 'file_storage/call_sq3YAjllLjEkNwyEI3gkbR7h.json'}

exec(code, env_args)
