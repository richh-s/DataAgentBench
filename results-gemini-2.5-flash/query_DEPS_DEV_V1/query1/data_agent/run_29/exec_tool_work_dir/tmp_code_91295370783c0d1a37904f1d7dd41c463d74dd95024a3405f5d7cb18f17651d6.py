code = """import pandas as pd
import re
import json

latest_release_packages_with_project = pd.read_json(locals()['var_function-call-5870560127057394999'])
project_info_data = pd.read_json(locals()['var_function-call-11437625441987451787'])

# Extract ProjectName from Project_Information for joining
project_info_data['ProjectName'] = project_info_data['Project_Information'].apply(lambda x: re.search(r'The project (.+?) on GitHub|', x).group(1))
project_info_data['ProjectName'] = project_info_data['ProjectName'].apply(lambda x: x.split(' is hosted on GitHub')[0] if x else None)


# Extract stars from Project_Information
def extract_stars(info):
    match = re.search(r'stars count of (\d+)|(\d+) stars', info)
    if match:
        return int(match.group(1) or match.group(2))
    return 0

project_info_data['Stars'] = project_info_data['Project_Information'].apply(extract_stars)

# Merge to get stars for each package
merged_data = pd.merge(latest_release_packages_with_project, project_info_data, on='ProjectName', how='left')

# Sort by stars and get top 5 unique packages with their latest version
top_5_packages = merged_data.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

# Select and format the final result
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4961496144865610435': 'file_storage/function-call-4961496144865610435.json', 'var_function-call-18282496109456010527': 'file_storage/function-call-18282496109456010527.json', 'var_function-call-3407010709341932649': 'file_storage/function-call-3407010709341932649.json', 'var_function-call-5870560127057394999': 'file_storage/function-call-5870560127057394999.json', 'var_function-call-11437625441987451787': 'file_storage/function-call-11437625441987451787.json'}

exec(code, env_args)
