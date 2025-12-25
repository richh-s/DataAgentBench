code = """import json

# Load symbols from step 1
with open(locals()['var_function-call-9049256654640604985'], 'r') as f:
    companies = json.load(f)
target_symbols = set([c['Symbol'] for c in companies])

# Load tables from step 2
with open(locals()['var_function-call-4946422261018176680'], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

# Intersect
valid_symbols = target_symbols.intersection(existing_tables)

# Construct Query
# "SELECT 'SYM' as Symbol, COUNT(*) as Days FROM SYM WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.2 * Low UNION ALL ..."
sqls = []
for sym in valid_symbols:
    sqls.append(f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low")

final_query = " UNION ALL ".join(sqls)
final_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-9049256654640604985': 'file_storage/function-call-9049256654640604985.json', 'var_function-call-12808969901347562370': 86, 'var_function-call-4946422261018176680': 'file_storage/function-call-4946422261018176680.json'}

exec(code, env_args)
