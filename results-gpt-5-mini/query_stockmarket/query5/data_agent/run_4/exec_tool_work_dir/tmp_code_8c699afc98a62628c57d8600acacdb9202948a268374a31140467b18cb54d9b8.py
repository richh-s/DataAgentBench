code = """import json
with open(var_call_E5c2YY2Csym0kXhekfXRBlVX, 'r') as f:
    data = json.load(f)
symbols = [rec['Symbol'] for rec in data]

# Build UNION ALL selects
parts = []
for s in symbols:
    # Quote table and column names to be safe
    part = f"SELECT '{s}' AS symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    parts.append(part)

if not parts:
    sql = "SELECT NULL as symbol, 0 as cnt WHERE 1=0;"
else:
    unions = " UNION ALL ".join(parts)
    sql = f"SELECT symbol, cnt FROM ( {unions} ) AS t ORDER BY cnt DESC LIMIT 1000;"

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_wEEkxu0dysYgfB649IqQvJ1V': 'file_storage/call_wEEkxu0dysYgfB649IqQvJ1V.json', 'var_call_fNX066P2IyOjKzz9kLNIrdpe': 'file_storage/call_fNX066P2IyOjKzz9kLNIrdpe.json', 'var_call_E5c2YY2Csym0kXhekfXRBlVX': 'file_storage/call_E5c2YY2Csym0kXhekfXRBlVX.json'}

exec(code, env_args)
