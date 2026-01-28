code = """import json
# Load large results from previous tool calls
with open(var_call_YAmGc7SHT2zMzksFygYdnQRl, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_cDQEaKskDLs8TaPk1lEF91pz, 'r') as f:
    trade_tables = json.load(f)

# Build set of trade table names for quick lookup
trade_set = set(trade_tables)

# Filter stockinfo for symbols present in trade_set
symbols = []
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym in trade_set:
        symbols.append(sym)
        mapping[sym] = rec.get('Company Description')

# Build SQL by unioning counts for each symbol for year 2017
# Use CASE WHEN to count up and down days. Quote identifiers.
union_queries = []
for s in symbols:
    q = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE \"Date\" LIKE '2017-%'"
    union_queries.append(q)

full_sql = 'WITH counts AS (\n' + '\nUNION ALL\n'.join(union_queries) + '\n)\nSELECT symbol, up_days, down_days FROM counts WHERE up_days > down_days ORDER BY up_days DESC LIMIT 5;'

result = {'sql': full_sql, 'mapping': mapping}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YAmGc7SHT2zMzksFygYdnQRl': 'file_storage/call_YAmGc7SHT2zMzksFygYdnQRl.json', 'var_call_cDQEaKskDLs8TaPk1lEF91pz': 'file_storage/call_cDQEaKskDLs8TaPk1lEF91pz.json'}

exec(code, env_args)
