code = """import pandas as pd
import json
import re

# Load the full results from the stored JSON files
with open(locals()['var_function-call-17602563485509606638'], 'r') as f:
    npm_packages = json.load(f)

with open(locals()['var_function-call-13666942267435733313'], 'r') as f:
    project_packageversion = json.load(f)

with open(locals()['var_function-call-15857448858264485759'], 'r') as f:
    project_info_raw = json.load(f)

df_npm = pd.DataFrame(npm_packages)
df_project_version = pd.DataFrame(project_packageversion)
df_project_info = pd.DataFrame(project_info_raw)

# Merge the two dataframes to link packages with their project names
merged_df = pd.merge(df_npm, df_project_version, on=['System', 'Name', 'Version'], how='inner')

# Get unique project names from the merged dataframe
unique_project_names = merged_df['ProjectName'].unique().tolist()

# Filter project_info to include only relevant projects
# This uses a vectorized approach for efficiency
df_filtered_project_info = df_project_info[
    df_project_info['Project_Information'].astype(str).str.contains('|'.join(re.escape(name) for name in unique_project_names))
].copy()

# Function to extract ProjectName and Fork Count
def extract_project_details(info):
    project_name_match = re.search(r'The project ([^\s]+/[^\s]+) on GitHub', info)
    project_name = project_name_match.group(1) if project_name_match else None
    
    forks_match = re.search(r'(\d+)\sforks', info)
    forks_count = int(forks_match.group(1)) if forks_match else 0
    return project_name, forks_count

# Apply the extraction function
df_filtered_project_info[['ExtractedProjectName', 'ForkCount']] = df_filtered_project_info['Project_Information'].apply(lambda x: pd.Series(extract_project_details(x)))

# Drop rows where ProjectName couldn't be extracted
df_filtered_project_info.dropna(subset=['ExtractedProjectName'], inplace=True)

# Filter to only include projects that were in the original merged_df
df_final_projects = df_filtered_project_info[df_filtered_project_info['ExtractedProjectName'].isin(unique_project_names)]

# Sort by ForkCount and get the top 5
top_5_projects = df_final_projects.sort_values(by='ForkCount', ascending=False).head(5)

# Format the result
result = top_5_projects[['ExtractedProjectName', 'ForkCount']].to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-17602563485509606638': 'file_storage/function-call-17602563485509606638.json', 'var_function-call-13666942267435733313': 'file_storage/function-call-13666942267435733313.json', 'var_function-call-13903376583627773087': 'file_storage/function-call-13903376583627773087.json', 'var_function-call-15857448858264485759': 'file_storage/function-call-15857448858264485759.json'}

exec(code, env_args)
