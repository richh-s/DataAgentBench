code = """import json
# read the two files containing symbol lists
with open(var_call_UpFSKAxq4enQyFMneNysTLNi, 'r') as f:
    nyse_etfs = json.load(f)
with open(var_call_kkqKOJniybxDUtWEO6yDgShT, 'r') as f:
    trade_tables = json.load(f)
# compute intersection
tables_set = set(trade_tables)
symbols = [s for s in nyse_etfs if s in tables_set]
# build union SQL parts
parts = []
for s in symbols:
    # safe table name and symbol
    t = s
    part = f"SELECT '{s}' AS Symbol FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    parts.append(part)
if parts:
    sql = "SELECT DISTINCT Symbol FROM (" + " UNION ALL ".join(parts) + ") AS t ORDER BY Symbol;"
else:
    sql = "SELECT '' AS Symbol WHERE false;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_tRlSKUeszajxFebpOVmuqsde': ['stockinfo'], 'var_call_DG0vN5pLFilWu9tTK6nlcgSy': 'file_storage/call_DG0vN5pLFilWu9tTK6nlcgSy.json', 'var_call_UpFSKAxq4enQyFMneNysTLNi': 'file_storage/call_UpFSKAxq4enQyFMneNysTLNi.json', 'var_call_kkqKOJniybxDUtWEO6yDgShT': 'file_storage/call_kkqKOJniybxDUtWEO6yDgShT.json'}

exec(code, env_args)
