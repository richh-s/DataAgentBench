code = """import json

with open(locals()['var_function-call-17712050282784208938'], 'r') as f:
    filenames = json.load(f)

query = json.dumps({"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}, "projection": {"filename": 1, "text": 1}})

print('__RESULT__:')
print(query)"""

env_args = {'var_function-call-13415103741321583316': 'file_storage/function-call-13415103741321583316.json', 'var_function-call-5959333085354367608': 'file_storage/function-call-5959333085354367608.json', 'var_function-call-12908803423484203231': 'file_storage/function-call-12908803423484203231.json', 'var_function-call-17712050282784208938': 'file_storage/function-call-17712050282784208938.json'}

exec(code, env_args)
