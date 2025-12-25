code = """import json
import pandas as pd

package_data = pd.read_json(locals()["var_function-call-3558731251827286140"])
package_data['VersionInfo'] = package_data['VersionInfo'].apply(json.loads)
package_data = pd.json_normalize(package_data.to_dict(orient='records'))

latest_releases = package_data[package_data['VersionInfo.IsRelease'] == True]
latest_releases = latest_releases.loc[latest_releases.groupby('Name')['VersionInfo.Ordinal'].idxmax()]

__RESULT__:
print(latest_releases.to_json(orient='records'))"""

env_args = {'var_function-call-3558731251827286140': 'file_storage/function-call-3558731251827286140.json'}

exec(code, env_args)
