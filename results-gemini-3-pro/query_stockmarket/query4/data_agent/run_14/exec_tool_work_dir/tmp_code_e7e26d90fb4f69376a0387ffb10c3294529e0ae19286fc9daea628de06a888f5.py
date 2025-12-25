code = """import json
path = locals()['var_function-call-5645677206837916636']
with open(path, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
# symbols = symbols[:50] # Try full list
parts = []
for sym in symbols:
    s = "SELECT '" + sym + "' as symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) as u, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) as d FROM \"" + sym + "\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    parts.append(s)
full = " UNION ALL ".join(parts)
q = "SELECT symbol, u, d, (u-d) as diff FROM (" + full + ") WHERE u > d ORDER BY diff DESC LIMIT 5"
print('__RESULT__:')
print(json.dumps([q]))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json', 'var_function-call-5783268603279882755': {'count1': 234, 'count2': 2753}, 'var_function-call-5645677206837916636': 'file_storage/function-call-5645677206837916636.json', 'var_function-call-16652445998382813743': {'d1': '2017-01-01', 'd2': '2017-12-31'}}

exec(code, env_args)
