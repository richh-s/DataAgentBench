code = """import json
# load the large result from storage
with open(var_call_yaVJBN8Wuonm0V8EkjDS6nzV, 'r') as f:
    languages = json.load(f)

# parse language_description to find repos that include Python
# We'll create a boolean flag has_python if 'Python (' appears in the description

records = []
for r in languages:
    repo = r.get('repo_name')
    desc = r.get('language_description','')
    has_python = 'Python (' in desc or 'Python ' in desc
    records.append({'repo_name': repo, 'language_description': desc, 'has_python': has_python})

# Output as JSON
print("__RESULT__:")
print(json.dumps(records[:100]))"""

env_args = {'var_call_tHY0UrDvwBsUXX94AGZ1JeYg': ['languages', 'repos', 'licenses'], 'var_call_BnuS3Ca7uzVDfjzMxCWE29k9': ['commits', 'contents', 'files'], 'var_call_yaVJBN8Wuonm0V8EkjDS6nzV': 'file_storage/call_yaVJBN8Wuonm0V8EkjDS6nzV.json'}

exec(code, env_args)
