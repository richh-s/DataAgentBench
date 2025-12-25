code = """import json

path_info = locals()['var_function-call-10876543030681688421']

with open(path_info, 'r') as f:
    data = json.load(f)

symbols = data['symbols']

parts = []
# Template for the query part
template = "SELECT '{}' as Symbol, COUNT(*) as Days FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low"

for sym in symbols:
    parts.append(template.format(sym, sym))

full_query = " UNION ALL ".join(parts)
full_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-10214436996742013991': 'file_storage/function-call-10214436996742013991.json', 'var_function-call-16037217244110734326': 'file_storage/function-call-16037217244110734326.json', 'var_function-call-10876543030681688421': 'file_storage/function-call-10876543030681688421.json', 'var_function-call-17426725772123534296': 'file_storage/function-call-17426725772123534296.json', 'var_function-call-11346198057420557082': "SELECT 'AGMH' as Symbol, COUNT(*) as Days FROM  + sym +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as Days FROM  + sym +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as Days FROM  + sym +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'ANDA' as Symbol, COUNT(*) as Days FROM  + sy"}

exec(code, env_args)
