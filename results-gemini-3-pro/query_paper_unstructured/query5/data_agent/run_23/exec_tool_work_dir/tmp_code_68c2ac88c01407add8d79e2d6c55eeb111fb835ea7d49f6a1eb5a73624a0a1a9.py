code = """import json

# Load the filenames from the previous result
with open(locals()['var_function-call-5140237096160835583'], 'r') as f:
    data = json.load(f)
    filenames = data['filenames']

# Construct the Mongo query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-4239113770536719479': 'file_storage/function-call-4239113770536719479.json', 'var_function-call-5140237096160835583': 'file_storage/function-call-5140237096160835583.json'}

exec(code, env_args)
