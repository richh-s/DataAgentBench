code = """import json
import pandas as pd
import re

# Load latest packages (already computed in previous step)
result_file = locals()['var_functions.query_db:8']
with open(result_file, 'r') as f:
    package_data = json.load(f)

# Parse to get latest versions (max ordinal per package)
latest_packages = {}
for row in package_data:
    try:
        version_info = json.loads(row['VersionInfo'])
        ordinal = version_info.get('Ordinal', 0)
        name = row['Name']
        version = row['Version']
        
        if name not in latest_packages or ordinal > latest_packages[name]['Ordinal']:
            latest_packages[name] = {
                'System': 'NPM',
                'Name': name,
                'Version': version,
                'Ordinal': ordinal
            }
    except:
        continue

# Load project_packageversion data and filter for NPM
proj_pkg_file = locals()['var_functions.query_db:22']
with open(proj_pkg_file, 'r') as f:
    proj_pkg_data = json.load(f)

df_latest = pd.DataFrame(list(latest_packages.values()))
df_proj_pkg = pd.DataFrame(proj_pkg_data)
df_proj_pkg = df_proj_pkg[df_proj_pkg['System'] == 'NPM']

# Merge to get ProjectName for each latest package
# Use inner join to only keep packages that have project info
merged = pd.merge(df_latest, df_proj_pkg, on=['System', 'Name', 'Version'], how='inner')

# Remove duplicates - keep only one ProjectName per package (some have multiple relation types)
merged = merged.drop_duplicates(subset=['System', 'Name', 'Version'])

# Load project_info data
proj_info_file = locals()['var_functions.query_db:26']
with open(proj_info_file, 'r') as f:
    proj_info_data = json.load(f)

df_proj_info = pd.DataFrame(proj_info_data)

# Extract repository name and stars from Project_Information
def extract_repo_and_stars(info_text):
    if not info_text or pd.isna(info_text):
        return None, 0
    
    # Extract repo name (format: "owner/repo")
    repo_match = re.search(r'project\s+([\w-]+/[\w-]+)', info_text, re.IGNORECASE)
    repo_name = repo_match.group(1) if repo_match else None
    
    # Extract stars
    stars_match = re.search(r'(\d+(?:,\d+)*)\s+stars?', info_text, re.IGNORECASE)
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
        except:
            stars = 0
    else:
        stars = 0
    
    return repo_name, stars

# Apply extraction
df_proj_info[['RepoName', 'Stars']] = df_proj_info['Project_Information'].apply(
    lambda x: pd.Series(extract_repo_and_stars(x))
)

# Now merge with our packages based on ProjectName = RepoName
# First, we need to map ProjectName from merged to RepoName from df_proj_info
# ProjectName is in format "owner/repo"
final_merged = pd.merge(
    merged,
    df_proj_info[['RepoName', 'Stars']],
    left_on='ProjectName',
    right_on='RepoName',
    how='inner'
)

# Sort by stars descending and get top 5
top_5 = final_merged.sort_values('Stars', ascending=False).head(5)

# Prepare result
result = []
for _, row in top_5.iterrows():
    result.append({
        'PackageName': row['Name'],
        'Version': row['Version'],
        'GitHubStars': int(row['Stars']),
        'GitHubRepo': row['ProjectName']
    })

# Also get some stats
stats = {
    'total_latest_npm_packages': len(df_latest),
    'packages_with_project_info': len(final_merged),
    'top_5_packages': result
}

print('__RESULT__:')
print(json.dumps(stats))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM'}], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.list_db:6': ['project_info', 'project_packageversion'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_packages': 15811, 'total_release_versions': 337844, 'latest_versions_count': 15811, 'sample_packages': [{'Name': '@discordx/music', 'Version': '6.0.2', 'Ordinal': 213}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'Ordinal': 40}, {'Name': '@discordx/utilities', 'Version': '5.2.1', 'Ordinal': 262}, {'Name': '@discoteam/vueify', 'Version': '9.4.1', 'Ordinal': 2}, {'Name': '@discourse/itsatrap', 'Version': '2.0.10', 'Ordinal': 10}, {'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0', 'Ordinal': 1}, {'Name': '@discoursegroup/commons-js', 'Version': '0.0.11', 'Ordinal': 10}, {'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4', 'Ordinal': 3}, {'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.384', 'Ordinal': 383}, {'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7', 'Ordinal': 3}]}, 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:18': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:20': {'total_latest_packages': 15811, 'sample_packages': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4', 'Ordinal': 27}, {'Name': '@edgedev/firebase', 'Version': '2.0.20', 'Ordinal': 133}]}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_latest_packages': 15811, 'project_pkg_entries': 597602, 'matches_found': 30838, 'sample_matches': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29, 'ProjectType': 'GITHUB', 'ProjectName': 'ec-europa/europa-component-library', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25, 'ProjectType': 'GITHUB', 'ProjectName': 'douganderson444/panzoom-node', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25, 'ProjectType': 'GITHUB', 'ProjectName': 'douganderson444/panzoom-node', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45, 'ProjectType': 'GITHUB', 'ProjectName': 'discue/ui-components', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45, 'ProjectType': 'GITHUB', 'ProjectName': 'discue/ui-components', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
