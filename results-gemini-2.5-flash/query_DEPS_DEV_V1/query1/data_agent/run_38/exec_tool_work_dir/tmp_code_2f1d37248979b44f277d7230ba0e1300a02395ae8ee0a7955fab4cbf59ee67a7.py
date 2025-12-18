code = """import pandas as pd
import re

latest_release_packages = pd.read_json(locals()['var_function-call-2139176942415530674'])
project_packageversion = pd.read_json(locals()['var_function-call-7421897730721124387'])
project_info = pd.read_json(locals()['var_function-call-13735147255475096839'])

# Merge latest_release_packages with project_packageversion
merged_packages = pd.merge(latest_release_packages, project_packageversion, on=['Name', 'Version'], how='inner')

# Extract ProjectName and Stars from Project_Information
def extract_project_details(project_information):
    # Regex to find project name in 'owner/repo' format
    project_name_match = re.search(r'(?:project|GitHub project|named) ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)', project_information)
    project_name = project_name_match.group(1) if project_name_match else None

    # Regex to find star count
    stars_match = re.search(r'(\d{1,3}(?:,\\d{3})*|\d+) stars', project_information)
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

# Apply the extraction function to create new columns
project_info_extracted = project_info['Project_Information'].apply(lambda x: pd.Series(extract_project_details(x), index=['ExtractedProjectName', 'Stars']))

# Combine with original project_info (keeping only relevant columns)
project_info_df = project_info_extracted.dropna(subset=['ExtractedProjectName'])

# Merge the dataframes
# We need to link `merged_packages.ProjectName` (from project_packageversion) with `project_info_df.ExtractedProjectName`
final_merged_df = pd.merge(merged_packages, project_info_df, left_on='ProjectName', right_on='ExtractedProjectName', how='inner')

# Drop duplicates based on package Name and Version, and ProjectName (to avoid multiple entries for same package/project combo)
final_merged_df = final_merged_df.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

# Sort by Stars in descending order and get the top 5
top_5_packages = final_merged_df.sort_values(by='Stars', ascending=False).head(5)

# Select the required columns for the final output
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14058135258420604114': 'file_storage/function-call-14058135258420604114.json', 'var_function-call-2139176942415530674': 'file_storage/function-call-2139176942415530674.json', 'var_function-call-7421897730721124387': 'file_storage/function-call-7421897730721124387.json', 'var_function-call-17641978269507743437': 'file_storage/function-call-17641978269507743437.json', 'var_function-call-13735147255475096839': 'file_storage/function-call-13735147255475096839.json'}

exec(code, env_args)
