code = """import json

with open(locals()['var_function-call-15718840696057436143'], 'r') as f:
    valid_symbols = json.load(f)

# valid_symbols has 1435 entries.
# Let's split into chunks of 400.
chunk_size = 400
queries = []

for i in range(0, len(valid_symbols), chunk_size):
    chunk = valid_symbols[i:i+chunk_size]
    sub_queries = []
    for sym in chunk:
        # Use double quotes for table name in case of special chars/reserved words (though symbols are usually safe)
        # Filter for 2015 and Price > 200
        q = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-4976631640626439833': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-10780135608603359427': 'file_storage/function-call-10780135608603359427.json', 'var_function-call-12146310968865699605': 'file_storage/function-call-12146310968865699605.json', 'var_function-call-15718840696057436143': 'file_storage/function-call-15718840696057436143.json', 'var_function-call-18247159550468154824': 1435}

exec(code, env_args)
