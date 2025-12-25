code = """import json

# Load stockinfo result
with open('var_function-call-6994133641640717647.json', 'r') as f:
    stock_info = json.load(f)

# Load table list
with open('var_function-call-7500770919421141587.json', 'r') as f:
    table_list = json.load(f)

# Create set of table names for fast lookup
table_set = set(table_list)

# Filter symbols
valid_stocks = []
for item in stock_info:
    sym = item['Symbol']
    if sym in table_set:
        valid_stocks.append(item)

print(f"Total valid symbols: {len(valid_stocks)}")
print(f"First 5 valid symbols: {[s['Symbol'] for s in valid_stocks[:5]]}")

# Prepare the SQL query
# We want: SELECT 'SYM' as Symbol, COUNT(CASE WHEN Close > Open THEN 1 END) as Up, COUNT(CASE WHEN Close < Open THEN 1 END) as Down FROM "SYM" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'
# But 'Date' is a string in the description. Format is likely YYYY-MM-DD.

queries = []
for item in valid_stocks:
    sym = item['Symbol']
    # Escape double quotes in symbol if any (unlikely for ticker but good practice)
    # Actually table names are just the symbol. 
    # Check if symbol has special chars that need escaping.
    # For SQL, usually wrapping in double quotes is enough.
    
    q = f"""SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "{sym}" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"""
    queries.append(q)

full_query = " UNION ALL ".join(queries)

# Check length of query
print(f"Query length: {len(full_query)}")

# If query is too long, we might need to split. 
# Let's save the list of valid_stocks for later use to map back to names.
print("__RESULT__:")
print(json.dumps({"count": len(valid_stocks), "query_length": len(full_query), "valid_stocks": valid_stocks}))"""

env_args = {'var_function-call-13244064727740908215': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-6994133641640717647': 'file_storage/function-call-6994133641640717647.json', 'var_function-call-7500770919421141587': 'file_storage/function-call-7500770919421141587.json'}

exec(code, env_args)
