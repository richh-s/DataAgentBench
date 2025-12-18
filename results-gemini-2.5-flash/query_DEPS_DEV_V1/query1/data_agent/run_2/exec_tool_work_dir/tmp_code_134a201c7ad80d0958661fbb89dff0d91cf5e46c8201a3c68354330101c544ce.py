code = """import json
import pandas as pd
import re

# Load the latest_releases from the previous step
with open(locals()['var_function-call-10745807278787046185'], 'r') as f:
    latest_releases_raw = json.load(f)
latest_releases_df = pd.DataFrame(latest_releases_raw)

# Load the project_packageversion data
with open(locals()['var_function-call-6715331795215155977'], 'r') as f:
    project_packageversion_raw = json.load(f)
project_packageversion_df = pd.DataFrame(project_packageversion_raw)

# Load the project_info data
with open(locals()['var_function-call-16511482794637801734'], 'r') as f:
    project_info_raw = json.load(f)
project_info_df = pd.DataFrame(project_info_raw)

# Merge the latest_releases with project_packageversion to get ProjectName
merged_package_project = pd.merge(latest_releases_df, project_packageversion_df, on=['Name', 'Version'], how='inner')

# Extract ProjectName from project_info_df if it's available and then merge
# First, create a temporary column in project_info_df for merging based on ProjectName from Project_Information
def extract_project_name_and_stars(project_info_str):
    project_name_match = re.search(r'The project (.+?) is hosted on GitHub', project_info_str) or \
                         re.search(r'The GitHub project named (.+?) currently has', project_info_str) or \
                         re.search(r'The project (.+?) on GitHub', project_info_str)
    stars_match = re.search(r'(\\d{1,3}(?:,\\d{3})*|\\d+) stars', project_info_str)
    
    project_name = project_name_match.group(1).strip() if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    
    return project_name, stars

project_info_df[['ExtractedProjectName', 'Stars']] = project_info_df['Project_Information'].apply(lambda x: pd.Series(extract_project_name_and_stars(x)))

# Rename ProjectName to avoid collision before merging
merged_package_project.rename(columns={'ProjectName': 'ProjectName_from_packageversion'}, inplace=True)

# Merge with project_info_df on the extracted project name
final_merged_df = pd.merge(merged_package_project,
                             project_info_df,
                             left_on='ProjectName_from_packageversion',
                             right_on='ExtractedProjectName',
                             how='inner')

# Group by package Name and Version, and find the max stars for each unique package (considering multiple repos for one package)
top_packages = final_merged_df.groupby(['Name', 'Version'])['Stars'].max().reset_index()

# Sort by stars in descending order and get the top 5
top_5_packages = top_packages.sort_values(by='Stars', ascending=False).head(5)

print("__RESULT__:")
print(top_5_packages.to_json(orient='records'))"""

env_args = {'var_function-call-3558731251827286140': 'file_storage/function-call-3558731251827286140.json', 'var_function-call-6339539474034341735': 'file_storage/function-call-6339539474034341735.json', 'var_function-call-14800795321996170339': {'status': 'success', 'original': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'parsed': {'IsRelease': True, 'Ordinal': 29}}, 'var_function-call-10745807278787046185': 'file_storage/function-call-10745807278787046185.json', 'var_function-call-6715331795215155977': 'file_storage/function-call-6715331795215155977.json', 'var_function-call-17343008165287654667': 'file_storage/function-call-17343008165287654667.json', 'var_function-call-16511482794637801734': 'file_storage/function-call-16511482794637801734.json'}

exec(code, env_args)
