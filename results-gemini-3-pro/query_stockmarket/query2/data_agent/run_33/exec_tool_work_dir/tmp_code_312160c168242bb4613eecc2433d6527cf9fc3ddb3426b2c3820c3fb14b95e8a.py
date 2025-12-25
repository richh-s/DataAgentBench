code = """import json

etf_path = locals()['var_function-call-689800581831186980']
tbl_path = locals()['var_function-call-10272020244024100123']

with open(etf_path) as f: etfs = json.load(f)
with open(tbl_path) as f: tbls = json.load(f)

syms = sorted(list(set(e['Symbol'] for e in etfs).intersection(tbls)))
batches = [syms[i:i+300] for i in range(0, len(syms), 300)]

qs = []
for b in batches:
    sqs = ["SELECT '{0}' as Symbol FROM \"{0}\" WHERE \"Date\" LIKE '2015-%' AND \"Adj Close\" > 200 LIMIT 1".format(s) for s in b]
    qs.append(" UNION ALL ".join(sqs))

print("__RESULT__:")
print(json.dumps(qs))"""

env_args = {'var_function-call-689800581831186980': 'file_storage/function-call-689800581831186980.json', 'var_function-call-10272020244024100123': 'file_storage/function-call-10272020244024100123.json', 'var_function-call-13327904948754133498': 'file_storage/function-call-13327904948754133498.json'}

exec(code, env_args)
