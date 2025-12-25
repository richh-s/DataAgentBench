code = """import json
import pandas as pd

package_info_data = pd.read_json(locals()['var_function-call-7766504306822188940'])

# Filter for IsRelease = true
release_packages = package_info_data[
    package_info_data['VersionInfo'].apply(
        lambda x: json.loads(x)['IsRelease'] if isinstance(x, str) else x['IsRelease']
    )
].copy()

# Extract Ordinal
release_packages['Ordinal'] = release_packages['VersionInfo'].apply(
    lambda x: json.loads(x)['Ordinal'] if isinstance(x, str) else x['Ordinal']
)

# Find the latest release version for each package
latest_release_packages = release_packages.loc[
    release_packages.groupby('Name')['Ordinal'].idxmax()
]

# Select relevant columns and reset index
latest_release_packages = latest_release_packages[['Name', 'Version']].reset_index(drop=True)

print('__RESULT__:')
print(latest_release_packages.to_json(orient='records'))"""

env_args = {'var_function-call-4269963862347431448': ['packageinfo'], 'var_function-call-7766504306822188940': 'file_storage/function-call-7766504306822188940.json'}

exec(code, env_args)
