code = """import json, pandas as pd, re

# load non-python repos list
path_nonpy = var_call_XgokpvBWT5lp2j0W7qe6Khep
with open(path_nonpy, 'r', encoding='utf-8') as f:
    nonpy = json.load(f)
nonpy_set = set(r['repo_name'] for r in nonpy)

df_readme = pd.DataFrame(var_call_jGbqH7RQR3mBNaTe2GV7D2hw)
if df_readme.empty:
    # no readmes matched due to query issue; handle gracefully
    res = {"non_python_repos": int(var_call_DcpvPnLulzSGq2TIvmBgTQay[0]['non_python_repos']),
           "non_python_repos_with_readme_md": 0,
           "non_python_repos_with_readme_md_and_copyright": 0,
           "proportion": None}
    print('__RESULT__:')
    print(json.dumps(res))
    raise SystemExit

# Filter to non-python repos
# Ensure content str
mask = df_readme['repo_name'].isin(nonpy_set)
df_np_readme = df_readme.loc[mask].copy()

def has_copyright(text):
    if text is None:
        return False
    t = str(text)
    # normalize
    # look for common markers
    patterns = [
        r'\bcopyright\b',
        r'\b©\b',
        r'\b\(c\)\b',
        r'\ball rights reserved\b'
    ]
    tl = t.lower()
    for p in patterns:
        if re.search(p, tl, flags=re.IGNORECASE):
            return True
    return False

# Deduplicate per repo: a repo may have multiple refs; count repo if any readme contains copyright
repo_any = df_np_readme.groupby('repo_name')['content'].apply(lambda s: any(has_copyright(x) for x in s))
with_readme = int(repo_any.shape[0])
with_c = int(repo_any.sum())
prop = (with_c / with_readme) if with_readme else None

res = {
    "non_python_repos": int(var_call_DcpvPnLulzSGq2TIvmBgTQay[0]['non_python_repos']),
    "non_python_repos_with_readme_md": with_readme,
    "non_python_repos_with_readme_md_and_copyright": with_c,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_XgokpvBWT5lp2j0W7qe6Khep': 'file_storage/call_XgokpvBWT5lp2j0W7qe6Khep.json', 'var_call_jGbqH7RQR3mBNaTe2GV7D2hw': [], 'var_call_DcpvPnLulzSGq2TIvmBgTQay': [{'non_python_repos': '2774729'}]}

exec(code, env_args)
