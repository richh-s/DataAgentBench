code = """import json

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

# Print the first document's text to confirm file reading
if civic_docs:
    result = civic_docs[0]['text'][:500] # Get first 500 characters of the first document
else:
    result = "No documents found."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json'}

exec(code, env_args)
