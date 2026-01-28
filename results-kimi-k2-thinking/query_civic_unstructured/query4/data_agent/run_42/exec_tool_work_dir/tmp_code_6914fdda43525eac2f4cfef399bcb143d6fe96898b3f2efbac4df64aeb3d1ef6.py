code = """# Access the MongoDB results from the variable
mongo_docs_res = var_functions.query_db:2

# Check type
print(f"Type: {type(mongo_docs_res)}")
print(f"Value: {mongo_docs_res}")

if isinstance(mongo_docs_res, str) and mongo_docs_res.endswith('.json'):
    # It's a file path, need to read it
    import json
    with open(mongo_docs_res, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_docs_res

print(f"Number of documents: {len(mongo_docs)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
