code = """import json

file_path = locals()['var_function-call-3637682741273971379']
with open(file_path, 'r') as f:
    batches = json.load(f)

valid_tickers = [t for b in batches for t in b]

batch_size = 140
query_batches = []

dq = chr(34)
sq = chr(39)

for i in range(0, len(valid_tickers), batch_size):
    batch = valid_tickers[i:i+batch_size]
    # Compact query
    # SELECT 'TICKER' s FROM "TICKER" WHERE "Adj Close">200 AND "Date" BETWEEN '2015-01-01' AND '2015-12-31' LIMIT 1
    parts = []
    for t in batch:
        q = 'SELECT ' + sq + t + sq + ' s FROM ' + dq + t + dq + ' WHERE ' + dq + 'Adj Close' + dq + '>200 AND ' + dq + 'Date' + dq + ' BETWEEN ' + sq + '2015-01-01' + sq + ' AND ' + sq + '2015-12-31' + sq + ' LIMIT 1'
        parts.append(q)
    full_q = ' UNION ALL '.join(parts)
    query_batches.append(full_q)

print(f"Generated {len(query_batches)} batches.")
print("__RESULT__:")
print(json.dumps(query_batches))"""

env_args = {'var_function-call-6291273035979822157': 'file_storage/function-call-6291273035979822157.json', 'var_function-call-17273355007471526409': 'file_storage/function-call-17273355007471526409.json', 'var_function-call-6700212571527904625': 1435, 'var_function-call-3183618801010455834': 'file_storage/function-call-3183618801010455834.json', 'var_function-call-3637682741273971379': 'file_storage/function-call-3637682741273971379.json', 'var_function-call-987961275821374124': 'OK', 'var_function-call-6667350370978215714': 'file_storage/function-call-6667350370978215714.json'}

exec(code, env_args)
