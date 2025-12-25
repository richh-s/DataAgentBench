code = """import json

# Load the result from stockinfo_database (list of dicts)
with open('var_function-call-11805765579617057108.json', 'r') as f:
    stockinfo_data = json.load(f)

etf_symbols = set(item['Symbol'] for item in stockinfo_data)

# Load the result from stocktrade_database (list of strings)
with open('var_function-call-18208316545680584426.json', 'r') as f:
    table_names = json.load(f)

available_tables = set(table_names)

# Intersection
valid_symbols = list(etf_symbols.intersection(available_tables))
valid_symbols.sort()

print(f"Total ETFs on NYSE Arca: {len(etf_symbols)}")
print(f"Valid Tables found: {len(valid_symbols)}")

# Generate SQL query
# I want to find symbols where Adj Close > 200 in 2015.
# Query structure:
# SELECT 'SYM' as Symbol FROM SYM WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1
# UNION ALL ...

queries = []
for sym in valid_symbols:
    q = f"""SELECT '{sym}' as Symbol FROM "{sym}" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1"""
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps({"valid_symbols_count": len(valid_symbols), "query": final_query}))"""

env_args = {'var_function-call-11805765579617057108': 'file_storage/function-call-11805765579617057108.json', 'var_function-call-18208316545680584426': 'file_storage/function-call-18208316545680584426.json'}

exec(code, env_args)
