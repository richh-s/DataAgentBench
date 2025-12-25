code = """import json

path = locals()['var_function-call-14501516431972951322']
with open(path, 'r') as f:
    stocks = json.load(f)

# Batch 1: 0-40
batch = stocks[0:40]

queries = []
for s in batch:
    sym = s['Symbol']
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_function-call-14501516431972951322': 'file_storage/function-call-14501516431972951322.json', 'var_function-call-15409720678341312675': 234, 'var_function-call-6232990311228431744': 'file_storage/function-call-6232990311228431744.json', 'var_function-call-8825046291804428721': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date >= '2017-01-01' AND Date <= '2017-", 'var_function-call-10826932887850884284': 'file_storage/function-call-10826932887850884284.json', 'var_function-call-4232774925114079970': 'file_storage/function-call-4232774925114079970.json'}

exec(code, env_args)
