code = """import pandas as pd
import json
import re

package_info = pd.read_json(locals()["var_function-call-11593268329304202645"])
project_package_version = pd.read_json(locals()["var_function-call-349226744254838744"])
project_info = pd.read_json(locals()["var_function-call-560584618969081478"])

# Merge package_info and project_package_version
merged_packages_projects = pd.merge(package_info, project_package_version, on=['System', 'Name', 'Version'], how='inner')

# Extract ProjectName and fork count from project_info
def extract_github_info(project_information):
    match_name = re.search(r'github.com/([a-zA-Z0-9-]+/[a-zA-Z0-9-._]+)', project_information)
    match_forks = re.search(r'(\d+,?\d*)\sforks', project_information)
    project_name = match_name.group(1) if match_name else None
    forks = int(match_forks.group(1).replace(',', '')) if match_forks else 0
    return project_name, forks

project_info_extracted = pd.DataFrame(project_info['Project_Information'].apply(lambda x: extract_github_info(x)).tolist(), columns=['ExtractedProjectName', 'ForkCount'])
project_info_extracted = project_info_extracted.dropna(subset=['ExtractedProjectName'])

# Get unique project names from the merged packages and projects
unique_merged_project_names = merged_packages_projects['ProjectName'].unique()

# Filter project_info_extracted to only include projects that are in our unique_merged_project_names
filtered_project_info = project_info_extracted[project_info_extracted['ExtractedProjectName'].isin(unique_merged_project_names)]

# Aggregate fork counts by project name, taking the maximum fork count if there are duplicates
project_fork_counts = filtered_project_info.groupby('ExtractedProjectName')['ForkCount'].max().reset_index()

# Sort by ForkCount in descending order and get the top 5
top_5_projects = project_fork_counts.sort_values(by='ForkCount', ascending=False).head(5)

# Debugging prints
print("__RESULT__:")
print(json.dumps({
    'merged_packages_projects_head': merged_packages_projects.head().to_dict(orient='records'),
    'project_info_extracted_head': project_info_extracted.head().to_dict(orient='records'),
    'len_unique_merged_project_names': len(unique_merged_project_names.tolist()),
    'len_filtered_project_info': len(filtered_project_info),
    'top_5_projects': top_5_projects.to_dict(orient='records')
}))"""

env_args = {'var_function-call-11593268329304202645': 'file_storage/function-call-11593268329304202645.json', 'var_function-call-349226744254838744': 'file_storage/function-call-349226744254838744.json', 'var_function-call-3330939106958871434': 'Querying all project_info is the next logical step.', 'var_function-call-560584618969081478': 'file_storage/function-call-560584618969081478.json', 'var_function-call-11071353427662756646': [], 'var_function-call-17021948697438999425': []}

exec(code, env_args)
