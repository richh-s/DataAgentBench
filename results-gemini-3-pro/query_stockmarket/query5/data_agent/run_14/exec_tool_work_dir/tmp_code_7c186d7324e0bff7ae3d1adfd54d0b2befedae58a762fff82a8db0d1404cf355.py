code = """import json

# Load the result from the previous step
path_tickers = locals()['var_function-call-12166660516732642610']

with open(path_tickers, 'r') as f:
    data = json.load(f)

tickers = data['tickers']

# Construct the SQL query
# "SELECT 'TICKER' as Symbol, COUNT(*) as Count FROM TICKER WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.2 * Low"
queries = []
for t in tickers:
    # Ensure ticker is safe (it's from the DB so it should be, but good to be careful with quotes)
    # DuckDB uses double quotes for identifiers
    q = f"SELECT '{t}' as Symbol, COUNT(*) as NumDays FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

final_query = " UNION ALL ".join(queries) + " ORDER BY NumDays DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-13634932259963143763': 'file_storage/function-call-13634932259963143763.json', 'var_function-call-13634932259963145996': 'file_storage/function-call-13634932259963145996.json', 'var_function-call-12166660516732642610': 'file_storage/function-call-12166660516732642610.json'}

exec(code, env_args)
