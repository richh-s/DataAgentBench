code = """import json

path = locals()['var_function-call-8543336388924568308']
with open(path, 'r') as f:
    data = json.load(f)

valid_symbols = data['valid_symbols']

queries = []
for sym in valid_symbols:
    # Use .format to avoid quote hell
    # Table names in double quotes
    q = "SELECT '{}' as Symbol, COUNT(*) as HighRangeDays FROM \"{}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)".format(sym, sym)
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY HighRangeDays DESC LIMIT 5"

# Print the full query in the result so I can copy it
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-1914327577488087948': 'file_storage/function-call-1914327577488087948.json', 'var_function-call-546925876155124567': 'file_storage/function-call-546925876155124567.json', 'var_function-call-8543336388924568308': 'file_storage/function-call-8543336388924568308.json', 'var_function-call-18149381421604452659': 'file_storage/function-call-18149381421604452659.json'}

exec(code, env_args)
