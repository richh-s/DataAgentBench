code = """import json

with open(locals()['var_function-call-14501516431972951322'], 'r') as f:
    stocks = json.load(f)

symbols = [s['Symbol'] for s in stocks]

queries = []
for sym in symbols:
    # Use double quotes for table names to handle case sensitivity or special chars if any
    q = f"""
    SELECT '{sym}' as Symbol, 
           SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, 
           SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays 
    FROM "{sym}" 
    WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'
    """
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14501516431972951322': 'file_storage/function-call-14501516431972951322.json', 'var_function-call-15409720678341312675': 234}

exec(code, env_args)
