code = """import pandas as pd
import json

packageinfo_df = pd.read_json(locals()['var_function-call-7022167941863055566'])

# Filter for NPM packages with 'MIT' license and 'IsRelease' = true
def parse_licenses_and_version_info(row):
    licenses = json.loads(row['Licenses'])
    version_info = json.loads(row['VersionInfo'])
    return pd.Series({
        'HasMITLicense': 'MIT' in licenses,
        'IsRelease': version_info.get('IsRelease', False)
    })

parsed_info = packageinfo_df.apply(parse_licenses_and_version_info, axis=1)
filtered_packages_df = packageinfo_df[parsed_info['HasMITLicense'] & parsed_info['IsRelease']]

# Select relevant columns for the next join
filtered_packages_df = filtered_packages_df[['Name', 'Version']]

print('__RESULT__:')
print(filtered_packages_df.to_json(orient='records'))"""

env_args = {'var_function-call-7022167941863055566': 'file_storage/function-call-7022167941863055566.json'}

exec(code, env_args)
