code = """import pandas as pd
import json
import re

# Load the latest releases with ProjectName from the previous step
with open(locals()['var_function-call-2024195598409583868'], 'r') as f:
    unique_project_names_dict = json.load(f)
unique_project_names = unique_project_names_dict['unique_project_names']

# Load project_info data
with open(locals()['var_function-call-14921129906520279837'], 'r') as f:
    project_info_data = json.load(f)
df_project_info = pd.DataFrame(project_info_data)

# Function to extract ProjectName and Stars from Project_Information
def parse_project_info(project_info_str):
    project_name_match = re.search(r'The project (\S+/\S+) is hosted on GitHub', project_info_str) # for cases with 'is hosted on GitHub'
    if not project_name_match:
        project_name_match = re.search(r'The GitHub project (\S+/\S+) currently', project_info_str) # for cases with 'The GitHub project'
    if not project_name_match:
        project_name_match = re.search(r'The project named (\S+/\S+) on GitHub currently', project_info_str) # for cases with 'The project named ... on GitHub currently'
    if not project_name_match:
        project_name_match = re.search(r'The project (\S+/\S+) on GitHub has garnered', project_info_str) # for cases with 'The project ... on GitHub has garnered'
    if not project_name_match:
        project_name_match = re.search(r'The project (\S+/\S+) on GitHub currently', project_info_str) # for cases with 'The project ... on GitHub currently'
    if not project_name_match:
        project_name_match = re.search(r'The project is a GitHub repository named (\S+/\S+)', project_info_str) # for cases with 'The project is a GitHub repository named'
    if not project_name_match:
        project_name_match = re.search(r'The project is hosted on GitHub under the name (\S+/\S+)', project_info_str) # for cases with 'The project is hosted on GitHub under the name'

    project_name = project_name_match.group(1) if project_name_match else None

    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', project_info_str)
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

# Apply the parsing function
df_project_info[['ProjectName_Parsed', 'Stars']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(parse_project_info(x)))

# Filter for relevant projects and drop duplicates
df_filtered_project_info = df_project_info[df_project_info['ProjectName_Parsed'].isin(unique_project_names)].drop_duplicates(subset=['ProjectName_Parsed'])

# Select relevant columns for merging
df_stars = df_filtered_project_info[['ProjectName_Parsed', 'Stars']].rename(columns={'ProjectName_Parsed': 'ProjectName'})

# Load df_merged from a previous step
with open(locals()['var_function-call-3458438926277201531'], 'r') as f:
    latest_releases = json.load(f)
df_latest_releases = pd.DataFrame(latest_releases)

with open(locals()['var_function-call-13207347577609905648'], 'r') as f:
    project_packageversion_data = json.load(f)
df_project_packageversion = pd.DataFrame(project_packageversion_data)

df_merged = pd.merge(df_latest_releases, df_project_packageversion, on=['Name', 'Version'], how='inner')

# Merge with star counts
df_final = pd.merge(df_merged, df_stars, on='ProjectName', how='left')

# Fill NaN stars with 0 (for projects not found or parsed)
df_final['Stars'] = df_final['Stars'].fillna(0).astype(int)

# Sort by stars and get top 5 unique packages (in case multiple versions of same package slipped through due to parsing)
top_5_packages = df_final.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5930656202702153224': 'file_storage/function-call-5930656202702153224.json', 'var_function-call-3458438926277201531': 'file_storage/function-call-3458438926277201531.json', 'var_function-call-13207347577609905648': 'file_storage/function-call-13207347577609905648.json', 'var_function-call-2024195598409583868': 'file_storage/function-call-2024195598409583868.json', 'var_function-call-14921129906520279837': 'file_storage/function-call-14921129906520279837.json'}

exec(code, env_args)
