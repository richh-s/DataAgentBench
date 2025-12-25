code = """import pandas as pd
import json

# Load the packageinfo data (from the first query result)
packageinfo_df = pd.read_json(locals()['var_function-call-18347306469434442166'])

# Load project_packageversion data (from the second query result)
project_packageversion_df = pd.read_json(locals()['var_function-call-15493387386679942922'])

# Load all project_info data (from the third query result)
project_info_all_df = pd.read_json(locals()['var_function-call-6369501038865689294'])

# Ensure 'Project_Information' is a string in project_info_all_df
project_info_all_df['Project_Information'] = project_info_all_df['Project_Information'].astype(str)

# Select relevant columns for the first merge
packageinfo_df_filtered = packageinfo_df[['System', 'Name', 'Version']]

# Merge packageinfo with project_packageversion
merged_package_project_df = pd.merge(packageinfo_df_filtered, project_packageversion_df, on=['System', 'Name', 'Version'], how='inner')

# Extract ProjectName from Project_Information in project_info_all_df
def extract_project_name_from_info(project_info_str):
    if not project_info_str:
        return None
    try:
        # Assuming Project_Information is a string like "The project owner/repo is hosted on GitHub..."
        # Or, if it's a JSON string, try to parse it and get 'Name'
        if project_info_str.startswith('{'):
            info_json = json.loads(project_info_str)
            if 'Name' in info_json:
                return info_json['Name']
        # Fallback to string parsing if not a JSON or 'Name' not found
        parts = project_info_str.split('project ', 1)
        if len(parts) > 1:
            project_part = parts[1].split(' is hosted', 1)[0]
            if '/' in project_part:
                return project_part.strip()
    except json.JSONDecodeError:
        pass
    return None

def extract_fork_count(project_info_str):
    if not project_info_str:
        return None
    try:
        # Check if the string is a valid JSON first
        if project_info_str.startswith('{') and project_info_str.endswith('}'):
            project_info_json = json.loads(project_info_str)
            return project_info_json.get('ForkCount')
        # If not a JSON, try to extract from the descriptive string
        import re
        match = re.search(r'and (\d+) forks', project_info_str)
        if match:
            return int(match.group(1))
    except (json.JSONDecodeError, ValueError):
        pass
    return None

project_info_all_df['ProjectName_extracted'] = project_info_all_df['Project_Information'].apply(extract_project_name_from_info)
project_info_all_df['ForkCount'] = project_info_all_df['Project_Information'].apply(extract_fork_count)

# Filter out rows where ProjectName_extracted or ForkCount are None
project_info_filtered_df = project_info_all_df.dropna(subset=['ProjectName_extracted', 'ForkCount'])

# Merge the filtered package/project data with project_info_filtered_df
# We need to ensure that the ProjectName in merged_package_project_df matches ProjectName_extracted in project_info_filtered_df
final_merged_df = pd.merge(
    merged_package_project_df,
    project_info_filtered_df,
    left_on='ProjectName',
    right_on='ProjectName_extracted',
    how='inner'
)

# Sort by ForkCount in descending order and get the top 5 unique projects
top_5_projects = final_merged_df.sort_values(by='ForkCount', ascending=False).drop_duplicates(subset=['ProjectName']).head(5)

# Format the output
result = top_5_projects[['ProjectName', 'ForkCount']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-18347306469434442166': 'file_storage/function-call-18347306469434442166.json', 'var_function-call-6369501038865689294': 'file_storage/function-call-6369501038865689294.json', 'var_function-call-15493387386679942922': 'file_storage/function-call-15493387386679942922.json'}

exec(code, env_args)
