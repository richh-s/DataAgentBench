code = """import json

file_packages = locals()['var_function-call-17365738394006126810']
file_projects = locals()['var_function-call-721206738028640762']

with open(file_packages, 'r') as f:
    packages = json.load(f)

valid_packages = set()
for p in packages:
    try:
        licenses_str = p['Licenses']
        if isinstance(licenses_str, str):
            licenses = json.loads(licenses_str)
        else:
            licenses = licenses_str
        
        has_mit = False
        if isinstance(licenses, list):
            if 'MIT' in licenses:
                has_mit = True
        elif isinstance(licenses, str):
             if licenses == 'MIT':
                 has_mit = True
        
        if not has_mit:
            continue
        
        v_info_str = p['VersionInfo']
        if isinstance(v_info_str, str):
            v_info = json.loads(v_info_str)
        else:
            v_info = v_info_str
            
        if not v_info.get('IsRelease', False):
            continue
            
        valid_packages.add((p['Name'], p['Version']))
    except:
        continue

with open(file_projects, 'r') as f:
    projects = json.load(f)

project_forks = {}
for p in projects:
    if (p['Name'], p['Version']) in valid_packages:
        project_forks[p['ProjectName']] = int(p['Forks'])

sorted_projects = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_projects[:10]

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-14137005432196006231': ['project_info', 'project_packageversion'], 'var_function-call-14137005432196006992': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-14137005432196007753': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-17365738394006126810': 'file_storage/function-call-17365738394006126810.json', 'var_function-call-721206738028640762': 'file_storage/function-call-721206738028640762.json', 'var_function-call-12957462019018192931': ['megafetis/vue3-treeselect', 'medikoo/es6-set', 'substack/https-browserify', 'sindresorhus/is-builtin-module', 'sboudrias/run-async']}

exec(code, env_args)
