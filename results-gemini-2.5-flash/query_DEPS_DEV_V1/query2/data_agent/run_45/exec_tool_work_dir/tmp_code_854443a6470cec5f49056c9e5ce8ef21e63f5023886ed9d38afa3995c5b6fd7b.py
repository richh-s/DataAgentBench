code = """import pandas as pd
import json

packageinfo_df = pd.read_json(locals()['var_function-call-9752221296848005442'])

# Filter for packages with 'MIT' license and IsRelease = true
mit_release_packages = []
for index, row in packageinfo_df.iterrows():
    licenses = json.loads(row['Licenses'])
    version_info = json.loads(row['VersionInfo'])
    if 'MIT' in licenses and version_info.get('IsRelease') == True:
        mit_release_packages.append({'System': row['System'], 'Name': row['Name'], 'Version': row['Version']})

result = pd.DataFrame(mit_release_packages).to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9752221296848005442': 'file_storage/function-call-9752221296848005442.json'}

exec(code, env_args)
