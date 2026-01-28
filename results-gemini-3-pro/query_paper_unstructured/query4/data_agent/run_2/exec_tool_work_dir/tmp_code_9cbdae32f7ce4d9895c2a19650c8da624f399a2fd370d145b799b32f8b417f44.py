code = """import json

file_path = locals()['var_function-call-332077821725117771']
with open(file_path, 'r') as f:
    docs = json.load(f)

print("__RESULT__:")
if len(docs) > 0:
    print(json.dumps({"filename": docs[0]['filename'], "preview": docs[0]['text'][:1000]}))
else:
    print(json.dumps({"message": "No documents found in file."}))"""

env_args = {'var_function-call-13901959142060692971': 'file_storage/function-call-13901959142060692971.json', 'var_function-call-1843899810838592799': 'file_storage/function-call-1843899810838592799.json', 'var_function-call-332077821725117771': 'file_storage/function-call-332077821725117771.json', 'var_function-call-14032909272112886475': []}

exec(code, env_args)
