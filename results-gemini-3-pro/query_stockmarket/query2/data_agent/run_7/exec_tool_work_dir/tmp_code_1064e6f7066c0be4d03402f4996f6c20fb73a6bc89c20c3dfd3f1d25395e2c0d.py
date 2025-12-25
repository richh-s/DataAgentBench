code = """import json

key = 'var_function-call-12240742963505795241'
fname = locals()[key]
with open(fname, 'r') as f:
    valid_symbols = json.load(f)

queries = []
chunk_size = 500
sq = chr(39) # single quote
dq = chr(34) # double quote

# Manual loop
current = 0
while current < len(valid_symbols):
    chunk = valid_symbols[current : current + chunk_size]
    current += chunk_size
    sub_queries = []
    for sym in chunk:
        # q = SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1
        q = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date >= " + sq + "2015-01-01" + sq + " AND Date <= " + sq + "2015-12-31" + sq + " LIMIT 1"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-11304267723591981203': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9114954391718964864': 'file_storage/function-call-9114954391718964864.json', 'var_function-call-10741500597713023606': 'file_storage/function-call-10741500597713023606.json', 'var_function-call-12240742963505795241': 'file_storage/function-call-12240742963505795241.json', 'var_function-call-10700936405339732652': 1435, 'var_function-call-8853969729957837933': 1435}

exec(code, env_args)
