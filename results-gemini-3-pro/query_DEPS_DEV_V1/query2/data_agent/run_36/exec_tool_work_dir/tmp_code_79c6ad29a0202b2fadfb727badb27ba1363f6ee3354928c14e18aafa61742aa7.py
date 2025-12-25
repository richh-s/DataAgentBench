code = """import json
import re
import pandas as pd

# Get file paths from local variables
file_mit = locals()['var_function-call-11414811561688244219']
file_pkg_ver = locals()['var_function-call-1321341902011472817']
file_proj_info = locals()['var_function-call-1321341902011470570']

# Load MIT packages
with open(file_mit, 'r') as f:
    mit_packages = json.load(f)

# Load project_packageversion
with open(file_pkg_ver, 'r') as f:
    project_packageversions = json.load(f)

# Load project_info
with open(file_proj_info, 'r') as f:
    project_infos = json.load(f)

# Create set of (Name, Version) for MIT packages
mit_pkg_set = set((p['Name'], p['Version']) for p in mit_packages)

# Filter project_packageversions
# Keep only if (Name, Version) is in mit_pkg_set
# And collect associated ProjectNames
target_project_names = set()
for pp in project_packageversions:
    if (pp['Name'], pp['Version']) in mit_pkg_set:
        target_project_names.add(pp['ProjectName'])

# Now iterate through project_infos and find matches for target_project_names
results = []

for p_info in project_infos:
    info_text = p_info['Project_Information']
    
    # Identify which project this is
    matched_project = None
    for target in target_project_names:
        # Check if target is in info_text
        if target in info_text:
            matched_project = target
            break
    
    if matched_project:
        # Extract fork count
        forks = 0
        found_forks = False
        
        # Regexes
        # Handle "5,782 forks"
        patterns = [
            r'(\d{1,3}(?:,\d{3})*|\d+)\s+forks?',
            r'forks\s+count\s+of\s+(\d{1,3}(?:,\d{3})*|\d+)',
            r'forked\s+(\d{1,3}(?:,\d{3})*|\d+)\s+times'
        ]
        
        for pat in patterns:
            match = re.search(pat, info_text)
            if match:
                forks = int(match.group(1).replace(',', ''))
                found_forks = True
                break
        
        if found_forks:
            results.append({'ProjectName': matched_project, 'Forks': forks})

# Sort by Forks descending
results.sort(key=lambda x: x['Forks'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:10]))"""

env_args = {'var_function-call-10298872378066867299': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-10298872378066866198': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-11414811561688244219': 'file_storage/function-call-11414811561688244219.json', 'var_function-call-13594925007200274555': [{'count_star()': '597602'}], 'var_function-call-4297682395291994398': [{'count_star()': '770'}], 'var_function-call-1321341902011470570': 'file_storage/function-call-1321341902011470570.json', 'var_function-call-1321341902011472817': 'file_storage/function-call-1321341902011472817.json'}

exec(code, env_args)
