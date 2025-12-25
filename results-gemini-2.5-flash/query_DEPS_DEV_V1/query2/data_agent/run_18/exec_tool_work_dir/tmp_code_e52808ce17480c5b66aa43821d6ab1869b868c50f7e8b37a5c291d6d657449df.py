code = """import pandas as pd
import json
import re

# Load data from storage keys
packageinfo_df = pd.read_json(locals()['var_function-call-9646753308636010247'])
project_packageversion_df = pd.read_json(locals()['var_function-call-937077842083223208'])
project_info_df = pd.read_json(locals()['var_function-call-7358335479007081136'])

# Filter packageinfo for NPM, MIT license, and IsRelease = true
# (This was already done in the SQL query, but re-filtering to be safe if data comes from file)
packageinfo_df = packageinfo_df[
    (packageinfo_df['Licenses'].str.contains('MIT')) &
    (packageinfo_df['VersionInfo'].str.contains('"IsRelease": true'))
]

# Merge packageinfo with project_packageversion on Name and Version
merged_package_project_df = pd.merge(packageinfo_df, project_packageversion_df, on=['Name', 'Version'], how='inner')

# Extract unique ProjectName values from the merged dataframe
unique_project_names = merged_package_project_df['ProjectName'].unique()

# Filter project_info to include only relevant projects
# project_info_df is a list of dicts, and Project_Information contains the project name in string
# So we need to parse Project_Information to get the actual project name (owner/repo)

def extract_github_repo(project_info_str):
    match = re.search(r'The project (?:named )?([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+) on GitHub', project_info_str)
    if match:
        return match.group(1)
    return None

project_info_df['ExtractedProjectName'] = project_info_df['Project_Information'].apply(extract_github_repo)

# Filter project_info_df to include only projects that match the unique_project_names
filtered_project_info_df = project_info_df[project_info_df['ExtractedProjectName'].isin(unique_project_names)]

# Function to extract fork count from Project_Information
def extract_fork_count(project_info_str):
    match = re.search(r'forks: (\d+)', project_info_str)
    if match:
        return int(match.group(1))
    return 0

# Apply the function to create a new 'ForkCount' column
filtered_project_info_df['ForkCount'] = filtered_project_info_df['Project_Information'].apply(extract_fork_count)

# Sort by ForkCount in descending order and get the top 5 unique projects
top_5_projects = filtered_project_info_df.sort_values(by='ForkCount', ascending=False).drop_duplicates(subset=['ExtractedProjectName']).head(5)

# Format the output
result = []
for index, row in top_5_projects.iterrows():
    result.append(f"{row['ExtractedProjectName']} (Forks: {row['ForkCount']})")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9550500136309637979': ['project_info', 'project_packageversion'], 'var_function-call-9646753308636010247': 'file_storage/function-call-9646753308636010247.json', 'var_function-call-937077842083223208': 'file_storage/function-call-937077842083223208.json', 'var_function-call-8194439917375433551': 'file_storage/function-call-8194439917375433551.json', 'var_function-call-16374127340173290672': [], 'var_function-call-17411513133372805238': 'file_storage/function-call-17411513133372805238.json', 'var_function-call-11625479866658419654': 'file_storage/function-call-11625479866658419654.json', 'var_function-call-16580001182551188191': 'file_storage/function-call-16580001182551188191.json', 'var_function-call-7358335479007081136': 'file_storage/function-call-7358335479007081136.json'}

exec(code, env_args)
