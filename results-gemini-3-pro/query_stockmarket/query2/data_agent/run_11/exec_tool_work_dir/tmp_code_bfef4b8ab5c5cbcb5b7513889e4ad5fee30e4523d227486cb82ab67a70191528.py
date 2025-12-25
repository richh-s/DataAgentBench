code = """import json

k1 = 'var_function-call-15483899617551082624'
k2 = 'var_function-call-17197364182680462886'

with open(locals()[k1], 'r') as f:
    etfs = json.load(f)
syms = [x['Symbol'] for x in etfs]

with open(locals()[k2], 'r') as f:
    tbls = json.load(f)

valid = sorted(list(set(syms).intersection(set(tbls))))

queries = []
# Just 5 for test
for t in valid[:5]:
    # Use f-string. Note triple quotes usage in f-string might be risky if code is wrapped in triple quotes.
    # Use simple string concatenation
    q = "SELECT '" + t + "' as Symbol FROM \"" + t + "\" WHERE \"Adj Close\" > 200 LIMIT 1"
    queries.append(q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json', 'var_function-call-2473417228619815935': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_function-call-10917053200744344963': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}

exec(code, env_args)
