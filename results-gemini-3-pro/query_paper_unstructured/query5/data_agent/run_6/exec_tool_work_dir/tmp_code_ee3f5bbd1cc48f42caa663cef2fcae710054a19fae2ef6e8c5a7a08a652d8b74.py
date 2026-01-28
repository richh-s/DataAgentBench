code = """import json

with open(locals()['var_function-call-9485982252767693581'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

mongo_query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {"filename": 1, "text": 1} # Only need filename and text
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-9485982252767693581': 'file_storage/function-call-9485982252767693581.json', 'var_function-call-9485982252767692568': 'file_storage/function-call-9485982252767692568.json', 'var_function-call-2245160326568444986': 188}

exec(code, env_args)
