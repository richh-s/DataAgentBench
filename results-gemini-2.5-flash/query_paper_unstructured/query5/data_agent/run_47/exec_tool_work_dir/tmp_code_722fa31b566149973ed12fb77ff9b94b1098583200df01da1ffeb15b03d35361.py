code = """import json

with open(locals()['var_function-call-9418595005871324257'], 'r') as f:
    filenames = json.load(f)

mongo_query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames},
        "text": {"$regex": "venue: CHI"}
    },
    "projection": {"filename": 1}
}
print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-12640829769598757948': 'file_storage/function-call-12640829769598757948.json', 'var_function-call-18000874535248489367': 'file_storage/function-call-18000874535248489367.json', 'var_function-call-9418595005871324257': 'file_storage/function-call-9418595005871324257.json'}

exec(code, env_args)
