code = """import json

# Load symbols from step 1
with open(locals()['var_function-call-2084531363548133324'], 'r') as f:
    stock_data = json.load(f)
target_symbols = set([row['Symbol'] for row in stock_data])

# Load tables from step 2
with open(locals()['var_function-call-13796056807525861367'], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

# Intersect
valid_symbols = target_symbols.intersection(existing_tables)
valid_symbols = sorted(list(valid_symbols))

# Construct Query
subqueries = []
for sym in valid_symbols:
    # Use double quotes for table names to be safe
    # Condition: Date starts with 2019 (Assuming 'YYYY-MM-DD')
    # Condition: (High - Low) > 0.20 * Low
    q = f"""SELECT '{sym}' as Symbol, COUNT(*) as Days FROM "{sym}" WHERE Date LIKE '2019-%' AND (High - Low) > 0.20 * Low"""
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-2084531363548133324': 'file_storage/function-call-2084531363548133324.json', 'var_function-call-241126668365207331': {'count': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-13796056807525861367': 'file_storage/function-call-13796056807525861367.json'}

exec(code, env_args)
