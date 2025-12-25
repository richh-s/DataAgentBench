code = """import json
import os

# Load ETF list
with open(locals()['var_function-call-17981552509113141854'], 'r') as f:
    etf_list = json.load(f)

# Load Table list
with open(locals()['var_function-call-3218142005520764474'], 'r') as f:
    table_list = json.load(f)
table_set = set(table_list)

# Filter ETFs
relevant_etfs = [x for x in etf_list if x['Symbol'] in table_set]

print(f"Total ETFs in DB: {len(etf_list)}")
print(f"Relevant ETFs (with tables): {len(relevant_etfs)}")

# Generate the query string to check length
# Query structure: SELECT 'SYM' FROM SYM WHERE "Adj Close" > 200 AND Date BETWEEN '2015-01-01' AND '2015-12-31' LIMIT 1 UNION ALL ...
# Approx length per symbol: ~120 chars
# Total length: 120 * count
print(f"Estimated query length: {120 * len(relevant_etfs)}")

# Let's see the first few symbols
print(f"Sample symbols: {[x['Symbol'] for x in relevant_etfs[:5]]}")

print("__RESULT__:")
print(json.dumps({"count": len(relevant_etfs)}))"""

env_args = {'var_function-call-5455133501503104484': ['stockinfo'], 'var_function-call-17981552509113141854': 'file_storage/function-call-17981552509113141854.json', 'var_function-call-3218142005520764474': 'file_storage/function-call-3218142005520764474.json'}

exec(code, env_args)
