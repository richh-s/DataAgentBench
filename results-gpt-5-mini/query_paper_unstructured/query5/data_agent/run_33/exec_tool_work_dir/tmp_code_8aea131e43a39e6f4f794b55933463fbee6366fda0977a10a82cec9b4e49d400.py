code = """import json
# Read the citations query result stored in var_call_clUmDxoXhXkk75ik6VU6Rg6E (a file path)
with open(var_call_clUmDxoXhXkk75ik6VU6Rg6E, 'r') as f:
    citations = json.load(f)

# Build list of filenames corresponding to paper_docs filenames (title + '.txt')
filenames = [rec['title'] + '.txt' for rec in citations]

# Output the list as a JSON string per required print format
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_clUmDxoXhXkk75ik6VU6Rg6E': 'file_storage/call_clUmDxoXhXkk75ik6VU6Rg6E.json'}

exec(code, env_args)
