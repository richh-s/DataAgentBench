code = """import json
path = locals()['var_function-call-17904107048790784824']
data = json.load(open(path))
res = []
for i in range(0, len(data), 500):
    ch = data[i:i+500]
    qs = ["SELECT '{0}' as S FROM \"{0}\" WHERE Date LIKE '2015-%' AND \"Adj Close\" > 200 LIMIT 1".format(x) for x in ch]
    res.append(" UNION ALL ".join(qs))
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-8664818229940641972': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-925302824515021952': 'file_storage/function-call-925302824515021952.json', 'var_function-call-16367137017631694844': 'file_storage/function-call-16367137017631694844.json', 'var_function-call-17904107048790784824': 'file_storage/function-call-17904107048790784824.json', 'var_function-call-13652979360882953487': 'Hello'}

exec(code, env_args)
