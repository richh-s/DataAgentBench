code = """import json

# Load symbols from first step
with open(locals()['var_function-call-4042981255458067865'], 'r') as f:
    stocks = json.load(f)
candidate_map = {s['Symbol']: s['Company Description'] for s in stocks}

# Load tables from second step
with open(locals()['var_function-call-9311016875752490112'], 'r') as f:
    all_tables = json.load(f)

# Find intersection
valid_symbols = [s for s in candidate_map.keys() if s in all_tables]

# Construct query
# We want for each symbol: Symbol, UpDays, DownDays
# Up: Close > Open, Down: Close < Open
# Year: 2017
# Date format is usually 'YYYY-MM-DD', so we can use string comparison or LIKE '2017%'

queries = []
for sym in valid_symbols:
    # Need to handle potential issues with table names if they are reserved keywords or contain special chars?
    # The list_db output shows standard names mostly. I should quote them just in case.
    # DuckDB quoting is usually double quotes.
    q = f"""
    SELECT 
        '{sym}' as Symbol, 
        SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, 
        SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays 
    FROM "{sym}" 
    WHERE Date LIKE '2017%'
    """
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
# We'll print a JSON object with the query and the candidate_map (to map back to names later)
print(json.dumps({"query": full_query, "map": candidate_map, "valid_count": len(valid_symbols)}))"""

env_args = {'var_function-call-4042981255458067865': 'file_storage/function-call-4042981255458067865.json', 'var_function-call-10851517854372074132': 234, 'var_function-call-9311016875752490112': 'file_storage/function-call-9311016875752490112.json'}

exec(code, env_args)
