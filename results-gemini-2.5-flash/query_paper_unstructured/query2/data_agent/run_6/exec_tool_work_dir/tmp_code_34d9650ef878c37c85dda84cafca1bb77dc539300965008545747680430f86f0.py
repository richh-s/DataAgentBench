code = """import json

with open(locals()['var_function-call-6202588959387934265'], 'r') as f:
    filenames = json.load(f)

# Construct the MongoDB query string directly with the list of filenames
mongo_query = {"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}, "projection": {"filename": 1, "text": 1, "_id": 0}}
print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-15841017489305148665': 'file_storage/function-call-15841017489305148665.json', 'var_function-call-13643055400716781753': 'file_storage/function-call-13643055400716781753.json', 'var_function-call-6202588959387934265': 'file_storage/function-call-6202588959387934265.json'}

exec(code, env_args)
