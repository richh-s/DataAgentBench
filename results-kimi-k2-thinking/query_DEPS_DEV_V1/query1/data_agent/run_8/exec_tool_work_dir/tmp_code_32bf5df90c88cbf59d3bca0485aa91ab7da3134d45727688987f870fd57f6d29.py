code = """import json
import pandas as pd
import re

# Load data using the correct variable names
packages = locals()['var_functions.query_db:6']
project_packages = locals()['var_functions.query_db:24']
project_info = locals()['var_functions.query_db:9']

# Helper to load data
def load_data(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r') as f:
            return json.load(f)
    return var

# Load all datasets
packages_data = load_data(packages)
proj_pkg_data = load_data(project_packages)
proj_info_data = load_data(project_info)

# Step 1: Get NPM release packages with ordinals
npm_releases = []
for pkg in packages_data:
    if pkg.get('System') == 'NPM':
        try:
            # Parse VersionInfo string
            version_info_str = pkg.get('VersionInfo', '{}')
            # Clean the string
            clean_str = version_info_str.replace('\n', '').replace('\r', '').strip()
            version_info = json.loads(clean_str)
            
            if version_info.get('IsRelease'):
                npm_releases.append({
                    'System': 'NPM',
                    'Name': pkg['Name'],
                    'Version': pkg['Version'],
                    'Ordinal': version_info.get('Ordinal', 0),
                    'PublishedAt': pkg.get('UpstreamPublishedAt', 0)
                })
        except Exception as e:
            continue

# Step 2: Find latest release for each package
if not npm_releases:
    result = []
else:
    pkg_df = pd.DataFrame(npm_releases)
    # Group by Name and get the row with max Ordinal for each
    latest_idx = pkg_df.groupby('Name')['Ordinal'].idxmax()
    latest_packages = pkg_df.loc[latest_idx].reset_index(drop=True)
    
    # Step 3: Load project_packageversion and get ProjectName
    proj_pkg_df = pd.DataFrame(proj_pkg_data)
    proj_pkg_df = proj_pkg_df[proj_pkg_df['System'] == 'NPM']
    
    # Merge to get ProjectName
    merged = latest_packages.merge(
        proj_pkg_df[['System', 'Name', 'Version', 'ProjectName']],
        on=['System', 'Name', 'Version'],
        how='inner'
    )
    
    # Step 4: Extract star counts from project_info
    stars_data = []
    for proj in proj_info_data:
        info_text = proj.get('Project_Information', '')
        # Look for star counts in various formats
        star_match = re.search(r'(\d[\d,]*)\s+stars', info_text, re.IGNORECASE)
        if star_match:
            stars = int(star_match.group(1).replace(',', ''))
            if stars > 0:  # Only include projects with stars
                stars_data.append({
                    'ProjectName': proj.get('ProjectName', ''),
                    'Stars': stars
                })
    
    # Step 5: Merge with stars and get top 5
    if stars_data:
        stars_df = pd.DataFrame(stars_data)
        
        # Final merge
        final_df = merged.merge(stars_df, on='ProjectName', how='inner')
        
        if not final_df.empty:
            # Sort by stars and get top 5
            top5 = final_df.sort_values('Stars', ascending=False).head(5)
            
            # Clean up result
            result = []
            for _, row in top5.iterrows():
                result.append({
                    'PackageName': row['Name'],
                    'Version': row['Version'],
                    'GitHubStars': row['Stars'],
                    'ProjectName': row['ProjectName']
                })
        else:
            result = []
    else:
        result = []

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:34': {'packages_count': 0, 'project_packages_count': 0, 'project_info_count': 0, 'sample_package': None, 'sample_project_pkg': None, 'sample_project_info': None}, 'var_functions.execute_python:36': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:9', 'var_functions.query_db:20', 'var_functions.query_db:24', 'var_functions.query_db:26', 'var_functions.execute_python:30', 'var_functions.execute_python:32', 'var_functions.execute_python:34', '__builtins__', 'json']}

exec(code, env_args)
