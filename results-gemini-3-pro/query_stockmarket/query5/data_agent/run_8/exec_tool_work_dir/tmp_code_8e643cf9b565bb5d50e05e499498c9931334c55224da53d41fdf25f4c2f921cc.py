code = """import json

# Load valid symbols
with open(locals()['var_function-call-11588894222788545089'], 'r') as f:
    data = json.load(f)
    valid_symbols = data['valid_symbols']

# Construct query
subqueries = []
for sym in valid_symbols:
    # Use double quotes for table names just in case, though they seem uppercase alphanumeric.
    # Condition: range > 20% of low price => (High - Low) > 0.2 * Low
    subqueries.append(f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)")

full_query = " UNION ALL ".join(subqueries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-2176412617243161922': 'file_storage/function-call-2176412617243161922.json', 'var_function-call-11082574715617122511': 'file_storage/function-call-11082574715617122511.json', 'var_function-call-11588894222788545089': 'file_storage/function-call-11588894222788545089.json'}

exec(code, env_args)
