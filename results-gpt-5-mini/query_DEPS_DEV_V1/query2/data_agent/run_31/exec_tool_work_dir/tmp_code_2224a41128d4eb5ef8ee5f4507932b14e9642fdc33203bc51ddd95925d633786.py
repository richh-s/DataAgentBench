code = """import json,sys,os
# var_call_P4UkSti8t5SZZ1nHGnj0x295 is provided in storage by previous query_db
p = var_call_P4UkSti8t5SZZ1nHGnj0x295
# If it's a path to a json file, load it; otherwise it's the list
if isinstance(p, str) and os.path.exists(p):
    data = json.load(open(p, 'r'))
else:
    data = p
# Filter entries where Licenses contains "MIT" (case-sensitive in data) and VersionInfo contains IsRelease true
result = []
seen = set()
for r in data:
    lic = r.get('Licenses') or ''
    verinfo = r.get('VersionInfo') or ''
    if 'MIT' in lic and '"IsRelease": true' in verinfo:
        key = (r.get('System'), r.get('Name'), r.get('Version'))
        if key not in seen:
            seen.add(key)
            result.append({'System': key[0], 'Name': key[1], 'Version': key[2]})
# print as JSON string
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_P4UkSti8t5SZZ1nHGnj0x295': 'file_storage/call_P4UkSti8t5SZZ1nHGnj0x295.json'}

exec(code, env_args)
