code = """import json

with open(locals()['var_function-call-4648634188354399784'], 'r') as f:
    valid_symbols = json.load(f)

batch = valid_symbols[:43]

sqls = []
for item in batch:
    sym = item['Symbol']
    part = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
    sqls.append(part)

full_query = " UNION ALL ".join(sqls)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-9914396351492829632': 'file_storage/function-call-9914396351492829632.json', 'var_function-call-9914396351492832197': 'file_storage/function-call-9914396351492832197.json', 'var_function-call-4648634188354399784': 'file_storage/function-call-4648634188354399784.json', 'var_function-call-10219029922974567872': 86, 'var_function-call-10494812981472623232': 'file_storage/function-call-10494812981472623232.json'}

exec(code, env_args)
