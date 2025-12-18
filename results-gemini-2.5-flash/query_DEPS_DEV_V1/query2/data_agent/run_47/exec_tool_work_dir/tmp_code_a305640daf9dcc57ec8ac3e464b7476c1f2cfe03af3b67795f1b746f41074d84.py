code = """import pandas as pd
import json
import re

# Read the full JSON files
with open(locals()['var_function-call-5259918869377991922'], 'r') as f:
    filtered_project_names_data = json.load(f)
with open(locals()['var_function-call-18055235091598077681'], 'r') as f:
    project_info_data = json.load(f)

# Convert to DataFrames
df_filtered_project_names = pd.DataFrame(filtered_project_names_data)
df_project_info = pd.DataFrame(project_info_data)

# Extract ProjectName and Fork Count from Project_Information
def extract_project_details(info):
    project_name_match = re.search(r'The project (.+?) on GitHub', info)
    fork_count_match = re.search(r'and (\d+) forks', info)
    if project_name_match and fork_count_match:
        return project_name_match.group(1).strip(), int(fork_count_match.group(1))
    return None, None

df_project_info[['ProjectName_Extracted', 'ForkCount']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(extract_project_details(x)))

# Filter project_info to only include relevant project names and drop rows where ProjectName_Extracted or ForkCount is None
df_filtered_project_info = df_project_info.dropna(subset=['ProjectName_Extracted', 'ForkCount'])
df_filtered_project_info = df_filtered_project_info[df_filtered_project_info['ProjectName_Extracted'].isin(df_filtered_project_names['ProjectName'])]

# Sort by ForkCount in descending order and get the top 5
top_5_projects = df_filtered_project_info.sort_values(by='ForkCount', ascending=False).head(5)

# Select and rename columns for the final output
final_result = top_5_projects[['ProjectName_Extracted', 'ForkCount']].rename(columns={'ProjectName_Extracted': 'ProjectName'})

print('__RESULT__:')
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-12206847146719381538': 'file_storage/function-call-12206847146719381538.json', 'var_function-call-14239026419335040227': 'file_storage/function-call-14239026419335040227.json', 'var_function-call-1909453510624210863': 'file_storage/function-call-1909453510624210863.json', 'var_function-call-5813020761262683926': 'file_storage/function-call-5813020761262683926.json', 'var_function-call-12858218957760100097': 'file_storage/function-call-5813020761262683926.json', 'var_function-call-12952062965713530265': 'file_storage/function-call-12952062965713530265.json', 'var_function-call-4332181918179202986': 'file_storage/function-call-4332181918179202986.json', 'var_function-call-2923847489395528065': 'file_storage/function-call-2923847489395528065.json', 'var_function-call-5259918869377991922': 'file_storage/function-call-5259918869377991922.json', 'var_function-call-18055235091598077681': 'file_storage/function-call-18055235091598077681.json'}

exec(code, env_args)
