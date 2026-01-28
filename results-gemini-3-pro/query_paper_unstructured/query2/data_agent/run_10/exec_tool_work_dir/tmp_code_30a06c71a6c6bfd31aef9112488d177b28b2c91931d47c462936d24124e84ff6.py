code = """import json
import os

# Load the SQLite result
with open(locals()['var_function-call-16389443028975404888'], 'r') as f:
    citations = json.load(f)

# Extract titles
titles = [r['title'] for r in citations]
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-16389443028975404888': 'file_storage/function-call-16389443028975404888.json'}

exec(code, env_args)
