code = """import json

# Load the SQL result
with open(locals()['var_function-call-7467905940371766253'], 'r') as f:
    sql_data = json.load(f)

# Count
count = len(sql_data)
ids = [int(item['article_id']) for item in sql_data]

print("__RESULT__:")
print(json.dumps({"count": count, "sample_ids": ids[:10]}))"""

env_args = {'var_function-call-7467905940371766253': 'file_storage/function-call-7467905940371766253.json'}

exec(code, env_args)
