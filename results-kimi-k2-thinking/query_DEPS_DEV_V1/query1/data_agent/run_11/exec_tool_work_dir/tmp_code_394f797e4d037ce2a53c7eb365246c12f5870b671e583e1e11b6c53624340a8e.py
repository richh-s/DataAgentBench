code = """import json
import pandas as pd

db8_path = locals()['var_functions.query_db:8']
with open(db8_path, 'r') as f:
    npm_packages = json.load(f)

print(f"Total NPM packages: {len(npm_packages)}")

# Parse VersionInfo and filter to latest release for each package
latest_packages = {}
for pkg in npm_packages:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if isinstance(version_info, dict) and version_info.get('IsRelease'):
            name = pkg['Name']
            version = pkg['Version']
            ordinal = version_info.get('Ordinal', 0)
            
            if name not in latest_packages or ordinal > latest_packages[name]['Ordinal']:
                latest_packages[name] = {
                    'Name': name,
                    'Version': version,
                    'Ordinal': ordinal
                }
    except:
        continue

print(f"Latest release packages count: {len(latest_packages)}")

# Convert to list for easier processing
latest_packages_list = list(latest_packages.values())
print(f"Sample latest packages: {latest_packages_list[:5]}")

# Output for next steps
result = json.dumps(latest_packages_list)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}]}

exec(code, env_args)
