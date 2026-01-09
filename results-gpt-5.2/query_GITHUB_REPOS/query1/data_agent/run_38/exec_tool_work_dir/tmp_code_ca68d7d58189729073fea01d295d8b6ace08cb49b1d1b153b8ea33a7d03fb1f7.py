code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

langs = load_records(var_call_J0QHSPvfQHiIuO8X0nJl0s5E)
readmes = load_records(var_call_NjeEIvVpfByDmiqyJoPI8cFG)

langs_df = pd.DataFrame(langs)
readmes_df = pd.DataFrame(readmes)

non_python_repos = set(langs_df['repo_name'].dropna().unique())
readmes_non_python = readmes_df[readmes_df['repo_name'].isin(non_python_repos)].copy()

# define copyright presence
pat = re.compile(r'(copyright\s*(?:\(c\)|©)?\s*\d{2,4})|(©\s*\d{2,4})|(all\s+rights\s+reserved)', re.IGNORECASE)
readmes_non_python['has_copyright'] = readmes_non_python['content'].fillna('').map(lambda x: bool(pat.search(x)))

# One README.md per repo expected; if multiple, treat repo as True if any has it.
repo_level = readmes_non_python.groupby('repo_name', as_index=False)['has_copyright'].max()

numerator = int(repo_level['has_copyright'].sum())
denominator = int(repo_level['repo_name'].nunique())
prop = (numerator / denominator) if denominator else None

out = {
    'non_python_repos_with_readme_md': denominator,
    'readme_md_with_copyright': numerator,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_J0QHSPvfQHiIuO8X0nJl0s5E': 'file_storage/call_J0QHSPvfQHiIuO8X0nJl0s5E.json', 'var_call_NjeEIvVpfByDmiqyJoPI8cFG': 'file_storage/call_NjeEIvVpfByDmiqyJoPI8cFG.json'}

exec(code, env_args)
