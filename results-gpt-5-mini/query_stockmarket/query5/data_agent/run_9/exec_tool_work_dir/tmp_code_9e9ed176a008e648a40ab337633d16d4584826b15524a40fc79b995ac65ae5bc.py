code = """import json
# Load previous tool results from storage paths
with open(var_call_ew9VLDirbm4RMvpPwbqpbkGx) as f:
    stockinfo = json.load(f)
with open(var_call_XHnP7G8F1ai6OXCc44J1pueW) as f:
    trade_tables = json.load(f)

# Get symbols from stockinfo where Market Category was S (query already filtered)
symbols = [rec['Symbol'] for rec in stockinfo]

# Intersect with available trade tables
trade_set = set(trade_tables)
symbols_in_both = [s for s in symbols if s in trade_set]

# Build a UNION ALL SQL selecting only 2019 days where High > 1.2 * Low
# Protect identifiers by double quotes
union_parts = []
for s in symbols_in_both:
    part = f"SELECT '{s}' as symbol, \"Date\", \"High\", \"Low\" FROM \"{s}\" WHERE \"Date\" LIKE '2019-%' AND \"High\" > 1.2 * \"Low\""
    union_parts.append(part)

if not union_parts:
    sql = "SELECT symbol, 0 as cnt FROM (SELECT NULL as symbol) t LIMIT 0;"
else:
    unionsql = "\nUNION ALL\n".join(union_parts)
    sql = f"SELECT symbol, COUNT(*) as cnt FROM (\n{unionsql}\n) t GROUP BY symbol ORDER BY cnt DESC LIMIT 5;"

# Print result in required format
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_ew9VLDirbm4RMvpPwbqpbkGx': 'file_storage/call_ew9VLDirbm4RMvpPwbqpbkGx.json', 'var_call_XHnP7G8F1ai6OXCc44J1pueW': 'file_storage/call_XHnP7G8F1ai6OXCc44J1pueW.json'}

exec(code, env_args)
