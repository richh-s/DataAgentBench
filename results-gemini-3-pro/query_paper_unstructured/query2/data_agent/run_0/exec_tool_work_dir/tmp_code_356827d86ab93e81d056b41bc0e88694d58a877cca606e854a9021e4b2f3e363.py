code = """import json

with open(locals()['var_function-call-2762186927541110364'], 'r') as f:
    citations_data = json.load(f)

titles = [item['title'] for item in citations_data]
filenames = [t + ".txt" for t in titles]

# Construct MongoDB query
query = {"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2762186927541110364': 'file_storage/function-call-2762186927541110364.json', 'var_function-call-633366278914912942': 'file_storage/function-call-633366278914912942.json', 'var_function-call-4289778566380079256': {'citations_count': 158, 'papers_count': 5}}

exec(code, env_args)
