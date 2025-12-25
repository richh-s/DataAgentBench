code = """import json

# Get file paths from local variables
path_info = locals()['var_function-call-13405563423262500002']
path_tables = locals()['var_function-call-13405563423262501427']

# Load data
with open(path_info, 'r') as f:
    stock_info = json.load(f)

with open(path_tables, 'r') as f:
    tables = json.load(f)

info_symbols = {}
for item in stock_info:
    info_symbols[item['Symbol']] = item['Company Description']

table_set = set(tables)
valid_symbols = [s for s in info_symbols.keys() if s in table_set]

subqueries = []
for sym in valid_symbols:
    # Use format to be clean
    # "SELECT 'SYM' as Symbol, COUNT(*) as Days FROM "SYM" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    sq = "SELECT '{}' as Symbol, COUNT(*) as Days FROM \"{}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)".format(sym, sym)
    subqueries.append(sq)

final_query = " UNION ALL ".join(subqueries)
wrapper_query = "SELECT Symbol, Days FROM (" + final_query + ") ORDER BY Days DESC LIMIT 5"

# Prepare result
result_data = {
    "count": len(valid_symbols),
    "query": wrapper_query,
    "symbol_map": info_symbols
}

print("__RESULT__:")
print(json.dumps(result_data))"""

env_args = {'var_function-call-13405563423262500002': 'file_storage/function-call-13405563423262500002.json', 'var_function-call-13405563423262501427': 'file_storage/function-call-13405563423262501427.json', 'var_function-call-7452566899761960412': 'file_storage/function-call-7452566899761960412.json'}

exec(code, env_args)
