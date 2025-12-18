code = """import json
import pandas as pd
import re

# Load data from previous steps
with open(locals()['var_function-call-2922338494650105706'], 'r') as f:
    df_project_names_data = json.load(f)
with open(locals()['var_function-call-4428353759157367123'], 'r') as f:
    project_info_data = json.load(f)

df_project_names = pd.DataFrame(df_project_names_data)
df_project_info = pd.DataFrame(project_info_data)

# Extract ProjectName and Stars from Project_Information
def extract_project_info(project_info_text):
    project_name_match = re.search(r'The project (.+?) is hosted on GitHub', project_info_text)
    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', project_info_text)
    
    project_name = project_name_match.group(1).strip() if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

# Apply the extraction function to create new columns
df_project_info[['ExtractedProjectName', 'Stars']] = df_project_info['Project_Information'].apply(extract_project_info).apply(pd.Series)

# Clean ExtractedProjectName to match the format in df_project_names
df_project_info['ExtractedProjectName'] = df_project_info['ExtractedProjectName'].apply(lambda x: x.split('/', 1)[-1].strip() if x else None)

# Drop rows where ExtractedProjectName is None
df_project_info.dropna(subset=['ExtractedProjectName'], inplace=True)

# Create a new ProjectName field by combining owner and repo for project_info, to be matched with ProjectName from project_packageversion
def normalize_project_name(project_name_full):
    if project_name_full:
        parts = project_name_full.split('/')
        if len(parts) >= 2:
            return f'{parts[0].strip()}/{parts[1].strip()}'
    return None

df_project_info['ProjectName'] = df_project_info['ExtractedProjectName'].apply(normalize_project_name)

# Merge df_project_names with project_info to get star counts
df_final_merge = pd.merge(df_project_names, df_project_info[['ProjectName', 'Stars']], on='ProjectName', how='inner')

# Group by package name and version, and sum the stars (in case a package version maps to multiple projects)
df_grouped = df_final_merge.groupby(['Name', 'Version'])['Stars'].sum().reset_index()

# Sort by stars in descending order and get the top 5
top_5_packages = df_grouped.sort_values(by='Stars', ascending=False).head(5)

print('__RESULT__:')
print(top_5_packages.to_json(orient='records'))"""

env_args = {'var_function-call-14123670748196616046': 'file_storage/function-call-14123670748196616046.json', 'var_function-call-423390990085849329': 'file_storage/function-call-423390990085849329.json', 'var_function-call-14968345244815715450': 'file_storage/function-call-14968345244815715450.json', 'var_function-call-2922338494650105706': 'file_storage/function-call-2922338494650105706.json', 'var_function-call-4428353759157367123': 'file_storage/function-call-4428353759157367123.json'}

exec(code, env_args)
