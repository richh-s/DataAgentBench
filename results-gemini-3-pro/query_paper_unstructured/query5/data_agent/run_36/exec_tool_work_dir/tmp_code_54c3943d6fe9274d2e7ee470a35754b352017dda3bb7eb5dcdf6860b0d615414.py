code = """import json

papers_path = locals()['var_function-call-16274009200495380828']
with open(papers_path, 'r') as f:
    papers = json.load(f)

filenames = [p.get('filename') for p in papers[:10]]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json', 'var_function-call-13758046956340935094': 0, 'var_function-call-9966761655225880711': []}

exec(code, env_args)
