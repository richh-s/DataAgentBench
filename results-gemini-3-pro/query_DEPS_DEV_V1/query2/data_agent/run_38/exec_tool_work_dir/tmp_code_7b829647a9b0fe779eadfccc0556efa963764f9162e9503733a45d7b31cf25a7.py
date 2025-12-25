code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-6539420380694691408']
with open(file_path, 'r') as f:
    project_info_data = json.load(f)

projects = []
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    
    name = None
    p1 = re.search(r'project (?:is hosted on GitHub under the name |named |is a GitHub repository named )?([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', info)
    if p1:
        name = p1.group(1)
    
    forks = 0
    forks_match = re.search(r'([\d,]+) forks|forks count of ([\d,]+)|forked ([\d,]+) times', info)
    if name:
        if forks_match:
            f_str = forks_match.group(1) or forks_match.group(2) or forks_match.group(3)
            forks = int(f_str.replace(',', ''))
        projects.append({'ProjectName': name, 'Forks': forks})

df = pd.DataFrame(projects).drop_duplicates()
df = df.sort_values('Forks', ascending=False).head(100)
top_projects = df['ProjectName'].tolist()

in_clause = ", ".join([f"'{name}'" for name in top_projects])
print("__RESULT__:")
print(json.dumps(in_clause))"""

env_args = {'var_function-call-7179101092357015596': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-7179101092357015271': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-7179101092357014946': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-2936867257169916719': [{'COUNT(*)': '176170'}], 'var_function-call-2936867257169916638': [{'count_star()': '597602'}], 'var_function-call-2936867257169916557': [{'count_star()': '770'}], 'var_function-call-6539420380694691408': 'file_storage/function-call-6539420380694691408.json', 'var_function-call-12313832699212497409': 'file_storage/function-call-12313832699212497409.json', 'var_function-call-5616184914363530156': 'file_storage/function-call-5616184914363530156.json'}

exec(code, env_args)
