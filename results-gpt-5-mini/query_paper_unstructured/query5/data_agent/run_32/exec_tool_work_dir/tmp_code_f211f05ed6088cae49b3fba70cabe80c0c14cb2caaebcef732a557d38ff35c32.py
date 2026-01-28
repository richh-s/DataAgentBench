code = """import json

# Load the citations query result file from storage
with open(var_call_Z3DAHvLOiNBp2rzBdZmAhv5Z, 'r') as f:
    citations = json.load(f)

# Extract titles and build corresponding filenames (title + .txt)
filenames = [rec['title'] + '.txt' for rec in citations]

# Print result in required format
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_Z3DAHvLOiNBp2rzBdZmAhv5Z': 'file_storage/call_Z3DAHvLOiNBp2rzBdZmAhv5Z.json'}

exec(code, env_args)
