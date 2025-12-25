code = """import json
import pandas as pd
import re

# Load project_info
with open(locals()['var_function-call-11491817822857708214'], 'r') as f:
    project_info_data = json.load(f)

# Parse project_info
project_stars = {}

def parse_info(info_str):
    # Extract Project Name
    # Patterns for name
    name_patterns = [
        r"The project ([\w\-\.]+/[\w\-\.]+) is hosted on GitHub",
        r"The project ([\w\-\.]+/[\w\-\.]+) on GitHub",
        r"The GitHub project named ([\w\-\.]+/[\w\-\.]+)",
        r"The GitHub project ([\w\-\.]+/[\w\-\.]+)",
        r"The project named ([\w\-\.]+/[\w\-\.]+)",
        r"The project is hosted on GitHub under the name ([\w\-\.]+/[\w\-\.]+)",
        r"The project is a GitHub repository named ([\w\-\.]+/[\w\-\.]+)"
    ]
    
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, info_str)
        if m:
            p_name = m.group(1)
            break
            
    # If no name found, maybe just look for the first "word/word" after "project"?
    if not p_name:
        m = re.search(r"project ([\w\-\.]+/[\w\-\.]+)", info_str)
        if m:
            p_name = m.group(1)

    # Extract Stars
    # Patterns for stars
    star_patterns = [
        r"(\d+) stars",
        r"stars count of (\d+)",
        r"total of (\d+) stars"
    ]
    
    stars = 0
    for pat in star_patterns:
        m = re.search(pat, info_str)
        if m:
            stars = int(m.group(1).replace(',', ''))
            break
            
    return p_name, stars

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    name, stars = parse_info(info)
    if name:
        project_stars[name] = stars

# Load packageinfo (latest versions)
with open(locals()['var_function-call-12675560371229068637'], 'r') as f:
    pkg_data = json.load(f)

df_pkg = pd.DataFrame(pkg_data)
# Convert UpstreamPublishedAt to float
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')

# Sort by Name and PublishedAt desc
df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False], inplace=True)
# Keep latest
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# Load project_packageversion
with open(locals()['var_function-call-12675560371229067774'], 'r') as f:
    ver_data = json.load(f)

df_ver = pd.DataFrame(ver_data)

# Merge latest packages with project versions
# We want to find the ProjectName for the LATEST version of the package.
merged = pd.merge(df_latest, df_ver, on=['Name', 'Version'], how='inner')

# Map stars
merged['Stars'] = merged['ProjectName'].map(project_stars)

# Filter out null stars (meaning project info wasn't found)
final_df = merged.dropna(subset=['Stars'])

# Sort by Stars
final_df['Stars'] = final_df['Stars'].astype(int)
top_5 = final_df.sort_values(by='Stars', ascending=False).head(5)

result = top_5[['Name', 'Version', 'Stars']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14096662834630328886': ['packageinfo'], 'var_function-call-14096662834630329937': ['project_info', 'project_packageversion'], 'var_function-call-13155824603158154318': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-13155824603158153081': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-13155824603158151844': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-10586296822676145367': [{'COUNT(*)': '661372'}], 'var_function-call-8111889515815362594': [{'count_star()': '597602'}], 'var_function-call-8111889515815365951': [{'count_star()': '770'}], 'var_function-call-11491817822857708214': 'file_storage/function-call-11491817822857708214.json', 'var_function-call-12675560371229067774': 'file_storage/function-call-12675560371229067774.json', 'var_function-call-12675560371229068637': 'file_storage/function-call-12675560371229068637.json'}

exec(code, env_args)
