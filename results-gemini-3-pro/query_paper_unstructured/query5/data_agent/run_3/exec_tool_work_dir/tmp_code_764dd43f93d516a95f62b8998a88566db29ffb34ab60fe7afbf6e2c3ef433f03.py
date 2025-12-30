code = """import json

# Load citation data
with open('var_function-call-5680722423366516433', 'r') as f:
    citations = json.load(f)

print(f"Total citation records: {len(citations)}")
titles = set(c['title'] for c in citations)
print(f"Unique titles: {len(titles)}")
print("__RESULT__:")
print(len(titles))"""

env_args = {'var_function-call-5680722423366514432': ['Citations', 'sqlite_sequence'], 'var_function-call-5680722423366516433': 'file_storage/function-call-5680722423366516433.json', 'var_function-call-5680722423366514338': 'file_storage/function-call-5680722423366514338.json'}

exec(code, env_args)
