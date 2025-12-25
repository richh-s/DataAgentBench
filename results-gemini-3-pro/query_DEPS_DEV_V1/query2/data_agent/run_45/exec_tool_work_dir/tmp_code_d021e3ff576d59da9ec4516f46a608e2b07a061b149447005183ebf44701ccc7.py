code = """import json

# Load project_data
with open(locals()['var_function-call-8522184770744345831'], 'r') as f:
    project_data = json.load(f) # {ProjectName: ForkCount}

# Load project_packageversion
with open(locals()['var_function-call-1049857498189876036'], 'r') as f:
    pkg_ver_list = json.load(f) # [{Name, Version, ProjectName}, ...]

candidates = []
candidate_names = set()

for row in pkg_ver_list:
    pn = row.get('ProjectName')
    if pn in project_data:
        # Keep this candidate
        candidates.append({
            'Name': row['Name'],
            'Version': row['Version'],
            'ProjectName': pn,
            'ForkCount': project_data[pn]
        })
        candidate_names.add(row['Name'])

print(f"Found {len(candidates)} candidate package versions.")
print(f"Found {len(candidate_names)} unique package names.")

# Prepare names for SQL query
# If there are not too many names, we can use IN clause.
names_list = list(candidate_names)
print("__RESULT__:")
print(json.dumps(names_list))"""

env_args = {'var_function-call-12766813875944643358': ['project_info', 'project_packageversion'], 'var_function-call-12766813875944642675': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-15726930161277794': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-15726930161277589': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-2618448446094669124': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-7902902596674928536': [{'count_star()': '770'}], 'var_function-call-2849774490259925492': [{'count_star()': '597602'}], 'var_function-call-3713556804398633586': 'file_storage/function-call-3713556804398633586.json', 'var_function-call-8522184770744345831': 'file_storage/function-call-8522184770744345831.json', 'var_function-call-10502820330694842970': 'file_storage/function-call-10502820330694842970.json', 'var_function-call-1049857498189876036': 'file_storage/function-call-1049857498189876036.json'}

exec(code, env_args)
