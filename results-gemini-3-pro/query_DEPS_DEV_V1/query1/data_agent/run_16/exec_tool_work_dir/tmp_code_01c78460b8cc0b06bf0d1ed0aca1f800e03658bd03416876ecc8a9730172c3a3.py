code = """import json
import pandas as pd
import re

p_info_path = locals()['var_function-call-9213377321793908029']
pp_ver_path = locals()['var_function-call-6520223462272974154']
pkg_info_path = locals()['var_function-call-6520223462272971781']

# 1. Parse Project Info
with open(p_info_path, 'r') as f:
    p_info_list = json.load(f)

proj_stars = {}
def extract_project_data(text):
    name = None
    m = re.search(r'project\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)\s+(?:is|on|has)', text)
    if m: name = m.group(1)
    else:
        m = re.search(r'named\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)', text)
        if m: name = m.group(1)
        else:
            m = re.search(r'under\s+the\s+name\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)', text)
            if m: name = m.group(1)
    
    if not name:
        tokens = text.split()
        for t in tokens:
            if '/' in t and not t.startswith('http') and t.count('/') == 1:
                t = t.rstrip(',.')
                if re.match(r'^[a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+$', t):
                    name = t
                    break
    
    stars = 0
    m_stars = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s+stars', text)
    if m_stars: stars = int(m_stars.group(1).replace(',', ''))
    else:
        m_stars = re.search(r'stars\s+count\s+of\s+(\d{1,3}(?:,\d{3})*|\d+)', text)
        if m_stars: stars = int(m_stars.group(1).replace(',', ''))
            
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
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 3. Join with Project Mapping
with open(pp_ver_path, 'r') as f:
    pp_list = json.load(f)
df_pp = pd.DataFrame(pp_list)
# Deduplicate mapping just in case
df_pp = df_pp.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

df_merged = pd.merge(df_latest, df_pp, on=['Name', 'Version'], how='inner')
df_merged['Stars'] = df_merged['ProjectName'].map(proj_stars)
df_final = df_merged.dropna(subset=['Stars'])

# Sort and Deduplicate by Name (since we want distinct packages)
# Although df_latest is unique by Name, df_merged might multiply if one package version maps to multiple projects (rare).
# We take the one with highest stars if that happens, or just first.
df_final = df_final.sort_values(by=['Stars', 'Name'], ascending=[False, True])
df_final = df_final.drop_duplicates(subset=['Name']) # Ensure distinct packages

top5 = df_final.head(5)
result_list = top5[['Name', 'Version', 'Stars']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-3273154451978480392': ['packageinfo'], 'var_function-call-3273154451978481543': ['project_info', 'project_packageversion'], 'var_function-call-4839089145212006103': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-4839089145212006344': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-4839089145212002489': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-107083277889019391': [{'COUNT(*)': '661372'}], 'var_function-call-107083277889016138': [{'count_star()': '597602'}], 'var_function-call-107083277889016981': [{'count_star()': '770'}], 'var_function-call-9213377321793908029': 'file_storage/function-call-9213377321793908029.json', 'var_function-call-6520223462272974154': 'file_storage/function-call-6520223462272974154.json', 'var_function-call-6520223462272971781': 'file_storage/function-call-6520223462272971781.json', 'var_function-call-15886001842188984301': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499.0, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499.0, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464.0, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464.0, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Stars': 57236.0, 'ProjectName': 'strapi/strapi'}]}

exec(code, env_args)
