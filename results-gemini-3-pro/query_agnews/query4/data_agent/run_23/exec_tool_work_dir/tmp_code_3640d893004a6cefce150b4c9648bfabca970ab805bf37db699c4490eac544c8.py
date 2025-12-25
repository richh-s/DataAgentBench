code = """import json

with open(locals()['var_function-call-1204321392425640290'], 'r') as f:
    metadata_rows = json.load(f)

article_ids = [int(row['article_id']) for row in metadata_rows]

# construct the mongo query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": article_ids}
    },
    "projection": {
        "_id": 0,
        "article_id": 1,
        "title": 1,
        "description": 1
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-1204321392425640290': 'file_storage/function-call-1204321392425640290.json', 'var_function-call-9833869308924201688': 6696}

exec(code, env_args)
