code = """import json

key = 'var_function-call-18089665588996577560'
filename = locals()[key]
with open(filename, 'r') as f:
    valid_symbols = json.load(f)

batch_size = 80
batch = valid_symbols[:batch_size]

subqueries = []
dq = chr(34)
sq = chr(39)

for sym in batch:
    # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Date" BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1
    s_sym = sq + sym + sq
    id_sym = dq + sym + dq
    date_cond = dq + "Date" + dq + " BETWEEN " + sq + "2015-01-01" + sq + " AND " + sq + "2015-12-31" + sq
    price_cond = dq + "Adj Close" + dq + " > 200"
    q = "SELECT " + s_sym + " as Symbol FROM " + id_sym + " WHERE " + date_cond + " AND " + price_cond + " LIMIT 1"
    subqueries.append(q)

full_query = " UNION ALL ".join(subqueries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-7344486637286600100': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2454856655276099395': 'file_storage/function-call-2454856655276099395.json', 'var_function-call-6642693361376335155': 'file_storage/function-call-6642693361376335155.json', 'var_function-call-18089665588996577560': 'file_storage/function-call-18089665588996577560.json', 'var_function-call-8976669871907571712': 1435, 'var_function-call-15282565031940966073': ['AAAU'], 'var_function-call-11959501744294715290': ["SELECT 'AAAU' as Symbol"], 'var_function-call-17591349959941982663': 'file_storage/function-call-17591349959941982663.json', 'var_function-call-5408369330593613139': 'file_storage/function-call-5408369330593613139.json'}

exec(code, env_args)
