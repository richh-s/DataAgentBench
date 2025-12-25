code = """import json
import re

# Load packageinfo results
with open(locals()['var_function-call-9678605239162412031'], 'r') as f:
    package_data = json.load(f)

# Filter packages
matched_packages = set()
for pkg in package_data:
    # Check IsRelease
    try:
        vinfo = json.loads(pkg['VersionInfo'])
        if not vinfo.get('IsRelease', False):
            continue
    except:
        continue
    
    # Check Licenses (already filtered by LIKE '%MIT%', but double check)
    try:
        licenses = json.loads(pkg['Licenses'])
        if not any('MIT' in l.upper() for l in licenses):
            continue
    except:
        continue
        
    matched_packages.add((pkg['Name'], pkg['Version']))

print(f"Matched packages: {len(matched_packages)}")

# Load project_packageversion
with open(locals()['var_function-call-5257754017598581359'], 'r') as f:
    ppv_data = json.load(f)

matched_projects = set()
for row in ppv_data:
    if (row['Name'], row['Version']) in matched_packages:
        matched_projects.add(row['ProjectName'])

print(f"Matched projects: {len(matched_projects)}")

# Load project_info
with open(locals()['var_function-call-4609968517919758329'], 'r') as f:
    pinfo_data = json.load(f)

project_forks = {}

# Regex patterns
name_pattern = re.compile(r'([\w\-\.]+)\/([\w\-\.]+)') 
# The above matches any owner/repo, but might match urls. 
# Better to look for specific context or just find the first owner/repo string in the text which is usually the project name.
# Looking at the preview, the project name is usually early in the string.
# "The project owner/repo ..."
# "The project named owner/repo ..."
# "The GitHub project owner/repo ..."
# "under the name owner/repo"
# "repository named owner/repo"

# Let's try to find the ProjectName from the list of matched_projects in the text, 
# because extracting it blindly might be error prone.
# But wait, I have 770 rows in project_info. 
# And I have a set of matched_projects.
# I can check which matched_project is present in the text.
# But `project_info` doesn't have the ProjectName column. 
# So I have to link the row in `project_info` to the `matched_projects`.
# If I iterate through `project_info`, I can extract the name and see if it is in `matched_projects`.

fork_patterns = [
    re.compile(r'(\d+) forks'),
    re.compile(r'forks count of (\d+)'),
    re.compile(r'forked (\d+) times')
]

for row in pinfo_data:
    info = row['Project_Information']
    
    # Extract name
    # We look for a substring that looks like 'owner/repo'
    # and verify if it's in matched_projects or just valid.
    # Given the text structure, we can try to extract.
    
    # Text usually starts with "The project " or similar.
    # Let's clean up common prefixes to isolate the name or find the name regex.
    # Name regex: a word, a slash, a word (and dots/dashes).
    
    found_name = None
    # Find all potential matches
    candidates = re.findall(r'\b[\w\-\.]+/[\w\-\.]+\b', info)
    
    # Filter candidates to remove URLs (e.g. github.com/owner/repo) if they got matched
    # But usually simple regex \bword/word\b won't match https://... 
    # unless it matches "owner/repo" inside it.
    
    # Let's assume the first candidate that isn't part of a URL or is consistent is the name.
    # Actually, in "The project owner/repo is...", "owner/repo" is the first candidate.
    
    if candidates:
        # Pick the first one that looks reasonable (not ending in .com if possible, but repo names can include dots)
        # In the preview: "lberrocal/npm-packages-template"
        found_name = candidates[0]
        # Check against matched_projects to be sure? 
        # If I only care about matched projects, I can check membership.
        # But I need to parse all project_infos to see which ones are the ones I need.
    
    if not found_name:
        continue
        
    # Extract forks
    forks = 0
    for pat in fork_patterns:
        m = pat.search(info)
        if m:
            forks = int(m.group(1))
            break
            
    # Store
    # We store all found projects just in case, then filter.
    project_forks[found_name] = forks

# Now filter by matched_projects
final_candidates = []
for proj in matched_projects:
    if proj in project_forks:
        final_candidates.append((proj, project_forks[proj]))
    else:
        # Maybe the name extraction failed or slight mismatch?
        # Try case insensitive?
        pass

# Sort
final_candidates.sort(key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(final_candidates[:10]))"""

env_args = {'var_function-call-9636060355559550789': ['project_info', 'project_packageversion'], 'var_function-call-13624772463423231076': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-17260295515790366767': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15925581530478279452': [{'count_star()': '770'}], 'var_function-call-445989961443657827': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-9399392989415678810': [{'count(*)': '661372'}], 'var_function-call-15714045994056598020': [{'count_star()': '597602'}], 'var_function-call-9678605239162412031': 'file_storage/function-call-9678605239162412031.json', 'var_function-call-5257754017598581359': 'file_storage/function-call-5257754017598581359.json', 'var_function-call-4609968517919758329': 'file_storage/function-call-4609968517919758329.json'}

exec(code, env_args)
