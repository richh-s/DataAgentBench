code = """import json

# Read the symbols
with open(locals()['var_function-call-18089665588996577560'], 'r') as f:
    valid_symbols = json.load(f)

# Create batches
batch_size = 500
batches = []
for i in range(0, len(valid_symbols), batch_size):
    batches.append(valid_symbols[i:i+batch_size])

queries = []
for batch in batches:
    subqueries = []
    for sym in batch:
        # Construct SQL part
        # We need to be careful with quotes. 
        # Query: SELECT 'SYM' as Symbol FROM "SYM" WHERE "Date" BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1
        sq = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        subqueries.append(sq)
    
    full_query = " UNION ALL ".join(subqueries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-7344486637286600100': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2454856655276099395': 'file_storage/function-call-2454856655276099395.json', 'var_function-call-6642693361376335155': 'file_storage/function-call-6642693361376335155.json', 'var_function-call-18089665588996577560': 'file_storage/function-call-18089665588996577560.json', 'var_function-call-8976669871907571712': 1435}

exec(code, env_args)
