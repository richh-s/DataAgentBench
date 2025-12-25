code = """import json

# Load symbols
with open(locals()['var_function-call-2084531363548133324'], 'r') as f:
    stock_data = json.load(f)
target_symbols = set([row['Symbol'] for row in stock_data])

# Load tables
with open(locals()['var_function-call-13796056807525861367'], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

# Intersect
valid_symbols = sorted(list(target_symbols.intersection(existing_tables)))

# Split into chunks of 30
chunk_size = 30
chunks = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

queries = []
q_quote = chr(39) # single quote
d_quote = chr(34) # double quote

for chunk in chunks:
    subqueries = []
    for sym in chunk:
        # Construct query using chr() to avoid syntax errors with quotes
        q = "SELECT " + q_quote + sym + q_quote + " as Symbol, COUNT(*) as Days FROM " + d_quote + sym + d_quote + " WHERE Date LIKE " + q_quote + "2019-%" + q_quote + " AND (High - Low) > 0.20 * Low"
        subqueries.append(q)
    full_q = " UNION ALL ".join(subqueries)
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-2084531363548133324': 'file_storage/function-call-2084531363548133324.json', 'var_function-call-241126668365207331': {'count': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-13796056807525861367': 'file_storage/function-call-13796056807525861367.json', 'var_function-call-10907591971367091177': 'file_storage/function-call-10907591971367091177.json', 'var_function-call-216696704061701173': 'file_storage/function-call-216696704061701173.json'}

exec(code, env_args)
