code = """import pandas as pd
import json
import re

latest_release_packages_with_project_name = pd.read_json(locals()['var_function-call-11456817341887634201'])
project_info_data = pd.read_json(locals()['var_function-call-16578603252911124814'])

def extract_project_name_and_stars(project_info_str):
    project_name_match = re.search(r'The project ([^\s/]+/[^\s]+) on GitHub', project_info_str)
    stars_match = re.search(r'stars, and (\d+) forks', project_info_str)
    
    project_name = project_name_match.group(1) if project_name_match else None
    stars = int(stars_match.group(1)) if stars_match else 0
    return project_name, stars

# Apply the function to extract ProjectName and Stars
project_info_data[['ProjectName', 'Stars']] = project_info_data['Project_Information'].apply(lambda x: pd.Series(extract_project_name_and_stars(x)))

# Merge the dataframes on ProjectName
merged_data = pd.merge(
    latest_release_packages_with_project_name,
    project_info_data[['ProjectName', 'Stars']],
    on='ProjectName',
    how='inner'
)

# Drop duplicate ProjectName entries, keeping the first (as package_info already filters latest version)
merged_data_unique_projects = merged_data.drop_duplicates(subset=['ProjectName'])

# Sort by Stars in descending order and get the top 5
top_5_packages = merged_data_unique_projects.sort_values(by='Stars', ascending=False).head(5)

result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2542952245398537233': ['packageinfo'], 'var_function-call-10417754161782902564': 'file_storage/function-call-10417754161782902564.json', 'var_function-call-5524596830193667260': 'file_storage/function-call-5524596830193667260.json', 'var_function-call-1109682220278830328': ['project_info', 'project_packageversion'], 'var_function-call-4454470930749183033': 'file_storage/function-call-4454470930749183033.json', 'var_function-call-11456817341887634201': 'file_storage/function-call-11456817341887634201.json', 'var_function-call-16578603252911124814': 'file_storage/function-call-16578603252911124814.json'}

exec(code, env_args)
