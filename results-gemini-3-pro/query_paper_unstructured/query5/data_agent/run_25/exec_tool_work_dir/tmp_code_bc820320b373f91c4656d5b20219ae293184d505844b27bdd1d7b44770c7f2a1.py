code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-6526070241227956252']

with open(file_path, 'r') as f:
    filenames = json.load(f)

# Take first 60
batch1 = filenames[:60]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": batch1}
    },
    "projection": {
        "filename": 1,
        "text": {"$substrCP": ["$text", 0, 3000]} 
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3704779829923578766': 'file_storage/function-call-3704779829923578766.json', 'var_function-call-4076760790261236942': 'file_storage/function-call-4076760790261236942.json', 'var_function-call-6526070241227956252': 'file_storage/function-call-6526070241227956252.json', 'var_function-call-3965175082720306182': 'file_storage/function-call-3965175082720306182.json'}

exec(code, env_args)
