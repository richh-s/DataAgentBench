code = """import json

with open(locals()['var_function-call-9049256654640604985'], 'r') as f:
    companies = json.load(f)
target_symbols = set([c['Symbol'] for c in companies])

with open(locals()['var_function-call-4946422261018176680'], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

valid_symbols = list(target_symbols.intersection(existing_tables))

sqls = []
for sym in valid_symbols:
    # Use simple string concatenation to avoid f-string quote issues
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low"
    sqls.append(q)

if not sqls:
    final_query = "SELECT 'NONE' as Symbol, 0 as Days"
else:
    final_query = " UNION ALL ".join(sqls)
    final_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-9049256654640604985': 'file_storage/function-call-9049256654640604985.json', 'var_function-call-12808969901347562370': 86, 'var_function-call-4946422261018176680': 'file_storage/function-call-4946422261018176680.json'}

exec(code, env_args)
