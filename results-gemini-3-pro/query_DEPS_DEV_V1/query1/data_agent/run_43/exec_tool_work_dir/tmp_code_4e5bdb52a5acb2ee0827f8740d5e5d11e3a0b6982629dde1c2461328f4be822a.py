code = """import pandas as pd
import json
import re

# Load data
# packageinfo
with open(locals()['var_function-call-16402973810217623789'], 'r') as f:
    pkg_data = json.load(f)
df_pkg = pd.DataFrame(pkg_data)

# project_packageversion
with open(locals()['var_function-call-3143689599835760985'], 'r') as f:
    ppv_data = json.load(f)
df_ppv = pd.DataFrame(ppv_data)

# project_info
with open(locals()['var_function-call-3624205932479868734'], 'r') as f:
    pi_data = json.load(f)
df_pi = pd.DataFrame(pi_data)

# Step 1: Filter latest versions
# Convert UpstreamPublishedAt to float
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and Date DESC
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Keep first (latest)
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# Step 2: Merge with project_packageversion to get ProjectName
# df_ppv has Name, Version, ProjectName
df_merged = pd.merge(df_latest, df_ppv, on=['Name', 'Version'], how='inner')

# Step 3: Parse Project_Information to get ProjectName (for linking) and Stars
def parse_info(info_str):
    stars = 0
    project_name = None
    
    # Extract Stars
    # Pattern 1: "X stars"
    m_stars = re.search(r'([\d,]+)\s+stars', info_str)
    if m_stars:
        stars_str = m_stars.group(1).replace(',', '')
        stars = int(stars_str)
    else:
        # Pattern 2: "stars count of X"
        m_stars2 = re.search(r'stars count of\s+([\d,]+)', info_str)
        if m_stars2:
            stars_str = m_stars2.group(1).replace(',', '')
            stars = int(stars_str)
            
    # Extract Project Name
    # Heuristic: Find a string looking like "owner/repo"
    # The text usually mentions the project name early on.
    # Strategies:
    # 1. "under the name owner/repo"
    # 2. "named owner/repo"
    # 3. "The project owner/repo"
    # 4. "The GitHub project owner/repo"
    
    match_name = None
    if 'under the name ' in info_str:
        part = info_str.split('under the name ')[1]
        match_name = part.split(' ')[0].split(',')[0].strip().rstrip('.')
    elif 'named ' in info_str:
        part = info_str.split('named ')[1]
        match_name = part.split(' ')[0].split(',')[0].strip().rstrip('.')
    else:
        # "The project X..." or "The GitHub project X..."
        m = re.search(r'The (?:GitHub )?project ([^\s,]+)', info_str)
        if m:
            match_name = m.group(1).strip().rstrip('.')
            
    return pd.Series([match_name, stars])

parsed = df_pi['Project_Information'].apply(parse_info)
parsed.columns = ['ProjectName', 'Stars']

# Clean up parsed ProjectName to match format in PPV (it might have extra punctuation if my split wasn't perfect, though rstrip('.') helps)
# Also handling case where parsing failed (None)
parsed = parsed.dropna(subset=['ProjectName'])

# Step 4: Merge df_merged with parsed info
# Note: ProjectName in df_ppv is "owner/repo". Ensure parsed is same.
final_df = pd.merge(df_merged, parsed, on='ProjectName', how='inner')

# Step 5: Sort and top 5
top5 = final_df.sort_values(by='Stars', ascending=False).head(5)

result = top5[['Name', 'Version']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14886076905453574563': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-16148788223358853875': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-17258975952112354656': [{'COUNT(*)': '661372'}], 'var_function-call-16598411849462343979': [{'count_star()': '597602'}], 'var_function-call-10486016052340990826': [{'count_star()': '770'}], 'var_function-call-16402973810217623789': 'file_storage/function-call-16402973810217623789.json', 'var_function-call-3143689599835760985': 'file_storage/function-call-3143689599835760985.json', 'var_function-call-3624205932479868734': 'file_storage/function-call-3624205932479868734.json'}

exec(code, env_args)
