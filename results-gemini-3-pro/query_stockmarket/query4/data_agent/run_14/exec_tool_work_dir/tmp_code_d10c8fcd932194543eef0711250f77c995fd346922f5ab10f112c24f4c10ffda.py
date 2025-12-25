code = """import json
path = locals()['var_function-call-5645677206837916636']
with open(path, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
batch = symbols[0:40]
dq = chr(34)
sq = chr(39)
parts = []
for sym in batch:
    s = "SELECT " + sq + sym + sq + " as symbol, SUM(CASE WHEN " + dq + "Close" + dq + " > " + dq + "Open" + dq + " THEN 1 ELSE 0 END) as u, SUM(CASE WHEN " + dq + "Close" + dq + " < " + dq + "Open" + dq + " THEN 1 ELSE 0 END) as d FROM " + dq + sym + dq + " WHERE " + dq + "Date" + dq + " >= " + sq + "2017-01-01" + sq + " AND " + dq + "Date" + dq + " <= " + sq + "2017-12-31" + sq
    parts.append(s)
full = " UNION ALL ".join(parts)
q = "SELECT symbol, u, d, (u-d) as diff FROM (" + full + ") WHERE u > d ORDER BY diff DESC LIMIT 5"
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json', 'var_function-call-5783268603279882755': {'count1': 234, 'count2': 2753}, 'var_function-call-5645677206837916636': 'file_storage/function-call-5645677206837916636.json', 'var_function-call-16652445998382813743': {'d1': '2017-01-01', 'd2': '2017-12-31'}, 'var_function-call-11638997856431239306': 'file_storage/function-call-11638997856431239306.json', 'var_function-call-6879186300581264802': 'file_storage/function-call-6879186300581264802.json'}

exec(code, env_args)
