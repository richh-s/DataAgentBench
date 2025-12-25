code = """import json

path = locals()['var_function-call-16488807000991432586']
with open(path, 'r') as f:
    valid_stocks = json.load(f)

queries = []
batch_size = 10
for i in range(0, len(valid_stocks), batch_size):
    batch = valid_stocks[i:i+batch_size]
    subqueries = []
    for s in batch:
        sym = s['Symbol']
        part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        subqueries.append(part)
    
    full_batch_query = " UNION ALL ".join(subqueries)
    queries.append(full_batch_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17490755573003883636': 'file_storage/function-call-17490755573003883636.json', 'var_function-call-8209134030405193310': 'file_storage/function-call-8209134030405193310.json', 'var_function-call-16488807000991432586': 'file_storage/function-call-16488807000991432586.json', 'var_function-call-8713500348890617850': 'file_storage/function-call-8713500348890617850.json', 'var_function-call-17926699237147091837': 'file_storage/function-call-17926699237147091837.json'}

exec(code, env_args)
