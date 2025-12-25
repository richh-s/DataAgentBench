code = """import json

path = locals()['var_function-call-13328234053547568424']
with open(path, 'r') as f:
    valid_symbols = json.load(f)

queries = []
sq = chr(39) # single quote
dq = chr(34) # double quote

for sym in valid_symbols:
    sym_lit = sym.replace("'", "''")
    sym_ident = sym.replace('"', '""')
    # SELECT 'SYM' as Symbol FROM "SYM" WHERE Date LIKE '2015%' AND "Adj Close" > 200 LIMIT 1
    q = "SELECT " + sq + sym_lit + sq + " as Symbol FROM " + dq + sym_ident + dq + " WHERE Date LIKE " + sq + "2015%" + sq + " AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-5292189082820966608': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-4017956319566786658': 'file_storage/function-call-4017956319566786658.json', 'var_function-call-17745112889233166129': 'file_storage/function-call-17745112889233166129.json', 'var_function-call-13328234053547568424': 'file_storage/function-call-13328234053547568424.json', 'var_function-call-10661001452431956929': 'test'}

exec(code, env_args)
