code = """import json
with open(var_call_RWOznzhcAB1bqpucDN0isQ8n, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_J6gHfxFPYsOEKD6kPD74HU0X, 'r') as f:
    tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
table_set = set(tables)
symbols_to_check = sorted([s for s in symbols if s in table_set])

sql_parts = []
for s in symbols_to_check:
    part = "SELECT '" + s + "' AS Symbol, Date, \"Adj Close\" FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200"
    sql_parts.append(part)

if sql_parts:
    full_sql = " UNION ALL ".join(sql_parts) + " ORDER BY Symbol, Date;"
else:
    full_sql = "SELECT NULL AS Symbol, NULL AS Date, NULL AS \"Adj Close\" WHERE FALSE;"

output = {'symbols_to_check_count': len(symbols_to_check), 'symbols_to_check_sample': symbols_to_check[:20], 'sql': full_sql}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_RWOznzhcAB1bqpucDN0isQ8n': 'file_storage/call_RWOznzhcAB1bqpucDN0isQ8n.json', 'var_call_J6gHfxFPYsOEKD6kPD74HU0X': 'file_storage/call_J6gHfxFPYsOEKD6kPD74HU0X.json'}

exec(code, env_args)
