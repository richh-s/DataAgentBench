code = """import json

path1 = locals()['var_function-call-1914327577488087948']
path2 = locals()['var_function-call-546925876155124567']

with open(path1, 'r') as f:
    target_data = json.load(f)

with open(path2, 'r') as f:
    all_tables = json.load(f)

target_symbols = []
for item in target_data:
    target_symbols.append(item['Symbol'])

available_tables = set(all_tables)
valid_symbols = []
for sym in target_symbols:
    if sym in available_tables:
        valid_symbols.append(sym)

queries = []
for sym in valid_symbols:
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as HighRangeDays FROM \"" + sym + "\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

full_query = ""
if len(queries) > 0:
    full_query = " UNION ALL ".join(queries) + " ORDER BY HighRangeDays DESC LIMIT 5"

res = {}
res['count'] = len(valid_symbols)
res['query'] = full_query
res['valid_symbols'] = valid_symbols

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-1914327577488087948': 'file_storage/function-call-1914327577488087948.json', 'var_function-call-546925876155124567': 'file_storage/function-call-546925876155124567.json'}

exec(code, env_args)
