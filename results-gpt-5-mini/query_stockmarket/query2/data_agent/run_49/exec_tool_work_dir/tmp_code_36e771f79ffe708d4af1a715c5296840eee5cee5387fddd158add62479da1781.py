code = """import json
with open(var_call_n7eyBtU9JJA5p4IL6Klc9EyV, 'r') as f:
    data = json.load(f)
symbols = data['symbols_to_check']

chunk_size = 200
sql_list = []
for i in range(0, len(symbols), chunk_size):
    chunk = symbols[i:i+chunk_size]
    parts = []
    for s in chunk:
        # use double quotes around table and column names
        parts.append('SELECT "' + s + '" AS Symbol, Date, "Adj Close" FROM "' + s + '" WHERE Date >= \"2015-01-01\" AND Date <= \"2015-12-31\" AND "Adj Close" > 200')
    sql = ' UNION ALL '.join(parts) + ' ORDER BY Symbol, Date;'
    sql_list.append(sql)

output = {'sql_list_count': len(sql_list), 'sql_list_sample_first_len': len(sql_list[0]) if sql_list else 0}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_RWOznzhcAB1bqpucDN0isQ8n': 'file_storage/call_RWOznzhcAB1bqpucDN0isQ8n.json', 'var_call_J6gHfxFPYsOEKD6kPD74HU0X': 'file_storage/call_J6gHfxFPYsOEKD6kPD74HU0X.json', 'var_call_n7eyBtU9JJA5p4IL6Klc9EyV': 'file_storage/call_n7eyBtU9JJA5p4IL6Klc9EyV.json'}

exec(code, env_args)
