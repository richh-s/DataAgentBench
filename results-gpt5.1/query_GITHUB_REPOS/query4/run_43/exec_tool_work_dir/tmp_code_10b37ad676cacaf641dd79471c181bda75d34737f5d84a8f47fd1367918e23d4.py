code = """import json, pandas as pd
from pathlib import Path

# Load full languages data from file
path = Path(var_call_ryEF71ZyVN94YUmMxtvZOnU6)
languages_data = json.loads(path.read_text())

langs_df = pd.DataFrame(languages_data)
commits_df = pd.DataFrame(var_call_AuDo1DlGM3oniRiobGFkUbzp)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# Determine main language is Python via simple heuristic: check if description starts with or contains patterns indicating Python is main
# We consider non-Python if the first language mentioned is not Python.

def is_python_main(desc: str) -> bool:
    if not isinstance(desc, str):
        return False
    lower = desc.lower()
    # identify first occurrence of language list segment before first '(' which usually follows language name
    # But simpler: check specific templates mentioning "mainly written in X" or "majority of the code is in X" etc.
    # We'll extract the first word before the first ' (' after phrases.
    # However, for reliability, we just check if patterns clearly say Python as main.
    if 'python (' in lower and ('mainly written in python' in lower or 'majority of the code is in python' in lower or 'while most of the project is built in python' in lower or 'the codebase includes: python' in lower or lower.strip().startswith('python (')):
        # But ensure that python appears before other languages like 'ruby ('
        first_paren = lower.find('(')
        first_python = lower.find('python')
        if first_python != -1 and (first_paren == -1 or first_python < first_paren + 10):
            return True
    return False

langs_df['is_python_main'] = langs_df['language_description'].apply(is_python_main)

# Merge commits with languages
merged = commits_df.merge(langs_df[['repo_name','is_python_main']], on='repo_name', how='left')

# Filter repos where main language is NOT Python (False or NaN)
non_python = merged[(merged['is_python_main'] == False) | (merged['is_python_main'].isna())]

# Order by commit_count desc and take top 5
top5 = non_python.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ryEF71ZyVN94YUmMxtvZOnU6': 'file_storage/call_ryEF71ZyVN94YUmMxtvZOnU6.json', 'var_call_AuDo1DlGM3oniRiobGFkUbzp': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
