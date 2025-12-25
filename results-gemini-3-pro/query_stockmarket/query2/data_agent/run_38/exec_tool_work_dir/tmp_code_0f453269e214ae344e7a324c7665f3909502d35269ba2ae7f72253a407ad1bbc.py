code = """import json

path = locals()['var_function-call-13328234053547568424']
with open(path, 'r') as f:
    valid_symbols = sorted(json.load(f))

batch_size = 120
batch_idx = 0
start = batch_idx * batch_size
end = start + batch_size
batch = valid_symbols[start:end]

queries = []
sq = chr(39)
dq = chr(34)

for sym in batch:
    sym_lit = sym.replace("'", "''")
    sym_ident = sym.replace('"', '""')
    # Minimal query: SELECT 'SYM' s FROM "SYM" WHERE Date LIKE '2015%' AND "Adj Close">200 LIMIT 1
    q = "SELECT " + sq + sym_lit + sq + " s FROM " + dq + sym_ident + dq + " WHERE Date LIKE " + sq + "2015%" + sq + " AND " + dq + "Adj Close" + dq + ">200 LIMIT 1"
    queries.append(q)

final_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-5292189082820966608': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-4017956319566786658': 'file_storage/function-call-4017956319566786658.json', 'var_function-call-17745112889233166129': 'file_storage/function-call-17745112889233166129.json', 'var_function-call-13328234053547568424': 'file_storage/function-call-13328234053547568424.json', 'var_function-call-10661001452431956929': 'test', 'var_function-call-17065412292088597051': 'file_storage/function-call-17065412292088597051.json', 'var_function-call-462821543102659357': 1435, 'var_function-call-6763714644241844842': 'file_storage/function-call-6763714644241844842.json', 'var_function-call-17257405434458548932': 'file_storage/function-call-17257405434458548932.json', 'var_function-call-6492883131542865576': 4963}

exec(code, env_args)
