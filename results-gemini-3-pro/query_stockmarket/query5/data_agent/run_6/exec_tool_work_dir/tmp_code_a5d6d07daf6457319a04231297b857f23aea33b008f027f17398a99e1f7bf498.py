code = """import json

# Load symbols
path1 = locals()['var_function-call-13664371360467966876']
with open(path1, 'r') as f:
    stock_data = json.load(f)
target_symbols = set(item['Symbol'] for item in stock_data)

# Load tables
path2 = locals()['var_function-call-9828464466004639384']
with open(path2, 'r') as f:
    tables = json.load(f)
tables = set(tables)

# Intersect
valid_symbols = sorted(list(target_symbols.intersection(tables)))

# Build query
subqueries = []
for sym in valid_symbols:
    # Construct query part
    q = "SELECT '{}' AS Symbol, COUNT(*) AS Count FROM \"{}\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)".format(sym, sym)
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries) + " ORDER BY Count DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-277767683765402362': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}], 'var_function-call-13664371360467966876': 'file_storage/function-call-13664371360467966876.json', 'var_function-call-2894604771842111862': 86, 'var_function-call-9828464466004639384': 'file_storage/function-call-9828464466004639384.json', 'var_function-call-9364308099402691955': [{'Date': '2018-08-15'}]}

exec(code, env_args)
