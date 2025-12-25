code = """import json
import re

# Access file paths from local variables
path_project_info = locals()['var_function-call-13643969310521994652']
path_ppv = locals()['var_function-call-13643969310521992085']
path_package_info = locals()['var_function-call-13643969310521993614']

# Load data
project_info_list = json.load(open(path_project_info))
ppv_list = json.load(open(path_ppv))
package_info_list = json.load(open(path_package_info))

# 1. Parse Project Info
project_metrics = {} # ProjectName -> Forks

def parse_forks(text):
    # Try "forks count of X"
    m = re.search(r'forks count of ([\d,]+)', text)
    if m:
        return int(m.group(1).replace(',', ''))
    # Try "X forks"
    m = re.search(r'([\d,]+) forks', text)
    if m:
        return int(m.group(1).replace(',', ''))
    return 0

def parse_name(text):
    patterns = [
        r'The project ([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+) is',
        r'The project ([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+) on',
        r'The GitHub project ([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+) currently',
        r'named ([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)',
        r'under the name ([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)',
        r'project ([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)' 
    ]
    
    for p in patterns:
        m = re.search(p, text)
        if m:
            name = m.group(1)
            if name.lower() not in ['is/hosted', 'on/github']:
                 return name.strip('.,')
    return None

for entry in project_info_list:
    desc = entry.get('Project_Information', '')
    name = parse_name(desc)
    forks = parse_forks(desc)
    if name:
        project_metrics[name] = forks

# 2. Build set of valid (Name, Version) from ppv matching MIT projects
valid_pkgs = set()
pkg_to_project = {} # (Name, Version) -> ProjectName

for row in ppv_list:
    p_name = row.get('ProjectName')
    if p_name in project_metrics:
        key = (row.get('Name'), row.get('Version'))
        valid_pkgs.add(key)
        pkg_to_project[key] = p_name

# 3. Filter packageinfo (releases)
final_projects = set()

for row in package_info_list:
    key = (row.get('Name'), row.get('Version'))
    if key in valid_pkgs:
        p_name = pkg_to_project[key]
        final_projects.add(p_name)

# 4. Get Top 5
result = []
for p_name in final_projects:
    forks = project_metrics.get(p_name, 0)
    result.append({'Project': p_name, 'Forks': forks})

result.sort(key=lambda x: x['Forks'], reverse=True)
top5 = result[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-13185733412178732325': ['project_info', 'project_packageversion'], 'var_function-call-13185733412178732504': ['packageinfo'], 'var_function-call-4415839618545502080': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-4415839618545503559': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-4415839618545500942': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}], 'var_function-call-10255119978212066279': [{'COUNT(*)': '337844'}], 'var_function-call-10255119978212067650': [{'count_star()': '597602'}], 'var_function-call-10255119978212069021': [{'count_star()': '520'}], 'var_function-call-13643969310521994652': 'file_storage/function-call-13643969310521994652.json', 'var_function-call-13643969310521992085': 'file_storage/function-call-13643969310521992085.json', 'var_function-call-13643969310521993614': 'file_storage/function-call-13643969310521993614.json'}

exec(code, env_args)
