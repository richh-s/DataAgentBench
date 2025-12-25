code = """import json

# Get file path from variable
file_path = locals()['var_function-call-9687647277801400069']

# Load the results
with open(file_path, 'r') as f:
    data = json.load(f)

target_symbols = data['target_symbols']

# Construct the query
# SELECT Symbol, COUNT(*) as Days FROM (
#   SELECT 'SYM' as Symbol, ...
# ) GROUP BY Symbol ORDER BY Days DESC LIMIT 5
# Or just UNION the counts directly.

parts = []
for sym in target_symbols:
    # Table names are the symbols. Best to quote them.
    # Condition: Date starts with 2019. (High - Low) > 0.2 * Low.
    # DuckDB/SQL syntax for Date string match: Date LIKE '2019%'
    part = f"""
    SELECT '{sym}' as Symbol, COUNT(*) as Days
    FROM "{sym}"
    WHERE "Date" LIKE '2019%' AND ("High" - "Low") > 0.2 * "Low"
    """
    parts.append(part)

full_query = " UNION ALL ".join(parts)
full_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json', 'var_function-call-9687647277801400069': 'file_storage/function-call-9687647277801400069.json'}

exec(code, env_args)
