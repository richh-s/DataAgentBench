code = """import json, pandas as pd
from pathlib import Path

def load_result(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.load(open(x))
    return x

readmes = load_result(var_call_NqpNaIYwulsNRVxn4HeI2cuF)
languages = load_result(var_call_0wOSAyeupFEKCOPAkE8Q9d0K)

readme_df = pd.DataFrame(readmes)[['sample_repo_name','content']]
languages_df = pd.DataFrame(languages)

mask_no_python = ~languages_df['language_description'].str.contains('python', case=False, na=False)
no_py_repos = languages_df[mask_no_python][['repo_name']].drop_duplicates()

merged = readme_df.merge(no_py_repos, left_on='sample_repo_name', right_on='repo_name')

copyright_mask = merged['content'].str.contains('copyright', case=False, na=False)

num_total = int(len(merged))
num_with = int(copyright_mask.sum())
prop = float(num_with / num_total) if num_total > 0 else None

result = {
    'num_readmes_considered': num_total,
    'num_with_copyright': num_with,
    'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_pvAQvdImn5NvwnKRwSfK7aBn': 'file_storage/call_pvAQvdImn5NvwnKRwSfK7aBn.json', 'var_call_0wOSAyeupFEKCOPAkE8Q9d0K': 'file_storage/call_0wOSAyeupFEKCOPAkE8Q9d0K.json', 'var_call_NqpNaIYwulsNRVxn4HeI2cuF': 'file_storage/call_NqpNaIYwulsNRVxn4HeI2cuF.json'}

exec(code, env_args)
