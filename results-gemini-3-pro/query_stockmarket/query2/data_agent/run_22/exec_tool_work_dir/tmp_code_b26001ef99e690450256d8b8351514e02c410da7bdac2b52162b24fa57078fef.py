code = """import json

with open(locals()['var_function-call-7696497825496925581'], 'r') as f:
    valid_etfs = json.load(f)

dq = chr(34)
parts = []
for sym in valid_etfs:
    sql = "SELECT '" + sym + "' as Symbol, MAX(" + dq + "Adj Close" + dq + ") as mp FROM " + dq + sym + dq + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(sql)

full_query = "SELECT Symbol FROM (" + " UNION ALL ".join(parts) + ") WHERE mp > 200"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-11251300445025460794': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-3995568477858160008': 'file_storage/function-call-3995568477858160008.json', 'var_function-call-16997364755516220008': 'file_storage/function-call-16997364755516220008.json', 'var_function-call-7696497825496925581': 'file_storage/function-call-7696497825496925581.json', 'var_function-call-14061231607560525758': 1435, 'var_function-call-6740885424165552969': 'file_storage/function-call-6740885424165552969.json'}

exec(code, env_args)
