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
star_pattern = re.compile(r'(\d{1,3}(?:,\d{3})*|\d+) stars')
name_pattern = re.compile(r'project (?:is hosted on [Gg]it[Hh]ub under the name |named |is a [Gg]it[Hh]ub repository named |[Gg]it[Hh]ub project |)([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)')

for item in project_info_list:
    text = item.get('Project_Information', '')
    star_match = star_pattern.search(text)
    if star_match:
        stars = int(star_match.group(1).replace(',', ''))
    else:
        stars = 0
    
    # Try pattern
    name_match = name_pattern.search(text)
    project_name = None
    if name_match:
        project_name = name_match.group(1)
    else:
        # Heuristic
        potential_names = re.findall(r'([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)', text)
        for name in potential_names:
            if 'github.com' not in name and ' ' not in name and name.count('/') == 1:
                # exclude common false positives if any?
                project_name = name
                break
    
    if project_name:
        project_stars[project_name] = stars

# 2. Latest Package Version
df_pkg = pd.DataFrame(package_info_list)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg.dropna(subset=['Name', 'Version'], inplace=True)
df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False], inplace=True)
latest_pkgs = df_pkg.drop_duplicates(subset=['Name'], keep='first')
latest_pkg_map = dict(zip(latest_pkgs['Name'], latest_pkgs['Version']))

# 3. Link
results = []
seen_packages = set()

# Pre-filter project_pv_list to only those in latest_pkg_map
# We need to iterate and check. 
# To speed up, maybe create a dict for project_pv_list: (Name, Version) -> ProjectName
# But project_pv_list is a list of dicts.
# 600k rows is fine to iterate.

for item in project_pv_list:
    name = item.get('Name')
    version = item.get('Version')
    project_name = item.get('ProjectName')
    
    if name in latest_pkg_map and latest_pkg_map[name] == version:
        if project_name in project_stars:
            stars = project_stars[project_name]
            
            # Avoid duplicate packages immediately?
            # Or collect all and then dedupe. 
            # If a package maps to multiple projects (unlikely), we might want the max stars.
            results.append({
                'Package': name,
                'Version': version,
                'Project': project_name,
                'Stars': stars
            })

# Convert to DF
df_res = pd.DataFrame(results)

if not df_res.empty:
    # Deduplicate by Package, keeping the one with max Stars (just in case)
    df_res.sort_values(by=['Stars'], ascending=False, inplace=True)
    df_res = df_res.drop_duplicates(subset=['Package'], keep='first')
    
    top_5 = df_res.head(5).to_dict(orient='records')
else:
    top_5 = []

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-12765485723334907841': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17147732955394573907': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15577757168303682267': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-937565460572617818': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-286075157217291400': [{'count_star()': '770'}], 'var_function-call-10477545953268515295': [{'count_star()': '597602'}], 'var_function-call-12664628000143355413': [{'COUNT(*)': '661372'}], 'var_function-call-15544277681777691989': 'file_storage/function-call-15544277681777691989.json', 'var_function-call-6976636483719730651': 'file_storage/function-call-6976636483719730651.json', 'var_function-call-10135252399049147363': 'file_storage/function-call-10135252399049147363.json', 'var_function-call-4071359497304908248': [{'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Project': 'sveltejs/svelte', 'Stars': 73499}, {'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Project': 'sveltejs/svelte', 'Stars': 73499}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Project': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Project': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Package': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Project': 'strapi/strapi', 'Stars': 57236}]}

exec(code, env_args)
