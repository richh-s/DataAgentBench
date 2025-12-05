code = """import json, pandas as pd, re

# Load full results if stored as file paths

def load_result(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

contents_rows = load_result(var_call_ThzIu9yFn0KsMs4DRXsPbG03)
language_rows = load_result(var_call_eWVEuSF1ZFFNwDEdWkf7Ez85)

contents_df = pd.DataFrame(contents_rows)[['sample_repo_name', 'content']]
languages_df = pd.DataFrame(language_rows)[['repo_name', 'language_description']]

# Identify repos that do NOT use Python
mask_no_python = ~languages_df['language_description'].str.contains('Python', case=False, na=False)
no_py_repos = languages_df[mask_no_python]['repo_name'].unique()

# Filter README contents for those repos
readme_no_py = contents_df[contents_df['sample_repo_name'].isin(no_py_repos)].copy()

# Define a simple heuristic for "copyright information"
pattern = re.compile(r'copyright|\bcopyright\s*\u00a9|\u00a9', re.IGNORECASE)
readme_no_py['has_copyright'] = readme_no_py['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

if len(readme_no_py) == 0:
    proportion = None
else:
    proportion = float(readme_no_py['copyright'].sum())

result = {
    'total_readmes_no_python': int(len(readme_no_py)),
    'readmes_with_copyright_info': int(readme_no_py['has_copyright'].sum()),
    'proportion': (readme_no_py['has_copyright'].sum() / len(readme_no_py)) if len(readme_no_py) > 0 else None
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ThzIu9yFn0KsMs4DRXsPbG03': 'file_storage/call_ThzIu9yFn0KsMs4DRXsPbG03.json', 'var_call_eWVEuSF1ZFFNwDEdWkf7Ez85': 'file_storage/call_eWVEuSF1ZFFNwDEdWkf7Ez85.json'}

exec(code, env_args)
