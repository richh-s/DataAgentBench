code = """import json, pandas as pd

filepath = locals()['var_functions.query_db:14']
with open(filepath) as f:
    data = json.load(f)

print('Loaded', len(data), 'records')

# Convert VersionInfo manually
for item in data:
    try:
        vinfo = item['VersionInfo'].strip()
        if '\n' in vinfo:
            vinfo = vinfo.replace('\n', ' ')
        parsed = json.loads(vinfo)
        item['IsRelease'] = parsed.get('IsRelease', False)
        item['Ordinal'] = parsed.get('Ordinal', 0)
    except:
        item['IsRelease'] = False
        item['Ordinal'] = 0

# Filter and find latest
filtered = [item for item in data if item['IsRelease']]

# Find latest version for each package
packages = {}
for item in filtered:
    name = item['Name']
    if name not in packages or item['Ordinal'] > packages[name]['Ordinal']:
        packages[name] = item

# Prepare result
result = [{
    'Name': pkg['Name'],
    'Version': pkg['Version']
} for pkg in packages.values()]

print('Found', len(result), 'latest releases')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}]}

exec(code, env_args)
