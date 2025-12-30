code = """import json

# Load the citations result
with open(locals()['var_function-call-2106421940036629061'], 'r') as f:
    citations_data = json.load(f)

# Extract titles and create filenames
titles = [record['title'] for record in citations_data]
filenames = [t + ".txt" for t in titles]

print(f"Total citations records: {len(citations_data)}")
print(f"First 5 filenames: {filenames[:5]}")

print("__RESULT__:")
print(json.dumps({"count": len(citations_data), "filenames_preview": filenames[:5]}))"""

env_args = {'var_function-call-2106421940036629061': 'file_storage/function-call-2106421940036629061.json'}

exec(code, env_args)
