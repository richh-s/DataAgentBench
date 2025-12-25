code = """import json, pandas as pd
from pathlib import Path

# Load full results from files
contents = json.load(open(var_call_Keq6mVefrUgKQwjR3GqEwsKj))
languages = json.load(open(var_call_508hDUFLOZH7wRTU2vGSQYHe))
python_repos = json.load(open(var_call_rM60woWpf1DKA5EwAf48pDbQ))

contents_df = pd.DataFrame(contents)
langs_df = pd.DataFrame(languages)
py_df = pd.DataFrame(python_repos)

# repos that use Python
py_repos = set(py_df['repo_name'].unique())

# add languages to contents
merged = contents_df.merge(langs_df, on='repo_name', how='left')

# keep repos that do NOT use Python
non_py = merged[~merged['repo_name'].isin(py_repos)].copy()

# function to detect copyright info (very simple heuristic)
import re
pattern = re.compile(r"copyright|\bc\s*\d{4}", re.IGNORECASE)

non_py['has_copyright'] = non_py['content'].fillna('').apply(lambda txt: bool(pattern.search(txt)))

# compute proportion
total = len(non_py)
with_c = int(non_py['copyright'].sum()) if 'copyright' in non_py.columns else int(non_py['has_copyright'].sum())
prop = with_c / total if total else None

result = {
  "total_non_python_readmes": int(total),
  "with_copyright_info": int(with_c),
  "proportion": prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Keq6mVefrUgKQwjR3GqEwsKj': 'file_storage/call_Keq6mVefrUgKQwjR3GqEwsKj.json', 'var_call_508hDUFLOZH7wRTU2vGSQYHe': 'file_storage/call_508hDUFLOZH7wRTU2vGSQYHe.json', 'var_call_rM60woWpf1DKA5EwAf48pDbQ': 'file_storage/call_rM60woWpf1DKA5EwAf48pDbQ.json'}

exec(code, env_args)
