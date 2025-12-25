code = """import json

# Load symbols
path1 = locals()['var_function-call-9762896799442664376']
with open(path1, 'r') as f:
    d1 = json.load(f)
    syms = set([x['Symbol'] for x in d1])

# Load tables
path2 = locals()['var_function-call-15346480681916956948']
with open(path2, 'r') as f:
    tbls = set(json.load(f))

valid = sorted(list(syms.intersection(tbls)))
print(f"Valid symbols count: {len(valid)}")
print("First 20:", valid[:20])

# Construct query for first 20
batch1 = valid[:20]
queries = []
for s in batch1:
    q = f"SELECT '{s}' as Symbol, COUNT(*) as Days FROM \"{s}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

final_q = " UNION ALL ".join(queries)
print('__RESULT__:')
print(json.dumps(final_q))"""

env_args = {'var_function-call-9762896799442664376': 'file_storage/function-call-9762896799442664376.json', 'var_function-call-7368161656916448319': 86, 'var_function-call-15346480681916956948': 'file_storage/function-call-15346480681916956948.json', 'var_function-call-4914821713470736250': 'file_storage/function-call-4914821713470736250.json'}

exec(code, env_args)
