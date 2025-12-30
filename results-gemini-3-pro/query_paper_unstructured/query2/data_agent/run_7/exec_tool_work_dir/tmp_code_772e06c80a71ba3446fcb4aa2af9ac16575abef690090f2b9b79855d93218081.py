code = """import json

# Read the result from the previous tool call
with open('var_function-call-14272256085625645601.json', 'r') as f:
    citations_data = json.load(f)

# Extract titles
titles = [item['title'] for item in citations_data]
print(f"Total papers cited in 2018: {len(titles)}")

# Construct filenames for MongoDB query
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-14272256085625645601': 'file_storage/function-call-14272256085625645601.json'}

exec(code, env_args)
