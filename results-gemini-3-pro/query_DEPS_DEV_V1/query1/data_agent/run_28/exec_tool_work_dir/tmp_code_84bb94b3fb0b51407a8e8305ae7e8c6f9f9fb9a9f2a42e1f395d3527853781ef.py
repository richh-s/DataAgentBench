code = """import pandas as pd
import json
import re

# Load project info
with open(locals()['var_function-call-7397591203671162166'], 'r') as f:
    project_info_data = json.load(f)

projects = []
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    
    project_name = None
    patterns = [
        r'The project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)',
        r'The GitHub project (?:named\s+)?([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)',
        r'under the name ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)',
        r'repository named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)',
        r'named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)'
    ]
    for pat in patterns:
        m = re.search(pat, info, re.IGNORECASE)
        if m:
            project_name = m.group(1)
            break
            
    stars = 0
    star_patterns = [
        r'(\d+(?:,\d+)*)\s+stars',
        r'stars count of (\d+(?:,\d+)*)',
        r'received (\d+(?:,\d+)*)\s+stars'
    ]
    for pat in star_patterns:
        m = re.search(pat, info)
        if m:
            stars = int(m.group(1).replace(',', ''))
            break
            
    if project_name:
        projects.append({'ProjectName': project_name, 'Stars': stars})

df_projects = pd.DataFrame(projects).drop_duplicates('ProjectName')

# Load package info
with open(locals()['var_function-call-12834192828708800722'], 'r') as f:
    package_data = json.load(f)
df_packages = pd.DataFrame(package_data)
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
df_latest = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False]).drop_duplicates('Name')

# Load mappings
with open(locals()['var_function-call-12834192828708799483'], 'r') as f:
    mapping_data = json.load(f)
df_mappings = pd.DataFrame(mapping_data).drop_duplicates() # Drop exact duplicates

# Merge
df_mapped = df_latest.merge(df_mappings, on=['Name', 'Version'], how='inner')
df_final = df_mapped.merge(df_projects, on='ProjectName', how='inner')

# Sort
df_top = df_final.sort_values('Stars', ascending=False).head(20)

print("__RESULT__:")
print(df_top[['Name', 'Version', 'Stars', 'ProjectName']].to_json(orient='records'))"""

env_args = {'var_function-call-8149522416778404198': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-8149522416778405079': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-4607885978618544362': [{'COUNT(*)': '661372'}], 'var_function-call-4607885978618545847': [{'count_star()': '770'}], 'var_function-call-969480325654969583': [{'count_star()': '597602'}], 'var_function-call-7397591203671162166': 'file_storage/function-call-7397591203671162166.json', 'var_function-call-12834192828708800722': 'file_storage/function-call-12834192828708800722.json', 'var_function-call-12834192828708799483': 'file_storage/function-call-12834192828708799483.json', 'var_function-call-2399730814761282984': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}]}

exec(code, env_args)
