code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-15998722402962133371'], 'r') as f:
    package_data = json.load(f)

with open(locals()['var_function-call-12921175548332527908'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-12921175548332528383'], 'r') as f:
    project_mapping_data = json.load(f)

# Convert to DataFrames
df_pkgs = pd.DataFrame(package_data)
df_info = pd.DataFrame(project_info_data)
df_map = pd.DataFrame(project_mapping_data)

# 1. Process df_pkgs (Filter strictly for MIT and IsRelease)
def check_mit(licenses_str):
    try:
        licenses = json.loads(licenses_str)
        # Check if any license is exactly MIT or contains MIT (being lenient as per query "license 'MIT'")
        # Usually exact match "MIT" is preferred but sometimes it's "MIT License" etc.
        # The prompt says "project license 'MIT'". I will assume "MIT" in the list.
        # Let's clean the strings and check.
        if isinstance(licenses, list):
            return any("MIT" == l.strip() for l in licenses)
        return False
    except:
        return False

def check_release(version_info_str):
    try:
        vi = json.loads(version_info_str)
        return vi.get('IsRelease') is True
    except:
        return False

df_pkgs['is_mit'] = df_pkgs['Licenses'].apply(check_mit)
df_pkgs['is_release'] = df_pkgs['VersionInfo'].apply(check_release)

df_pkgs_filtered = df_pkgs[df_pkgs['is_mit'] & df_pkgs['is_release']].copy()
# We only need Name and Version to join
df_pkgs_filtered = df_pkgs_filtered[['Name', 'Version']]

# 2. Process df_info (Extract ProjectName and ForkCount)
def parse_info(info_str):
    if not isinstance(info_str, str):
        return None, 0
    
    # Extract ProjectName
    # Patterns for name
    name_patterns = [
        r"The project ([\w\-\.]+/[[\w\-\.]+) is hosted on GitHub",
        r"The project ([\w\-\.]+/[[\w\-\.]+) on GitHub",
        r"The project named ([\w\-\.]+/[[\w\-\.]+) on GitHub",
        r"The project named ([\w\-\.]+/[[\w\-\.]+) is hosted",
        r"The GitHub project ([\w\-\.]+/[[\w\-\.]+) currently",
        r"The GitHub project named ([\w\-\.]+/[[\w\-\.]+) currently",
        r"under the name ([\w\-\.]+/[[\w\-\.]+),",
        r"The project is hosted on GitHub under the name ([\w\-\.]+/[[\w\-\.]+)"
    ]
    project_name = None
    for p in name_patterns:
        m = re.search(p, info_str)
        if m:
            project_name = m.group(1)
            break
            
    # Extract Fork Count
    # Patterns for forks
    fork_patterns = [
        r"(\d+) forks\.",
        r"forks count of (\d+)",
        r"forked (\d+) times",
        r"(\d+) forks,"
    ]
    fork_count = 0
    for p in fork_patterns:
        m = re.search(p, info_str)
        if m:
            fork_count = int(m.group(1).replace(',', ''))
            break
            
    if project_name:
        return project_name, fork_count
    return None, 0

parsed = df_info['Project_Information'].apply(parse_info)
df_info['ProjectName'] = parsed.apply(lambda x: x[0] if x else None)
df_info['ForkCount'] = parsed.apply(lambda x: x[1] if x else 0)

# Drop rows where ProjectName couldn't be parsed
df_info_clean = df_info.dropna(subset=['ProjectName'])

# 3. Join
# Join packages with mapping
# Inner join to ensure we only look at packages that have a mapping
merged_1 = pd.merge(df_pkgs_filtered, df_map, on=['Name', 'Version'], how='inner')

# Join with info
merged_2 = pd.merge(merged_1, df_info_clean, on='ProjectName', how='inner')

# 4. Aggregate
# We want unique projects with highest fork count
unique_projects = merged_2[['ProjectName', 'ForkCount']].drop_duplicates()
top_5 = unique_projects.sort_values(by='ForkCount', ascending=False).head(5)

result = top_5[['ProjectName', 'ForkCount']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3423223874830064254': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-3423223874830065497': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-3423223874830062644': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-3826428956406176678': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-15998722402962133371': 'file_storage/function-call-15998722402962133371.json', 'var_function-call-2107134680251870117': [{'count_star()': '597602'}], 'var_function-call-12312557686997261771': [{'count_star()': '770'}], 'var_function-call-12921175548332527908': 'file_storage/function-call-12921175548332527908.json', 'var_function-call-12921175548332528383': 'file_storage/function-call-12921175548332528383.json'}

exec(code, env_args)
