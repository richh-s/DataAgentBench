code = """import json

# Load files
with open('var_function-call-2542358163233930626.json', 'r') as f:
    cand_list = json.load(f)
    candidates = set(c['Symbol'] for c in cand_list)

with open('var_function-call-17634865684080335630.json', 'r') as f:
    tables = set(json.load(f))

# Intersect
symbols = sorted(list(candidates.intersection(tables)))

# Construct query
parts = []
for sym in symbols:
    # SQL: SELECT 'SYM' AS Symbol FROM "SYM" WHERE "Adj Close" > 200 AND "Date" BETWEEN '2015-01-01' AND '2015-12-31' LIMIT 1
    # We use explicit concatenation to avoid f-string quote issues
    q = "SELECT '" + sym + "' AS Symbol FROM \"" + sym + "\" WHERE \"Adj Close\" > 200 AND \"Date\" BETWEEN '2015-01-01' AND '2015-12-31' LIMIT 1"
    parts.append(q)

final_query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-2542358163233930626': 'file_storage/function-call-2542358163233930626.json', 'var_function-call-17634865684080335630': 'file_storage/function-call-17634865684080335630.json'}

exec(code, env_args)
