code = """import pandas as pd
import json

package_info_data = pd.read_json(locals()['var_function-call-18082248841366330894'])
package_info_df = pd.DataFrame(package_info_data)

def get_version_info(version_info_str):
    try:
        return json.loads(version_info_str)
    except json.JSONDecodeError:
        return {}

package_info_df['ParsedVersionInfo'] = package_info_df['VersionInfo'].apply(get_version_info)
package_info_df = package_info_df[package_info_df['ParsedVersionInfo'].apply(lambda x: x.get('IsRelease', False))]
package_info_df['Ordinal'] = package_info_df['ParsedVersionInfo'].apply(lambda x: x.get('Ordinal', 0))

latest_releases = package_info_df.loc[package_info_df.groupby('Name')['Ordinal'].idxmax()]
result = latest_releases[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-319072262640543040': ['packageinfo'], 'var_function-call-18082248841366330894': 'file_storage/function-call-18082248841366330894.json'}

exec(code, env_args)
