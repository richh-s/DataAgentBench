code = """import json

with open(locals()['var_function-call-5345887261916225138'], 'r') as f:
    target_stocks = json.load(f)

# Limit to chunks if necessary, but 234 should fit in one large query string (approx 234 * 150 chars = 35KB).
# DuckDB should handle this fine.

queries = []
for stock in target_stocks:
    sym = stock['Symbol']
    # Use double quotes for table names in case of reserved words or special chars
    # Although symbols usually are fine, safety first.
    q = f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date LIKE '2017%'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-6147490569046073636': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-505177984360171283': 'file_storage/function-call-505177984360171283.json', 'var_function-call-13180068455188980204': 'file_storage/function-call-13180068455188980204.json', 'var_function-call-5345887261916225138': 'file_storage/function-call-5345887261916225138.json', 'var_function-call-4829142318152718752': 234}

exec(code, env_args)
