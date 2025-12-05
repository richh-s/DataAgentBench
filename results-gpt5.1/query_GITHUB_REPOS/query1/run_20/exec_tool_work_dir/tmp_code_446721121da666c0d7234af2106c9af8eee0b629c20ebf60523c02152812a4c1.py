code = """import json, pandas as pd
from pathlib import Path

readmes_path = Path(var_call_5VwB6jBAs5SPEAIptfy7Zyzb)
languages_path = Path(var_call_iIjkoFlKBrOw692UN9alKEke)

with readmes_path.open() as f:
    readmes = json.load(f)
with languages_path.open() as f:
    languages = json.load(f)

readmes_df = pd.DataFrame(readmes)
languages_df = pd.DataFrame(languages)

# Determine repos that do NOT use Python
mask_no_python = ~languages_df['language_description'].str.contains('Python', case=False, na=False)
no_python_repos = set(languages_df[mask_no_python]['repo_name'].unique())

# Filter README.md files for those repos
readmes_no_python = readmes_df[readmes_df['sample_repo_name'].isin(no_python_repos)].copy()

patterns = ['copyright', '©', 'copr.']
content_lower = readmes_no_python['content'].fillna('').str.lower()
mask_copyright = content_lower.apply(lambda txt: any(pat in txt for pat in patterns))

num_readmes_no_python = int(len(readmes_no_python))
num_with_copyright = int(mask_copyright.sum())
prop = float(num_with_copyright / num_readmes_no_python) if num_readmes_no_python > 0 else None

result = {
    'num_readmes_no_python': num_readmes_no_python,
    'num_readmes_with_copyright': num_with_copyright,
    'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cFX5rRZSKX4Gr8qHzzvU3iKA': 'file_storage/call_cFX5rRZSKX4Gr8qHzzvU3iKA.json', 'var_call_iIjkoFlKBrOw692UN9alKEke': 'file_storage/call_iIjkoFlKBrOw692UN9alKEke.json', 'var_call_bsfYrILNW0yjpYWevXwqM0eP': ['commits', 'contents', 'files'], 'var_call_FXcuIAF23Q47nxcnDi5AxVm8': [{'cid': '0', 'name': 'id', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'content', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'sample_repo_name', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'sample_ref', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'sample_path', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'sample_symlink_target', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'repo_data_description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_5VwB6jBAs5SPEAIptfy7Zyzb': 'file_storage/call_5VwB6jBAs5SPEAIptfy7Zyzb.json'}

exec(code, env_args)
