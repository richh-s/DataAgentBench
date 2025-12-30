code = """import json

# Load citations
with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations_list = json.load(f)

# Check for 0 citations
zeros = [c for c in citations_list if int(c['citation_count']) == 0]
print("__RESULT__:")
print(json.dumps(len(zeros)))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8}

exec(code, env_args)
