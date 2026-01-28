code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

non_python = load_records(var_call_bCYZ2IRnJRGOeAysrLrdsJaf)
readmes = load_records(var_call_RFCjGFQJdicsXAZ24vkljf0R)

non_python_set = set(r['repo_name'] for r in non_python if r.get('repo_name') is not None)

# regex for copyright markers
pat = re.compile(r"(?:copyright|©|\(c\))", re.IGNORECASE)

total = 0
with_copyright = 0

for r in readmes:
    repo = r.get('repo_name')
    if repo in non_python_set:
        total += 1
        content = r.get('content') or ''
        if pat.search(content):
            with_copyright += 1

prop = (with_copyright / total) if total else None
result = {
    'non_python_repos_with_readme_md_count': total,
    'readme_md_with_copyright_count': with_copyright,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bCYZ2IRnJRGOeAysrLrdsJaf': 'file_storage/call_bCYZ2IRnJRGOeAysrLrdsJaf.json', 'var_call_RFCjGFQJdicsXAZ24vkljf0R': 'file_storage/call_RFCjGFQJdicsXAZ24vkljf0R.json'}

exec(code, env_args)
