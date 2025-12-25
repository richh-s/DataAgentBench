code = """import json

with open(locals()['var_function-call-14621584579191841765'], 'r') as f:
    articles_2015 = json.load(f)

print("__RESULT__:")
print(len(articles_2015))"""

env_args = {'var_function-call-14621584579191841765': 'file_storage/function-call-14621584579191841765.json'}

exec(code, env_args)
