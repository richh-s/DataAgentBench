code = """import json

# Load papers
with open(locals()['var_function-call-17448438011554741318'], 'r') as f:
    papers_list = json.load(f)

filenames = [p['filename'] for p in papers_list]
unique_filenames = set(filenames)

print("__RESULT__:")
print(json.dumps(len(filenames) == len(unique_filenames)))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8, 'var_function-call-3893205258143355360': 0, 'var_function-call-9991689489332659929': True}

exec(code, env_args)
