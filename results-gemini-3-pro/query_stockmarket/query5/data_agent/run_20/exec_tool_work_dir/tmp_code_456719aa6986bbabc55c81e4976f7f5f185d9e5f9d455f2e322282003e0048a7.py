code = """import json

path1 = locals()['var_function-call-9762896799442664376']
with open(path1, 'r') as f:
    d1 = json.load(f)

path2 = locals()['var_function-call-15346480681916956948']
with open(path2, 'r') as f:
    tbls = set(json.load(f))

syms = set([x['Symbol'] for x in d1])
valid = sorted(list(syms.intersection(tbls)))

# Batch 1: 0-20
batch = valid[0:20]

parts = []
for s in batch:
    part = "SELECT '{0}' as Symbol, COUNT(*) as Days FROM \"{0}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)".format(s)
    parts.append(part)

query = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-9762896799442664376': 'file_storage/function-call-9762896799442664376.json', 'var_function-call-7368161656916448319': 86, 'var_function-call-15346480681916956948': 'file_storage/function-call-15346480681916956948.json', 'var_function-call-4914821713470736250': 'file_storage/function-call-4914821713470736250.json'}

exec(code, env_args)
