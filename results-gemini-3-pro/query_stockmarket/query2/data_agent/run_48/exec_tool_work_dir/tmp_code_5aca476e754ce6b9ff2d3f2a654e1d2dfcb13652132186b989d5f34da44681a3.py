code = """import json

file_path = locals()['var_function-call-260988811028178288']
with open(file_path, 'r') as f:
    symbols = json.load(f)

batch_size = 110
queries = []
dq = chr(34)

for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    sub_queries = []
    for sym in batch:
        q = "SELECT '" + sym + "' FROM " + dq + sym + dq + " WHERE Date LIKE '2015-%' AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-6186779081342052772': ['stockinfo'], 'var_function-call-13990833261283906636': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-13207844345041209212': 'file_storage/function-call-13207844345041209212.json', 'var_function-call-11466035443477802505': 'file_storage/function-call-11466035443477802505.json', 'var_function-call-260988811028178288': 'file_storage/function-call-260988811028178288.json', 'var_function-call-12097754673837591275': 1435, 'var_function-call-2940039926885170812': [{'Date': '2018-08-15'}], 'var_function-call-6650499876681190630': 'file_storage/function-call-6650499876681190630.json', 'var_function-call-14288082701687559034': 'file_storage/function-call-14288082701687559034.json', 'var_function-call-3072697572983194448': 'file_storage/function-call-3072697572983194448.json'}

exec(code, env_args)
