code = """import json

path = locals()['var_function-call-11859459418229751864']
with open(path, 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

# Split into 2 chunks
chunk_size = (len(filenames) + 1) // 2
chunks = [filenames[i:i + chunk_size] for i in range(0, len(filenames), chunk_size)]

queries = []
for chunk in chunks:
    q = {
        "collection": "paper_docs",
        "filter": {
            "filename": {"$in": chunk}
        }
    }
    queries.append(json.dumps(q))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-11859459418229751864': 'file_storage/function-call-11859459418229751864.json', 'var_function-call-11859459418229752705': 'file_storage/function-call-11859459418229752705.json', 'var_function-call-3949769233705587424': 188, 'var_function-call-16819266969204168891': 'file_storage/function-call-16819266969204168891.json', 'var_function-call-17188296458694660473': 'file_storage/function-call-17188296458694660473.json'}

exec(code, env_args)
