code = """import json

file_path = locals()['var_function-call-7362815310734823686']
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

# Extract IDs and convert to int
article_ids = [int(r['article_id']) for r in metadata_records]

# Create Mongo query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": article_ids}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-7362815310734823686': 'file_storage/function-call-7362815310734823686.json', 'var_function-call-5837169514191744689': 14860}

exec(code, env_args)
