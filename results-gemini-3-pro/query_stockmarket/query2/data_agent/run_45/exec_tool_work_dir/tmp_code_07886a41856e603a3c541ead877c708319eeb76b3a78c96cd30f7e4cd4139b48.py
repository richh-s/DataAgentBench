code = """import json

# Get file paths
etf_file_path = locals()['var_function-call-3295962867968348472']

# Load ETF symbols
with open(etf_file_path, 'r') as f:
    valid_etfs = json.load(f)

# Take first 100
batch = valid_etfs[:100]

# Construct query
parts = []
for symbol in batch:
    parts.append(f"SELECT '{symbol}' as Symbol FROM \"{symbol}\" WHERE \"Date\" LIKE '2015%' AND \"Adj Close\" > 200 LIMIT 1")

query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3501888639631551339': 'file_storage/function-call-3501888639631551339.json', 'var_function-call-1897156142471319365': 'file_storage/function-call-1897156142471319365.json', 'var_function-call-3295962867968348472': 'file_storage/function-call-3295962867968348472.json', 'var_function-call-11530623601656083675': 1435, 'var_function-call-3709276694871422927': [{'Date': '2018-08-15'}]}

exec(code, env_args)
