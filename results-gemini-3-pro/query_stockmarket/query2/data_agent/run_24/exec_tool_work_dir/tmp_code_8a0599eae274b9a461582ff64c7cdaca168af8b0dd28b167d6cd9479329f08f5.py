code = """import json

# Load files
with open(locals()['var_function-call-17981552509113141854'], 'r') as f:
    etf_list = json.load(f)
with open(locals()['var_function-call-3218142005520764474'], 'r') as f:
    table_set = set(json.load(f))

# Filter
relevant_etfs = [x['Symbol'] for x in etf_list if x['Symbol'] in table_set]
relevant_etfs.sort()

# Batch 1
batch = relevant_etfs[0:500]

queries = []
for sym in batch:
    # SQL: SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date LIKE '2015-%' LIMIT 1
    # We construct it using format to avoid quote confusion
    q = "SELECT '{}' as Symbol FROM \"{}\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015-%' LIMIT 1".format(sym, sym)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5455133501503104484': ['stockinfo'], 'var_function-call-17981552509113141854': 'file_storage/function-call-17981552509113141854.json', 'var_function-call-3218142005520764474': 'file_storage/function-call-3218142005520764474.json', 'var_function-call-13141348390779095294': {'count': 1435}}

exec(code, env_args)
