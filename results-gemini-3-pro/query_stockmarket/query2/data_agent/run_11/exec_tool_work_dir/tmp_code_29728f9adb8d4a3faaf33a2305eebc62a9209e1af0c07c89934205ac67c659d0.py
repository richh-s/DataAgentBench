code = """import json

k1 = 'var_function-call-15483899617551082624'
k2 = 'var_function-call-17197364182680462886'

p_etfs = locals()[k1]
p_tbls = locals()[k2]

with open(p_etfs, 'r') as f:
    etfs = json.load(f)
syms = [x['Symbol'] for x in etfs]

with open(p_tbls, 'r') as f:
    tbls = json.load(f)

valid = sorted(list(set(syms).intersection(set(tbls))))

queries = []
batch = []
bs = 50

for i, s in enumerate(valid):
    batch.append(s)
    if len(batch) == bs or i == len(valid) - 1:
        parts = []
        for t in batch:
            # Construct SQL string
            # Double quotes around table name t
            # Single quotes around symbol literal t
            # Date range check
            # Adj Close check
            # We construct it using concatenation to avoid f-string or escape issues if any
            sql = "SELECT '" + t + "' as Symbol FROM \"" + t + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
            parts.append(sql)
        
        full_q = " UNION ALL ".join(parts)
        queries.append(full_q)
        batch = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json', 'var_function-call-2473417228619815935': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
