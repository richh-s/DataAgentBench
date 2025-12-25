code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-2087285380968627995'], 'r') as f:
    project_info = json.load(f)
with open(locals()['var_function-call-2087285380968627122'], 'r') as f:
    ppv = json.load(f)
with open(locals()['var_function-call-2087285380968626249'], 'r') as f:
    packages = json.load(f)

# 1. Project Info
project_stars_map = {}
name_patterns = [
    r"The project ([a-zA-Z0-9-_\.]+/[a-zA-Z0-9-_\.]+)",
    r"The GitHub project ([a-zA-Z0-9-_\.]+/[a-zA-Z0-9-_\.]+)",
    r"The project named ([a-zA-Z0-9-_\.]+/[a-zA-Z0-9-_\.]+)",
    r"under the name ([a-zA-Z0-9-_\.]+/[a-zA-Z0-9-_\.]+)",
    r"The GitHub project named ([a-zA-Z0-9-_\.]+/[a-zA-Z0-9-_\.]+)"
]
star_patterns = [
    r"(\d+(?:,\d+)*) stars",
    r"stars count of (\d+(?:,\d+)*)",
    r"total of (\d+(?:,\d+)*) stars"
]

for entry in project_info:
    info = entry.get('Project_Information', '')
    if not info:
        continue
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, info)
        if m:
            p_name = m.group(1)
            break
    stars = 0
    for pat in star_patterns:
        m = re.search(pat, info)
        if m:
            s_str = m.group(1).replace(',', '')
            stars = int(s_str)
            break
    if p_name:
        project_stars_map[p_name.lower()] = stars

# 2. Packages
df_pkg = pd.DataFrame(packages)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 3. Links
df_ppv = pd.DataFrame(ppv)
df_ppv['ProjectName_lower'] = df_ppv['ProjectName'].str.lower()

# 4. Join
df_merged = pd.merge(df_latest, df_ppv, on=['Name', 'Version'], how='inner')

# 5. Map Stars
df_merged['Stars'] = df_merged['ProjectName_lower'].map(project_stars_map)
df_final = df_merged.dropna(subset=['Stars'])

# 6. Deduplicate by Name (keep highest stars, then first)
# Sort by Stars desc, then Name
df_final = df_final.sort_values(by=['Stars', 'Name'], ascending=[False, True])
df_final_unique = df_final.drop_duplicates(subset=['Name'], keep='first')

print("__RESULT__:")
print(df_final_unique[['Name', 'Version', 'Stars', 'ProjectName']].head(10).to_json(orient='records'))"""

env_args = {'var_function-call-4900717798252391877': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-4900717798252389922': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-4900717798252392063': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-7758093602925576692': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-5967498012308057473': ['project_info', 'project_packageversion'], 'var_function-call-5967498012308057448': [{'count_star()': '770'}], 'var_function-call-5967498012308057423': [{'COUNT(*)': '661372'}], 'var_function-call-2239323048433581039': [{'count_star()': '597602'}], 'var_function-call-2087285380968627995': 'file_storage/function-call-2087285380968627995.json', 'var_function-call-2087285380968627122': 'file_storage/function-call-2087285380968627122.json', 'var_function-call-2087285380968626249': 'file_storage/function-call-2087285380968626249.json', 'var_function-call-17666320778115824591': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499.0, 'ProjectName': 'sveltejs/svelte'}], 'var_function-call-15286883127738249223': {'top_list': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931.0, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499.0, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499.0, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464.0, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464.0, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dollarshaveclub/cli>1.11.4>lodash', 'Version': '4.17.11', 'Stars': 57779.0, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.11.4>lodash', 'Version': '4.17.11', 'Stars': 57779.0, 'ProjectName': 'lodash/lodash'}], 'debug': {'typescript_latest': [], 'typescript_links_count': 0}}}

exec(code, env_args)
