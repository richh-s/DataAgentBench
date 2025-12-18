code = """import json

package_data = json.loads(open(locals()['var_function-call-13869052368742656528'], 'r').read())

latest_releases = {}

for package in package_data:
    name = package['Name']
    version = package['Version']
    version_info_str = package['VersionInfo']

    try:
        version_info = json.loads(version_info_str)
        is_release = version_info.get('IsRelease')
        ordinal = version_info.get('Ordinal')

        if is_release and ordinal is not None:
            if name not in latest_releases or ordinal > latest_releases[name]['Ordinal']:
                latest_releases[name] = {
                    'System': package['System'],
                    'Name': name,
                    'Version': version,
                    'Ordinal': ordinal
                }
    except json.JSONDecodeError:
        # Handle cases where VersionInfo might not be a valid JSON
        continue

# Convert the dictionary of latest releases back to a list of dictionaries
latest_releases_list = list(latest_releases.values())

print("__RESULT__:")
print(json.dumps(latest_releases_list))"""

env_args = {'var_function-call-13869052368742656528': 'file_storage/function-call-13869052368742656528.json'}

exec(code, env_args)
