code = """import json

# First, let's read the full packageinfo results to process
import pandas as pd

# The full results are stored in a file
packageinfo_file = var_functions.query_db:4

with open(packageinfo_file, 'r') as f:
    packageinfo_data = json.load(f)

# Convert to DataFrame for easier processing
df_pkg = pd.DataFrame(packageinfo_data)

# Filter for MIT license and release status
def has_mit_license(licenses_str):
    try:
        licenses = json.loads(licenses_str)
        return 'MIT' in licenses
    except:
        return False

def is_release(version_info_str):
    try:
        # Remove newlines and extra spaces
        version_info_str_clean = version_info_str.replace('\n', '').strip()
        version_info = json.loads(version_info_str_clean)
        return version_info.get('IsRelease', False) == True
    except:
        return False

# Apply filters
df_pkg_filtered = df_pkg[
    df_pkg['Licenses'].apply(has_mit_license) & 
    df_pkg['VersionInfo'].apply(is_release)
].copy()

print(f"Filtered {len(df_pkg_filtered)} MIT-licensed NPM release packages")

# Now join with project_packageversion data
pkg_version_file = var_functions.query_db:8

with open(pkg_version_file, 'r') as f:
    pkg_version_data = json.load(f)

df_pkg_version = pd.DataFrame(pkg_version_data)

# Merge packages with their GitHub projects
# First, let's see the first few rows of each
print("Sample package data:")
print(df_pkg_filtered[['System', 'Name', 'Version']].head())
print("\nSample project_packageversion data:")
print(df_pkg_version[['System', 'Name', 'Version', 'ProjectName']].head())

# Merge on System, Name, Version
df_merged = pd.merge(
    df_pkg_filtered,
    df_pkg_version,
    on=['System', 'Name', 'Version'],
    how='inner'
)

print(f"\nMerged data shape: {df_merged.shape}")
print(f"Unique ProjectNames: {df_merged['ProjectName'].nunique()}")

# Now get project_info data
project_info_file = var_functions.query_db:6

with open(project_info_file, 'r') as f:
    project_info_data = json.load(f)

df_proj_info = pd.DataFrame(project_info_data)

print(f"\nProject info shape: {df_proj_info.shape}")
print("Sample project_info Project_Information:")
print(df_proj_info['Project_Information'].head())

# Function to extract fork count from Project_Information
def extract_fork_count(project_info_str):
    try:
        import re
        # Look for patterns like "X forks" or "forks count: X"
        match = re.search(r'(\d+)\s+forks?', str(project_info_str), re.IGNORECASE)
        if match:
            return int(match.group(1))
    except:
        return 0
    return 0

df_proj_info['ForkCount'] = df_proj_info['Project_Information'].apply(extract_fork_count)

# Now merge the project info with our packages
# First, we need to match on ProjectName from project_packageversion
# The ProjectName in project_packageversion (e.g., "dataminingsupply/dms-io") 
# should match some part of Project_Information in project_info

# Let's see if there are any matches
print("\nSample ProjectNames from merged data:")
print(df_merged['ProjectName'].unique()[:10])

# For now, let's write intermediate results to files for debugging
# Then we'll do the final analysis with top 5 by forks

print("__RESULT__:")
print(json.dumps({
    "packages_with_mit_releases": len(df_pkg_filtered),
    "merged_projects": len(df_merged),
    "project_info_entries": len(df_proj_info),
    "sample_package_names": df_merged['ProjectName'].unique()[:10].tolist(),
    "sample_proj_info": df_proj_info['Project_Information'].head(3).tolist()  
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
