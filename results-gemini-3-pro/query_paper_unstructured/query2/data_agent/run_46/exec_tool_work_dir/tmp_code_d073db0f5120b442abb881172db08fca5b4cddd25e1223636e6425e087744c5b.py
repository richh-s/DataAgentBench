code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-4970464269223372421']

# Load the citations result
with open(file_path, 'r') as f:
    citations = json.load(f)

print(f"Total citations records: {len(citations)}")
# Create a map for easy lookup later: title -> citation_count
title_citation_map = {c['title']: c['citation_count'] for c in citations}
filenames = [t + ".txt" for t in title_citation_map.keys()]
print(f"Example filenames: {filenames[:5]}")

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-4970464269223372421': 'file_storage/function-call-4970464269223372421.json'}

exec(code, env_args)
