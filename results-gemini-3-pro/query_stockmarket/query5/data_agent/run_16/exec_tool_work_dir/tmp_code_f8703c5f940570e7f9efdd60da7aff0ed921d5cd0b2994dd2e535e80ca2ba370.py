code = """import json
data = json.load(open(locals()['var_function-call-17687104531794543290']))
qs = []
for d in data:
    s = d['Symbol']
    qs.append("SELECT '" + s + "' as Symbol, COUNT(*) as cnt FROM \"" + s + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low")
final_q = " UNION ALL ".join(qs) + " ORDER BY cnt DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-4309411817698627857': 'file_storage/function-call-4309411817698627857.json', 'var_function-call-2225053238657252843': 'file_storage/function-call-2225053238657252843.json', 'var_function-call-17687104531794543290': 'file_storage/function-call-17687104531794543290.json', 'var_function-call-17493952526099454849': 86, 'var_function-call-17506123654459597090': 'file_storage/function-call-17506123654459597090.json'}

exec(code, env_args)
