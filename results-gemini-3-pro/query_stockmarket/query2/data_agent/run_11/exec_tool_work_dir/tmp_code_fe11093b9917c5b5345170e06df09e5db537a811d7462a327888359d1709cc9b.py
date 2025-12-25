code = """import json

k1 = 'var_function-call-15483899617551082624'
k2 = 'var_function-call-17197364182680462886'

with open(locals()[k1], 'r') as f:
    etfs = json.load(f)
syms = [x['Symbol'] for x in etfs]

with open(locals()[k2], 'r') as f:
    tbls = json.load(f)

valid = sorted(list(set(syms).intersection(set(tbls))))

dq = chr(34)
sq = chr(39)

queries = []
batch_size = 80 # Safe margin
current_batch = []

for i, t in enumerate(valid):
    current_batch.append(t)
    if len(current_batch) == batch_size or i == len(valid) - 1:
        parts = []
        for s in current_batch:
            col = dq + "Adj Close" + dq
            date_cond = "Date LIKE " + sq + "2015%" + sq
            q = "SELECT " + sq + s + sq + " as Symbol FROM " + dq + s + dq + " WHERE " + date_cond + " AND " + col + " > 200 LIMIT 1"
            parts.append(q)
        
        full_q = " UNION ALL ".join(parts)
        queries.append(full_q)
        current_batch = []

print("__RESULT__:")
print(json.dumps({"lengths": [len(q) for q in queries], "num_queries": len(queries), "first_query": queries[0]}))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json', 'var_function-call-2473417228619815935': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_function-call-10917053200744344963': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_function-call-11455913189919788816': 'file_storage/function-call-11455913189919788816.json', 'var_function-call-2015969074599324201': 'file_storage/function-call-2015969074599324201.json', 'var_function-call-9446504676593591183': 'file_storage/function-call-9446504676593591183.json'}

exec(code, env_args)
