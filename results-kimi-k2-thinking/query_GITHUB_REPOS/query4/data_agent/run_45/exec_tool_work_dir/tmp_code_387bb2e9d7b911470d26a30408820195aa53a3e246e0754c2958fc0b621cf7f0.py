code = """import json
import pandas as pd
import re

# Load the languages data
df_languages = pd.DataFrame(locals()['var_functions.query_db:2'])

# Load the commit counts data  
df_commits = pd.DataFrame(locals()['var_functions.query_db:8'])

print(f'Loaded {len(df_languages)} language records and {len(df_commits)} commit records')
print(f'Commits data: {df_commits.head()}')
print(f'First language record: {df_languages.iloc[0]}')"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
