code = """import json
path = locals()['var_function-call-16716209027256917724']
with open(path, 'r') as f:
    data = json.load(f)
symbols = []
for item in data:
    symbols.append(item['Symbol'])

parts = []
for sym in symbols:
    part = "SELECT '" + sym + "' as S, COUNT(*) as C FROM \"" + sym + "\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    parts.append(part)

final_query = " UNION ALL ".join(parts)
final_query += " ORDER BY C DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-5873850458865278019': 'file_storage/function-call-5873850458865278019.json', 'var_function-call-10785221419564258441': 'file_storage/function-call-10785221419564258441.json', 'var_function-call-16716209027256917724': 'file_storage/function-call-16716209027256917724.json', 'var_function-call-139130541756909283': 86}

exec(code, env_args)
