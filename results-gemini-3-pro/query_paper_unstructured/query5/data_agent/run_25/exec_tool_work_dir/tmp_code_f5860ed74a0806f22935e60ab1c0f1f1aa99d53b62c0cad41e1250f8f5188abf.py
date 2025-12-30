code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-6526070241227956252']

with open(file_path, 'r') as f:
    filenames = json.load(f)

# Create the query dictionary
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {
        "filename": 1,
        "text": {"$substrCP": ["$text", 0, 5000]} # Get first 5000 chars
    }
}

# Print as JSON string
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3704779829923578766': 'file_storage/function-call-3704779829923578766.json', 'var_function-call-4076760790261236942': 'file_storage/function-call-4076760790261236942.json', 'var_function-call-6526070241227956252': 'file_storage/function-call-6526070241227956252.json'}

exec(code, env_args)
