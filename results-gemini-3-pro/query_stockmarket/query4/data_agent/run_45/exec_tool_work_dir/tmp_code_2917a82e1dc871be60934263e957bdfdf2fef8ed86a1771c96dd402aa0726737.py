code = """import json
path = locals()['var_function-call-16488807000991432586']
with open(path, 'r') as f:
    valid_stocks = json.load(f)

q_parts = []
for s in valid_stocks:
    sym = s['Symbol']
    part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    q_parts.append(part)

full = " UNION ALL ".join(q_parts)
final = "SELECT Symbol, UpDays, DownDays FROM (" + full + ") WHERE UpDays > DownDays ORDER BY UpDays DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_function-call-17490755573003883636': 'file_storage/function-call-17490755573003883636.json', 'var_function-call-8209134030405193310': 'file_storage/function-call-8209134030405193310.json', 'var_function-call-16488807000991432586': 'file_storage/function-call-16488807000991432586.json', 'var_function-call-8713500348890617850': 'file_storage/function-call-8713500348890617850.json'}

exec(code, env_args)
