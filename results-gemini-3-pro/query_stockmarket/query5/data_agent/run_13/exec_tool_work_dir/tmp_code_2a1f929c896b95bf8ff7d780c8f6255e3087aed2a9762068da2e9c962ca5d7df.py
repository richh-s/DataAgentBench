code = """import json

# Get file path
file_path_result = locals()['var_function-call-11004709737379666324']

# Load data
with open(file_path_result, 'r') as f:
    data = json.load(f)

symbols = data['symbols']

# Construct query
subqueries = []
for sym in symbols:
    # Ensure symbol is safe (alphanumeric), though they usually are.
    # Also wrap table name in double quotes if needed, but standard SQL usually fine.
    # DuckDB is case insensitive for table names usually, but these are specific tables.
    # The prompt says table names are the ticker symbol.
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > 0.20 * Low"
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries)
final_query = f"SELECT Symbol, Days FROM ({final_query}) ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-7798081154467211843': 'file_storage/function-call-7798081154467211843.json', 'var_function-call-7798081154467211922': 'file_storage/function-call-7798081154467211922.json', 'var_function-call-11004709737379666324': 'file_storage/function-call-11004709737379666324.json'}

exec(code, env_args)
