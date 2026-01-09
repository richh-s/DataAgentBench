code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_Fq36jZMEJmTayeHv4jYkRATW)
ppv = load_records(var_call_aVDQnetI9CWNkRET4zlGQuJt)
pi = load_records(var_call_o8pE6bkGpDAIw2aXLo7A7fS9)

pkg_df = pd.DataFrame(pkg).drop_duplicates(subset=['System','Name','Version'])
ppv_df = pd.DataFrame(ppv).drop_duplicates(subset=['System','Name','Version','ProjectName'])

# Join package versions to project mapping
j = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Parse project_info strings: extract repo and forks
pi_df = pd.DataFrame(pi)

repo_re = re.compile(r'project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
forks_re = re.compile(r'([0-9][0-9,]*)\s+forks?')

def extract_repo(s):
    if s is None:
        return None
    m = repo_re.search(str(s))
    return m.group(1) if m else None

def extract_forks(s):
    if s is None:
        return None
    m = forks_re.search(str(s))
    if not m:
        return None
    return int(m.group(1).replace(',',''))

pi_df['ProjectName'] = pi_df['Project_Information'].map(extract_repo)
pi_df['Forks'] = pi_df['Project_Information'].map(extract_forks)

# Filter project license MIT
pi_df = pi_df[pi_df['Licenses'].astype(str).str.contains('"MIT"', regex=False)]

# Merge to get forks
j2 = j.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='inner')

# Aggregate by project, take max forks (should be constant)
out = j2.groupby('ProjectName', as_index=False)['Forks'].max()
out = out.dropna(subset=['Forks']).sort_values('Forks', ascending=False).head(5)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3rDAVNRP6UUr2exXTWd0wAa5': ['packageinfo'], 'var_call_asmHgM8HGlHFXVXTVvbPI4ui': ['project_info', 'project_packageversion'], 'var_call_h4avd2CMZErRSs0xMlKfs0vY': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_ONAVafaCVxbotVTmwN8G61Zr': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_call_3HDNBjiqwYUWqmtTcynsNuwd': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_call_Fq36jZMEJmTayeHv4jYkRATW': 'file_storage/call_Fq36jZMEJmTayeHv4jYkRATW.json', 'var_call_aVDQnetI9CWNkRET4zlGQuJt': 'file_storage/call_aVDQnetI9CWNkRET4zlGQuJt.json', 'var_call_o8pE6bkGpDAIw2aXLo7A7fS9': 'file_storage/call_o8pE6bkGpDAIw2aXLo7A7fS9.json'}

exec(code, env_args)
