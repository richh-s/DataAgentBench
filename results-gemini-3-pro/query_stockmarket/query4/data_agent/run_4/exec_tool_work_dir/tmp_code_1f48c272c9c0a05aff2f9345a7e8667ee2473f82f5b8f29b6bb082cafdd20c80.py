code = """import json

previous_result_file = locals()['var_function-call-14133125675221425702']
with open(previous_result_file, 'r') as f:
    data = json.load(f)
    candidates = data['candidates']

chunk = candidates[0:60]
queries = []
for item in chunk:
    sym = item['Symbol']
    q = "SELECT '" + sym + "' AS Symbol, Open, Close FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-15963372887811120509': 'file_storage/function-call-15963372887811120509.json', 'var_function-call-11545474830056359161': 'file_storage/function-call-11545474830056359161.json', 'var_function-call-14133125675221425702': 'file_storage/function-call-14133125675221425702.json', 'var_function-call-5008870228021754307': [{'Date': '2019-10-24'}], 'var_function-call-3816975989307448527': 'file_storage/function-call-3816975989307448527.json', 'var_function-call-14005701755922109127': 'file_storage/function-call-14005701755922109127.json'}

exec(code, env_args)
