code = """import json

with open(locals()['var_function-call-663389646352767259'], 'r') as f:
    symbols = json.load(f)

batch = symbols[:500]
queries = []
for sym in batch:
    # Use double quotes for table names in case of reserved words or special chars
    q = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-3977650505949918097': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-12570417509960838288': 'file_storage/function-call-12570417509960838288.json', 'var_function-call-3414087167265724678': 'file_storage/function-call-3414087167265724678.json', 'var_function-call-663389646352767259': 'file_storage/function-call-663389646352767259.json', 'var_function-call-13483088293029906291': 1435}

exec(code, env_args)
