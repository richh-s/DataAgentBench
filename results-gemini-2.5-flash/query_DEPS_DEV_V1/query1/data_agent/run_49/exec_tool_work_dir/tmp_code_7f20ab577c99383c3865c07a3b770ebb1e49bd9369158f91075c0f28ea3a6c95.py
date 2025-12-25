code = """import json
import pandas as pd
import re

# Load latest releases data
with open(locals()['var_function-call-16586323392008278469'], 'r') as f:
    latest_releases = pd.DataFrame(json.load(f))

# Load project_packageversion data
with open(locals()['var_function-call-15194476211329142731'], 'r') as f:
    project_packageversion = pd.DataFrame(json.load(f))

# Load project_info data
with open(locals()['var_function-call-11605755017189908268'], 'r') as f:
    project_info = pd.DataFrame(json.load(f))

# Merge latest_releases with project_packageversion to get ProjectName
merged_df = pd.merge(latest_releases, project_packageversion, on=['System', 'Name', 'Version'], how='inner')

# Extract ProjectName and Stars from Project_Information
def extract_github_info(project_info_str):
    project_name = None
    stars = 0
    
    # Try to extract project name from two common patterns
    project_name_match_1 = re.search(r'The project (.+?) on GitHub', project_info_str)
    project_name_match_2 = re.search(r'The GitHub project named (.+?) currently', project_info_str)

    if project_name_match_1:
        project_name = project_name_match_1.group(1)
    elif project_name_match_2:
        project_name = project_name_match_2.group(1)

    # Try to extract stars count from two common patterns
    stars_match_1 = re.search(r'stars count of (\d+)', project_info_str)
    stars_match_2 = re.search(r'(\d+)\s*stars', project_info_str)

    if stars_match_1:
        stars = int(stars_match_1.group(1))
    elif stars_match_2:
        stars = int(stars_match_2.group(1).replace(',', ''))
        
    return project_name, stars

project_info[['ExtractedProjectName', 'Stars']] = project_info['Project_Information'].apply(lambda x: pd.Series(extract_github_info(x)))

# Merge with project_info on ProjectName
final_df = pd.merge(merged_df, project_info, left_on='ProjectName', right_on='ExtractedProjectName', how='inner')

# Sort by Stars and get top 5
top_5_packages = final_df.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

# Select desired columns for output
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-7931738845791159468': 'file_storage/function-call-7931738845791159468.json', 'var_function-call-16586323392008278469': 'file_storage/function-call-16586323392008278469.json', 'var_function-call-15194476211329142731': 'file_storage/function-call-15194476211329142731.json', 'var_function-call-11605755017189908268': 'file_storage/function-call-11605755017189908268.json'}

exec(code, env_args)
