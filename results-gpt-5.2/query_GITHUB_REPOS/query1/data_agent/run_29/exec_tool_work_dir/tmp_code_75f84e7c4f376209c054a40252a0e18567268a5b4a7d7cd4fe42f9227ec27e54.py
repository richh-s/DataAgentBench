code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

non_python_repos = load_records(var_call_bhiy0bwNA9FsuASQ3efOrvdd)
readmes = load_records(var_call_hxZ2Yie2EEAd3TfiOd5XeL1f)

non_python_set = {r['repo_name'] for r in non_python_repos}

# repo -> list of contents (in case multiple readmes across refs)
repo_to_contents = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo in non_python_set:
        c = r.get('content') or ''
        repo_to_contents.setdefault(repo, []).append(c)

# define copyright detection
copyright_re = re.compile(r'(?i)(?:^|\b)(copyright|©)\b')

def has_copyright(text):
    if not text:
        return False
    return bool(copyright_re.search(text))

repos_with_readme = set(repo_to_contents.keys())
num_with_readme = len(repos_with_readme)

num_with_copyright = 0
for repo, contents_list in repo_to_contents.items():
    if any(has_copyright(t) for t in contents_list):
        num_with_copyright += 1

prop = (num_with_copyright / num_with_readme) if num_with_readme else None

result = {
    'non_python_repos_with_readme_md': num_with_readme,
    'with_copyright_in_readme_md': num_with_copyright,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bhiy0bwNA9FsuASQ3efOrvdd': 'file_storage/call_bhiy0bwNA9FsuASQ3efOrvdd.json', 'var_call_qi7PPScHDiHvwv4FJGtTpOzO': 'file_storage/call_qi7PPScHDiHvwv4FJGtTpOzO.json', 'var_call_hxZ2Yie2EEAd3TfiOd5XeL1f': 'file_storage/call_hxZ2Yie2EEAd3TfiOd5XeL1f.json'}

exec(code, env_args)
