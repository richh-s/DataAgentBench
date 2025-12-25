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
    # match "1,234 stars" or "10 stars"
    m = re.search(r'([\d,]+) stars', text)
    if m:
        return int(m.group(1).replace(',', ''))
    return 0

def parse_project_name(text):
    # Patterns based on observation
    # "The project owner/repo ..."
    # "The project named owner/repo ..."
    # "The GitHub project named owner/repo ..."
    # "The project is hosted on GitHub under the name owner/repo ..."
    # "The project is a GitHub repository named owner/repo ..."
    
    # Try finding the pattern [\w\-\.]+/[\w\-\.]+ that is NOT a url (doesn't start with http)
    # But usually it follows specific keywords.
    
    patterns = [
        r'The project ([\w\-\.]+/[\w\-\.]+)',
        r'project named ([\w\-\.]+/[\w\-\.]+)',
        r'under the name ([\w\-\.]+/[\w\-\.]+)',
        r'repository named ([\w\-\.]+/[\w\-\.]+)',
        r'GitHub project ([\w\-\.]+/[\w\-\.]+)'
    ]
    
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return m.group(1)
    
    # Fallback: find any word with / that is not a URL part
    words = text.split()
    for w in words:
        if '/' in w and not w.startswith('http') and not w.endswith('.'):
             # basic validation for owner/repo
             parts = w.split('/')
             if len(parts) == 2 and len(parts[0]) > 0 and len(parts[1]) > 0:
                 return w.rstrip(',.')
    return None

parsed_count = 0
for entry in proj_info_data:
    text = entry.get('Project_Information', '')
    name = parse_project_name(text)
    stars = parse_stars(text)
    if name:
        proj_stars[name] = stars
        parsed_count += 1

print(f"Parsed {parsed_count} projects with stars.")

# Load packageinfo
path_pkg_info = locals()['var_function-call-6908991174938387119']
with open(path_pkg_info, 'r') as f:
    pkg_data = json.load(f)

df_pkg = pd.DataFrame(pkg_data)
# UpstreamPublishedAt might be string, convert to float
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')

# Find latest version for each Name
# Sort by Name, UpstreamPublishedAt desc
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates keeping first (latest)
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# Load project_packageversion
path_mapping = locals()['var_function-call-6908991174938386604']
with open(path_mapping, 'r') as f:
    mapping_data = json.load(f)
df_mapping = pd.DataFrame(mapping_data)

# Join latest packages with mapping
# We need ProjectName for the specific (Name, Version)
df_joined = pd.merge(df_latest, df_mapping, on=['Name', 'Version'], how='inner')

# Map stars
df_joined['Stars'] = df_joined['ProjectName'].map(proj_stars)

# Drop rows where Stars is NaN (meaning no project info found)
df_joined = df_joined.dropna(subset=['Stars'])

# Sort by Stars desc
df_top = df_joined.sort_values(by='Stars', ascending=False).head(5)

result = df_top[['Name', 'Version']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14323055692995400030': ['project_info', 'project_packageversion'], 'var_function-call-14323055692995403027': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-14323055692995401928': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-2321877848884823765': [{'count(*)': '661372'}], 'var_function-call-2321877848884823364': [{'count_star()': '597602'}], 'var_function-call-2321877848884822963': [{'count_star()': '770'}], 'var_function-call-2256820548148582661': 'file_storage/function-call-2256820548148582661.json', 'var_function-call-6908991174938387119': 'file_storage/function-call-6908991174938387119.json', 'var_function-call-6908991174938386604': 'file_storage/function-call-6908991174938386604.json'}

exec(code, env_args)
