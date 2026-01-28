code = """import json

with open(locals()['var_function-call-16373116911178695907'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-16373116911178694920': ['Citations', 'sqlite_sequence'], 'var_function-call-16373116911178695907': 'file_storage/function-call-16373116911178695907.json', 'var_function-call-16373116911178696894': 'file_storage/function-call-16373116911178696894.json', 'var_function-call-13177130613489876308': 188, 'var_function-call-10911967024250333804': 'file_storage/function-call-10911967024250333804.json', 'var_function-call-9748881427492013847': 'file_storage/function-call-9748881427492013847.json', 'var_function-call-1936871565962322545': 'file_storage/function-call-1936871565962322545.json', 'var_function-call-18151132234637647575': {'citations_count': 188, 'paper_docs_count': 5}}

exec(code, env_args)
