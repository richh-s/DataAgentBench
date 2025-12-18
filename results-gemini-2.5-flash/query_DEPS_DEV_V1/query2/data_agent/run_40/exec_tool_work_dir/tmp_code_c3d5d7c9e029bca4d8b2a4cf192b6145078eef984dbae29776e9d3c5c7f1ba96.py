code = """import pandas as pd
import json

filtered_packages_path = locals()['var_function-call-13040228337869759428']
with open(filtered_packages_path, 'r') as f:
    filtered_packages = json.load(f)
df_filtered_packages = pd.DataFrame(filtered_packages)

project_packageversion_path = locals()['var_function-call-2951311016274759351']
with open(project_packageversion_path, 'r') as f:
    project_packageversion = json.load(f)
df_project_packageversion = pd.DataFrame(project_packageversion)

merged_df = pd.merge(df_filtered_packages, df_project_packageversion, on=['System', 'Name', 'Version'], how='inner')
result = merged_df[['System', 'Name', 'Version', 'ProjectName']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10134544977520819277': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-11799025015653969009': 'file_storage/function-call-11799025015653969009.json', 'var_function-call-13040228337869759428': 'file_storage/function-call-13040228337869759428.json', 'var_function-call-2951311016274759351': 'file_storage/function-call-2951311016274759351.json'}

exec(code, env_args)
