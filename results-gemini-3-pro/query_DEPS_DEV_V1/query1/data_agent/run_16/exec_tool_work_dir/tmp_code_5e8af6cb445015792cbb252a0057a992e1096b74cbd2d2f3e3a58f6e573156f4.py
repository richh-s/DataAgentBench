code = """import json
import pandas as pd
import re

# File paths
p_info_path = locals()['var_function-call-9213377321793908029']
pp_ver_path = locals()['var_function-call-6520223462272974154']
pkg_info_path = locals()['var_function-call-6520223462272971781']

# 1. Parse Project Info
with open(p_info_path, 'r') as f:
    p_info_list = json.load(f)

proj_stars = {}

def extract_project_data(text):
    # Extract Name
    # Try specific patterns first
    name = None
    # Pattern 1: "project <name> is/on"
    m = re.search(r'project\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)\s+(?:is|on|has)', text)
    if m:
        name = m.group(1)
    else:
        # Pattern 2: "named <name>"
        m = re.search(r'named\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)', text)
        if m:
            name = m.group(1)
        else:
            # Pattern 3: "under the name <name>"
            m = re.search(r'under\s+the\s+name\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)', text)
            if m:
                name = m.group(1)
    
    # Fallback: Find any token with '/'
    if not name:
        tokens = text.split()
        for t in tokens:
            if '/' in t and not t.startswith('http') and t.count('/') == 1:
                # remove trailing punctuation
                t = t.rstrip(',.')
                # Verify it looks like owner/repo
                if re.match(r'^[a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+$', t):
                    name = t
                    break
    
    # Extract Stars
    stars = 0
    # Pattern A: "X stars"
    # handle "total of X stars"
    m_stars = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s+stars', text)
    if m_stars:
        stars = int(m_stars.group(1).replace(',', ''))
    else:
        # Pattern B: "stars count of X"
        m_stars = re.search(r'stars\s+count\s+of\s+(\d{1,3}(?:,\d{3})*|\d+)', text)
        if m_stars:
            stars = int(m_stars.group(1).replace(',', ''))
            
    return name, stars

for entry in p_info_list:
    txt = entry.get('Project_Information', '')
    p_name, p_stars = extract_project_data(txt)
    if p_name:
        proj_stars[p_name] = p_stars

# 2. Get Latest Packages
with open(pkg_info_path, 'r') as f:
    pkg_list = json.load(f)

df_pkg = pd.DataFrame(pkg_list)
# Ensure numeric
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
# Sort by Name asc, Date desc
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates on Name, keeping first (latest)
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 3. Join with Project Mapping
with open(pp_ver_path, 'r') as f:
    pp_list = json.load(f)

df_pp = pd.DataFrame(pp_list)

# Inner join to link latest package version to project
# Note: df_pp has (Name, Version, ProjectName)
# df_latest has (Name, Version)
df_merged = pd.merge(df_latest, df_pp, on=['Name', 'Version'], how='inner')

# 4. Map Stars
df_merged['Stars'] = df_merged['ProjectName'].map(proj_stars)

# Remove unmapped
df_final = df_merged.dropna(subset=['Stars'])

# Top 5
top5 = df_final.sort_values(by='Stars', ascending=False).head(5)

# Result list
result_list = top5[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records') # keeping stars/proj for debug, will format for final answer

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-3273154451978480392': ['packageinfo'], 'var_function-call-3273154451978481543': ['project_info', 'project_packageversion'], 'var_function-call-4839089145212006103': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-4839089145212006344': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-4839089145212002489': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-107083277889019391': [{'COUNT(*)': '661372'}], 'var_function-call-107083277889016138': [{'count_star()': '597602'}], 'var_function-call-107083277889016981': [{'count_star()': '770'}], 'var_function-call-9213377321793908029': 'file_storage/function-call-9213377321793908029.json', 'var_function-call-6520223462272974154': 'file_storage/function-call-6520223462272974154.json', 'var_function-call-6520223462272971781': 'file_storage/function-call-6520223462272971781.json'}

exec(code, env_args)
