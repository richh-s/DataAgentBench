code = """import json
with open(var_call_yaVJBN8Wuonm0V8EkjDS6nzV, 'r') as f:
    languages = json.load(f)
with open(var_call_UBMJOv5iBDIAsagxjv07iwzf, 'r') as f:
    contents = json.load(f)

# map repo -> language_description
lang_map = {r.get('repo_name'): r.get('language_description','') for r in languages}
non_python_repos = {repo for repo,desc in lang_map.items() if 'python' not in (desc or '').lower()}

num = 0
den = 0
for c in contents:
    path = (c.get('sample_path') or '').strip().lower()
    repo = c.get('sample_repo_name')
    if path == 'readme.md' and repo in non_python_repos:
        den += 1
        cont = c.get('content') or ''
        low = cont.lower()
        if 'copyright' in low or '©' in cont or 'all rights reserved' in low:
            num += 1

prop = None
if den > 0:
    prop = num / den

result = {'numerator': num, 'denominator': den, 'proportion': prop}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tHY0UrDvwBsUXX94AGZ1JeYg': ['languages', 'repos', 'licenses'], 'var_call_BnuS3Ca7uzVDfjzMxCWE29k9': ['commits', 'contents', 'files'], 'var_call_yaVJBN8Wuonm0V8EkjDS6nzV': 'file_storage/call_yaVJBN8Wuonm0V8EkjDS6nzV.json', 'var_call_9AwfFr8J5A6Lcf15q4gosFmY': 'file_storage/call_9AwfFr8J5A6Lcf15q4gosFmY.json', 'var_call_UBMJOv5iBDIAsagxjv07iwzf': 'file_storage/call_UBMJOv5iBDIAsagxjv07iwzf.json'}

exec(code, env_args)
