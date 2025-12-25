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

# Function to extract ProjectName (owner/repo) and Stars
def extract_project_details(project_info_text):
    project_name = None
    stars = 0
    if isinstance(project_info_text, str):
        # Regex to find 'owner/repo' pattern in the text
        # This assumes the project name is usually after 'The project ' and before ' is hosted on GitHub'
        # or directly recognizable as owner/repo pattern in other descriptions.
        project_name_match = re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)', project_info_text)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
        else:
            # A fallback if the first regex doesn't match, look for owner/repo pattern anywhere
            owner_repo_match = re.search(r'([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)', project_info_text)
            if owner_repo_match:
                project_name = owner_repo_match.group(1).strip()

        stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', project_info_text)
        if stars_match:
            stars = int(stars_match.group(1).replace(',', ''))
    return project_name, stars

# Apply the extraction function
df_project_info[['ProjectName', 'Stars']] = df_project_info['Project_Information'].apply(extract_project_details).apply(pd.Series)

# Drop rows where ProjectName couldn't be extracted
df_project_info.dropna(subset=['ProjectName'], inplace=True)

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
