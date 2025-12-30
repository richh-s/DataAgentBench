code = """import json

file_path = locals()['var_function-call-17290402157997289971']
with open(file_path, 'r') as f:
    paper_titles = json.load(f)

filenames = [title + '.txt' for title in paper_titles]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-15052837677645358985': 'file_storage/function-call-15052837677645358985.json', 'var_function-call-17290402157997289971': 'file_storage/function-call-17290402157997289971.json'}

exec(code, env_args)
