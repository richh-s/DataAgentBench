code = """import pandas as pd
import json
import re

merged_packages_projects_path = locals()['var_function-call-2841072566522271773']
with open(merged_packages_projects_path, 'r') as f:
    merged_packages_projects = json.load(f)
df_merged_packages_projects = pd.DataFrame(merged_packages_projects)

project_info_path = locals()['var_function-call-13736190906264197990']
with open(project_info_path, 'r') as f:
    project_info = json.load(f)
df_project_info = pd.DataFrame(project_info)

# Function to extract ProjectName and Forks from Project_Information
def extract_project_info_robust(info_string):
    project_name = None
    forks = None

    # Extract forks count
    forks_match = re.search(r'forks count of (\d+)', info_string)
    if forks_match:
        forks = int(forks_match.group(1))

    # Extract ProjectName (owner/repo format)
    # This regex tries to find 'owner/repo' that is typically found after "project " or "named " and before " on GitHub"
    project_name_match = re.search(r'(?:project|named) ([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+) on GitHub', info_string)
    if project_name_match:
        project_name = project_name_match.group(1)
    else:
        # Fallback for cases where "project" or "named" might not be present or in a different format
        # It tries to find a pattern that looks like "owner/repo"
        project_name_match = re.search(r'([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+)(?: is hosted on GitHub| on GitHub| currently has)', info_string)
        if project_name_match:
            project_name = project_name_match.group(1)

    return project_name, forks

df_project_info[['ExtractedProjectName', 'Forks']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(extract_project_info_robust(x)))

df_project_info_filtered = df_project_info.dropna(subset=['ExtractedProjectName', 'Forks'])

# Merge with the filtered packages
final_merged_df = pd.merge(df_merged_packages_projects, df_project_info_filtered, left_on='ProjectName', right_on='ExtractedProjectName', how='inner')

# Sort by forks and get top 5, ensuring unique project names
top_5_projects = final_merged_df.sort_values(by='Forks', ascending=False).drop_duplicates(subset=['ProjectName']).head(5)

result = top_5_projects[['ProjectName', 'Forks']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10134544977520819277': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-11799025015653969009': 'file_storage/function-call-11799025015653969009.json', 'var_function-call-13040228337869759428': 'file_storage/function-call-13040228337869759428.json', 'var_function-call-2951311016274759351': 'file_storage/function-call-2951311016274759351.json', 'var_function-call-2841072566522271773': 'file_storage/function-call-2841072566522271773.json', 'var_function-call-13736190906264197990': 'file_storage/function-call-13736190906264197990.json'}

exec(code, env_args)
