code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-10128853651664279531']

# Load the SQLite result
with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Extract titles and create filenames
titles = [record['title'] for record in citations_data]
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-10128853651664279531': 'file_storage/function-call-10128853651664279531.json'}

exec(code, env_args)
