code = """import json

# Access the file paths from the variables
path_info = locals()['var_function-call-9978005257229487382']
path_tables = locals()['var_function-call-9978005257229485951']

# Load data
with open(path_info, 'r') as f:
    stock_info = json.load(f)

with open(path_tables, 'r') as f:
    tables = json.load(f)

table_set = set(tables)

# Filter symbols
valid_symbols = []
for item in stock_info:
    sym = item['Symbol']
    if sym in table_set:
        valid_symbols.append(sym)

# Construct SQL
# Using a loop to build the query parts
sqls = []
for sym in valid_symbols:
    # Construct the query for each symbol
    # "SELECT 'SYM' AS Symbol, COUNT(*) AS Days FROM "SYM" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    q = "SELECT '" + sym + "' AS Symbol, COUNT(*) AS Days FROM \"" + sym + "\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    sqls.append(q)

# Combine with UNION ALL
full_query = " UNION ALL ".join(sqls) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-9978005257229487382': 'file_storage/function-call-9978005257229487382.json', 'var_function-call-9978005257229485951': 'file_storage/function-call-9978005257229485951.json'}

exec(code, env_args)
