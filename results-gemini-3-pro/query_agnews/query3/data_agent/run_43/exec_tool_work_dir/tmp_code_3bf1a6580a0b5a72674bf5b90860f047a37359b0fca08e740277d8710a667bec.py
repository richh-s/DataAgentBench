code = """import json
import pandas as pd

with open(locals()['var_function-call-3374216410515213481'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
print(f"Count: {len(df)}")
print(f"IDs: {df['article_id'].head().tolist()}")
print(f"Max ID: {df['article_id'].max()}")
print("__RESULT__:")
print(json.dumps({"count": len(df), "sample_ids": df['article_id'].head().tolist()}))"""

env_args = {'var_function-call-3374216410515213481': 'file_storage/function-call-3374216410515213481.json'}

exec(code, env_args)
