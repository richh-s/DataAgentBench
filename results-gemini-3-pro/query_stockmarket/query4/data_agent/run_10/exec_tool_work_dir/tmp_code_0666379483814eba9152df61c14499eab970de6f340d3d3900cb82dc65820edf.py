code = """import json

# Load candidate symbols from stockinfo result
with open(locals()['var_function-call-6393703521614786747'], 'r') as f:
    candidates = json.load(f)

candidate_symbols = set(c['Symbol'] for c in candidates)

# Load available tables
with open(locals()['var_function-call-14160190749123252694'], 'r') as f:
    tables = json.load(f)

available_tables = set(tables)

# Intersect
valid_symbols = list(candidate_symbols.intersection(available_tables))

# Construct SQL query
# To avoid too long query string, let's limit to top 5? No, I need to find the top 5 from ALL.
# I'll try to construct the full query.
queries = []
for sym in valid_symbols:
    q = f"""SELECT '{sym}' AS Symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) AS UpDays, SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) AS DownDays FROM "{sym}" WHERE "Date" >= '2017-01-01' AND "Date" <= '2017-12-31'"""
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print(f"Number of valid symbols: {len(valid_symbols)}")
print(f"Query length: {len(full_query)}")

# Check if query length is reasonable (e.g. < 100k chars).
# If it's too long, I might need to split it.
# 200 symbols * ~150 chars = 30k chars. Should be fine.

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-6393703521614786747': 'file_storage/function-call-6393703521614786747.json', 'var_function-call-17168036801476034566': 234, 'var_function-call-14160190749123252694': 'file_storage/function-call-14160190749123252694.json'}

exec(code, env_args)
