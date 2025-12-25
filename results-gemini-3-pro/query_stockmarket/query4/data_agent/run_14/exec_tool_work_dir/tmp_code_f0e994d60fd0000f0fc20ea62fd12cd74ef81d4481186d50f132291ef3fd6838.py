code = """import json

# Read the symbols from the previous result
path = locals()['var_function-call-5645677206837916636']
with open(path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
chunks = [symbols[i:i + 50] for i in range(0, len(symbols), 50)]

queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        p = "SELECT '" + sym + "' as symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) as down_days FROM \"" + sym + "\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
        parts.append(p)
    
    full = " UNION ALL ".join(parts)
    # Get top 5 from this chunk to save space
    q = "SELECT symbol, up_days, down_days, (up_days - down_days) as diff FROM (" + full + ") WHERE up_days > down_days ORDER BY diff DESC LIMIT 5"
    queries.append(q)

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json', 'var_function-call-5783268603279882755': {'count1': 234, 'count2': 2753}, 'var_function-call-5645677206837916636': 'file_storage/function-call-5645677206837916636.json'}

exec(code, env_args)
