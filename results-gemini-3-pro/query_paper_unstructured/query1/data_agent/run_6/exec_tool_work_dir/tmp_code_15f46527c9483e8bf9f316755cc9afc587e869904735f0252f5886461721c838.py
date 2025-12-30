code = """import json

with open(locals()['var_function-call-8026237664886157710'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
counts = []
for p in papers:
    c = p['text'].lower().count("food")
    if c > 0:
        counts.append((p['filename'], c))

counts.sort(key=lambda x: x[1], reverse=True)
print(json.dumps(counts[:20]))"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json', 'var_function-call-12216116696517767484': {'total_citations': 0, 'food_papers_count': 0, 'food_titles': []}, 'var_function-call-11714859170304537355': []}

exec(code, env_args)
