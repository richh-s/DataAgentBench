code = """import pandas as pd
import json
import re

# Load data from previous steps
with open(locals()['var_function-call-16398008791917807893'], 'r') as f:
    unique_project_names = json.load(f)
with open(locals()['var_function-call-3922761009034456357'], 'r') as f:
    project_info_data = json.load(f)

df_project_info = pd.DataFrame(project_info_data)

# Extract ProjectName and Fork count from Project_Information
def extract_github_info(project_info_string):
    project_name_match = re.search(r'The project ([a-zA-Z0-9\-_/.]+) on GitHub', project_info_string)
    fork_count_match = re.search(r'and (\d+) forks', project_info_string)

    project_name = project_name_match.group(1) if project_name_match else None
    fork_count = int(fork_count_match.group(1)) if fork_count_match else 0
    return project_name, fork_count

# Apply the extraction function
df_project_info['Extracted_ProjectName'], df_project_info['ForkCount'] = zip(*df_project_info['Project_Information'].apply(extract_github_info))

# Filter for relevant projects and sort by fork count
filtered_projects = df_project_info[df_project_info['Extracted_ProjectName'].isin(unique_project_names)]
sorted_projects = filtered_projects.sort_values(by='ForkCount', ascending=False)

# Select top 5 and format the output
top_5_projects = sorted_projects.head(5)[['Extracted_ProjectName', 'ForkCount']]
result = top_5_projects.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-1309086887589599005': 'file_storage/function-call-1309086887589599005.json', 'var_function-call-525686674368958973': 'file_storage/function-call-525686674368958973.json', 'var_function-call-5659482174854748273': 'file_storage/function-call-5659482174854748273.json', 'var_function-call-16871407265358957043': 'file_storage/function-call-16871407265358957043.json', 'var_function-call-14954928567739724652': 'file_storage/function-call-14954928567739724652.json', 'var_function-call-16398008791917807893': 'file_storage/function-call-16398008791917807893.json', 'var_function-call-3922761009034456357': 'file_storage/function-call-3922761009034456357.json'}

exec(code, env_args)
