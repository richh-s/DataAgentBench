code = """import json, re, pandas as pd

# Load full results if they are file paths
from pathlib import Path

def load_result(obj):
    if isinstance(obj, str) and obj.endswith('.json') and Path(obj).exists():
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

readmes = load_result(var_call_c2EeZwuQQlL8EzP6pkGzF2Na)
languages = load_result(var_call_NLCuRq3Ycr6fcjmsDFFeUrYl)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(languages)

# Filter repos that do NOT use Python in language_description (case-insensitive, word boundary for 'Python')
mask_no_python = ~langs_df['language_description'].str.contains(r'Python', case=False, na=False)
no_py_langs = langs_df[mask_no_python][['repo_name']]

# Join with readmes on repo_name
merged = pd.merge(no_py_langs, readmes_df, on='repo_name', how='inner')

# Define a simple heuristic for copyright info
pattern = re.compile(r'copyright\s*(?:\u00a9|\(c\))?|\u00a9\s*\d{4}|\(c\)\s*\d{4}', re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

merged['has_copyright'] = merged['content'].apply(copyright)

total = int(len(merged))
with_copyright = int(merged['has_copyright'].sum())
proportion = with_copyright / total if total > 0 else None

result = {
    'total_non_python_repos_with_readme': total,
    'num_with_copyright_in_readme': with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_c2EeZwuQQlL8EzP6pkGzF2Na': 'file_storage/call_c2EeZwuQQlL8EzP6pkGzF2Na.json', 'var_call_NLCuRq3Ycr6fcjmsDFFeUrYl': 'file_storage/call_NLCuRq3Ycr6fcjmsDFFeUrYl.json'}

exec(code, env_args)
