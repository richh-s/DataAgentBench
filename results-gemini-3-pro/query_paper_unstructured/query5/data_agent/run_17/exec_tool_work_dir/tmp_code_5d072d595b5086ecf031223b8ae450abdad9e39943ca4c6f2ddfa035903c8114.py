code = """import json

# Load the citation data
with open('var_function-call-1858146419099260835', 'r') as f:
    citations = json.load(f)

print(f"Total citation records: {len(citations)}")
filenames = [c['title'] + ".txt" for c in citations]
print(f"First 5 filenames: {filenames[:5]}")

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json'}

exec(code, env_args)
