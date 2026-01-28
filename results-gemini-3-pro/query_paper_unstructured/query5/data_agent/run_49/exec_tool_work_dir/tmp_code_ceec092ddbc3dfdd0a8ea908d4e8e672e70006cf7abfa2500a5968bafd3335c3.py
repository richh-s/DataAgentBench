code = """import json

# Load the SQLite result
with open(locals()['var_function-call-6443066931320893183'], 'r') as f:
    citations_data = json.load(f)

# Extract titles and prepare filenames
titles = [record['title'] for record in citations_data]
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-6443066931320893183': 'file_storage/function-call-6443066931320893183.json'}

exec(code, env_args)
