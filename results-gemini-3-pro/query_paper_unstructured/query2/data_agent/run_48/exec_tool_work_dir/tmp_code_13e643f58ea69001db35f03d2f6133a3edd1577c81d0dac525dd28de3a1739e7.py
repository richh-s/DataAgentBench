code = """import json

# Load citations
citations_path = locals()['var_function-call-2553281828849054275']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Extract titles and append .txt
filenames = [c['title'] + ".txt" for c in citations]

# Construct query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2553281828849054275': 'file_storage/function-call-2553281828849054275.json', 'var_function-call-11306034102406453313': 158, 'var_function-call-12620038734802007538': 'file_storage/function-call-12620038734802007538.json', 'var_function-call-6192357641571030232': 5}

exec(code, env_args)
