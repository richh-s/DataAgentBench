code = """import pandas as pd
import json
import re

# Load data
with open('var_function-call-2351918247091588917.json') as f: # project_info
    p_info = json.load(f)

with open('var_function-call-2351918247091587704.json') as f: # project_packageversion
    p_pkg = json.load(f)

with open('var_function-call-2351918247091586491.json') as f: # packageinfo
    pkg_info = json.load(f)

# 1. Parse project_info
project_stars = {}
for record in p_info:
    text = record.get('Project_Information', '')
    if not text:
        continue
        
    # Extract Stars
    clean_text = text.replace(',', '')
    stars = 0
    # Match: "X stars" or "X star"
    m1 = re.search(r'(\d+)\s+stars?', clean_text)
    if m1:
        stars = int(m1.group(1))
    else:
        # Match: "stars count of X"
        m2 = re.search(r'stars?\s+count\s+of\s+(\d+)', clean_text)
        if m2:
            stars = int(m2.group(1))
            
    # Extract Project Name
    # Find all potential owner/repo strings
    # Pattern: word/word where word can contain -, _, .
    candidates = re.findall(r'\b([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)\b', text)
    
    # Filter candidates
    valid_candidates = []
    for c in candidates:
        if 'github.com' in c.lower(): continue
        if 'npm' in c.lower() and '/' in c and not c.startswith('@'): 
             # "npm-packages-template" is fine, "registry.npmjs.org" is not.
             if 'registry' in c.lower(): continue
        valid_candidates.append(c)
    
    if valid_candidates:
        # Heuristic: The project name usually appears early.
        # But sometimes "The project is hosted on GitHub under the name ..." puts "GitHub" before the name.
        # "The project <name> ..."
        # Let's take the first valid candidate that looks like owner/repo.
        proj_name = valid_candidates[0]
        project_stars[proj_name] = stars

# 2. Filter project_packageversion
df_pkg_proj = pd.DataFrame(p_pkg)
# Filter to only projects we have star info for
df_pkg_proj = df_pkg_proj[df_pkg_proj['ProjectName'].isin(project_stars.keys())]
# Add stars
df_pkg_proj['Stars'] = df_pkg_proj['ProjectName'].map(project_stars)

# 3. Find latest version per package from packageinfo
df_info = pd.DataFrame(pkg_info)
df_info['UpstreamPublishedAt'] = pd.to_numeric(df_info['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and Time desc
df_info = df_info.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Keep top
latest_versions = df_info.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 4. Join
# We want to match packages in df_pkg_proj that are the latest version
merged = pd.merge(df_pkg_proj, latest_versions, on=['Name', 'Version'], how='inner')

# 5. Sort by Stars
# Handle duplicates? A project might have multiple packages. 
# If they are all popular (same stars), they should all be listed.
merged = merged.sort_values(by=['Stars', 'Name'], ascending=[False, True])

# Top 5
top5 = merged[['Name', 'Version', 'Stars', 'ProjectName']].head(5)

print("__RESULT__:")
print(top5.to_json(orient='records'))"""

env_args = {'var_function-call-11315270921350870976': ['packageinfo'], 'var_function-call-11315270921350870213': ['project_info', 'project_packageversion'], 'var_function-call-17129893425440481263': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-17129893425440477878': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-17129893425440478589': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-10452383027913877335': [{'count(*)': '661372'}], 'var_function-call-10452383027913875566': [{'count_star()': '597602'}], 'var_function-call-10452383027913877893': [{'count_star()': '770'}], 'var_function-call-2351918247091588917': 'file_storage/function-call-2351918247091588917.json', 'var_function-call-2351918247091587704': 'file_storage/function-call-2351918247091587704.json', 'var_function-call-2351918247091586491': 'file_storage/function-call-2351918247091586491.json'}

exec(code, env_args)
