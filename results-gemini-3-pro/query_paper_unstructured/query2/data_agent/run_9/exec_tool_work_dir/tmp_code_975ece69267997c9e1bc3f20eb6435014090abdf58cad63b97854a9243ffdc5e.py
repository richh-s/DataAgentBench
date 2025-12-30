code = """import json

file_path = locals()['var_function-call-18015536077059182288']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Extract titles and append .txt
filenames = [c['title'] + ".txt" for c in citations]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-18015536077059182288': 'file_storage/function-call-18015536077059182288.json', 'var_function-call-869791821563470546': 158}

exec(code, env_args)
