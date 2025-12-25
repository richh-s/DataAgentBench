code = """import json

key1 = locals()['var_function-call-15041179575620663469']
key2 = locals()['var_function-call-15041179575620664610']

with open(key1, 'r') as f:
    stock_candidates = json.load(f)
with open(key2, 'r') as f:
    tables = json.load(f)

candidate_symbols = set([s['Symbol'] for s in stock_candidates])
available_tables = set(tables)
valid_symbols = sorted(list(candidate_symbols.intersection(available_tables)))

chunk1 = valid_symbols[:120]

queries = []
for sym in chunk1:
    q = "SELECT '{0}' AS Symbol, COUNT(CASE WHEN Close > Open THEN 1 END) AS UpDays, COUNT(CASE WHEN Close < Open THEN 1 END) AS DownDays FROM \"{0}\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31' GROUP BY Symbol".format(sym)
    queries.append(q)

final_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-15041179575620663469': 'file_storage/function-call-15041179575620663469.json', 'var_function-call-15041179575620664610': 'file_storage/function-call-15041179575620664610.json', 'var_function-call-228974588171735030': 234, 'var_function-call-1702929696304922110': [{'Date': '1987-09-30'}]}

exec(code, env_args)
