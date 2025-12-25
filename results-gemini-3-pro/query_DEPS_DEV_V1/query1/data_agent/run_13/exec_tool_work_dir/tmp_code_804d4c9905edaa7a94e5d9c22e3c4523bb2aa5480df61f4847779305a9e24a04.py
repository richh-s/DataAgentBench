code = """import json
import pandas as pd

# Load projects
with open(locals()['var_function-call-16897518294623731975'], 'r') as f:
    projects = json.load(f)
df_projects = pd.DataFrame(projects)

# Load package versions (project mapping)
with open(locals()['var_function-call-14244133376442832097'], 'r') as f:
    ppv = json.load(f)
df_ppv = pd.DataFrame(ppv)

# Load package metadata (NPM)
with open(locals()['var_function-call-16817776376308692077'], 'r') as f:
    meta = json.load(f)
df_meta = pd.DataFrame(meta)

# 1. Merge projects and ppv to get candidates
# Note: df_projects has ProjectName, Stars
# df_ppv has Name, Version, ProjectName
df_candidates = pd.merge(df_ppv, df_projects, on='ProjectName')

# 2. Get unique package names in candidates
candidate_names = set(df_candidates['Name'].unique())

# 3. Filter meta to only these names
df_meta_filtered = df_meta[df_meta['Name'].isin(candidate_names)].copy()

# 4. Find latest version for each package
# Convert UpstreamPublishedAt to float just in case
df_meta_filtered['UpstreamPublishedAt'] = pd.to_numeric(df_meta_filtered['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and UpstreamPublishedAt desc
df_meta_filtered = df_meta_filtered.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates keeping first (latest)
df_latest = df_meta_filtered.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 5. Join candidates with latest versions
# We want to keep the candidate only if its version matches the latest version
# Wait, df_candidates has all versions mapped to projects.
# But we only care about the project stars for the package.
# The query says: "Considering only the latest release versions for each distinct NPM package"
# So we consider the package "Name" and its "Latest Version".
# And we want to know the "popularity" based on GitHub stars.
# The stars are associated with the Project, which is associated with the Package.
# So if Package P (latest v1.0) is mapped to Project X, we take stars of X.
# We need to ensure we link the *latest* version to the project.
# Sometimes different versions might map to different projects (rare, but possible if repo moved).
# So we join df_latest with df_ppv on (Name, Version) to get the ProjectName for the latest version.
# Then join with df_projects to get Stars.

df_final = pd.merge(df_latest, df_ppv, on=['Name', 'Version'], how='inner')
df_final = pd.merge(df_final, df_projects, on='ProjectName', how='inner')

# 6. Sort by Stars desc
df_top = df_final.sort_values(by='Stars', ascending=False).head(5)

# Format result
result = df_top[['Name', 'Version', 'Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4271576314138119226': ['packageinfo'], 'var_function-call-4271576314138116435': ['project_info', 'project_packageversion'], 'var_function-call-9503947768837045966': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-9503947768837046145': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-9503947768837042228': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-7789172278500659468': [{'COUNT(*)': '661372'}], 'var_function-call-7789172278500661759': [{'count_star()': '770'}], 'var_function-call-17321684328639176066': [{'count_star()': '597602'}], 'var_function-call-16582028529214248885': 'file_storage/function-call-16582028529214248885.json', 'var_function-call-16897518294623731975': 'file_storage/function-call-16897518294623731975.json', 'var_function-call-14244133376442832097': 'file_storage/function-call-14244133376442832097.json', 'var_function-call-8276939618615715061': 'file_storage/function-call-8276939618615715061.json', 'var_function-call-16817776376308692077': 'file_storage/function-call-16817776376308692077.json'}

exec(code, env_args)
