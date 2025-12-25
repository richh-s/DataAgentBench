code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-15544277681777691989'], 'r') as f:
    project_info_list = json.load(f)

with open(locals()['var_function-call-6976636483719730651'], 'r') as f:
    project_pv_list = json.load(f)

with open(locals()['var_function-call-10135252399049147363'], 'r') as f:
    package_info_list = json.load(f)

# 1. Parse project_info
project_stars = {}

# Patterns for extraction
star_pattern = re.compile(r'(\d{1,3}(?:,\d{3})*|\d+) stars')
name_pattern = re.compile(r'project (?:is hosted on [Gg]it[Hh]ub under the name |named |is a [Gg]it[Hh]ub repository named |[Gg]it[Hh]ub project |)([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)')

for item in project_info_list:
    text = item.get('Project_Information', '')
    
    # Extract stars
    star_match = star_pattern.search(text)
    if star_match:
        stars_str = star_match.group(1).replace(',', '')
        stars = int(stars_str)
    else:
        stars = 0
        
    # Extract name
    # Trying specific patterns first
    name_match = name_pattern.search(text)
    project_name = None
    if name_match:
        project_name = name_match.group(1)
    else:
        # Fallback: find any token with '/' that isn't in a url context?
        # Simple heuristic: find strings matching owner/repo
        potential_names = re.findall(r'([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)', text)
        for name in potential_names:
            if 'github.com' not in name and ' ' not in name and name.count('/') == 1:
                project_name = name
                break
    
    if project_name:
        project_stars[project_name] = stars

# 2. Determine latest version for each package
# Convert to DataFrame for easier grouping
df_pkg = pd.DataFrame(package_info_list)
# Ensure UpstreamPublishedAt is float
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')

# Drop entries without Name or Version
df_pkg.dropna(subset=['Name', 'Version'], inplace=True)

# Find latest version: group by Name, idxmax UpstreamPublishedAt
# Sort by Name and PublishedAt desc
df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False], inplace=True)
# Drop duplicates, keeping first (which is latest)
latest_pkgs = df_pkg.drop_duplicates(subset=['Name'], keep='first')
# Create a set of (Name, Version) for fast lookup
latest_pkg_set = set(zip(latest_pkgs['Name'], latest_pkgs['Version']))

# 3. Link project to package
# We iterate through project_packageversion and check if (Name, Version) is in latest_pkg_set
# And if ProjectName is in project_stars

results = []

for item in project_pv_list:
    name = item.get('Name')
    version = item.get('Version')
    project_name = item.get('ProjectName')
    
    if (name, version) in latest_pkg_set:
        if project_name in project_stars:
            stars = project_stars[project_name]
            results.append({
                'Package': name,
                'Version': version,
                'Project': project_name,
                'Stars': stars
            })

# 4. Sort and get top 5
df_res = pd.DataFrame(results)
if not df_res.empty:
    df_res.sort_values(by='Stars', ascending=False, inplace=True)
    top_5 = df_res.head(5).to_dict(orient='records')
else:
    top_5 = []

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-12765485723334907841': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17147732955394573907': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15577757168303682267': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-937565460572617818': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-286075157217291400': [{'count_star()': '770'}], 'var_function-call-10477545953268515295': [{'count_star()': '597602'}], 'var_function-call-12664628000143355413': [{'COUNT(*)': '661372'}], 'var_function-call-15544277681777691989': 'file_storage/function-call-15544277681777691989.json', 'var_function-call-6976636483719730651': 'file_storage/function-call-6976636483719730651.json', 'var_function-call-10135252399049147363': 'file_storage/function-call-10135252399049147363.json'}

exec(code, env_args)
