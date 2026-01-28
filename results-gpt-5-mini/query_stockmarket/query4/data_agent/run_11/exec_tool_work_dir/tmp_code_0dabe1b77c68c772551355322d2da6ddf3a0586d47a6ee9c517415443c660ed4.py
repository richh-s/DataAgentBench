code = """import json
# Load the previous execute_python result which contains symbols and company_map
with open(var_call_hB51LNj4HBIPXgHh9EP2EY5p, 'r') as f:
    data = json.load(f)
symbols = data['symbols']

# Build the SQL union query for DuckDB (stocktrade_database)
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down FROM \"{s}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    parts.append(part)

union_sql = "\nUNION ALL\n".join(parts)
final_sql = f"SELECT symbol, up, down FROM (\n{union_sql}\n) t ORDER BY up DESC, (up-down) DESC;"

output = {"sql": final_sql}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HGxGds5f8SCXsL6NTr9BiGCQ': 'file_storage/call_HGxGds5f8SCXsL6NTr9BiGCQ.json', 'var_call_v1NFBApJOAiRiTEJJ90yq5aL': 'file_storage/call_v1NFBApJOAiRiTEJJ90yq5aL.json', 'var_call_hB51LNj4HBIPXgHh9EP2EY5p': 'file_storage/call_hB51LNj4HBIPXgHh9EP2EY5p.json'}

exec(code, env_args)
