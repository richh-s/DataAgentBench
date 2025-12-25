code = """import json

path1 = locals()['var_function-call-6393703521614786747']
with open(path1, 'r') as f:
    candidates = json.load(f)

candidate_symbols = set(c['Symbol'] for c in candidates)

path2 = locals()['var_function-call-14160190749123252694']
with open(path2, 'r') as f:
    tables = json.load(f)

available_tables = set(tables)

valid_symbols = list(candidate_symbols.intersection(available_tables))

queries = []
for sym in valid_symbols:
    # Use single quotes for python string
    # SQL: SELECT 'SYM' AS Symbol ... FROM "SYM" ...
    q = 'SELECT \'{0}\' AS Symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) AS UpDays, SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) AS DownDays FROM "{0}" WHERE "Date" >= \'2017-01-01\' AND "Date" <= \'2017-12-31\''.format(sym)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-6393703521614786747': 'file_storage/function-call-6393703521614786747.json', 'var_function-call-17168036801476034566': 234, 'var_function-call-14160190749123252694': 'file_storage/function-call-14160190749123252694.json'}

exec(code, env_args)
