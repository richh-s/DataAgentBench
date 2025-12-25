code = """import json

with open(locals()['var_function-call-4241544829162874194'], 'r') as f:
    valid_symbols = json.load(f)

batch = valid_symbols[:500]
queries = []
dq = chr(34)
sq = chr(39)
for sym in batch:
    q = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE Date >= " + sq + "2015-01-01" + sq + " AND Date <= " + sq + "2015-12-31" + sq + " AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
    queries.append(q)

final_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-14195711220532126717': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-13030058367102200413': 'file_storage/function-call-13030058367102200413.json', 'var_function-call-151626240589154895': 'file_storage/function-call-151626240589154895.json', 'var_function-call-4241544829162874194': 'file_storage/function-call-4241544829162874194.json', 'var_function-call-10903685240376781787': 1435}

exec(code, env_args)
