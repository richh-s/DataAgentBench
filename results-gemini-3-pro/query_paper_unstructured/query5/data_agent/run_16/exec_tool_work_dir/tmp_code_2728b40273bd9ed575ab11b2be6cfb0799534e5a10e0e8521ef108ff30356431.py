code = """import json

# Load the SQLite result
with open('var_function-call-7498192109235549923.json', 'r') as f:
    citations = json.load(f)

print(f"Total citation records in 2020: {len(citations)}")
print(f"Sample titles: {[c['title'] for c in citations[:5]]}")
print("__RESULT__:")
print(json.dumps([c['title'] for c in citations]))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json'}

exec(code, env_args)
