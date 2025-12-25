code = """import json

path1 = locals()['var_function-call-15016460926965200659']
path2 = locals()['var_function-call-570738584850609366']

with open(path1, 'r') as f:
    d1 = json.load(f)
s_set = set(x['Symbol'] for x in d1)

with open(path2, 'r') as f:
    d2 = json.load(f)
valid = [s for s in d2 if s in s_set]

# Batching
batch_size = 50
batches = []
current_batch = []

for s in valid:
    current_batch.append(s)
    if len(current_batch) >= batch_size:
        batches.append(current_batch)
        current_batch = []
if current_batch:
    batches.append(current_batch)

queries = []
for batch in batches:
    sqls = []
    for s in batch:
        part1 = "SELECT '" + s + "' as Symbol, COUNT(*) as cnt FROM "
        part2 = '"' + s + '"'
        part3 = " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
        sqls.append(part1 + part2 + part3)
    if sqls:
        queries.append(" UNION ALL ".join(sqls))

print("__RESULT__:")
print(json.dumps({"count": len(valid), "num_batches": len(queries), "queries": queries}))"""

env_args = {'var_function-call-15016460926965200659': 'file_storage/function-call-15016460926965200659.json', 'var_function-call-570738584850609366': 'file_storage/function-call-570738584850609366.json', 'var_function-call-533584454606138071': 'file_storage/function-call-533584454606138071.json', 'var_function-call-12519658004391371257': 'file_storage/function-call-12519658004391371257.json'}

exec(code, env_args)
