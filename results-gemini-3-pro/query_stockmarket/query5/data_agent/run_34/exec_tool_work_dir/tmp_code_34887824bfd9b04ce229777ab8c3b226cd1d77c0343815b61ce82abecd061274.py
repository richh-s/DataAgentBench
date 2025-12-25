code = """import json

k1 = 'var_function-call-17161419678548834227'
k2 = 'var_function-call-7632084380373401256'

res1 = locals()[k1]
data = json.loads(res1)
target_symbols = data['symbols']

with open(locals()[k2], 'r') as f:
    tables = json.load(f)

existing_tables = set(tables)
valid_symbols = []
for s in target_symbols:
    if s in existing_tables:
        valid_symbols.append(s)

queries = []
for s in valid_symbols:
    q = "SELECT '" + s + "' as Symbol, COUNT(*) as Days FROM " + '"' + s + '"' + " WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    queries.append(q)

final = " UNION ALL ".join(queries)
final = final + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_function-call-8819135185628577805': 'file_storage/function-call-8819135185628577805.json', 'var_function-call-17161419678548834227': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-7632084380373401256': 'file_storage/function-call-7632084380373401256.json', 'var_function-call-6572907001312719127': 'test'}

exec(code, env_args)
