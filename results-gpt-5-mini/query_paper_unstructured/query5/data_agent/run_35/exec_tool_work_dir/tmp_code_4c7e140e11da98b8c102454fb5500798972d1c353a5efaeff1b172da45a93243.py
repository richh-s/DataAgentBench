code = """import json
# var_call_4vquK5qDMFJNwMzQacyha82d is the storage key containing the file path to the large query result
path = var_call_4vquK5qDMFJNwMzQacyha82d
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# extract titles
titles = [rec['title'] for rec in data]
# build filenames
filenames = [t + '.txt' for t in titles]
import json
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_4vquK5qDMFJNwMzQacyha82d': 'file_storage/call_4vquK5qDMFJNwMzQacyha82d.json'}

exec(code, env_args)
