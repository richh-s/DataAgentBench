code = """import json
# var_call_8UvW6KsMY3Sq7CHGXoSaQiC8 is available in storage
path = var_call_8UvW6KsMY3Sq7CHGXoSaQiC8
data = json.load(open(path, 'r'))
symbols = [rec['Symbol'] for rec in data]

# Build SQL to check max Adj Close in 2015 for each symbol
parts = []
for s in symbols:
    part = f"SELECT * FROM (SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') WHERE max_adj > 200"
    parts.append(part)

if parts:
    sql = "\nUNION ALL\n".join(parts)
else:
    sql = "SELECT NULL as symbol, NULL as max_adj WHERE 0=1"

import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json'}

exec(code, env_args)
