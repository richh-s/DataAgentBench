code = """import json
import pandas as pd

with open(locals()['var_function-call-6339539474034341735'], 'r') as f:
    package_data_raw = json.load(f)

package_data = pd.DataFrame(package_data_raw)

def parse_version_info(version_info_str):
    try:
        return json.loads(version_info_str.replace('\n', '').replace('\\', ''))
    except (json.JSONDecodeError, TypeError):
        return {}

package_data['VersionInfo_Parsed'] = package_data['VersionInfo'].apply(parse_version_info)
package_data['IsRelease'] = package_data['VersionInfo_Parsed'].apply(lambda x: x.get('IsRelease', False))
package_data['Ordinal'] = package_data['VersionInfo_Parsed'].apply(lambda x: x.get('Ordinal', -1))

latest_releases = package_data[package_data['IsRelease'] == True]
latest_releases = latest_releases.loc[latest_releases.groupby('Name')['Ordinal'].idxmax()]

print("__RESULT__:")
print(latest_releases[['Name', 'Version']].to_json(orient='records'))"""

env_args = {'var_function-call-3558731251827286140': 'file_storage/function-call-3558731251827286140.json', 'var_function-call-6339539474034341735': 'file_storage/function-call-6339539474034341735.json'}

exec(code, env_args)
