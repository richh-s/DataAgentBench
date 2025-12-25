code = """import json

# Load the result from the previous step
with open(locals()['var_function-call-7730568976014147704'], 'r') as f:
    metadata_records = json.load(f)

ids = [r['article_id'] for r in metadata_records]
print(f"Total articles: {len(ids)}")
print(f"First 10 IDs: {ids[:10]}")
print("__RESULT__:")
print(json.dumps({"count": len(ids), "ids": ids}))"""

env_args = {'var_function-call-7730568976014147704': 'file_storage/function-call-7730568976014147704.json'}

exec(code, env_args)
