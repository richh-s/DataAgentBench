code = """import json
import pandas as pd
import re

# Load raw NPM package info data
package_info_path = locals()['var_function-call-17987907313070896504']
with open(package_info_path, 'r') as f:
    npm_packages_data_raw = json.load(f)

# Process package info to find the latest release for each package
latest_packages = {}
for record in npm_packages_data_raw:
    name = record['Name']
    version = record['Version']
    upstream_published_at = pd.to_numeric(record['UpstreamPublishedAt'], errors='coerce')
    if pd.isna(upstream_published_at):
        continue

    version_info = json.loads(record['VersionInfo'])
    is_release = version_info.get('IsRelease', False)
    ordinal = version_info.get('Ordinal', 0)

    if is_release:
        if name not in latest_packages:
            latest_packages[name] = {
                'Name': name,
                'Version': version,
                'UpstreamPublishedAt': upstream_published_at,
                'Ordinal': ordinal
            }
        else:
            current_latest = latest_packages[name]
            # Prioritize UpstreamPublishedAt, then Ordinal for "latest"
            if upstream_published_at > current_latest['UpstreamPublishedAt'] or \
               (upstream_published_at == current_latest['UpstreamPublishedAt'] and ordinal > current_latest['Ordinal']):
                latest_packages[name] = {
                    'Name': name,
                    'Version': version,
                    'UpstreamPublishedAt': upstream_published_at,
                    'Ordinal': ordinal
                }

latest_releases_df = pd.DataFrame(list(latest_packages.values()))

# Load project_packageversion data
project_packageversion_path = locals()['var_function-call-11796813297896638897']
with open(project_packageversion_path, 'r') as f:
    project_packageversion_data = json.load(f)
project_packageversion_df = pd.DataFrame(project_packageversion_data)

# Merge latest releases with project_packageversion to get ProjectName
merged_with_project_names = pd.merge(
    latest_releases_df[['Name', 'Version']], # Only need these columns from latest_releases_df for merging
    project_packageversion_df[['Name', 'Version', 'ProjectName']],
    on=['Name', 'Version'],
    how='inner'
)

# Load project_info data
project_info_path = locals()['var_function-call-7572030270991276449']
with open(project_info_path, 'r') as f:
    project_info_data = json.load(f)
project_info_df = pd.DataFrame(project_info_data)

# Extract ProjectName and Stars from Project_Information in project_info_df
def extract_project_name(project_info_str):
    match = re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) is hosted on GitHub', project_info_str)
    if match:
        return match.group(1)
    match = re.search(r'The GitHub project named ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) currently has', project_info_str)
    if match:
        return match.group(1)
    return None

def extract_stars(project_info_str):
    match = re.search(r'(\\d{1,3}(?:,\\d{3})*|\\d+) stars', project_info_str)
    if match:
        return int(match.group(1).replace(',', ''))
    return 0

project_info_df['ProjectName'] = project_info_df['Project_Information'].apply(extract_project_name)
project_info_df['Stars'] = project_info_df['Project_Information'].apply(extract_stars)

# Filter project_info_df to only include relevant project names
relevant_project_names = merged_with_project_names['ProjectName'].unique()
project_info_filtered_df = project_info_df[project_info_df['ProjectName'].isin(relevant_project_names)]

# Merge the combined data with project_info_filtered_df on ProjectName to get stars
final_merged_df = pd.merge(
    merged_with_project_names,
    project_info_filtered_df[['ProjectName', 'Stars']],
    on='ProjectName',
    how='inner'
)

# Remove duplicate entries for packages that might be associated with multiple projects with stars,
# keeping the one with the maximum stars for a given package (Name)
final_merged_df = final_merged_df.loc[final_merged_df.groupby('Name')['Stars'].idxmax()]

# Sort by Stars in descending order and get the top 5
top_5_packages = final_merged_df.sort_values(by='Stars', ascending=False).head(5)

# Prepare the final answer string
result_list = []
for index, row in top_5_packages.iterrows():
    result_list.append(f"{row['Name']} (Version: {row['Version']}, Stars: {row['Stars']})")

final_answer = "Top 5 most popular NPM packages (latest release versions) by GitHub stars:\\n" + "\\n".join(result_list)

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-12560013352706620762': 'file_storage/function-call-12560013352706620762.json', 'var_function-call-983267557488247430': 'file_storage/function-call-983267557488247430.json', 'var_function-call-15254362132007005664': 'file_storage/function-call-15254362132007005664.json', 'var_function-call-11796813297896638897': 'file_storage/function-call-11796813297896638897.json', 'var_function-call-19334942049497322': 'file_storage/function-call-19334942049497322.json', 'var_function-call-1838911449515096989': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-10047082292450705144': 'file_storage/function-call-10047082292450705144.json', 'var_function-call-10594968900220876800': 'file_storage/function-call-10594968900220876800.json', 'var_function-call-1091179815436112658': 'file_storage/function-call-1091179815436112658.json', 'var_function-call-14944319500008854638': 'file_storage/function-call-14944319500008854638.json', 'var_function-call-11294984930735967271': 'file_storage/function-call-11294984930735967271.json', 'var_function-call-6129744792787430713': 'file_storage/function-call-6129744792787430713.json', 'var_function-call-1444223083232544588': 'file_storage/function-call-1444223083232544588.json', 'var_function-call-7572030270991276449': 'file_storage/function-call-7572030270991276449.json', 'var_function-call-13714167941614183449': 'file_storage/function-call-13714167941614183449.json', 'var_function-call-6356381069879717131': 'file_storage/function-call-6356381069879717131.json', 'var_function-call-14121628837960875821': 'file_storage/function-call-14121628837960875821.json', 'var_function-call-17987907313070896504': 'file_storage/function-call-17987907313070896504.json'}

exec(code, env_args)
