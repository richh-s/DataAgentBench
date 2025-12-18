code = """import json
import pandas as pd

# Load package info data
package_info_path = locals()['var_function-call-14944319500008854638']
with open(package_info_path, 'r') as f:
    npm_packages_data_raw = json.load(f)

# Manually process the data to avoid pandas DataFrame overhead for initial filtering
processed_packages = []
for record in npm_packages_data_raw:
    name = record['Name']
    version = record['Version']
    upstream_published_at = float(record['UpstreamPublishedAt'])
    
    version_info = json.loads(record['VersionInfo'])
    is_release = version_info.get('IsRelease', False)
    ordinal = version_info.get('Ordinal', 0)
    
    if is_release:
        processed_packages.append({
            'Name': name,
            'Version': version,
            'UpstreamPublishedAt': upstream_published_at,
            'Ordinal': ordinal
        })

# Create a DataFrame from the pre-filtered and pre-parsed data
released_packages_df = pd.DataFrame(processed_packages)

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

env_args = {'var_function-call-12560013352706620762': 'file_storage/function-call-12560013352706620762.json', 'var_function-call-983267557488247430': 'file_storage/function-call-983267557488247430.json', 'var_function-call-15254362132007005664': 'file_storage/function-call-15254362132007005664.json', 'var_function-call-11796813297896638897': 'file_storage/function-call-11796813297896638897.json', 'var_function-call-19334942049497322': 'file_storage/function-call-19334942049497322.json', 'var_function-call-1838911449515096989': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-10047082292450705144': 'file_storage/function-call-10047082292450705144.json', 'var_function-call-10594968900220876800': 'file_storage/function-call-10594968900220876800.json', 'var_function-call-1091179815436112658': 'file_storage/function-call-1091179815436112658.json', 'var_function-call-14944319500008854638': 'file_storage/function-call-14944319500008854638.json', 'var_function-call-11294984930735967271': 'file_storage/function-call-11294984930735967271.json'}

exec(code, env_args)
