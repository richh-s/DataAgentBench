code = """import json

with open(locals()['var_function-call-18000874535248489367'], 'r') as f:
    paper_titles = json.load(f)

filenames = [title + '.txt' for title in paper_titles]
print('__RESULT__:')
print(json.dumps(filenames))"""

env_args = {'var_function-call-12640829769598757948': 'file_storage/function-call-12640829769598757948.json', 'var_function-call-18000874535248489367': 'file_storage/function-call-18000874535248489367.json'}

exec(code, env_args)
