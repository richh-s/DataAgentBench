code = """import json

# Load citations
with open(locals()['var_function-call-2409786745775470204'], 'r') as f:
    citations = json.load(f)

titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2409786745775470204': 'file_storage/function-call-2409786745775470204.json', 'var_function-call-12345480976137177995': 'file_storage/function-call-12345480976137177995.json', 'var_function-call-13418569887635270290': 'file_storage/function-call-13418569887635270290.json', 'var_function-call-6164372942284620757': {'citations_count': 158, 'papers_count': 5, 'matched_count': 2}}

exec(code, env_args)
