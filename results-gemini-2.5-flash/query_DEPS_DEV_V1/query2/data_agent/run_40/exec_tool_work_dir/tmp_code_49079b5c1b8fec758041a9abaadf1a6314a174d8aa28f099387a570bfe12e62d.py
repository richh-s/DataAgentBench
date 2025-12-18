code = """import pandas as pd
import json

packageinfo_data_path = locals()['var_function-call-11799025015653969009']
with open(packageinfo_data_path, 'r') as f:
    packageinfo_data = json.load(f)

df_packageinfo = pd.DataFrame(packageinfo_data)

# Filter for NPM packages with 'MIT' license and IsRelease = true
def filter_packages(row):
    try:
        licenses = json.loads(row['Licenses'])
        version_info = json.loads(row['VersionInfo'])
        is_mit_license = 'MIT' in licenses
        is_release = version_info.get('IsRelease', False)
        return is_mit_license and is_release
    except (json.JSONDecodeError, TypeError):
        return False

filtered_packages = df_packageinfo[df_packageinfo.apply(filter_packages, axis=1)]
result = filtered_packages[['System', 'Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10134544977520819277': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-11799025015653969009': 'file_storage/function-call-11799025015653969009.json'}

exec(code, env_args)
