code = """import json
import pandas as pd
import re

latest_versions_path = locals()['var_function-call-6736456767449372573']
with open(latest_versions_path, 'r') as f:
    latest_versions = json.load(f)

df_latest_versions = pd.DataFrame(latest_versions)

package_project_path = locals()['var_function-call-4903430011242550830']
with open(package_project_path, 'r') as f:
    package_project = json.load(f)

df_package_project = pd.DataFrame(package_project)

project_info_path = locals()['var_function-call-17144170111151454078']
with open(project_info_path, 'r') as f:
    project_info = json.load(f)

df_project_info = pd.DataFrame(project_info)

# Merge latest_versions with project_packageversion
df_merged_packages = pd.merge(df_latest_versions, df_package_project, on=['Name', 'Version'], how='inner')

def parse_project_info(project_info_string):
    project_name_match = re.search(r'The project (.*?) on GitHub', project_info_string) or \
                         re.search(r'The GitHub project named (.*?) currently has', project_info_string) or \
                         re.search(r'The project named (.*?) is hosted on GitHub', project_info_string) or \
                         re.search(r'The project (.*?) is hosted on GITHUB', project_info_string)

    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s*stars', project_info_string)

    project_name = project_name_match.group(1).strip() if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

# Apply the parsing function to create new columns
df_project_info[['ProjectName_parsed', 'Stars']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(parse_project_info(x)))

# Filter out rows where ProjectName_parsed is None
df_project_info_filtered = df_project_info[df_project_info['ProjectName_parsed'].notna()]

# Merge with project_info using the parsed ProjectName
df_final_merge = pd.merge(df_merged_packages, df_project_info_filtered, left_on='ProjectName', right_on='ProjectName_parsed', how='inner')

# Sort by stars and get top 5, considering distinct packages and their latest versions
top_5_packages = df_final_merge.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

print("__RESULT__:")
print(top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records'))"""

env_args = {'var_function-call-5263700515361630309': 'file_storage/function-call-5263700515361630309.json', 'var_function-call-6736456767449372573': 'file_storage/function-call-6736456767449372573.json', 'var_function-call-4903430011242550830': 'file_storage/function-call-4903430011242550830.json', 'var_function-call-1747811955003797846': 'file_storage/function-call-1747811955003797846.json', 'var_function-call-8251494281848279597': ['project_info', 'project_packageversion'], 'var_function-call-17144170111151454078': 'file_storage/function-call-17144170111151454078.json'}

exec(code, env_args)
