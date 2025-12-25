code = """import json

path = locals()['var_function-call-2661790456130058223']
with open(path, 'r') as f:
    data = json.load(f)

symbols = data['valid_symbols']
chunk_size = 50
queries = []

for i in range(0, len(symbols), chunk_size):
    chunk = symbols[i:i + chunk_size]
    union_parts = []
    for sym in chunk:
        # Use simple string concatenation or formatting
        part = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date LIKE '2017%'"
        union_parts.append(part)
    
    full_query = " UNION ALL ".join(union_parts)
    queries.append(full_query)

print(f"Generated {len(queries)} queries.")
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17110094942828308105': 'file_storage/function-call-17110094942828308105.json', 'var_function-call-769695609142017775': 'file_storage/function-call-769695609142017775.json', 'var_function-call-2661790456130058223': 'file_storage/function-call-2661790456130058223.json'}

exec(code, env_args)
