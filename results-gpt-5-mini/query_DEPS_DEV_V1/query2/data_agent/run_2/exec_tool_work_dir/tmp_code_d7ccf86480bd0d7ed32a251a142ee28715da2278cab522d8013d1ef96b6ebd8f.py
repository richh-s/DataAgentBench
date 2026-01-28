code = """import json
# Load the large result from the previous query stored as a .json file path in var_call_ysJS0k7S8uOWRnHAFwKZT3Nt
with open(var_call_ysJS0k7S8uOWRnHAFwKZT3Nt, 'r') as f:
    data = json.load(f)
# Extract distinct package names for NPM
names = sorted({rec['Name'] for rec in data if rec.get('System') == 'NPM'})

print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_ysJS0k7S8uOWRnHAFwKZT3Nt': 'file_storage/call_ysJS0k7S8uOWRnHAFwKZT3Nt.json'}

exec(code, env_args)
