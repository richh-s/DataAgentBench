code = """import json
import os

# Read the full results from packageinfo
pkg_file_path = var_functions.query_db:6

# Check if this is a file path
if isinstance(pkg_file_path, str) and pkg_file_path.endswith('.json'):
    with open(pkg_file_path, 'r') as f:
        packages = json.load(f)
else:
    # It's likely a direct JSON result
    packages = pkg_file_path if isinstance(pkg_file_path, list) else []

# Let's parse the VersionInfo JSON to extract IsRelease
valid_packages = []
for pkg in packages:
    try:
        # Parse VersionInfo
        version_info_str = pkg.get('VersionInfo', '{}')
        version_info = json.loads(version_info_str)
        
        # Check if this is a release version
        is_release = version_info.get('IsRelease', False)
        
        # Parse UpstreamPublishedAt timestamp
        timestamp_str = pkg.get('UpstreamPublishedAt', '0')
        timestamp = float(timestamp_str)
        
        if is_release:
            valid_packages.append({
                'Name': pkg.get('Name'),
                'Version': pkg.get('Version'),
                'UpstreamPublishedAt': timestamp,
                'VersionInfo': version_info
            })
    except Exception as e:
        continue

# Group by Name and find latest version for each package
from collections import defaultdict

latest_packages = {}
for pkg in valid_packages:
    name = pkg['Name']
    timestamp = pkg['UpstreamPublishedAt']
    
    if name not in latest_packages or timestamp > latest_packages[name]['UpstreamPublishedAt']:
        latest_packages[name] = pkg

# Convert to list
latest_list = list(latest_packages.values())

# Sort by name for consistency
latest_list_sorted = sorted(latest_list, key=lambda x: x['Name'])

result = json.dumps(latest_list_sorted[:1000])  # Limit for performance
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.8.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.9.3', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/fp', 'Version': '0.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dom-packages/fp', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'lohfu/domp-is', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.1.3', 'ProjectType': 'GITHUB', 'ProjectName': 'lohfu/domp-is', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dosyago/ws', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.4', 'ProjectType': 'GITHUB', 'ProjectName': 'dosyago/ws', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '2.1.0', 'ProjectType': 'GITHUB', 'ProjectName': 'shellscape/dot', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '0.1.0', 'ProjectType': 'GITHUB', 'ProjectName': 'shellscape/dot', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}]}

exec(code, env_args)
