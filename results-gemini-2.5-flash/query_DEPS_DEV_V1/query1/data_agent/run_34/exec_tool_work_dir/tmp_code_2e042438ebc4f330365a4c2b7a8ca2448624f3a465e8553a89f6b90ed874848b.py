code = """import pandas as pd
import re
import json

latest_versions = pd.read_json(locals()['var_function-call-17265720179471351159'])
project_packageversion = pd.read_json(locals()['var_function-call-4412461587474726199'])
project_info = pd.read_json(locals()['var_function-call-16654197820230102275'])

# Extract ProjectName from Project_Information, assuming the format 'The project owner/repo on GitHub'
# Sometimes the ProjectName might be within the Project_Information, sometimes it's not present.
# We will try to extract it from 'Project_Information' first, and if not present, try to construct it from Homepage.
project_info['ExtractedProjectName'] = project_info['Project_Information'].apply(lambda x: re.search(r'The project ([a-zA-Z0-9-]+/[a-zA-Z0-9-._]+) on GitHub', x).group(1) if re.search(r'The project ([a-zA-Z0-9-]+/[a-zA-Z0-9-._]+) on GitHub', x) else None)

# If ExtractedProjectName is still None, try to extract from Homepage for well-known GitHub patterns
project_info['ExtractedProjectName'] = project_info.apply(lambda row: row['ExtractedProjectName'] if row['ExtractedProjectName'] else (
    re.search(r'https?://github.com/([a-zA-Z0-9-]+/[a-zA-Z0-9-._]+)', row['Homepage']).group(1) if pd.notnull(row['Homepage']) and re.search(r'https?://github.com/([a-zA-Z0-9-]+/[a-zA-Z0-9-._]+)', row['Homepage']) else None
), axis=1)

# Extract star count from Project_Information
project_info['Stars'] = project_info['Project_Information'].apply(lambda x: int(re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', x.replace(',', '')).group(1)) if re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', x.replace(',', '')) else 0)

# Filter out rows where ExtractedProjectName is None and drop duplicates
project_info_filtered = project_info.dropna(subset=['ExtractedProjectName']).drop_duplicates(subset=['ExtractedProjectName'])

# Merge with the latest versions and package-project links
merged_df = pd.merge(latest_versions, project_packageversion, on=['Name', 'Version'], how='inner')
final_df = pd.merge(merged_df, project_info_filtered, left_on='ProjectName', right_on='ExtractedProjectName', how='inner')

# Select distinct packages with the highest star count
top_packages = final_df.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name'])

# Get the top 5
final_result = top_packages.head(5)[['Name', 'Version', 'Stars']].to_json(orient='records')

print("__RESULT__:")
print(final_result)"""

env_args = {'var_function-call-16604940366570429364': 'file_storage/function-call-16604940366570429364.json', 'var_function-call-17265720179471351159': 'file_storage/function-call-17265720179471351159.json', 'var_function-call-4412461587474726199': 'file_storage/function-call-4412461587474726199.json', 'var_function-call-14824657385659779511': 'file_storage/function-call-14824657385659779511.json', 'var_function-call-11155285134186140264': ['project_info', 'project_packageversion'], 'var_function-call-16654197820230102275': 'file_storage/function-call-16654197820230102275.json'}

exec(code, env_args)
