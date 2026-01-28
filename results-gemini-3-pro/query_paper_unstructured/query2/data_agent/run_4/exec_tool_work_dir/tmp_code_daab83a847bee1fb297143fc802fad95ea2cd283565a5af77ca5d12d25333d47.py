code = """import json

# Load the citation results
with open('var_function-call-14649324199470214251.json', 'r') as f:
    citations = json.load(f)

titles = [r['title'] for r in citations]
print(f"Count: {len(titles)}")
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-14649324199470214251': 'file_storage/function-call-14649324199470214251.json'}

exec(code, env_args)
