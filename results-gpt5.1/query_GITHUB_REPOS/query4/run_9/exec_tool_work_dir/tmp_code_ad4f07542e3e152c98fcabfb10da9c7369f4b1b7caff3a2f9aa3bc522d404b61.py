code = """import json
import pandas as pd

commits = pd.DataFrame(var_call_jK2asaNlZmvKX0WpBlhxyplF)
with open(var_call_QZBSqmBfCFfY8jAsJJbcp01R, 'r') as f:
    languages = pd.DataFrame(json.load(f))

def is_main_language_python(desc: str) -> bool:
    lower = desc.lower()
    first_part = lower.split(')', 1)[0]
    return 'python' in first_part

languages['is_python_main'] = languages['language_description'].apply(is_main_language_python)
non_python_langs = languages[languages['is_python_main'] == False][['repo_name']]

merged = pd.merge(commits, non_python_langs, on='repo_name', how='inner')
merged['commit_count'] = merged['commit_count'].astype(int)
result = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_jK2asaNlZmvKX0WpBlhxyplF': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_QZBSqmBfCFfY8jAsJJbcp01R': 'file_storage/call_QZBSqmBfCFfY8jAsJJbcp01R.json'}

exec(code, env_args)
