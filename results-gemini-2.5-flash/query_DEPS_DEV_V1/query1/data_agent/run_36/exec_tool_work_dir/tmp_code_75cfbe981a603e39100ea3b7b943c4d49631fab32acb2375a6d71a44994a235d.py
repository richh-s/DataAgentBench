code = """import pandas as pd
import re
import json

project_links = pd.read_json(locals()['var_function-call-16487132357101574628'])
project_info_data = pd.read_json(locals()['var_function-call-16018689579009619391'])

# Extract ProjectName from Project_Information to match with project_links
def extract_project_name(project_info_string):
    match = re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+) on GitHub', project_info_string)
    if match:
        return match.group(1)
    match = re.search(r'The GitHub project named ([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)', project_info_string)
    if match:
        return match.group(1)
    match = re.search(r'The project is hosted on GitHub under the name ([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)', project_info_string)
    if match:
        return match.group(1)
    return None

project_info_data['ProjectName'] = project_info_data['Project_Information'].apply(extract_project_name)

# Extract star count
def extract_stars(project_info_string):
    match = re.search(r'stars count of ([0-9,]+)', project_info_string)
    if match:
        return int(match.group(1).replace(',', ''))
    match = re.search(r'([0-9,]+) stars', project_info_string)
    if match:
        return int(match.group(1).replace(',', ''))
    return 0

project_info_data['Stars'] = project_info_data['Project_Information'].apply(extract_stars)

# Merge project_links with project_info to get star count for each package
final_merged_data = pd.merge(project_links,
                             project_info_data[['ProjectName', 'Stars']],
                             on='ProjectName',
                             how='inner')

# Drop duplicates, keeping the entry with the highest stars if multiple projects link to the same package
final_merged_data = final_merged_data.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name'])

# Sort by stars and get the top 5
top_5_packages = final_merged_data.nlargest(5, 'Stars')

# Select the required columns for the final answer
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4269963862347431448': ['packageinfo'], 'var_function-call-7766504306822188940': 'file_storage/function-call-7766504306822188940.json', 'var_function-call-8167732489261780147': 'file_storage/function-call-8167732489261780147.json', 'var_function-call-4108480433027455811': 'file_storage/function-call-4108480433027455811.json', 'var_function-call-16487132357101574628': 'file_storage/function-call-16487132357101574628.json', 'var_function-call-16018689579009619391': 'file_storage/function-call-16018689579009619391.json'}

exec(code, env_args)
