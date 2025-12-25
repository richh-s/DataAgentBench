code = """import json
path = locals()['var_function-call-15718840696057436143']
with open(path, 'r') as f:
    syms = json.load(f)

queries = []
size = 300
for i in range(0, len(syms), size):
    chunk = syms[i:i+size]
    parts = []
    for s in chunk:
        q = "SELECT '" + s + "' as Symbol FROM \"" + s + "\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        parts.append(q)
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-4976631640626439833': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-10780135608603359427': 'file_storage/function-call-10780135608603359427.json', 'var_function-call-12146310968865699605': 'file_storage/function-call-12146310968865699605.json', 'var_function-call-15718840696057436143': 'file_storage/function-call-15718840696057436143.json', 'var_function-call-18247159550468154824': 1435, 'var_function-call-748487799813922742': 'hello', 'var_function-call-15438848725478178333': 'file_storage/function-call-15718840696057436143.json', 'var_function-call-965022865682277480': 1435}

exec(code, env_args)
