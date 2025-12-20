code = """import json

# Load the metadata results
with open(locals()['var_function-call-7590950680837321910'], 'r') as f:
    metadata = json.load(f)

# Extract IDs
all_ids = [int(r['article_id']) for r in metadata]
batch_ids = all_ids[0:600]

print("__RESULT__:")
print(json.dumps(batch_ids))"""

env_args = {'var_function-call-7590950680837321910': 'file_storage/function-call-7590950680837321910.json', 'var_function-call-5634683902169255579': 'file_storage/function-call-5634683902169255579.json'}

exec(code, env_args)
