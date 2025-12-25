code = """import json

key1 = locals()['var_function-call-15041179575620663469']
key2 = locals()['var_function-call-15041179575620664610']

with open(key1, 'r') as f:
    cand = json.load(f)
with open(key2, 'r') as f:
    tabs = json.load(f)

syms = sorted(list(set([x['Symbol'] for x in cand]).intersection(set(tabs))))

# Chunk 1: 0-40
chunk = syms[0:40]
qs = []
for s in chunk:
    qs.append("SELECT '" + s + "' AS Symbol, COUNT(CASE WHEN Close > Open THEN 1 END) AS UpDays, COUNT(CASE WHEN Close < Open THEN 1 END) AS DownDays FROM \"" + s + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' GROUP BY Symbol")

print("__RESULT__:")
print(json.dumps(" UNION ALL ".join(qs)))"""

env_args = {'var_function-call-15041179575620663469': 'file_storage/function-call-15041179575620663469.json', 'var_function-call-15041179575620664610': 'file_storage/function-call-15041179575620664610.json', 'var_function-call-228974588171735030': 234, 'var_function-call-1702929696304922110': [{'Date': '1987-09-30'}], 'var_function-call-7421439178259456422': 'file_storage/function-call-7421439178259456422.json', 'var_function-call-17986789611422463090': 'file_storage/function-call-17986789611422463090.json'}

exec(code, env_args)
