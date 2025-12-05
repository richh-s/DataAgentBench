code = """import json, pandas as pd

commits_top = pd.DataFrame(var_call_47QclYr21Q3l1pHxQ5QfZ2p7)

# load full languages table
import pathlib
with open(var_call_eD7zkPqAMKY08dFKWXeLPkVH, 'r') as f:
    languages_full = json.load(f)
langs = pd.DataFrame(languages_full)

# determine main language from natural language description by picking the first language mentioned before the first '(' character
# Example pattern: "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes)."
# or "The codebase includes: Shell (21,286 bytes), Ruby (2,160 bytes)." -> first listed is main

def extract_main_language(desc: str):
    if not isinstance(desc, str):
        return None
    # find first '(' and look backwards to previous space or punctuation
    idx = desc.find('(')
    if idx == -1:
        return None
    sub = desc[:idx].rstrip()
    # split on spaces and punctuation, take last token
    for sep in [',', ':']:
        if sep in sub:
            sub = sub.split(sep)[-1].strip()
    parts = sub.split()
    if not parts:
        return None
    return parts[-1]

langs['main_language'] = langs['language_description'].map(extract_main_language)

# join commits_top with languages on repo_name
merged = commits_top.merge(langs[['repo_name','main_language']], on='repo_name', how='left')

# filter where main_language is not Python (case-insensitive) or is null but description does not indicate Python anywhere
merged['is_python'] = merged['main_language'].str.lower().eq('python')

non_python = merged[~merged['is_python']].copy()

# sort by commit_count desc (cast to int) and take top 5
non_python['commit_count'] = non_python['commit_count'].astype(int)
non_python = non_python.sort_values('commit_count', ascending=False).head(5)

result = non_python['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_47QclYr21Q3l1pHxQ5QfZ2p7': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_eD7zkPqAMKY08dFKWXeLPkVH': 'file_storage/call_eD7zkPqAMKY08dFKWXeLPkVH.json', 'var_call_lsh1HYXCgyrVNLY1sDzZXGHD': [{'name': 'languages'}, {'name': 'repos'}, {'name': 'licenses'}]}

exec(code, env_args)
