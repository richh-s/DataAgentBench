code = """import json

with open(locals()['var_function-call-2250333741242077047'], 'r') as f:
    tickers = json.load(f)

batch_size = 200
queries = []
for i in range(0, len(tickers), batch_size):
    batch = tickers[i:i+batch_size]
    sub_queries = []
    for t in batch:
        q = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(t)
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-8523386402673308911': ['stockinfo'], 'var_function-call-10504201525486646859': 'file_storage/function-call-10504201525486646859.json', 'var_function-call-11124697286812708806': 'file_storage/function-call-11124697286812708806.json', 'var_function-call-2250333741242077047': 'file_storage/function-call-2250333741242077047.json', 'var_function-call-1568197735561327246': 1435}

exec(code, env_args)
