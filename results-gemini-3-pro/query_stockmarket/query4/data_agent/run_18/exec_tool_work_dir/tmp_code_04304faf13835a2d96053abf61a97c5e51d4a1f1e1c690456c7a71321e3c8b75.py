code = """import json

with open(locals()['var_function-call-3888203055902686164'], 'r') as f:
    data = json.load(f)

candidates = data['valid_candidates']
batch = candidates[0:50]

queries = []
for c in batch:
    sym = c['Symbol']
    # Use .format to be cleaner
    # q = "SELECT '{}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(sym, sym)
    # I need to be careful with quotes.
    # Python string: 'SELECT \'{}\' as Symbol ... FROM "{}" ...'
    q = "SELECT '{}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(sym, sym)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-11613122979303732925': 'file_storage/function-call-11613122979303732925.json', 'var_function-call-9272637941847982752': 'file_storage/function-call-9272637941847982752.json', 'var_function-call-3888203055902686164': 'file_storage/function-call-3888203055902686164.json', 'var_function-call-12664513076850193570': 234}

exec(code, env_args)
