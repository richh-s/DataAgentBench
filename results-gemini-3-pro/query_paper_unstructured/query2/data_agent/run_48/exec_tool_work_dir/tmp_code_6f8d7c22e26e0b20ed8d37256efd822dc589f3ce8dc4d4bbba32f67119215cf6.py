code = """import json

# Read the citation results from the previous tool call
with open('var_function-call-2553281828849054275', 'r') as f:
    citations_data = json.load(f)

print(f"Total citation records: {len(citations_data)}")
print("__RESULT__:")
print(json.dumps(len(citations_data)))"""

env_args = {'var_function-call-2553281828849054275': 'file_storage/function-call-2553281828849054275.json'}

exec(code, env_args)
