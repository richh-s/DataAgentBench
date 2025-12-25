code = """import json
import re
import pandas as pd

# Load project_info result
with open(locals()['var_function-call-6044978201937607283'], 'r') as f:
    project_info_list = json.load(f)

projects = []

# Regex for Project Name: looks for owner/repo format.
# Common patterns in the text:
# "The project owner/repo ..."
# "The project named owner/repo ..."
# "The GitHub project owner/repo ..."
# "The project is hosted on GitHub under the name owner/repo..."
# I'll look for a string with a slash that isn't a url.
name_pattern = re.compile(r'\b([a-zA-Z0-9\-\.]+/[a-zA-Z0-9\-\_\.]+)\b')

# Regex for Forks
forks_pattern1 = re.compile(r'([\d,]+) forks')
forks_pattern2 = re.compile(r'forks count of ([\d,]+)')
forks_pattern3 = re.compile(r'forked ([\d,]+) times')

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    if not text:
        continue
        
    # Extract Name
    # We skip "github.com/" if present, but usually it's just "owner/repo"
    # Let's try to find the first token with a '/'
    match_name = name_pattern.search(text)
    if match_name:
        p_name = match_name.group(1)
        # Verify it looks like a repo (has /)
        if '/' not in p_name:
            p_name = None
    else:
        p_name = None
        
    # Extract Forks
    forks = 0
    m1 = forks_pattern1.search(text)
    m2 = forks_pattern2.search(text)
    m3 = forks_pattern3.search(text)
    
    val_str = "0"
    if m1:
        val_str = m1.group(1)
    elif m2:
        val_str = m2.group(1)
    elif m3:
        val_str = m3.group(1)
        
    try:
        forks = int(val_str.replace(',', ''))
    except:
        forks = 0
        
    if p_name:
        projects.append({'ProjectName': p_name, 'Forks': forks})

# Create DataFrame
df_projects = pd.DataFrame(projects)
# Drop duplicates if any
df_projects = df_projects.drop_duplicates(subset=['ProjectName'])
# Sort
df_projects = df_projects.sort_values(by='Forks', ascending=False)

print("__RESULT__:")
print(df_projects.to_json(orient='records'))"""

env_args = {'var_function-call-6141831193502255658': ['project_info', 'project_packageversion'], 'var_function-call-15926626213755592094': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-15926626213755592703': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-24275564304897523': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-24275564304896716': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}], 'var_function-call-15029560057788468594': [{'COUNT(*)': '176998'}], 'var_function-call-15029560057788466521': [{'count_star()': '770'}], 'var_function-call-6044978201937607283': 'file_storage/function-call-6044978201937607283.json'}

exec(code, env_args)
