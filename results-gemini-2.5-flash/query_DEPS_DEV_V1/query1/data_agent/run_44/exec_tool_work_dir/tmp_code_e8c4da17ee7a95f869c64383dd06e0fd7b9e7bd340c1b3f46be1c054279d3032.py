code = """import json
import pandas as pd

package_info_path = locals()['var_function-call-12560013352706620762']
with open(package_info_path, 'r') as f:
    npm_packages_data = json.load(f)

npm_packages_df = pd.DataFrame(npm_packages_data)

# Convert 'UpstreamPublishedAt' to numeric, then divide by 1000 to convert from milliseconds to seconds,
# and then to datetime for proper sorting
npm_packages_df['UpstreamPublishedAt'] = pd.to_numeric(npm_packages_df['UpstreamPublishedAt'], errors='coerce') / 1000
npm_packages_df['UpstreamPublishedAt'] = pd.to_datetime(npm_packages_df['UpstreamPublishedAt'], unit='s')

# Parse 'VersionInfo' to extract 'IsRelease' and 'Ordinal'
def parse_version_info(version_info_str):
    try:
        info = json.loads(version_info_str)
        return info.get('IsRelease', False), info.get('Ordinal', 0)
    except (json.JSONDecodeError, TypeError):
        return False, 0

npm_packages_df[['IsRelease', 'Ordinal']] = npm_packages_df['VersionInfo'].apply(
    lambda x: pd.Series(parse_version_info(x))
)

# Filter for releases only
released_packages_df = npm_packages_df[npm_packages_df['IsRelease']].copy()

# Sort by Name, then by UpstreamPublishedAt (desc), then by Ordinal (desc) to get the latest release
released_packages_df.sort_values(
    by=['Name', 'UpstreamPublishedAt', 'Ordinal'],
    ascending=[True, False, False],
    inplace=True
)

# Drop duplicates based on 'Name' to keep only the latest release for each package
latest_releases_df = released_packages_df.drop_duplicates(subset=['Name'], keep='first')

# Select only the necessary columns for the next step
final_packages_for_join = latest_releases_df[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(final_packages_for_join)"""

env_args = {'var_function-call-12560013352706620762': 'file_storage/function-call-12560013352706620762.json'}

exec(code, env_args)
