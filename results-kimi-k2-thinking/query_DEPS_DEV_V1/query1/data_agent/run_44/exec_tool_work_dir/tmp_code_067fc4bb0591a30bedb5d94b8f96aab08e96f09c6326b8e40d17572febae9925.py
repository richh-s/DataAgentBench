code = """import json, pandas as pd

# Load package data
with open(locals()['var_functions.query_db:14'], 'r') as f:
    packages = json.load(f)

# Load project mappings  
with open(locals()['var_functions.query_db:34'], 'r') as f:
    projects = json.load(f)

# Parse packages to find latest release version per package
latest = {}
for pkg in packages:
    try:
        # Parse the VersionInfo string (which contains JSON)
        vinfo_str = pkg['VersionInfo'].strip()
        vinfo_str = vinfo_str.replace('\n', ' ').replace('\r', '')
        vinfo = json.loads(vinfo_str)
        
        if vinfo.get('IsRelease', False):
            name = pkg['Name']
            ordinal = vinfo.get('Ordinal', 0)
            if name not in latest or ordinal > latest[name][1]:
                latest[name] = (pkg['Version'], ordinal)
    except Exception as e:
        continue

# Build final list of latest releases
latest_releases = [{'Name': name, 'Version': ver} for name, (ver, _) in latest.items()]

# Print stats
print('Packages with latest releases:', len(latest_releases))
print('Project mappings records:', len(projects))

# Check project mappings structure
proj_df = pd.DataFrame(projects[:5])
print('Project types unique values:', set(r.get('ProjectType') for r in projects if 'ProjectType' in r))

# Count GitHub projects
# github_count = sum(1 for p in projects if p.get('ProjectType') == 'GITHUB')
# print('GitHub projects in mappings:', github_count)

print('__RESULT__:')
print(json.dumps({
    'latest_packages_count': len(latest_releases),
    'projects_sample': projects[0] if projects else None
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
