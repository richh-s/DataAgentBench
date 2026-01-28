code = """import json
with open(var_call_wcdrTGvraMvb3WJXAUedBSw6, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_count, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_count FROM \"{s}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'")
sql = "\nUNION ALL\n".join(parts)
sql = "SELECT symbol, up_count, down_count FROM (\n" + sql + "\n) AS all_counts WHERE up_count>down_count ORDER BY up_count DESC LIMIT 5;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_dXlfw7PBbNWvRB8DrF5zCYoo': 'file_storage/call_dXlfw7PBbNWvRB8DrF5zCYoo.json', 'var_call_7bDFcW723n8AK6WYWmUMLAlr': 'file_storage/call_7bDFcW723n8AK6WYWmUMLAlr.json', 'var_call_wcdrTGvraMvb3WJXAUedBSw6': 'file_storage/call_wcdrTGvraMvb3WJXAUedBSw6.json'}

exec(code, env_args)
