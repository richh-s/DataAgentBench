code = """import json

# Load parsed projects (ProjectName -> ForkCount)
with open(locals()['var_function-call-8724906084912738584'], 'r') as f:
    projects_map = json.load(f)

# Load valid packages (Set of (Name, Version))
valid_pkgs = set()
with open(locals()['var_function-call-7305311866666711801'], 'r') as f:
    # This file contains a list of dicts [{"Name": "...", "Version": "..."}]
    data = json.load(f)
    for item in data:
        valid_pkgs.add((item['Name'], item['Version']))

# Load project package versions and filter
confirmed_projects = set()

with open(locals()['var_function-call-22683437480122395'], 'r') as f:
    # This file contains a list of dicts [{"Name": "...", "Version": "...", "ProjectName": "..."}]
    ppv_data = json.load(f)
    for item in ppv_data:
        p_name = item.get('ProjectName')
        if p_name in projects_map:
            # Check if this package version is valid
            pkg_key = (item.get('Name'), item.get('Version'))
            if pkg_key in valid_pkgs:
                confirmed_projects.add(p_name)

# Collect results
results = []
for p_name in confirmed_projects:
    results.append({
        "Project": p_name,
        "Forks": projects_map[p_name]
    })

# Sort by Forks DESC
results.sort(key=lambda x: x['Forks'], reverse=True)

# Top 5
top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-14691372144725519031': ['project_info', 'project_packageversion'], 'var_function-call-10876858305684503756': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-10876858305684502769': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-10876858305684501782': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-2500214839282026509': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-13729864712426550123': [{'COUNT(*)': '176170'}], 'var_function-call-9935959928802624992': [{'count_star()': '597602'}], 'var_function-call-9935959928802626867': [{'count_star()': '770'}], 'var_function-call-2542227473669098196': 'file_storage/function-call-2542227473669098196.json', 'var_function-call-8724906084912738584': 'file_storage/function-call-8724906084912738584.json', 'var_function-call-6894933779218998922': 'file_storage/function-call-6894933779218998922.json', 'var_function-call-7305311866666711801': 'file_storage/function-call-7305311866666711801.json', 'var_function-call-22683437480122395': 'file_storage/function-call-22683437480122395.json'}

exec(code, env_args)
