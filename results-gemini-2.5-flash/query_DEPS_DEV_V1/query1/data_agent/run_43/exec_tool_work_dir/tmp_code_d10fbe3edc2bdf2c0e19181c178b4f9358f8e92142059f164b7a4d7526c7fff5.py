code = """import json
import pandas as pd
import re

project_names_df = pd.read_json(locals()['var_function-call-1874775251536209977'])
project_info = pd.read_json(locals()['var_function-call-17993832017128958570'])

# Extract ProjectName from Project_Information
def extract_project_name(project_info_str):
    match = re.search(r'The project ([^\s/]+/[^\s]+) on GitHub', project_info_str)
    if match:
        return match.group(1)
    match = re.search(r'The GitHub project named ([^\s/]+/[^\s]+)', project_info_str)
    if match:
        return match.group(1)
    match = re.search(r'The project ([^\s/]+/[^\s]+) is hosted on GitHub', project_info_str)
    if match:
        return match.group(1)
    match = re.search(r'The project is a GitHub repository named ([^\s/]+/[^\s]+),', project_info_str)
    if match:
        return match.group(1)
    return None

def extract_stars(project_info_str):
    match = re.search(r'stars count of ([0-9,]+)', project_info_str)
    if match:
        return int(match.group(1).replace(',', ''))
    match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', project_info_str)
    if match:
        return int(match.group(1).replace(',', ''))
    return 0

project_info['ProjectName_extracted'] = project_info['Project_Information'].apply(extract_project_name)
project_info['Stars'] = project_info['Project_Information'].apply(extract_stars)

# Filter out rows where ProjectName_extracted is None and drop duplicates
project_info_filtered = project_info.dropna(subset=['ProjectName_extracted']).drop_duplicates(subset=['ProjectName_extracted'])

# Merge with project_names_df
final_df = pd.merge(project_names_df, project_info_filtered, left_on='ProjectName', right_on='ProjectName_extracted', how='inner')

# Sort by stars and get top 5
top_5_packages = final_df.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14514614563328429382': 'file_storage/function-call-14514614563328429382.json', 'var_function-call-16376705841661688536': 'file_storage/function-call-16376705841661688536.json', 'var_function-call-7731484911699807901': 'file_storage/function-call-7731484911699807901.json', 'var_function-call-1874775251536209977': 'file_storage/function-call-1874775251536209977.json', 'var_function-call-17993832017128958570': 'file_storage/function-call-17993832017128958570.json'}

exec(code, env_args)
