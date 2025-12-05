code = """import json, pandas as pd, re

readmes_path = var_call_cM4xWmBLFzJ5MJw61VxrtLAE
langs_path = var_call_P93wozz6JdmiI0MgT6OItNiY

with open(readmes_path) as f:
    readmes = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

langs_df['has_python'] = langs_df['language_description'].str.contains('Python', case=False, na=False)

repos_no_python = set(langs_df.loc[~langs_df['has_python'], 'repo_name'])

readmes_df = readmes_df.rename(columns={'sample_repo_name': 'repo_name'})

no_py_readmes = readmes_df[readmes_df['repo_name'].isin(repos_no_python)].copy()

copyright_patterns = [
    r'copyright\s*\u00a9',
    r'\u00a9',
    r'copyright \d{4}',
    r'\(c\) \d{4}',
    r'\bcopyright\b',
]
regex = re.compile('|'.join(copyright_patterns), re.IGNORECASE)

non_null = no_py_readmes['content'].fillna('')
mask = non_null.apply(lambda x: bool(regex.search(x)))

num_with_copyright = int(mask.sum())
num_total = int(len(no_py_readmes))
prop = float(num_with_copyright / num_total) if num_total > 0 else None

result = {'total_readmes_no_python': num_total,
          'with_copyright': num_with_copyright,
          'proportion': prop}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cM4xWmBLFzJ5MJw61VxrtLAE': 'file_storage/call_cM4xWmBLFzJ5MJw61VxrtLAE.json', 'var_call_P93wozz6JdmiI0MgT6OItNiY': 'file_storage/call_P93wozz6JdmiI0MgT6OItNiY.json', 'var_call_kefTYO6sxnmvoS7nL8tjtPam': 'file_storage/call_kefTYO6sxnmvoS7nL8tjtPam.json', 'var_call_W61ZBEDc080nLxqYjrhoRY3r': 'file_storage/call_W61ZBEDc080nLxqYjrhoRY3r.json'}

exec(code, env_args)
