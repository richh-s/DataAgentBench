code = """import json

key_etf = 'var_function-call-17981552509113141854'
key_tables = 'var_function-call-3218142005520764474'

with open(locals()[key_etf], 'r') as f:
    etf_list = json.load(f)

with open(locals()[key_tables], 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)
relevant_etfs = [x['Symbol'] for x in etf_list if x['Symbol'] in table_set]
relevant_etfs.sort()

batch = relevant_etfs[:500]
queries = []
for sym in batch:
    q = "SELECT '{}' as Symbol FROM \"{}\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015-%' LIMIT 1".format(sym, sym)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5455133501503104484': ['stockinfo'], 'var_function-call-17981552509113141854': 'file_storage/function-call-17981552509113141854.json', 'var_function-call-3218142005520764474': 'file_storage/function-call-3218142005520764474.json', 'var_function-call-13141348390779095294': {'count': 1435}, 'var_function-call-17805212614560321345': 'Hello'}

exec(code, env_args)
