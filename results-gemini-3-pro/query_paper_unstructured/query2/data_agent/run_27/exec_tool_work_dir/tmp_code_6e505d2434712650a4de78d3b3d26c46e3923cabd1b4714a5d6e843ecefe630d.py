code = """import json

# Load citations data
with open(locals()['var_function-call-5470000503429213885'], 'r') as f:
    citations_data = json.load(f)

titles = [entry['title'] for entry in citations_data]
filenames = [t + ".txt" for t in titles]

print(f"Number of filenames: {len(filenames)}")

# Prepare the MongoDB query dictionary
mongo_query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

# Print the query string. 
# If it's too long, I'll see the preview and decide.
print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-5470000503429213885': 'file_storage/function-call-5470000503429213885.json', 'var_function-call-2990459940617742049': 'file_storage/function-call-2990459940617742049.json', 'var_function-call-6979605928025397528': 'file_storage/function-call-6979605928025397528.json'}

exec(code, env_args)
