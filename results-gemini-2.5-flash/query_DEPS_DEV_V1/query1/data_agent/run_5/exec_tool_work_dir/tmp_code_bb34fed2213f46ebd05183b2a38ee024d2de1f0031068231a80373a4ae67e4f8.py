code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-819794979649356386'], 'r') as f:
    df_project_names_data = json.load(f)
with open(locals()['var_function-call-12915621300755632550'], 'r') as f:
    project_info_data = json.load(f)

df_project_names = pd.DataFrame(df_project_names_data)
df_project_info = pd.DataFrame(project_info_data)

# Function to extract ProjectName and stars from Project_Information
def parse_project_info(project_info_str):
    project_name_match = re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)', project_info_str)
    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', project_info_str)

    project_name = project_name_match.group(1) if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

# Apply the parsing function to create new columns
df_project_info[['ParsedProjectName', 'Stars']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(parse_project_info(x)))

# Filter out rows where ParsedProjectName is None
df_project_info_filtered = df_project_info.dropna(subset=['ParsedProjectName'])

# Merge with the project names DataFrame
df_final = pd.merge(df_project_names,
                    df_project_info_filtered[['ParsedProjectName', 'Stars']],
                    left_on='ProjectName',
                    right_on='ParsedProjectName',
                    how='inner')

# Sort by stars and get top 5 unique packages
top_5_packages = df_final.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

# Select desired output columns
result = top_5_packages[['Name', 'Version', 'Stars']]

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-8060708402497588293': 'file_storage/function-call-8060708402497588293.json', 'var_function-call-9499888413576322647': 'file_storage/function-call-9499888413576322647.json', 'var_function-call-12126072723896480889': 'file_storage/function-call-12126072723896480889.json', 'var_function-call-819794979649356386': 'file_storage/function-call-819794979649356386.json', 'var_function-call-12915621300755632550': 'file_storage/function-call-12915621300755632550.json'}

exec(code, env_args)
