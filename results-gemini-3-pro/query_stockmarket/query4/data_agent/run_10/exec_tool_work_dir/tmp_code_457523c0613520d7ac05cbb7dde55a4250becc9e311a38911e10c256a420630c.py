code = """import json

# Load the result from the file
with open(locals()['var_function-call-6393703521614786747'], 'r') as f:
    data = json.load(f)

print(f"Total symbols: {len(data)}")

# Print the first few to check format
print(data[:5])

print("__RESULT__:")
print(json.dumps(len(data)))"""

env_args = {'var_function-call-6393703521614786747': 'file_storage/function-call-6393703521614786747.json'}

exec(code, env_args)
