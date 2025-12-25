code = """import json

# Get file path
file_path = locals()['var_function-call-2951448566390777149']

# Load data
with open(file_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
# Sort to be deterministic
symbols.sort()

# Chunk 1: 0 to 100
chunk = symbols[0:100]
dq = chr(34)
parts = []
for s in chunk:
    q = "SELECT '" + s + "' as Symbol FROM " + dq + s + dq + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
    parts.append(q)

query = " UNION ALL ".join(parts)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-14301945511223140359': 'file_storage/function-call-14301945511223140359.json', 'var_function-call-6882633768806362112': 'file_storage/function-call-6882633768806362112.json', 'var_function-call-2951448566390777149': 'file_storage/function-call-2951448566390777149.json', 'var_function-call-4592447069327499722': [{'Date': '2018-08-15'}], 'var_function-call-414595352554108006': 'file_storage/function-call-414595352554108006.json'}

exec(code, env_args)
