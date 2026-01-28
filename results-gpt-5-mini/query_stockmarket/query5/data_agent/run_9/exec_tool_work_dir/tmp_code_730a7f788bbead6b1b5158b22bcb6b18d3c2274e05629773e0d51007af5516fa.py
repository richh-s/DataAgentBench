code = """import json
with open(var_call_ew9VLDirbm4RMvpPwbqpbkGx) as f:
    stockinfo = json.load(f)
with open(var_call_XHnP7G8F1ai6OXCc44J1pueW) as f:
    trade_tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)
symbols_in_both = [s for s in symbols if s in trade_set]

if not symbols_in_both:
    sql = "SELECT symbol, 0 as cnt FROM (SELECT NULL as symbol) t LIMIT 0;"
else:
    parts = []
    for s in symbols_in_both:
        part = "SELECT '{}' as symbol, \"Date\", \"High\", \"Low\" FROM \"{}\" WHERE \"Date\" LIKE '2019-%' AND \"High\" > 1.2 * \"Low\"".format(s, s)
        parts.append(part)
    unionsql = "\nUNION ALL\n".join(parts)
    sql = "SELECT symbol, COUNT(*) as cnt FROM (\n{}\n) t GROUP BY symbol ORDER BY cnt DESC LIMIT 5;".format(unionsql)

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_ew9VLDirbm4RMvpPwbqpbkGx': 'file_storage/call_ew9VLDirbm4RMvpPwbqpbkGx.json', 'var_call_XHnP7G8F1ai6OXCc44J1pueW': 'file_storage/call_XHnP7G8F1ai6OXCc44J1pueW.json'}

exec(code, env_args)
