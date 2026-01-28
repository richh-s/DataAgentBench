code = """import json

# Read the complete MongoDB query result from the .json file file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    docs = json.load(f)

print("Total documents:", len(docs))
print("First document keys:", list(docs[0].keys()) if docs else "No documents")
print("Sample document preview:")
if docs:
    import pprint
    pprint.pprint(docs[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
