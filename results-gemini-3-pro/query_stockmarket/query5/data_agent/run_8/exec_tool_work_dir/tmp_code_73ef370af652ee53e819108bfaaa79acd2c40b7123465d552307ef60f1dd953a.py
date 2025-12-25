code = """import json

path = locals()['var_function-call-11588894222788545089']
with open(path, 'r') as f:
    data = json.load(f)

valid_symbols = data['valid_symbols']
parts = []
for s in valid_symbols:
    parts.append("SELECT '{0}' as Symbol, COUNT(*) as Days FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)".format(s))

query = " UNION ALL ".join(parts) + " ORDER BY Days DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2176412617243161922': 'file_storage/function-call-2176412617243161922.json', 'var_function-call-11082574715617122511': 'file_storage/function-call-11082574715617122511.json', 'var_function-call-11588894222788545089': 'file_storage/function-call-11588894222788545089.json'}

exec(code, env_args)
