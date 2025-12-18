code = """import json
import pandas as pd

# Load data from previous steps
with open(locals()['var_function-call-2805671709898573738'], 'r') as f:
    non_python_repos_data = json.load(f)
df_non_python_repos = pd.DataFrame(non_python_repos_data)

commit_counts_data = locals()['var_function-call-6959371651224567252']
df_commit_counts = pd.DataFrame(commit_counts_data)

# Convert commit_count to numeric
df_commit_counts['commit_count'] = pd.to_numeric(df_commit_counts['commit_count'])

# Merge the two dataframes to get commit counts for non-Python repositories
merged_df = pd.merge(df_non_python_repos, df_commit_counts, on='repo_name', how='inner')

# Filter out any repositories where the main language is Python (double-check)
# This step should technically already be done by `df_non_python_repos`, but good for robustness
final_filtered_df = merged_df[merged_df['main_language'] != 'Python']

# Sort by commit_count in descending order and get the top 5
top_five_repos = final_filtered_df.sort_values(by='commit_count', ascending=False).head(5)

# Extract and format the repository names
result = top_five_repos['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6648005358843189280': 'file_storage/function-call-6648005358843189280.json', 'var_function-call-4624580587509127227': 'file_storage/function-call-4624580587509127227.json', 'var_function-call-2805671709898573738': 'file_storage/function-call-2805671709898573738.json', 'var_function-call-6959371651224567252': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-9873578702012780336': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react']}

exec(code, env_args)
