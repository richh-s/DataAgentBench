code = """import json

path = locals()['var_function-call-6054795489737292266']
with open(path, 'r') as f:
    valid_symbols = json.load(f)

batch = valid_symbols[0:500]
queries = []
dq = chr(34)
sq = chr(39)

for sym in batch:
    # SELECT 'sym' as Symbol FROM "sym" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND "Adj Close" > 200 LIMIT 1
    q = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE Date >= " + sq + "2015-01-01" + sq + " AND Date <= " + sq + "2015-12-31" + sq + " AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-352515498678611110': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-9156895254517831471': 'file_storage/function-call-9156895254517831471.json', 'var_function-call-7507699247137649927': 'file_storage/function-call-7507699247137649927.json', 'var_function-call-6054795489737292266': 'file_storage/function-call-6054795489737292266.json', 'var_function-call-7140710157930819947': 1435, 'var_function-call-7078156043657250268': 'Success', 'var_function-call-7521773820331769561': '2015-01-01'}

exec(code, env_args)
