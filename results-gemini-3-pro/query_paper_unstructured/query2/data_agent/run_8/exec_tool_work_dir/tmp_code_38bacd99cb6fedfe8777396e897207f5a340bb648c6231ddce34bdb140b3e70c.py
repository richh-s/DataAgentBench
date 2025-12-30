code = """import json

file_path = locals()['var_function-call-17666330447833607191']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Create a list of filenames
filenames = [c['title'] + ".txt" for c in citations]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-17666330447833607191': 'file_storage/function-call-17666330447833607191.json', 'var_function-call-11031819639720739797': 'file_storage/function-call-11031819639720739797.json', 'var_function-call-11580890549591616551': 158}

exec(code, env_args)
