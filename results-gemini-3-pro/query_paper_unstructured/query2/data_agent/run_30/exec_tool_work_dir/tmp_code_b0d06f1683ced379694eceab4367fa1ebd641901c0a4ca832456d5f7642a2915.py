code = """import json

file_path = locals()['var_function-call-3647625760159840601']
with open(file_path, 'r') as f:
    citations_data = json.load(f)

filenames = [item['title'] + ".txt" for item in citations_data]
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158}

exec(code, env_args)
