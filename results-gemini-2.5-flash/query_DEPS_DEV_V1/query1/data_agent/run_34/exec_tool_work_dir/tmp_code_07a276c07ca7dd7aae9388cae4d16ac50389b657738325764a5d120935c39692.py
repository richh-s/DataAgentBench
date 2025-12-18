code = """import pandas as pd
import json

package_data = pd.read_json(locals()['var_function-call-16604940366570429364'])

# Filter for IsRelease = true and extract Ordinal
package_data['VersionInfo'] = package_data['VersionInfo'].apply(lambda x: json.loads(x) if pd.notnull(x) else {})
package_data = package_data[package_data['VersionInfo'].apply(lambda x: x.get('IsRelease', False))]
package_data['Ordinal'] = package_data['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Find the latest release version for each package
latest_versions = package_data.loc[package_data.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
latest_versions = latest_versions[['Name', 'Version']]

print("__RESULT__:")
print(latest_versions.to_json(orient='records'))"""

env_args = {'var_function-call-16604940366570429364': 'file_storage/function-call-16604940366570429364.json'}

exec(code, env_args)
