code = """import json
import re

# Load matched projects logic
with open(locals()['var_function-call-9678605239162412031'], 'r') as f:
    package_data = json.load(f)

matched_packages = set()
for pkg in package_data:
    try:
        vinfo = json.loads(pkg['VersionInfo'])
        if not vinfo.get('IsRelease', False):
            continue
        licenses = json.loads(pkg['Licenses'])
        if not any('MIT' in str(l).upper() for l in licenses):
            continue
        matched_packages.add((pkg['Name'], pkg['Version']))
    except:
        continue

with open(locals()['var_function-call-5257754017598581359'], 'r') as f:
    ppv_data = json.load(f)

matched_projects = set()
for row in ppv_data:
    if (row['Name'], row['Version']) in matched_packages:
        matched_projects.add(row['ProjectName'])

# Load project_info
with open(locals()['var_function-call-4609968517919758329'], 'r') as f:
    pinfo_data = json.load(f)

project_forks = {}
# Regex without boundaries, just the pattern
name_pattern = re.compile(r'([a-zA-Z0-9\._\-]+/[a-zA-Z0-9\._\-]+)')
fork_patterns = [
    re.compile(r'(\d+) forks'),
    re.compile(r'forks count of (\d+)'),
    re.compile(r'forked (\d+) times')
]

for row in pinfo_data:
    info = row['Project_Information']
    candidates = name_pattern.findall(info)
    found_name = None
    
    for cand in candidates:
        if 'github.com' in cand:
            continue
        if 'registry.npmjs.org' in cand:
            continue
        # Check if valid project name format (contains /)
        if '/' in cand:
            found_name = cand
            break
            
    if found_name:
        forks = 0
        for pat in fork_patterns:
            m = pat.search(info)
            if m:
                forks = int(m.group(1))
                break
        
        # Only add if it's in our matched_projects? 
        # Or add all and filter later. Adding all is safer.
        # But wait, duplicates? 
        # If multiple rows have same project name (unlikely for this table), take max.
        if found_name in project_forks:
            project_forks[found_name] = max(project_forks[found_name], forks)
        else:
            project_forks[found_name] = forks

# Filter and sort
final_candidates = []
for proj in matched_projects:
    if proj in project_forks:
        final_candidates.append((proj, project_forks[proj]))

final_candidates.sort(key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(final_candidates[:5]))"""

env_args = {'var_function-call-9636060355559550789': ['project_info', 'project_packageversion'], 'var_function-call-13624772463423231076': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-17260295515790366767': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15925581530478279452': [{'count_star()': '770'}], 'var_function-call-445989961443657827': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-9399392989415678810': [{'count(*)': '661372'}], 'var_function-call-15714045994056598020': [{'count_star()': '597602'}], 'var_function-call-9678605239162412031': 'file_storage/function-call-9678605239162412031.json', 'var_function-call-5257754017598581359': 'file_storage/function-call-5257754017598581359.json', 'var_function-call-4609968517919758329': 'file_storage/function-call-4609968517919758329.json', 'var_function-call-8323604072629525820': [], 'var_function-call-16343491410577248913': {'num_package_matches': 85158, 'num_project_matches': 5477, 'num_info_parsed': 0, 'sample_matched_projects': ['swuecho/camelsnakekebab_bs', 'dsibilly/mersenne-twister', 'droppedcode/typedoc-plugin-copy-assets', 'east-ds-bot/framework', 'dword-design/atomizer-plugin-vertical-rhythm'], 'sample_extracted_names': [], 'final_count': 0}, 'var_function-call-17657097156770507889': [], 'var_function-call-2002233146175608221': {'sample_matched_projects': ['e-xisto/base-css-framework', 'dropbug/amazon-mws', 'dvlpralamin/star-field', 'dvhb/craco-extend-scope', 'durkajs/example-template'], 'sample_parsed_projects': [], 'num_parsed': 0, 'intersection': []}, 'var_function-call-1101451736578876372': {'sample_info': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'matches': ['lberrocal/npm-packages-template']}}

exec(code, env_args)
