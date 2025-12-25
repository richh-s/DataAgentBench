code = """import json

# Find the key
key = [k for k in locals().keys() if '14292262882502578030' in k][0]

with open(locals()[key], 'r') as f:
    relevant_symbols = json.load(f)

# Construct SQL query
subqueries = []
for sym in relevant_symbols:
    # Use " around table name, ' around string literal
    subqueries.append(f"SELECT '{sym}' as Symbol, MAX(\"Adj Close\") as MaxPrice FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX(\"Adj Close\") > 200")

full_query = " UNION ALL ".join(subqueries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-3254348820866010282': ['stockinfo'], 'var_function-call-11353124838619122226': [{'Listing Exchange': 'P', 'ETF': 'Y'}, {'Listing Exchange': 'Q', 'ETF': 'N'}, {'Listing Exchange': 'Q', 'ETF': 'Y'}, {'Listing Exchange': 'Z', 'ETF': 'Y'}, {'Listing Exchange': 'A', 'ETF': 'N'}, {'Listing Exchange': 'N', 'ETF': 'N'}, {'Listing Exchange': 'Z', 'ETF': 'N'}, {'Listing Exchange': 'P', 'ETF': 'N'}, {'Listing Exchange': 'A', 'ETF': 'Y'}], 'var_function-call-16699873059185475533': 'file_storage/function-call-16699873059185475533.json', 'var_function-call-2578122726742308737': 'file_storage/function-call-2578122726742308737.json', 'var_function-call-14292262882502578030': 'file_storage/function-call-14292262882502578030.json'}

exec(code, env_args)
