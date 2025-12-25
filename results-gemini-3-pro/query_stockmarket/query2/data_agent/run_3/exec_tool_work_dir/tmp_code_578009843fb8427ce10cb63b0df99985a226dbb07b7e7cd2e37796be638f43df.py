code = """import json

file_path = locals()['var_function-call-2951448566390777149']

with open(file_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
symbols.sort()

# Reset state
batch_size = 100
start = 0
end = start + batch_size
chunk = symbols[start:end]

dq = chr(34)
parts = []
for s in chunk:
    q = "SELECT '" + s + "' as Symbol FROM " + dq + s + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date GLOB '2015*' LIMIT 1"
    parts.append(q)

query = " UNION ALL ".join(parts)

# Save state
with open('idx.txt', 'w') as f:
    f.write(str(end))

with open('found_symbols.json', 'w') as f:
    json.dump([], f)

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-14301945511223140359': 'file_storage/function-call-14301945511223140359.json', 'var_function-call-6882633768806362112': 'file_storage/function-call-6882633768806362112.json', 'var_function-call-2951448566390777149': 'file_storage/function-call-2951448566390777149.json', 'var_function-call-4592447069327499722': [{'Date': '2018-08-15'}], 'var_function-call-414595352554108006': 'file_storage/function-call-414595352554108006.json', 'var_function-call-8106184226971700121': 'file_storage/function-call-8106184226971700121.json', 'var_function-call-4248295959890080196': [], 'var_function-call-12837184720204771452': 'file_storage/function-call-12837184720204771452.json'}

exec(code, env_args)
