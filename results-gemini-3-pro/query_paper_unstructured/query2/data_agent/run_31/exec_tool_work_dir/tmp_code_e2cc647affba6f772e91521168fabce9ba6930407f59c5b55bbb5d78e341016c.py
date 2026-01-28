code = """import json

# Read the SQL result
with open('var_function-call-17293997296042542905.json', 'r') as f:
    citations = json.load(f)

# Extract filenames (title + .txt)
# The database description says: "The paper title in the Citations SQLite table matches the filename (without .txt extension)"
filenames = [c['title'] + '.txt' for c in citations]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-17293997296042542905': 'file_storage/function-call-17293997296042542905.json'}

exec(code, env_args)
