code = """import json
key_name = 'var_function-call-16488807000991432586'
path = locals()[key_name]
with open(path, 'r') as f:
    valid_stocks = json.load(f)

queries = []
i = 0
while i < len(valid_stocks):
    batch = valid_stocks[i:i+10]
    q_parts = []
    for s in batch:
        sym = s['Symbol']
        # Remove date literals to test syntax
        q = 'SELECT \'{0}\' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "{0}"'.format(sym)
        q_parts.append(q)
    full = " UNION ALL ".join(q_parts)
    queries.append(full)
    i += 10

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17490755573003883636': 'file_storage/function-call-17490755573003883636.json', 'var_function-call-8209134030405193310': 'file_storage/function-call-8209134030405193310.json', 'var_function-call-16488807000991432586': 'file_storage/function-call-16488807000991432586.json', 'var_function-call-8713500348890617850': 'file_storage/function-call-8713500348890617850.json', 'var_function-call-17926699237147091837': 'file_storage/function-call-17926699237147091837.json', 'var_function-call-7020907782818588183': 'file_storage/function-call-7020907782818588183.json', 'var_function-call-7283447733642380468': 'file_storage/function-call-7283447733642380468.json'}

exec(code, env_args)
