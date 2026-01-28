code = """import json
# Load the citation query result from the provided storage file path
with open(var_call_yEYd1i8bfORfLdhaGVD6Uj4J, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build list of filenames corresponding to titles (append .txt)
filenames = [rec['title'] + '.txt' for rec in citations]

# Print result in required format as a JSON string
import json
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_yEYd1i8bfORfLdhaGVD6Uj4J': 'file_storage/call_yEYd1i8bfORfLdhaGVD6Uj4J.json'}

exec(code, env_args)
