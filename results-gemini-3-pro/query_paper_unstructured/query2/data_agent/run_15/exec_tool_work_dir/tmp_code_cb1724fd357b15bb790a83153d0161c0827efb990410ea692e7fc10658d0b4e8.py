code = """import json

# Get the file path for the SQLite result (from step 1)
file_path = locals()['var_function-call-974393757557094033']

with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Extract titles and create filenames
titles = [item['title'] for item in citations_data]
filenames = [t + ".txt" for t in titles]

# Create the Mongo query
mongo_query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-974393757557094033': 'file_storage/function-call-974393757557094033.json', 'var_function-call-2257219218276061774': 'file_storage/function-call-2257219218276061774.json', 'var_function-call-16565743143175934457': {'collection': 'paper_docs', 'filter': {'filename': {'$in': []}}, 'projection': {'filename': 1, 'text': 1}}}

exec(code, env_args)
