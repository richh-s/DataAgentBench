code = """import json

path = locals()['var_function-call-5393401746744770363']
with open(path, 'r') as f:
    relevant_stocks = json.load(f)

symbols = [s['Symbol'] for s in relevant_stocks]

batch_size = 50
batches = [symbols[i:i + batch_size] for i in range(0, len(symbols), batch_size)]

queries = []
for batch in batches:
    sub_queries = []
    for sym in batch:
        q = "SELECT '" + sym + "' as Symbol, " \
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, " \
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays " \
            "FROM \"" + sym + "\" " \
            "WHERE Date LIKE '2017-%'"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-4648296412800543447': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-9041391857086701632': 'file_storage/function-call-9041391857086701632.json', 'var_function-call-17919836016928791743': 'file_storage/function-call-17919836016928791743.json', 'var_function-call-5393401746744770363': 'file_storage/function-call-5393401746744770363.json', 'var_function-call-6371941685169067473': 234}

exec(code, env_args)
