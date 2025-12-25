code = """import json

symbols = json.load(open(var_call_3N9de2VM7GDn752Ud8hMghzN))

queries = []
for s in symbols:
    q = "SELECT '" + s + "' as Symbol FROM '" + s + "' WHERE substr(Date,1,4)='2015' AND \"Adj Close\" > 200 LIMIT 1"
    queries.append(q)

union_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_call_bJICUAbpJUwglQ5xaYtXCzka': 'file_storage/call_bJICUAbpJUwglQ5xaYtXCzka.json', 'var_call_zRgyKPBN7HPsNtEzD5tmKyk7': 'file_storage/call_zRgyKPBN7HPsNtEzD5tmKyk7.json', 'var_call_dKtuWwbdc9VgYczEvrI5TyyY': 'file_storage/call_dKtuWwbdc9VgYczEvrI5TyyY.json', 'var_call_3N9de2VM7GDn752Ud8hMghzN': 'file_storage/call_3N9de2VM7GDn752Ud8hMghzN.json'}

exec(code, env_args)
