code = """import json
key = 'var_function-call-17687104531794543290'
path = locals()[key]
with open(path, 'r') as f:
    data = json.load(f)

qs = []
for d in data:
    s = d['Symbol']
    q = "SELECT '" + s + "' as Symbol, COUNT(*) as cnt FROM \"" + s + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low"
    qs.append(q)

final = " UNION ALL ".join(qs) + " ORDER BY cnt DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_function-call-4309411817698627857': 'file_storage/function-call-4309411817698627857.json', 'var_function-call-2225053238657252843': 'file_storage/function-call-2225053238657252843.json', 'var_function-call-17687104531794543290': 'file_storage/function-call-17687104531794543290.json', 'var_function-call-17493952526099454849': 86, 'var_function-call-17506123654459597090': 'file_storage/function-call-17506123654459597090.json', 'var_function-call-1278789372639230579': 'file_storage/function-call-1278789372639230579.json', 'var_function-call-14387363582166172085': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + s + "}

exec(code, env_args)
