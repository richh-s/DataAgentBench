code = """import json

with open(locals()['var_function-call-4042981255458067865'], 'r') as f:
    stocks = json.load(f)
candidate_map = {s['Symbol']: s['Company Description'] for s in stocks}

with open(locals()['var_function-call-9311016875752490112'], 'r') as f:
    all_tables = json.load(f)

valid_symbols = [s for s in candidate_map.keys() if s in all_tables]

queries = []
for sym in valid_symbols:
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date LIKE '2017%'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps({"query": full_query, "valid_count": len(valid_symbols)}))"""

env_args = {'var_function-call-4042981255458067865': 'file_storage/function-call-4042981255458067865.json', 'var_function-call-10851517854372074132': 234, 'var_function-call-9311016875752490112': 'file_storage/function-call-9311016875752490112.json'}

exec(code, env_args)
