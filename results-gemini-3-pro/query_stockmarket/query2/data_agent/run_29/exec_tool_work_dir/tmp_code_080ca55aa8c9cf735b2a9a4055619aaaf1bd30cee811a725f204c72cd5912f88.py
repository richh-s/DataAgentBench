code = """import json

path = locals()['var_function-call-7704237748048051693']
with open(path, 'r') as f:
    relevant_symbols = json.load(f)

queries = []
batch_size = 300
dq = chr(34) # double quote
sq = chr(39) # single quote

for i in range(0, len(relevant_symbols), batch_size):
    batch = relevant_symbols[i:i+batch_size]
    sub_queries = []
    for sym in batch:
        # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Date" LIKE '2015-%' AND "Adj Close" > 200 LIMIT 1
        q = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE " + dq + "Date" + dq + " LIKE " + sq + "2015-%" + sq + " AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
        sub_queries.append(q)
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3424898909852780043': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-2015005240419911970': 'file_storage/function-call-2015005240419911970.json', 'var_function-call-3113271170216609049': 'file_storage/function-call-3113271170216609049.json', 'var_function-call-7704237748048051693': 'file_storage/function-call-7704237748048051693.json', 'var_function-call-735419123404957743': 1435, 'var_function-call-15825120823567229313': 'OK', 'var_function-call-5185520773681868023': 'QUS'}

exec(code, env_args)
