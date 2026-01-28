code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-3465492661884944588']

# Read the SQLite result
with open(file_path, 'r') as f:
    citations = json.load(f)

print(f"Total citations records: {len(citations)}")

# Prepare list of filenames
titles = [r['title'] for r in citations]
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps({"count": len(citations), "filenames_preview": filenames[:5]}))"""

env_args = {'var_function-call-3465492661884944588': 'file_storage/function-call-3465492661884944588.json', 'var_function-call-5093555136357275627': 'file_storage/function-call-5093555136357275627.json'}

exec(code, env_args)
