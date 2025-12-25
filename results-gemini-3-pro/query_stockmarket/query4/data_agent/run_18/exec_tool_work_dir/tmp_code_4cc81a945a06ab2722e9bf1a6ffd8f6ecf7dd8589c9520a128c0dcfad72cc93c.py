code = """import json

# Load symbols from stockinfo
with open(locals()['var_function-call-11613122979303732925'], 'r') as f:
    candidates = json.load(f)

# Load available tables
with open(locals()['var_function-call-9272637941847982752'], 'r') as f:
    tables = json.load(f)

# Create a set of available tables for O(1) lookup
tables_set = set(tables)

# Filter candidates
valid_candidates = []
for c in candidates:
    sym = c['Symbol']
    if sym in tables_set:
        valid_candidates.append(c)

print(f"Total candidates: {len(candidates)}")
print(f"Valid candidates (with tables): {len(valid_candidates)}")

# Generate SQL query
# To avoid huge query string issues or limits, let's see how many we have.
# If < 500, maybe one query is fine.

queries = []
for c in valid_candidates:
    sym = c['Symbol']
    # Use double quotes for table name in case of keywords or case sensitivity (DuckDB handles case usually but quotes are safer for mixed case if any)
    # The table names in list_db seem to be uppercase.
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

# Check length
print(f"Query length: {len(full_query)}")

# Store result to be used in next step
result = {
    "valid_candidates": valid_candidates,
    "full_query": full_query,
    "count": len(valid_candidates)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11613122979303732925': 'file_storage/function-call-11613122979303732925.json', 'var_function-call-9272637941847982752': 'file_storage/function-call-9272637941847982752.json'}

exec(code, env_args)
