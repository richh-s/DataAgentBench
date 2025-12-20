code = """import json

with open(locals()['var_function-call-13685975547188021313'], 'r') as f:
    metadata_2015 = json.load(f)

print("__RESULT__:")
print(len(metadata_2015))"""

env_args = {'var_function-call-13685975547188021313': 'file_storage/function-call-13685975547188021313.json'}

exec(code, env_args)
