code = """import json

path = locals()['var_function-call-17687104531794543290']
with open(path, 'r') as f:
    valid_companies = json.load(f)

queries = []
for company in valid_companies:
    symbol = company['Symbol']
    q = "SELECT '{0}' as Symbol, COUNT(*) as cnt FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low".format(symbol)
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-4309411817698627857': 'file_storage/function-call-4309411817698627857.json', 'var_function-call-2225053238657252843': 'file_storage/function-call-2225053238657252843.json', 'var_function-call-17687104531794543290': 'file_storage/function-call-17687104531794543290.json', 'var_function-call-17493952526099454849': 86, 'var_function-call-17506123654459597090': 'file_storage/function-call-17506123654459597090.json', 'var_function-call-1278789372639230579': 'file_storage/function-call-1278789372639230579.json', 'var_function-call-14387363582166172085': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + s + "}

exec(code, env_args)
