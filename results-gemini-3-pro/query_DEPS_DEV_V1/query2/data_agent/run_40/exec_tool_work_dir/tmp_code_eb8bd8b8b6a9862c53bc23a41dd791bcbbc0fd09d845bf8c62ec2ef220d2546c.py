code = """import json
import re
import pandas as pd

try:
    with open(locals()['var_function-call-6044978201937607283'], 'r') as f:
        project_info_list = json.load(f)
except Exception as e:
    project_info_list = []
    print(f"Error loading json: {e}")

projects = []

# Regex to capture "owner/repo"
# Typically follows "The project ", "The GitHub project ", "named ", "name "
# And contains a slash.
# Example: "lberrocal/npm-packages-template"
# I'll iterate words to find one with '/'
for entry in project_info_list:
    text = entry.get('Project_Information', '')
    if not text:
        continue
    
    # Simple extraction: find word with '/'
    # Remove punctuation like commas or trailing periods
    words = text.split()
    p_name = None
    for w in words:
        # clean punctuation
        clean_w = w.strip(".,;")
        if '/' in clean_w and clean_w.count('/') == 1 and not clean_w.startswith('http'):
             # Basic check to avoid "N/A" or date "1/2" (unlikely in this context but possible)
             # Usually repo names have alphanumeric chars.
             if any(c.isalpha() for c in clean_w):
                 p_name = clean_w
                 break
    
    # Parse Forks
    # Patterns: "X forks", "forks count of X", "forked X times"
    forks = 0
    # normalize text
    norm_text = text.replace(',', '')
    
    # "X forks"
    m1 = re.search(r'(\d+) forks', norm_text)
    # "forks count of X"
    m2 = re.search(r'forks count of (\d+)', norm_text)
    # "forked X times"
    m3 = re.search(r'forked (\d+) times', norm_text)
    
    if m1:
        forks = int(m1.group(1))
    elif m2:
        forks = int(m2.group(1))
    elif m3:
        forks = int(m3.group(1))
        
    if p_name:
        projects.append({'ProjectName': p_name, 'Forks': forks})

df_projects = pd.DataFrame(projects)

if not df_projects.empty:
    df_projects = df_projects.sort_values(by='Forks', ascending=False)
    result = df_projects.to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6141831193502255658': ['project_info', 'project_packageversion'], 'var_function-call-15926626213755592094': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-15926626213755592703': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-24275564304897523': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-24275564304896716': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}], 'var_function-call-15029560057788468594': [{'COUNT(*)': '176998'}], 'var_function-call-15029560057788466521': [{'count_star()': '770'}], 'var_function-call-6044978201937607283': 'file_storage/function-call-6044978201937607283.json'}

exec(code, env_args)
