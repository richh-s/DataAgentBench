code = """import json

# Load stockinfo result
with open('var_function-call-13405563423262500002.json', 'r') as f:
    stock_info = json.load(f)

# Load stocktrade table list
with open('var_function-call-13405563423262501427.json', 'r') as f:
    tables = json.load(f)

# Extract symbols
info_symbols = {item['Symbol']: item['Company Description'] for item in stock_info}
table_set = set(tables)

# Intersect
valid_symbols = [s for s in info_symbols.keys() if s in table_set]

print(f"Total info symbols: {len(info_symbols)}")
print(f"Total tables: {len(table_set)}")
print(f"Matching symbols: {len(valid_symbols)}")

# Generate Query
# To avoid extremely long queries, let's see how many we have.
# If < 500, a UNION ALL query is likely fine.
# If > 500, we might need to batch or think of another way.

if len(valid_symbols) > 0:
    subqueries = []
    for sym in valid_symbols:
        # Wrap symbol in double quotes for table name to handle special chars if any (though usually simple)
        # But wait, table names in the list are strings.
        # Check if table names have special chars? The list showed "AAAU", etc.
        # Safest to double quote table name.
        sq = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
        subqueries.append(sq)
    
    full_query = " UNION ALL ".join(subqueries)
    final_query = f"SELECT Symbol, Days FROM ({full_query}) ORDER BY Days DESC LIMIT 5"
    
    print("__RESULT__:")
    print(json.dumps({"query": final_query, "count": len(valid_symbols), "symbol_map": info_symbols}))
else:
    print("__RESULT__:")
    print(json.dumps({"query": "", "count": 0}))"""

env_args = {'var_function-call-13405563423262500002': 'file_storage/function-call-13405563423262500002.json', 'var_function-call-13405563423262501427': 'file_storage/function-call-13405563423262501427.json'}

exec(code, env_args)
