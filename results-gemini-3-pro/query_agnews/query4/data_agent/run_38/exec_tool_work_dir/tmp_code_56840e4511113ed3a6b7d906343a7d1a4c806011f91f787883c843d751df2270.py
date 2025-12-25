code = """import json

file_path = locals()['var_function-call-663649913820504999']
with open(file_path, 'r') as f:
    article_ids = json.load(f)

# Construct the Mongo query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": article_ids}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-5438198083873646081': 'file_storage/function-call-5438198083873646081.json', 'var_function-call-663649913820504999': 'file_storage/function-call-663649913820504999.json'}

exec(code, env_args)
