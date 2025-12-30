code = """import json

# Read citations
file_path = locals()['var_function-call-16511466985029168842']
with open(file_path, 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

# Split into 2 batches
batch1 = filenames[:100]
batch2 = filenames[100:]

query1 = {"collection": "paper_docs", "filter": {"filename": {"$in": batch1}}}
query2 = {"collection": "paper_docs", "filter": {"filename": {"$in": batch2}}}

print("__RESULT__:")
print(json.dumps([query1, query2]))"""

env_args = {'var_function-call-16511466985029168842': 'file_storage/function-call-16511466985029168842.json', 'var_function-call-15099835547672752747': 188, 'var_function-call-5147540656333355159': 'file_storage/function-call-5147540656333355159.json', 'var_function-call-9629483487568902526': 'file_storage/function-call-9629483487568902526.json', 'var_function-call-14190453142206389286': 'file_storage/function-call-14190453142206389286.json', 'var_function-call-435985432642912850': 'file_storage/function-call-435985432642912850.json'}

exec(code, env_args)
