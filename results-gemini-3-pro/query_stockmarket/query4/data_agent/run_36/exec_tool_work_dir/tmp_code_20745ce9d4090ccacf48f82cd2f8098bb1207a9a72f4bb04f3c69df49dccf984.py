code = """import json

path = locals()['var_function-call-2661790456130058223']
with open(path, 'r') as f:
    data = json.load(f)

symbols = data['valid_symbols']
union_parts = []
q1 = chr(39)
q2 = chr(34)

for sym in symbols:
    part = "SELECT " + q1 + sym + q1 + " as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM " + q2 + sym + q2 + " WHERE substr(Date, 1, 4) = " + q1 + "2017" + q1
    union_parts.append(part)

full_query = " UNION ALL ".join(union_parts)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-17110094942828308105': 'file_storage/function-call-17110094942828308105.json', 'var_function-call-769695609142017775': 'file_storage/function-call-769695609142017775.json', 'var_function-call-2661790456130058223': 'file_storage/function-call-2661790456130058223.json', 'var_function-call-3680617775405342251': 'file_storage/function-call-3680617775405342251.json', 'var_function-call-10135136864544930688': 'file_storage/function-call-10135136864544930688.json'}

exec(code, env_args)
