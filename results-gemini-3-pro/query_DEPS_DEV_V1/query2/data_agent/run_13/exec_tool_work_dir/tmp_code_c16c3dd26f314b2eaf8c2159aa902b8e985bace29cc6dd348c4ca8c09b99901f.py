code = """import pandas as pd
import json

# Load files
with open(locals()['var_function-call-8918250771806459077'], 'r') as f:
    projects_list = json.load(f)

with open(locals()['var_function-call-16620465441968118169'], 'r') as f:
    mappings_list = json.load(f)

with open(locals()['var_function-call-16620465441968119408'], 'r') as f:
    candidates_list = json.load(f)

# Create DataFrames
df_projects = pd.DataFrame(projects_list)
df_mappings = pd.DataFrame(mappings_list)
df_candidates = pd.DataFrame(candidates_list)

# Join
# Filter mappings to only those in candidates (MIT + Release)
# Note: Ensure types match for join keys.
df_valid_pkgs = pd.merge(df_mappings, df_candidates, on=['Name', 'Version'])

# Filter projects to only those associated with valid packages
df_final = pd.merge(df_valid_pkgs, df_projects, on='ProjectName')

# Get unique projects and sort
result = df_final[['ProjectName', 'Forks']].drop_duplicates().sort_values('Forks', ascending=False).head(5)

print("__RESULT__:")
print(json.dumps(result['ProjectName'].tolist()))"""

env_args = {'var_function-call-348549672667182463': ['packageinfo'], 'var_function-call-348549672667184936': ['project_info', 'project_packageversion'], 'var_function-call-7614129763956883238': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-7614129763956880957': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-7614129763956882772': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-8453879922968270084': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-12455573901807678865': [{'count(*)': '176998'}], 'var_function-call-12455573901807679654': [{'count_star()': '770'}], 'var_function-call-5303905894268228522': [{'count_star()': '597602'}], 'var_function-call-4211593429733531638': 'file_storage/function-call-4211593429733531638.json', 'var_function-call-8918250771806459077': 'file_storage/function-call-8918250771806459077.json', 'var_function-call-16620465441968118169': 'file_storage/function-call-16620465441968118169.json', 'var_function-call-16620465441968119408': 'file_storage/function-call-16620465441968119408.json'}

exec(code, env_args)
