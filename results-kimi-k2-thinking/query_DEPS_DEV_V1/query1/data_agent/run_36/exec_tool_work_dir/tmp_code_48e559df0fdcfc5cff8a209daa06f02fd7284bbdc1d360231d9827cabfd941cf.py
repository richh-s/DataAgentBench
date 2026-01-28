code = """import json
import pandas as pd

# Read the full result from the file
result_file = locals()['var_functions.query_db:8']
with open(result_file, 'r') as f:
    release_data = json.load(f)

# Parse VersionInfo to extract Ordinal
parsed_data = []
for row in release_data:
    try:
        version_info = json.loads(row['VersionInfo'])
        ordinal = version_info.get('Ordinal', 0)
        parsed_data.append({
            'Name': row['Name'],
            'Version': row['Version'],
            'Ordinal': ordinal
        })
    except:
        continue

# Convert to DataFrame
df = pd.DataFrame(parsed_data)

# Find latest version for each package (max ordinal)
latest_versions = df.loc[df.groupby('Name')['Ordinal'].idxmax()]

result = {
    'total_packages': len(df['Name'].unique()),
    'total_release_versions': len(df),
    'latest_versions_count': len(latest_versions),
    'sample_packages': latest_versions.head(10).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM'}], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.list_db:6': ['project_info', 'project_packageversion'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
