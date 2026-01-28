code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str):
        # treat as path
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

langs = load_records(var_call_h45pg7j4zRvTgt0Iu6441Voj)
readmes = load_records(var_call_KfBieKamBlBkCS7LD7GoMbUD)

langs_df = pd.DataFrame(langs)
readme_df = pd.DataFrame(readmes)

# Determine repos that do NOT use Python based on language_description containing 'Python'
langs_df['uses_python'] = langs_df['language_description'].str.contains(r'\bPython\b', case=False, regex=True, na=False)
non_py_repos = set(langs_df.loc[~langs_df['uses_python'], 'repo_name'].dropna().unique())

# Consider only repos with a README.md content present
readme_df = readme_df.dropna(subset=['repo_name'])
readme_df = readme_df[readme_df['repo_name'].isin(non_py_repos)].copy()

# If multiple README.md per repo, treat as include copyright if any contains it

def has_copyright(txt):
    if txt is None:
        return False
    t = txt.lower()
    # common copyright markers
    return bool(re.search(r'(copyright\s*\(c\)|copyright\s*©|\bcopyright\b|\b©\b)', t))

readme_df['has_copyright'] = readme_df['content'].map(has_copyright)
by_repo = readme_df.groupby('repo_name', as_index=False)['has_copyright'].max()

num_with_readme = int(by_repo.shape[0])
num_with_copyright = int(by_repo['has_copyright'].sum())
prop = (num_with_copyright / num_with_readme) if num_with_readme else None

out = {
    'non_python_repos_with_readme_count': num_with_readme,
    'non_python_repos_with_readme_and_copyright_count': num_with_copyright,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_h45pg7j4zRvTgt0Iu6441Voj': 'file_storage/call_h45pg7j4zRvTgt0Iu6441Voj.json', 'var_call_KfBieKamBlBkCS7LD7GoMbUD': 'file_storage/call_KfBieKamBlBkCS7LD7GoMbUD.json'}

exec(code, env_args)
