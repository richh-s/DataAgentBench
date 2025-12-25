code = """import pandas as pd
import json
import re

# Load the list of unique project names
with open(locals()['var_function-call-6595577811828910103'], 'r') as f:
    unique_project_names = json.load(f)

# Load all project information
with open(locals()['var_function-call-15778257827323835560'], 'r') as f:
    project_info_data = json.load(f)

df_project_info = pd.DataFrame(project_info_data)

# Filter project_info to include only relevant projects
def extract_project_name(info):
    match = re.search(r'The project (.+?) (is hosted on GitHub|on GitHub is a popular|on GitHub currently has)', info)
    if match:
        return match.group(1).strip()
    return None

df_project_info['ExtractedProjectName'] = df_project_info['Project_Information'].apply(extract_project_name)

# Some ProjectNames might be 'owner/repo' or just 'repo'. Need to handle this.
# Let's create a dictionary for faster lookup, mapping both 'owner/repo' and 'repo' to ProjectName for broad matching.
project_name_set = set(unique_project_names)
project_name_lookup = set()
for name in unique_project_names:
    project_name_lookup.add(name.lower())
    if '/' in name:
        project_name_lookup.add(name.split('/')[1].lower())


def check_project_match(extracted_name, project_name_lookup):
    if extracted_name is None:
        return False
    # Try to match extracted_name directly or its 'repo' part
    if extracted_name.lower() in project_name_lookup:
        return True
    if '/' in extracted_name:
        if extracted_name.split('/')[1].lower() in project_name_lookup:
            return True
    return False

df_filtered_project_info = df_project_info[df_project_info['ExtractedProjectName'].apply(lambda x: check_project_match(x, project_name_lookup))].copy()

# Function to extract fork count
def extract_fork_count(project_info_text):
    match = re.search(r'and forks count of (\d+)', project_info_text)
    if match:
        return int(match.group(1))
    match = re.search(r'and (\d+) forks', project_info_text)
    if match:
        return int(match.group(1))
    return 0

df_filtered_project_info['ForkCount'] = df_filtered_project_info['Project_Information'].apply(extract_fork_count)

# Sort by ForkCount and get top 5
top_5_projects = df_filtered_project_info.sort_values(by='ForkCount', ascending=False).head(5)

# Prepare the result for output
result = []
for index, row in top_5_projects.iterrows():
    # Try to find a more precise ProjectName from the original list if possible
    original_project_name = row['ExtractedProjectName'] if row['ExtractedProjectName'] in unique_project_names else \
                            next((name for name in unique_project_names if name.lower().endswith('/' + row['ExtractedProjectName'].split('/')[-1].lower())), row['ExtractedProjectName'])

    result.append({
        "ProjectName": original_project_name,
        "ForkCount": row['ForkCount']
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15112375380608411619': 'file_storage/function-call-15112375380608411619.json', 'var_function-call-16962072619477001668': 'file_storage/function-call-16962072619477001668.json', 'var_function-call-14340074552170906766': 'file_storage/function-call-14340074552170906766.json', 'var_function-call-6595577811828910103': 'file_storage/function-call-6595577811828910103.json', 'var_function-call-3251080008270179193': [], 'var_function-call-15778257827323835560': 'file_storage/function-call-15778257827323835560.json'}

exec(code, env_args)
