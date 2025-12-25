code = """import json

key1 = locals()['var_function-call-15041179575620663469']
key2 = locals()['var_function-call-15041179575620664610']

with open(key1, 'r') as f:
    cand = json.load(f)
with open(key2, 'r') as f:
    tabs = json.load(f)

syms = sorted(list(set([x['Symbol'] for x in cand]).intersection(set(tabs))))
chunk = syms[:120]

qs = []
for s in chunk:
    qs.append("SELECT '" + s + "' AS Symbol, COUNT(CASE WHEN Close > Open THEN 1 END) AS UpDays, COUNT(CASE WHEN Close < Open THEN 1 END) AS DownDays FROM \"" + s + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'")

print("__RESULT__:")
print(json.dumps(" UNION ALL ".join(qs)))"""

env_args = {'var_function-call-15041179575620663469': 'file_storage/function-call-15041179575620663469.json', 'var_function-call-15041179575620664610': 'file_storage/function-call-15041179575620664610.json', 'var_function-call-228974588171735030': 234, 'var_function-call-1702929696304922110': [{'Date': '1987-09-30'}]}

exec(code, env_args)
