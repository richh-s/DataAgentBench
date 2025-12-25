code = """import json

with open(locals()['var_function-call-13078718259946536180'], 'r') as f:
    metadata_records = json.load(f)

# Extract IDs
article_ids = [int(r['article_id']) for r in metadata_records]

# I need to keep the mapping of article_id to region for later
id_to_region = {int(r['article_id']): r['region'] for r in metadata_records}

print("__RESULT__:")
print(json.dumps({"article_ids": article_ids, "id_to_region": id_to_region}))"""

env_args = {'var_function-call-13078718259946536180': 'file_storage/function-call-13078718259946536180.json'}

exec(code, env_args)
