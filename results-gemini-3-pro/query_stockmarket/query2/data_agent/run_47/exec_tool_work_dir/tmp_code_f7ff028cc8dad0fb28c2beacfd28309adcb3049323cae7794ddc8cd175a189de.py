code = """import json

key = 'var_function-call-18089665588996577560'
filename = locals()[key]
with open(filename, 'r') as f:
    valid_symbols = json.load(f)

queries = []
# Just do for first 2 symbols to test
for sym in valid_symbols[:2]:
    part1 = "SELECT '" + sym + "' as Symbol"
    part2 = " FROM \"" + sym + "\""
    part3 = " WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'"
    part4 = " AND \"Adj Close\" > 200 LIMIT 1"
    queries.append(part1 + part2 + part3 + part4)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-7344486637286600100': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2454856655276099395': 'file_storage/function-call-2454856655276099395.json', 'var_function-call-6642693361376335155': 'file_storage/function-call-6642693361376335155.json', 'var_function-call-18089665588996577560': 'file_storage/function-call-18089665588996577560.json', 'var_function-call-8976669871907571712': 1435, 'var_function-call-15282565031940966073': ['AAAU'], 'var_function-call-11959501744294715290': ["SELECT 'AAAU' as Symbol"]}

exec(code, env_args)
