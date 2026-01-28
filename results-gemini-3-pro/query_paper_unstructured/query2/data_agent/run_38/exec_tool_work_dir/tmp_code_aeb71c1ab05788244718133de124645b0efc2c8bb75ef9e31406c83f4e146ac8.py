code = """import json

with open(locals()['var_function-call-4481896084510856696'], 'r') as f:
    citations = json.load(f)

print(f"Total citations in 2018: {len(citations)}")
print(f"First 5 titles: {[c['title'] for c in citations[:5]]}")

# Prepare titles for querying
titles = [c['title'] for c in citations]
# Check for duplicates?
titles = list(set(titles))
print(f"Unique titles: {len(titles)}")

print("__RESULT__:")
print(json.dumps({"count": len(citations), "unique_titles": len(titles)}))"""

env_args = {'var_function-call-4481896084510856696': 'file_storage/function-call-4481896084510856696.json', 'var_function-call-12106380733343301840': 'file_storage/function-call-12106380733343301840.json'}

exec(code, env_args)
