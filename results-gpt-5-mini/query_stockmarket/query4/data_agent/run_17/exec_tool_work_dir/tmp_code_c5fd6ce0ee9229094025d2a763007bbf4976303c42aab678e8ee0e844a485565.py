code = """import json
# Read the mapping file produced earlier
with open(var_call_CS6mbDQaTBWaHXltXPXrtA1x, 'r') as f:
    data = json.load(f)
symbols = data.get('symbols', [])
# We'll limit to symbols length >0
if not symbols:
    sql = ""
else:
    parts = []
    for s in symbols:
        # safe quoting of symbol as table name: double quotes
        part = f"SELECT '{s}' AS symbol, \"Open\", \"Close\" FROM \"{s}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
        parts.append(part)
    union = "\nUNION ALL\n".join(parts)
    sql = (
        "SELECT symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down_days "
        "FROM (\n" + union + "\n) AS all_data "
        "GROUP BY symbol "
        "HAVING SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) > SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) "
        "ORDER BY up_days DESC "
        "LIMIT 5;"
    )
# Print result in required format
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_bYQyMqrBbLBPnHo5oOIwzCIP': ['stockinfo'], 'var_call_Js61eKeKPd8pJkBCv55jt5nu': 'file_storage/call_Js61eKeKPd8pJkBCv55jt5nu.json', 'var_call_LbZzmGVobT3Mgm9lwFj5SNHc': 'file_storage/call_LbZzmGVobT3Mgm9lwFj5SNHc.json', 'var_call_CS6mbDQaTBWaHXltXPXrtA1x': 'file_storage/call_CS6mbDQaTBWaHXltXPXrtA1x.json'}

exec(code, env_args)
