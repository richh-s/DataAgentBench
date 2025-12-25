code = """import json
import pandas as pd
import re

# Load the merged data from the JSON file
with open(locals()['var_function-call-250625152414992415'], 'r') as f:
    merged_data = json.load(f)
df_merged = pd.DataFrame(merged_data)

# Load the project_info data from the JSON file
with open(locals()['var_function-call-8200592992837259740'], 'r') as f:
    project_info_data = json.load(f)
df_project_info = pd.DataFrame(project_info_data)

# Function to extract ProjectName and stars from Project_Information
def parse_project_info(info):
    project_name_match = re.search(r'The project (?:named )?([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)', info)
    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', info)
    project_name = project_name_match.group(1) if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

# Apply the parsing function to Project_Information
df_project_info[['ParsedProjectName', 'Stars']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(parse_project_info(x)))

# Merge with the previously merged DataFrame
final_merged_df = pd.merge(df_merged,
                           df_project_info[['ParsedProjectName', 'Stars']],
                           left_on='ProjectName',
                           right_on='ParsedProjectName',
                           how='inner')

# Drop duplicate ProjectName entries, keeping the one with the highest stars
final_merged_df = final_merged_df.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name', 'Version'])

# Sort by stars in descending order and get the top 5
top_5_packages = final_merged_df.sort_values(by='Stars', ascending=False).head(5)

# Select the desired columns for the final output
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10633105012564164927': 'file_storage/function-call-10633105012564164927.json', 'var_function-call-11853220714125296449': 'file_storage/function-call-11853220714125296449.json', 'var_function-call-11866910325374558453': 'file_storage/function-call-11866910325374558453.json', 'var_function-call-250625152414992415': 'file_storage/function-call-250625152414992415.json', 'var_function-call-11210701122410254638': 'file_storage/function-call-11210701122410254638.json', 'var_function-call-14781363690694402053': 'file_storage/function-call-14781363690694402053.json', 'var_function-call-15320682117982437166': ['project_info', 'project_packageversion'], 'var_function-call-8200592992837259740': 'file_storage/function-call-8200592992837259740.json'}

exec(code, env_args)
