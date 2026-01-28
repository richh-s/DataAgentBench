code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

langs = load_records(var_call_o0O53hfjPR6GhqOUbVvLrZ7f)
readmes = load_records(var_call_mTxwSE2kdQ1VeMcPNFSPkMNf)

langs_set = set(r['repo_name'] for r in langs if r.get('repo_name') is not None)

# Only consider repos (without Python) that have a README.md in contents
rows = []
for r in readmes:
    repo = r.get('repo_name')
    if repo in langs_set:
        rows.append({'repo_name': repo, 'content': r.get('content') or ''})

df = pd.DataFrame(rows)

# regex for copyright info
# accept: 'copyright', '(c)', '©', 'all rights reserved'
pat = re.compile(r"(?is)(copyright\s*(?:\(c\)|©)?\s*\d{0,4}|\(c\)\s*\d{0,4}|©\s*\d{0,4}|all\s+rights\s+reserved)")

df['has_copyright'] = df['content'].astype(str).str.contains(pat, regex=True)

n_total = int(df['repo_name'].nunique())
# if multiple readmes per repo, count repo as true if any true
repo_any = df.groupby('repo_name', as_index=False)['has_copyright'].any()

n_with = int(repo_any['has_copyright'].sum())
prop = (n_with / n_total) if n_total else None

result = {
    'non_python_repos_with_readme_md': n_total,
    'repos_with_copyright_in_readme_md': n_with,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o0O53hfjPR6GhqOUbVvLrZ7f': 'file_storage/call_o0O53hfjPR6GhqOUbVvLrZ7f.json', 'var_call_mTxwSE2kdQ1VeMcPNFSPkMNf': 'file_storage/call_mTxwSE2kdQ1VeMcPNFSPkMNf.json'}

exec(code, env_args)
