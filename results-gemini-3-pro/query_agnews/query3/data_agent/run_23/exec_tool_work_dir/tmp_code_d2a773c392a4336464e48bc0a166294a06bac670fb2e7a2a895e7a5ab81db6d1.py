code = """import json
import pandas as pd

# Load the SQL result
with open(locals()['var_function-call-18349184007638640037'], 'r') as f:
    sql_data = json.load(f)

ids = [int(item['article_id']) for item in sql_data]
print(f"Count: {len(ids)}")
print(f"Sample IDs: {ids[:5]}")
print("__RESULT__:")
print(json.dumps({"count": len(ids), "ids": ids}))"""

env_args = {'var_function-call-18349184007638640037': 'file_storage/function-call-18349184007638640037.json'}

exec(code, env_args)
