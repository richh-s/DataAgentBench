code = """import json
import re

# Load data
with open(locals()['var_function-call-2147260523063638709'], 'r') as f:
    packages = json.load(f)

with open(locals()['var_function-call-16184911310845776769'], 'r') as f:
    ppv = json.load(f)

with open(locals()['var_function-call-16184911310845776842'], 'r') as f:
    pinfo = json.load(f)

# Filter packages
valid_packages = set()
for p in packages:
    try:
        # Check License
        licenses = json.loads(p['Licenses'])
        if 'MIT' not in licenses:
            continue
        
        # Check IsRelease
        vinfo = json.loads(p['VersionInfo'])
        if not vinfo.get('IsRelease', False):
            continue
            
        valid_packages.add((p['Name'], p['Version']))
    except Exception as e:
        continue

# Filter project mappings
project_names = set()
for row in ppv:
    if (row['Name'], row['Version']) in valid_packages:
        project_names.add(row['ProjectName'])

# Parse Project Info
project_metrics = []
for row in pinfo:
    info = row['Project_Information']
    # Extract Name
    # Patterns:
    # "The project name is..."
    # "The project name on..."
    # "The GitHub project name currently..."
    # "The project is hosted on GitHub under the name name, and..."
    
    name_match = re.search(r'The (?:GitHub )?project (?:named )?([^ ]+) (?:is|on|currently|has)', info)
    if not name_match:
        # Try alternate pattern: "The project is hosted on GitHub under the name ([^,]+),"
        name_match = re.search(r'under the name ([^,]+),', info)
    
    if name_match:
        p_name = name_match.group(1)
        # Extract Forks
        forks_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) forks', info)
        if forks_match:
            forks_str = forks_match.group(1).replace(',', '')
            forks = int(forks_str)
            
            if p_name in project_names:
                project_metrics.append({'ProjectName': p_name, 'Forks': forks})

# Sort and get top 5
project_metrics.sort(key=lambda x: x['Forks'], reverse=True)
top_5 = project_metrics[:5]

# Unique projects (in case of duplicates in project_info, though unlikely)
unique_top = []
seen = set()
for pm in project_metrics:
    if pm['ProjectName'] not in seen:
        unique_top.append(pm['ProjectName'])
        seen.add(pm['ProjectName'])
    if len(unique_top) >= 5:
        break

print("__RESULT__:")
print(json.dumps(unique_top))"""

env_args = {'var_function-call-3339045285131283823': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-3339045285131283082': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-3339045285131282341': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2147260523063638709': 'file_storage/function-call-2147260523063638709.json', 'var_function-call-4102770415333273072': [{'count_star()': '597602'}], 'var_function-call-10895330699367045298': [{'count_star()': '770'}], 'var_function-call-16184911310845776769': 'file_storage/function-call-16184911310845776769.json', 'var_function-call-16184911310845776842': 'file_storage/function-call-16184911310845776842.json'}

exec(code, env_args)
