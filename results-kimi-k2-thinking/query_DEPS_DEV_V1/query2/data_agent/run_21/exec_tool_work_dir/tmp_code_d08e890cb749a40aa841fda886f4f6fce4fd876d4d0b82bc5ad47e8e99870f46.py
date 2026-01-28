code = """import json
import pandas as pd
import re

# Access the stored data
packages_data = locals()['var_functions.query_db:0']
ppv_data = locals()['var_functions.query_db:2']
proj_info_data = locals()['var_functions.query_db:14']

# Load into DataFrames
packages_df = pd.DataFrame(packages_data)
ppv_df = pd.DataFrame(ppv_data)
proj_info_df = pd.DataFrame(proj_info_data)

# Filter packages with MIT license and IsRelease=true
mit_release_packages = []

for idx, row in packages_df.iterrows():
    try:
        # Parse licenses
        licenses = json.loads(row['Licenses']) if row['Licenses'] and row['Licenses'] != 'None' else []
        if 'MIT' in licenses:
            # Parse VersionInfo
            version_info = json.loads(row['VersionInfo']) if row['VersionInfo'] and row['VersionInfo'] != 'None' else {}
            if version_info.get('IsRelease', False):
                mit_release_packages.append({
                    'System': row['System'],
                    'Name': row['Name'],
                    'Version': row['Version']
                })
    except:
        continue

mit_release_df = pd.DataFrame(mit_release_packages)

# Merge with project_packageversion to get ProjectName
merged_df = pd.merge(
    mit_release_df,
    ppv_df[['System', 'Name', 'Version', 'ProjectName']],
    on=['System', 'Name', 'Version'],
    how='inner'
)

# Merge with project_info to get project details
# Extract project name from Project_Information for matching
proj_info_df['Extracted_ProjectName'] = proj_info_df['Project_Information'].apply(
    lambda x: re.search(r'The project (\S+?) on', x).group(1) if re.search(r'The project (\S+?) on', x) else None
)

final_merged_df = pd.merge(
    merged_df,
    proj_info_df[['Extracted_ProjectName', 'Project_Information']],
    left_on='ProjectName',
    right_on='Extracted_ProjectName',
    how='inner'
)

# Extract fork count from Project_Information
def extract_forks(project_info_text):
    match = re.search(r'(\d+) forks', project_info_text)
    if match:
        return int(match.group(1))
    return 0

final_merged_df['ForkCount'] = final_merged_df['Project_Information'].apply(extract_forks)

# Sort by fork count descending and get top 5
top_5_projects = final_merged_df.nlargest(5, 'ForkCount')[['ProjectName', 'ForkCount']]

print('__RESULT__:')
print(top_5_projects.to_json(orient='records'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}]}

exec(code, env_args)
