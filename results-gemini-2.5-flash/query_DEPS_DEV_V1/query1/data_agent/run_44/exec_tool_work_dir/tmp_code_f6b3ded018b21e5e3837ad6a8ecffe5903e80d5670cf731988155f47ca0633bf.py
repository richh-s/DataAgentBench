code = """import json
import pandas as pd
import numpy as np

# Load package info data
package_info_path = locals()['var_function-call-14944319500008854638']
with open(package_info_path, 'r') as f:
    npm_packages_data = json.load(f)

npm_packages_df = pd.DataFrame(npm_packages_data)

# Convert 'UpstreamPublishedAt' to numeric, coercing errors to NaN
npm_packages_df['UpstreamPublishedAt'] = pd.to_numeric(npm_packages_df['UpstreamPublishedAt'], errors='coerce')

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

# Filter for releases only and drop rows where UpstreamPublishedAt is NaN
released_packages_df = npm_packages_df[npm_packages_df['IsRelease']].copy()
released_packages_df = released_packages_df.dropna(subset=['UpstreamPublishedAt'])

# Find the latest release for each package more efficiently
# Sort by Name, UpstreamPublishedAt (desc), Ordinal (desc)
# Then drop duplicates on 'Name' to keep only the first (latest) entry
latest_releases_df = released_packages_df.sort_values(
    by=['Name', 'UpstreamPublishedAt', 'Ordinal'],
    ascending=[True, False, False]
).drop_duplicates(subset=['Name'], keep='first')

# Select only the necessary columns for the next step
final_packages_for_join = latest_releases_df[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(final_packages_for_join)"""

env_args = {'var_function-call-12560013352706620762': 'file_storage/function-call-12560013352706620762.json', 'var_function-call-983267557488247430': 'file_storage/function-call-983267557488247430.json', 'var_function-call-15254362132007005664': 'file_storage/function-call-15254362132007005664.json', 'var_function-call-11796813297896638897': 'file_storage/function-call-11796813297896638897.json', 'var_function-call-19334942049497322': 'file_storage/function-call-19334942049497322.json', 'var_function-call-1838911449515096989': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-10047082292450705144': 'file_storage/function-call-10047082292450705144.json', 'var_function-call-10594968900220876800': 'file_storage/function-call-10594968900220876800.json', 'var_function-call-1091179815436112658': 'file_storage/function-call-1091179815436112658.json', 'var_function-call-14944319500008854638': 'file_storage/function-call-14944319500008854638.json'}

exec(code, env_args)
