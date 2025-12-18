code = """import pandas as pd
import json
import re

# Load packageinfo data
packageinfo_data_path = locals()['var_function-call-18266025669230000881']
with open(packageinfo_data_path, 'r') as f:
    packageinfo_data = json.load(f)
df_packageinfo = pd.DataFrame(packageinfo_data)

# Filter for NPM packages and parse VersionInfo
df_packageinfo = df_packageinfo[df_packageinfo['System'] == 'NPM'].copy()
df_packageinfo['VersionInfo'] = df_packageinfo['VersionInfo'].apply(json.loads)

# Filter for releases and extract Ordinal
df_packageinfo = df_packageinfo[df_packageinfo['VersionInfo'].apply(lambda x: x.get('IsRelease', False))]
df_packageinfo['Ordinal'] = df_packageinfo['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Find the latest version for each package
latest_versions = df_packageinfo.loc[df_packageinfo.groupby('Name')['Ordinal'].idxmax()]
latest_versions = latest_versions[['Name', 'Version', 'System']]

# Load project_packageversion data
project_packageversion_data_path = locals()['var_function-call-6178734886903610851']
with open(project_packageversion_data_path, 'r') as f:
    project_packageversion_data = json.load(f)
df_project_packageversion = pd.DataFrame(project_packageversion_data)

# Merge latest versions with project_packageversion
merged_df = pd.merge(latest_versions, df_project_packageversion, on=['Name', 'Version', 'System'], how='inner')

# Load project_info data
project_info_data_path = locals()['var_function-call-166425299707613856']
with open(project_info_data_path, 'r') as f:
    project_info_data = json.load(f)
df_project_info = pd.DataFrame(project_info_data)

# Extract ProjectName and stars from Project_Information
def extract_project_info(project_information):
    project_name_match = re.search(r'The project ([^\s/]+/[^\s]+) is hosted on GitHub', project_information)
    if not project_name_match:
        project_name_match = re.search(r'The GitHub project named ([^\s/]+/[^\s]+)', project_information)
    if not project_name_match:
        project_name_match = re.search(r'The project named ([^\s/]+/[^\s]+) on GitHub', project_information)
    if not project_name_match:
        project_name_match = re.search(r'The project ([^\s/]+/[^\s]+) on GitHub', project_information)
    if not project_name_match:
        project_name_match = re.search(r'The project is a GitHub repository named ([^\s/]+/[^\s]+)', project_information)

    project_name = project_name_match.group(1) if project_name_match else None

    stars_match = re.search(r'stars count of (\d+)', project_information)
    if not stars_match:
        stars_match = re.search(r'has (\d+) stars', project_information)
    if not stars_match:
        stars_match = re.search(r'total of (\d+),? stars', project_information)
    if not stars_match:
        stars_match = re.search(r'received (\d+) stars', project_information)
    
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

df_project_info[['ProjectName_extracted', 'Stars']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(extract_project_info(x)))

# Merge with project_info based on ProjectName
final_df = pd.merge(merged_df, df_project_info, left_on='ProjectName', right_on='ProjectName_extracted', how='inner')

# Sort by stars and get top 5
top_5_packages = final_df.sort_values(by='Stars', ascending=False).head(5)

# Select desired output columns
result = top_5_packages[['Name', 'Version', 'Stars']]

print('__RESULT__:')
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-10744039473036088012': ['packageinfo'], 'var_function-call-16529299900424573549': 'file_storage/function-call-16529299900424573549.json', 'var_function-call-137916510950457112': ['project_info', 'project_packageversion'], 'var_function-call-6178734886903610851': 'file_storage/function-call-6178734886903610851.json', 'var_function-call-18266025669230000881': 'file_storage/function-call-18266025669230000881.json', 'var_function-call-166425299707613856': 'file_storage/function-call-166425299707613856.json'}

exec(code, env_args)
