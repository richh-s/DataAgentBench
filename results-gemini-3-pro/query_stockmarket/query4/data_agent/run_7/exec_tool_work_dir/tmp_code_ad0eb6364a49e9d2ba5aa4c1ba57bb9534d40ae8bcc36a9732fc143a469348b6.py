code = """import json

# Load stock info
with open(locals()['var_function-call-7866507991507907549'], 'r') as f:
    stock_info = json.load(f)

# Load trade tables
with open(locals()['var_function-call-10532225946016359418'], 'r') as f:
    trade_tables = json.load(f)

# Create a set of available tables
trade_table_set = set(trade_tables)

# Filter stock info
valid_stocks = []
for s in stock_info:
    sym = s['Symbol']
    if sym in trade_table_set:
        valid_stocks.append(s)

print(f"Total candidate stocks: {len(stock_info)}")
print(f"Stocks with trade data: {len(valid_stocks)}")

# If manageable, prepare the query
if len(valid_stocks) > 0:
    queries = []
    for s in valid_stocks:
        sym = s['Symbol']
        # Escape double quotes if necessary, though symbols are usually safe.
        # Enclose table name in double quotes just in case.
        q = f"""SELECT '{sym}' as Symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) as Down FROM "{sym}" WHERE "Date" >= '2017-01-01' AND "Date" <= '2017-12-31'"""
        queries.append(q)
    
    full_query = " UNION ALL ".join(queries)
    
    # Store full_query in a variable to print or save?
    # It might be very large. 
    # Let's print the length
    print(f"Query length: {len(full_query)}")
    
    # If length is < 100,000, I can probably run it.
    if len(full_query) < 200000:
        print("__RESULT__:")
        print(json.dumps(full_query))
    else:
        print("__RESULT__:")
        print(json.dumps("QUERY_TOO_LONG"))
else:
    print("__RESULT__:")
    print(json.dumps("NO_MATCHES"))"""

env_args = {'var_function-call-9385571556607626088': [{'Listing Exchange': 'P', 'ETF': 'Y'}, {'Listing Exchange': 'Q', 'ETF': 'N'}, {'Listing Exchange': 'Q', 'ETF': 'Y'}, {'Listing Exchange': 'Z', 'ETF': 'Y'}, {'Listing Exchange': 'A', 'ETF': 'N'}, {'Listing Exchange': 'N', 'ETF': 'N'}, {'Listing Exchange': 'Z', 'ETF': 'N'}, {'Listing Exchange': 'P', 'ETF': 'N'}, {'Listing Exchange': 'A', 'ETF': 'Y'}], 'var_function-call-7866507991507907549': 'file_storage/function-call-7866507991507907549.json', 'var_function-call-10532225946016359418': 'file_storage/function-call-10532225946016359418.json'}

exec(code, env_args)
