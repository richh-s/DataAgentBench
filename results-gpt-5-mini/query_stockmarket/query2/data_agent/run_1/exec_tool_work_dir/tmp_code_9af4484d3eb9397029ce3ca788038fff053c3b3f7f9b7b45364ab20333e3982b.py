code = """import json
with open(var_call_h7weTyR1OHJUYmUz3zTOdl67, 'r') as f:
    symbols = json.load(f)
parts = []
for s in symbols:
    parts.append("SELECT '{}' AS Symbol FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s, s))
if parts:
    sql = "SELECT DISTINCT Symbol FROM (" + " UNION ALL ".join(parts) + ") AS t ORDER BY Symbol;"
else:
    sql = "SELECT '' AS Symbol WHERE false;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_tRlSKUeszajxFebpOVmuqsde': ['stockinfo'], 'var_call_DG0vN5pLFilWu9tTK6nlcgSy': 'file_storage/call_DG0vN5pLFilWu9tTK6nlcgSy.json', 'var_call_UpFSKAxq4enQyFMneNysTLNi': 'file_storage/call_UpFSKAxq4enQyFMneNysTLNi.json', 'var_call_kkqKOJniybxDUtWEO6yDgShT': 'file_storage/call_kkqKOJniybxDUtWEO6yDgShT.json', 'var_call_h7weTyR1OHJUYmUz3zTOdl67': 'file_storage/call_h7weTyR1OHJUYmUz3zTOdl67.json'}

exec(code, env_args)
