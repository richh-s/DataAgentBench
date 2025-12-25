code = """import json

with open(locals()['var_function-call-4648634188354399784'], 'r') as f:
    valid_symbols = json.load(f)

sqls = []
for item in valid_symbols:
    sym = item['Symbol']
    # Double quote table names to be safe, though usually not needed for simple tickers.
    # But some tickers might be reserved words.
    sql = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
    sqls.append(sql)

full_query = " UNION ALL ".join(sqls)
full_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-9914396351492829632': 'file_storage/function-call-9914396351492829632.json', 'var_function-call-9914396351492832197': 'file_storage/function-call-9914396351492832197.json', 'var_function-call-4648634188354399784': 'file_storage/function-call-4648634188354399784.json', 'var_function-call-10219029922974567872': 86}

exec(code, env_args)
