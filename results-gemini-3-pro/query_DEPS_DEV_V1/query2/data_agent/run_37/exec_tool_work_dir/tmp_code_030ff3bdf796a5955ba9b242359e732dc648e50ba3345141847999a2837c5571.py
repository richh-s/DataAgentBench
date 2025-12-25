code = """import json
import pandas as pd
import re

# Load packageinfo (filtered)
with open(locals()['var_function-call-12508025483221890516'], 'r') as f:
    pkgs = json.load(f)
df_pkgs = pd.DataFrame(pkgs)

# Load project_packageversion
with open(locals()['var_function-call-12508025483221892971'], 'r') as f:
    ppv = json.load(f)
df_ppv = pd.DataFrame(ppv)

# Load project_info
with open(locals()['var_function-call-12307945730263045788'], 'r') as f:
    pinfo = json.load(f)
df_pinfo_raw = pd.DataFrame(pinfo)

# Filter valid projects
# Merge to find which ppv rows correspond to our filtered packages
df_valid_projects = pd.merge(df_ppv, df_pkgs, on=['Name', 'Version'], how='inner')
valid_project_names = set(df_valid_projects['ProjectName'].unique())

# Parse project_info
parsed_data = []
for text in df_pinfo_raw['Project_Information']:
    # Regex for name
    # We look for "project <name>", "named <name>", "name <name>"
    # Note: text usually starts with "The project " or "The GitHub project named ".
    # Sometimes "The project is hosted ... under the name ..."
    
    # Try a few patterns
    # Pattern A: "project <name> " (most common)
    name_match = re.search(r'project\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)', text)
    if not name_match:
        # Pattern B: "named <name>"
        name_match = re.search(r'named\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)', text)
    if not name_match:
        # Pattern C: "name <name>"
        name_match = re.search(r'name\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)', text)
        
    if not name_match:
        continue
        
    project_name = name_match.group(1)
    
    # Regex for forks
    forks = 0
    forks_match = re.search(r'(\d+)\s+forks', text)
    if forks_match:
        forks = int(forks_match.group(1))
    else:
        forks_match = re.search(r'forks\s+count\s+of\s+(\d+)', text)
        if forks_match:
            forks = int(forks_match.group(1))
        else:
            forks_match = re.search(r'forked\s+(\d+)\s+times', text)
            if forks_match:
                forks = int(forks_match.group(1))

    parsed_data.append({'ProjectName': project_name, 'Forks': forks})

df_parsed = pd.DataFrame(parsed_data)

# Filter by valid project names
df_final = df_parsed[df_parsed['ProjectName'].isin(valid_project_names)].copy()

# Sort
df_final = df_final.sort_values(by='Forks', ascending=False)

# Get top 5
top5 = df_final.head(5)['ProjectName'].tolist()

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-6691597743141490400': ['packageinfo'], 'var_function-call-6691597743141488651': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-6691597743141486902': ['project_info', 'project_packageversion'], 'var_function-call-6691597743141489249': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-6691597743141487500': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-4537041203834059277': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-15142775191574149698': [{'COUNT(*)': '176998'}], 'var_function-call-8362777713033535379': [{'count_star()': '770'}], 'var_function-call-16475130448301575381': [{'count_star()': '597602'}], 'var_function-call-12307945730263045788': 'file_storage/function-call-12307945730263045788.json', 'var_function-call-12508025483221890516': 'file_storage/function-call-12508025483221890516.json', 'var_function-call-12508025483221892971': 'file_storage/function-call-12508025483221892971.json'}

exec(code, env_args)
