code = """import json

with open(locals()['var_function-call-4127219778048163343'], 'r') as f:
    target_stocks = json.load(f)

batch = target_stocks[0:60]
queries = []
for stock in batch:
    sym = stock['Symbol']
    # Use simple string concatenation to avoid syntax issues in execution environment
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) as Down FROM \"" + sym + "\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(full_query)"""

env_args = {'var_function-call-16810398710687085223': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-1631025954943238764': 'file_storage/function-call-1631025954943238764.json', 'var_function-call-4060108603261474737': 'file_storage/function-call-4060108603261474737.json', 'var_function-call-4127219778048163343': 'file_storage/function-call-4127219778048163343.json', 'var_function-call-2579092286742790265': 234}

exec(code, env_args)
