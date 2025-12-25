code = """import json
import pandas as pd
import re

# Load files
with open(locals()['var_function-call-1721215846481005156'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-11862853823822712371'], 'r') as f:
    project_pv_data = json.load(f)

with open(locals()['var_function-call-17947288627373787963'], 'r') as f:
    pkg_info_data = json.load(f)

# 1. Parse Project Info
project_stars = {}

def parse_project_info(text):
    # Extract Project Name
    # Patterns: "project <name> on GitHub", "project <name> is", "project named <name>", "project <name> currently"
    name_match = re.search(r"project (?:named )?([^\s,]+)(?:\s+on\s+GitHub|\s+is\s+hosted|\s+currently|\s+under)", text, re.IGNORECASE)
    if not name_match:
        name_match = re.search(r"under the name ([^\s,]+),", text, re.IGNORECASE)
    
    project_name = name_match.group(1) if name_match else None
    
    # Extract Stars
    stars_match = re.search(r"(\d+(?:,\d+)*)\s+stars", text, re.IGNORECASE)
    if not stars_match:
        stars_match = re.search(r"stars count of (\d+(?:,\d+)*)", text, re.IGNORECASE)
        
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    else:
        stars = 0
        
    return project_name, stars

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    pname, pstars = parse_project_info(info)
    if pname:
        if '/' in pname:
            project_stars[pname] = pstars

# 2. Process Package Info (Latest Release)
df_pkg = pd.DataFrame(pkg_info_data)

def is_release(x):
    try:
        if isinstance(x, str):
            x = json.loads(x)
        return x.get('IsRelease', False)
    except:
        return False

df_pkg['IsRelease'] = df_pkg['VersionInfo'].apply(is_release)
df_pkg = df_pkg[df_pkg['IsRelease'] == True]
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg = df_pkg.dropna(subset=['UpstreamPublishedAt'])
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest_pkg = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 3. Process Project Package Version
df_pv = pd.DataFrame(project_pv_data)
known_projects = set(project_stars.keys())
df_pv = df_pv[df_pv['ProjectName'].isin(known_projects)]
# Drop duplicates in pv if any
df_pv = df_pv.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

# 4. Merge
df_merged = pd.merge(df_latest_pkg, df_pv, on=['Name', 'Version'], how='inner')
df_merged['Stars'] = df_merged['ProjectName'].map(project_stars)

# Sort and dedup by Name (just in case a package maps to multiple projects, we take the one with highest stars? Or usually 1:1)
# If a package maps to multiple projects, we should pick the one with max stars?
# The query asks for "which packages".
df_merged = df_merged.sort_values(by='Stars', ascending=False)
df_unique = df_merged.drop_duplicates(subset=['Name'])

df_final = df_unique.head(5)

result = df_final[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16170636577986746024': ['project_info', 'project_packageversion'], 'var_function-call-7647749992733011650': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-10268962386289525301': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-597601748783409707': [{'count(*)': '661372'}], 'var_function-call-17609943704248183482': [{'is_rel': '1'}, {'is_rel': '1'}, {'is_rel': '1'}, {'is_rel': '0'}, {'is_rel': '1'}], 'var_function-call-17148589570304586521': [{'count_star()': '597602'}], 'var_function-call-4068640838107323963': [{'count_star()': '770'}], 'var_function-call-1721215846481005156': 'file_storage/function-call-1721215846481005156.json', 'var_function-call-11862853823822712371': 'file_storage/function-call-11862853823822712371.json', 'var_function-call-17947288627373787963': 'file_storage/function-call-17947288627373787963.json', 'var_function-call-15140132161765818169': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dreampie/semantic-ui', 'Version': '2.2.11', 'Stars': 51069, 'ProjectName': 'semantic-org/semantic-ui'}]}

exec(code, env_args)
