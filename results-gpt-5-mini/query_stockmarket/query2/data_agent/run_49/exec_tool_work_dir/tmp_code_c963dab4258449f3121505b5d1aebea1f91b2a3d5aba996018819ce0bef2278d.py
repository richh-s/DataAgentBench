code = """import json
with open(var_call_n7eyBtU9JJA5p4IL6Klc9EyV, 'r') as f:
    data = json.load(f)
symbols = data['symbols_to_check']

sql_parts = []
for s in symbols:
    part = "SELECT '" + s + "' AS Symbol, Date, \"Adj Close\" FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200"
    sql_parts.append(part)

if sql_parts:
    full_sql = ' UNION ALL '.join(sql_parts) + ' ORDER BY Symbol, Date;'
else:
    full_sql = "SELECT NULL AS Symbol, NULL AS Date, NULL AS \"Adj Close\" WHERE FALSE;"

output = {'full_sql': full_sql}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_RWOznzhcAB1bqpucDN0isQ8n': 'file_storage/call_RWOznzhcAB1bqpucDN0isQ8n.json', 'var_call_J6gHfxFPYsOEKD6kPD74HU0X': 'file_storage/call_J6gHfxFPYsOEKD6kPD74HU0X.json', 'var_call_n7eyBtU9JJA5p4IL6Klc9EyV': 'file_storage/call_n7eyBtU9JJA5p4IL6Klc9EyV.json'}

exec(code, env_args)
