code = """import json
import pandas as pd

with open(locals()['var_function-call-3558731251827286140'], 'r') as f:
    package_data_raw = json.load(f)

package_data = pd.DataFrame(package_data_raw)
package_data['VersionInfo_Parsed'] = package_data['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
package_data['IsRelease'] = package_data['VersionInfo_Parsed'].apply(lambda x: x.get('IsRelease'))
package_data['Ordinal'] = package_data['VersionInfo_Parsed'].apply(lambda x: x.get('Ordinal'))

latest_releases = package_data[package_data['IsRelease'] == True]
latest_releases = latest_releases.loc[latest_releases.groupby('Name')['Ordinal'].idxmax()]

__RESULT__:
print(latest_releases.to_json(orient='records'))"""

env_args = {'var_function-call-3558731251827286140': 'file_storage/function-call-3558731251827286140.json'}

exec(code, env_args)
