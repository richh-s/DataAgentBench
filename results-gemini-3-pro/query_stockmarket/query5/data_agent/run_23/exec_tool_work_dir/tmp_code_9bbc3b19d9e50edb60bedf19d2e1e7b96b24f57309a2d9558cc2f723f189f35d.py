code = """import json

path_info = locals()['var_function-call-10876543030681688421']

with open(path_info, 'r') as f:
    data = json.load(f)

symbols = data['symbols']

parts = []
for sym in symbols:
    # Concatenation instead of f-string just in case
    # "SELECT 'SYM' as Symbol, COUNT(*) as Days FROM "SYM" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low"
    part = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low"
    parts.append(part)

full_query = " UNION ALL ".join(parts)
full_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-10214436996742013991': 'file_storage/function-call-10214436996742013991.json', 'var_function-call-16037217244110734326': 'file_storage/function-call-16037217244110734326.json', 'var_function-call-10876543030681688421': 'file_storage/function-call-10876543030681688421.json'}

exec(code, env_args)
