code = """import json
import pandas as pd
import re

readmes_path = var_call_aKqaCcYSt54L2Z2vmuk5JMl4
languages_path = var_call_jfTpnO4hGsr3EjjnTyWmDOsu

if isinstance(readmes_path, str):
    with open(readmes_path, 'r') as f:
        readmes = json.load(f)
else:
    readmes = readmes_path

if isinstance(languages_path, str):
    with open(languages_path, 'r') as f:
        languages = json.load(f)
else:
    languages = languages_path

readmes_df = pd.DataFrame(readmes)
languages_df = pd.DataFrame(languages)

languages_df['uses_python'] = languages_df['language_description'].str.contains('Python (', case=False, na=False)
python_repos = set(languages_df.loc[languages_df['uses_python'], 'repo_name'])

readmes_df['uses_python'] = readmes_df['sample_repo_name'].isin(python_repos)
non_python_readmes = readmes_df[~readmes_df['uses_python']]

patterns = ['copyright', '©', 'all rights reserved']
pattern = re.compile('|'.join(re.escape(p) for p in patterns), re.IGNORECASE)

content_lower = non_python_readmes['content'].fillna('')
mask = content_lower.apply(lambda x: bool(pattern.search(x)))

num_non_python = int(len(non_python_readmes))
num_with_copyright = int(mask.sum())
proportion = float(num_with_copyright) / num_non_python if num_non_python > 0 else None

result = {
    'num_non_python_readmes': num_non_python,
    'num_with_copyright_info': num_with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_aKqaCcYSt54L2Z2vmuk5JMl4': 'file_storage/call_aKqaCcYSt54L2Z2vmuk5JMl4.json', 'var_call_jfTpnO4hGsr3EjjnTyWmDOsu': 'file_storage/call_jfTpnO4hGsr3EjjnTyWmDOsu.json'}

exec(code, env_args)
