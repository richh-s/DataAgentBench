code = """import json
# var_call_UlwTYnxK8aLPvZD04YhbL5xk is available in storage
data = json.load(open(var_call_UlwTYnxK8aLPvZD04YhbL5xk, 'r'))
symbols = [rec['Symbol'] for rec in data]

# To avoid overly long queries, we'll build unions in chunks of 200 symbols and combine with UNION ALL
parts = []
for s in symbols:
    # ensure double quotes around table name
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"{s}\""
    parts.append(part)

sql = '\nUNION ALL\n'.join(parts) + '\nORDER BY cnt DESC;'

# Output the SQL string as JSON
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_Ad4UsH2M8L6uC8cGxj7jUQRQ': 'file_storage/call_Ad4UsH2M8L6uC8cGxj7jUQRQ.json', 'var_call_SiXzvTbfmBNhOMQ5JDOIG3NS': 'file_storage/call_SiXzvTbfmBNhOMQ5JDOIG3NS.json', 'var_call_UlwTYnxK8aLPvZD04YhbL5xk': 'file_storage/call_UlwTYnxK8aLPvZD04YhbL5xk.json'}

exec(code, env_args)
