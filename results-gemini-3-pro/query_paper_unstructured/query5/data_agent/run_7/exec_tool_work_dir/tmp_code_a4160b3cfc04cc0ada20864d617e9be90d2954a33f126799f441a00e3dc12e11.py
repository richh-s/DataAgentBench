code = """import json

citations_file = locals()['var_function-call-8931525846963248243']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# unique titles
titles = list(set([c['title'] for c in citations]))
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps({"count": len(titles), "filenames": filenames[:10]})) # Print only first 10 to check format, but I need to know the count."""

env_args = {'var_function-call-8931525846963248243': 'file_storage/function-call-8931525846963248243.json'}

exec(code, env_args)
