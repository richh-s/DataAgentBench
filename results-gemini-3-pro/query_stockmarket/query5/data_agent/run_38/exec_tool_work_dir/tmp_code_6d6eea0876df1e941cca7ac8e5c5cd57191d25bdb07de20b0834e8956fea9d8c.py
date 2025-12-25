code = """import json

# Access the file path from the previous tool result
file_path = locals()['var_function-call-260576047833116338']

with open(file_path, 'r') as f:
    data = json.load(f)

matching_symbols = data['matching_symbols']
matching_symbols.sort()

# Construct the query
subqueries = []
for sym in matching_symbols:
    # Use double quotes for table names in SQL
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as DaysCount FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"
    subqueries.append(q)

full_query = " UNION ALL ".join(subqueries) + " ORDER BY DaysCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-403440647070611719': 'file_storage/function-call-403440647070611719.json', 'var_function-call-403440647070612544': 'file_storage/function-call-403440647070612544.json', 'var_function-call-260576047833116338': 'file_storage/function-call-260576047833116338.json'}

exec(code, env_args)
