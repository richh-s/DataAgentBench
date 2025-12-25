code = """import json

with open(locals()['var_function-call-9049256654640604985'], 'r') as f:
    companies = json.load(f)
target_symbols = set([c['Symbol'] for c in companies])

with open(locals()['var_function-call-4946422261018176680'], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

valid_symbols = list(target_symbols.intersection(existing_tables))
valid_symbols.sort()

mid = len(valid_symbols) // 2
batch1 = valid_symbols[:mid]
batch2 = valid_symbols[mid:]

def build_query(symbols):
    sqls = []
    for sym in symbols:
        q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low"
        sqls.append(q)
    return " UNION ALL ".join(sqls)

q1 = build_query(batch1)
q2 = build_query(batch2)

print("__RESULT__:")
print(json.dumps([q1, q2]))"""

env_args = {'var_function-call-9049256654640604985': 'file_storage/function-call-9049256654640604985.json', 'var_function-call-12808969901347562370': 86, 'var_function-call-4946422261018176680': 'file_storage/function-call-4946422261018176680.json', 'var_function-call-1046178286130878323': 'file_storage/function-call-1046178286130878323.json'}

exec(code, env_args)
