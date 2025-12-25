code = """import json
import pandas as pd
import re

# Load data files
project_info_path = locals()['var_function-call-13833522886656870590']
package_info_path = locals()['var_function-call-10945398366575275035']
project_pkg_path = locals()['var_function-call-13423498931535120920']

with open(project_info_path, 'r') as f:
    project_info_data = json.load(f)

with open(package_info_path, 'r') as f:
    package_info_data = json.load(f)

with open(project_pkg_path, 'r') as f:
    project_pkg_data = json.load(f)

# 1. Parse Project Info
project_stats = {} # ProjectName -> ForkCount

def parse_forks(text):
    # Patterns for fork count
    patterns = [
        r'(\d+) forks\.',
        r'forks count of (\d+)',
        r'forked (\d+) times',
        r'and (\d+) fork',
        r'(\d+) fork[,.]' # singular
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            return int(m.group(1))
    return 0

def parse_project_name(text):
    # Patterns for project name
    # "The project <NAME> is hosted"
    # "The project <NAME> on GitHub"
    # "The project named <NAME> ..."
    # "The project is hosted on GitHub under the name <NAME>,"
    # "The project is a GitHub repository named <NAME>,"
    
    # Common pattern: token with /
    # But let's try specific contexts first
    patterns = [
        r'The project ([^\s]+) is hosted',
        r'The project ([^\s]+) on GitHub',
        r'The project named ([^\s]+) ',
        r'The project is hosted on GitHub under the name ([^\s,]+)',
        r'The project is a GitHub repository named ([^\s,]+)'
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            name = m.group(1)
            if '/' in name: # Validity check
                return name
    
    # Fallback: Find any token with '/' that is not a URL
    tokens = text.split()
    for t in tokens:
        if '/' in t and 'http' not in t and t.count('/') == 1:
            # Strip punctuation
            t = t.strip('.,')
            return t
    return None

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    name = parse_project_name(info)
    forks = parse_forks(info)
    if name:
        project_stats[name] = forks

# 2. Process Packages
# We need valid (Name, Version) tuples
valid_packages = set()
for pkg in package_info_data:
    # Double check filters just in case
    # System=NPM is handled by query
    # Licenses LIKE %MIT% handled by query
    # VersionInfo LIKE %IsRelease% handled by query
    
    # Precise check on VersionInfo
    try:
        vinfo = json.loads(pkg['VersionInfo'])
        if vinfo.get('IsRelease') is True:
             valid_packages.add((pkg['Name'], pkg['Version']))
    except:
        pass

# 3. Match with Projects
# Find projects that have at least one valid package
relevant_projects = set()
for rec in project_pkg_data:
    # rec has Name, Version, ProjectName
    if (rec['Name'], rec['Version']) in valid_packages:
        relevant_projects.add(rec['ProjectName'])

# 4. Get stats for relevant projects
results = []
for p_name in relevant_projects:
    if p_name in project_stats:
        results.append({'ProjectName': p_name, 'Forks': project_stats[p_name]})

# 5. Top 5
df = pd.DataFrame(results)
if not df.empty:
    top5 = df.sort_values(by='Forks', ascending=False).head(5)
    print("__RESULT__:")
    print(top5.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-5493423872707380861': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-13284152617661678929': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-6890520070290423859': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-6535480407539735233': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-8714269570964313689': [{'Count(*)': '661372'}], 'var_function-call-1814967464397173625': [{'count_star()': '770'}], 'var_function-call-2755016363428305689': [{'Count(*)': '176170'}], 'var_function-call-5690002749993533260': [{'count_star()': '597602'}], 'var_function-call-13833522886656870590': 'file_storage/function-call-13833522886656870590.json', 'var_function-call-10945398366575275035': 'file_storage/function-call-10945398366575275035.json', 'var_function-call-13423498931535120920': 'file_storage/function-call-13423498931535120920.json'}

exec(code, env_args)
