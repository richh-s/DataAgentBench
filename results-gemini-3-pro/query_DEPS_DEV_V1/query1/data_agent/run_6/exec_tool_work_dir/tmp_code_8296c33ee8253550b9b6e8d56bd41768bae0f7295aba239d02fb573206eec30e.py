code = """import json
import pandas as pd
import re

# Load project_info
path_proj_info = locals()['var_function-call-2256820548148582661']
with open(path_proj_info, 'r') as f:
    proj_info_data = json.load(f)

# Parse project_info
proj_stars = {}

def parse_stars(text):
    # normalize
    t = text.lower()
    # Patterns
    patterns = [
        r'([\d,]+) stars',
        r'stars count of ([\d,]+)',
        r'total of ([\d,]+) stars',
        r'received ([\d,]+) stars'
    ]
    for pat in patterns:
        m = re.search(pat, t)
        if m:
            try:
                return int(m.group(1).replace(',', ''))
            except:
                continue
    return 0

def parse_project_name(text):
    # "The project owner/repo ..."
    patterns = [
        r'The project ([\w\-\.]+/[\w\-\.]+)',
        r'project named ([\w\-\.]+/[\w\-\.]+)',
        r'under the name ([\w\-\.]+/[\w\-\.]+)',
        r'repository named ([\w\-\.]+/[\w\-\.]+)',
        r'GitHub project ([\w\-\.]+/[\w\-\.]+)',
        r'project ([\w\-\.]+/[\w\-\.]+) on GitHub'
    ]
    
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return m.group(1)
            
    # Fallback: look for "owner/repo"
    words = text.split()
    for w in words:
        if '/' in w and not w.startswith('http') and not w.endswith('.'):
             parts = w.split('/')
             if len(parts) == 2 and all(p for p in parts):
                 return w.rstrip(',.')
    return None

for entry in proj_info_data:
    text = entry.get('Project_Information', '')
    name = parse_project_name(text)
    stars = parse_stars(text)
    if name and stars > 0:
        proj_stars[name] = stars

# print top 5 projects found
sorted_projs = sorted(proj_stars.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 parsed projects:", sorted_projs)

# Load packageinfo
path_pkg_info = locals()['var_function-call-6908991174938387119']
with open(path_pkg_info, 'r') as f:
    pkg_data = json.load(f)
df_pkg = pd.DataFrame(pkg_data)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')

# Check specific packages
print("React in pkg?", 'react' in df_pkg['Name'].values)
print("Lodash in pkg?", 'lodash' in df_pkg['Name'].values)

# Latest version
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# Load mapping
path_mapping = locals()['var_function-call-6908991174938386604']
with open(path_mapping, 'r') as f:
    mapping_data = json.load(f)
df_mapping = pd.DataFrame(mapping_data)

# Join
df_joined = pd.merge(df_latest, df_mapping, on=['Name', 'Version'], how='inner')

# Map stars
df_joined['Stars'] = df_joined['ProjectName'].map(proj_stars)
df_joined = df_joined.dropna(subset=['Stars'])

# Deduplicate by Name (keep highest stars just in case of weird mapping, or just one)
# Actually, Name is unique in df_latest. Join with mapping might explode if 1 pkg -> N projects.
# If so, take the one with most stars?
df_joined = df_joined.sort_values(by='Stars', ascending=False)
df_joined = df_joined.drop_duplicates(subset=['Name'])

top_5 = df_joined.head(5)[['Name', 'Version', 'Stars']] # Include stars for debug
print("Top 5 Packages:")
print(top_5.to_string())

result = top_5[['Name', 'Version']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14323055692995400030': ['project_info', 'project_packageversion'], 'var_function-call-14323055692995403027': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-14323055692995401928': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-2321877848884823765': [{'count(*)': '661372'}], 'var_function-call-2321877848884823364': [{'count_star()': '597602'}], 'var_function-call-2321877848884822963': [{'count_star()': '770'}], 'var_function-call-2256820548148582661': 'file_storage/function-call-2256820548148582661.json', 'var_function-call-6908991174938387119': 'file_storage/function-call-6908991174938387119.json', 'var_function-call-6908991174938386604': 'file_storage/function-call-6908991174938386604.json', 'var_function-call-8756697278668063938': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2'}]}

exec(code, env_args)
