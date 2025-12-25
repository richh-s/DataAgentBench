code = """import json, re
import pandas as pd

with open(var_call_kk1qTuwFtmDn7As73PuclLwG, 'r') as f:
    readmes = json.load(f)
with open(var_call_MCzRxxkoUtFpHOSRHhY04rIE, 'r') as f:
    langs = json.load(f)

df_readmes = pd.DataFrame(readmes)
df_langs = pd.DataFrame(langs)

python_mask = df_langs['language_description'].str.contains('Python', case=False, na=False)
python_repos = set(df_langs.loc[python_mask, 'repo_name'])

non_python_readmes = df_readmes[~df_readmes['sample_repo_name'].isin(python_repos)].copy()

pattern = re.compile(r"copyright|\bc\s*\d{2,4}|\u00a9", re.IGNORECASE)

non_python_readmes['has_copyright'] = non_python_readmes['content'].fillna('').apply(
    lambda txt: bool(pattern.search(txt))
)

total = int(len(non_python_readmes))
with_copyright = int(non_python_readmes['has_copyright'].sum()) if total > 0 else 0

proportion = with_copyright / total if total > 0 else None

result = {
    'total_non_python_readmes': total,
    'with_copyright': with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kk1qTuwFtmDn7As73PuclLwG': 'file_storage/call_kk1qTuwFtmDn7As73PuclLwG.json', 'var_call_MCzRxxkoUtFpHOSRHhY04rIE': 'file_storage/call_MCzRxxkoUtFpHOSRHhY04rIE.json'}

exec(code, env_args)
