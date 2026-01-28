code = """import json
# var_call_GFY4OJaYJwwlSMS6nFnauMDQ is provided in storage and contains the path to the JSON file with the query result
path = var_call_GFY4OJaYJwwlSMS6nFnauMDQ
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Build list of filenames corresponding to the titles
filenames = [r['title'] + '.txt' for r in records]
import json
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_GFY4OJaYJwwlSMS6nFnauMDQ': 'file_storage/call_GFY4OJaYJwwlSMS6nFnauMDQ.json'}

exec(code, env_args)
