code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

non_py = load_records(var_call_uiILBWf3vtZukJKHm7dYjXpb)
readmes = load_records(var_call_hnf5FaD9gbt0CfZWb2AqoOHn)

non_py_set = set(r['repo_name'] for r in non_py)

# For repos without Python, find if README.md includes copyright info
# Heuristic: line/phrase containing 'copyright' or '(c)' or '©'
pat = re.compile(r'(copyright|\(c\)|©)', re.IGNORECASE)

seen = set()
with_copy = set()
for r in readmes:
    repo = r.get('repo_name')
    if repo not in non_py_set:
        continue
    if repo in seen:
        continue
    seen.add(repo)
    content = r.get('content') or ''
    if pat.search(content):
        with_copy.add(repo)

total = len(seen)  # repos without Python that have a README.md in table
prop = (len(with_copy) / total) if total else None

out = {
    'repos_without_python_with_readme_md': total,
    'repos_without_python_with_readme_md_and_copyright_info': len(with_copy),
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_uiILBWf3vtZukJKHm7dYjXpb': 'file_storage/call_uiILBWf3vtZukJKHm7dYjXpb.json', 'var_call_hnf5FaD9gbt0CfZWb2AqoOHn': 'file_storage/call_hnf5FaD9gbt0CfZWb2AqoOHn.json'}

exec(code, env_args)
