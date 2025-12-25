code = """import json
import re

# Load data
with open(locals()['var_function-call-18204407829612454580'], 'r') as f:
    project_info_list = json.load(f)

with open(locals()['var_function-call-10062229100743089117'], 'r') as f:
    latest_pkgs = json.load(f)

with open(locals()['var_function-call-10062229100743086290'], 'r') as f:
    mappings = json.load(f)

# 1. Parse Project Info
project_stars_map = {}

# Regex patterns
# Pattern for name: "The project OWNER/REPO " or "The GitHub project OWNER/REPO " or "The project named OWNER/REPO "
# Looking at examples:
# "The project lberrocal/npm-packages-template is hosted on GitHub..."
# "The project leaflet/leaflet on GitHub..."
# "The GitHub project ledgerproject/keypairoom currently..."
# "The project named leo-ran/easy-node-server is hosted..."
# "The project is hosted on GitHub under the name learnfrontend-dc/product-cart..."
# "The project is a GitHub repository named letrungdo/react-ui-component-lib..."

# A more robust way might be to look for the "owner/repo" pattern which usually contains a slash.
# But "owner/repo" might appear in description text too.
# However, the structure seems generated.
# Let's try to extract the project name by finding the string "project <name>" or "named <name>" or "name <name>".
# And verifying it looks like 'owner/repo'.

# Pattern for stars: "X stars" or "stars count of X".
# Handle commas in X.

star_pattern = re.compile(r'(\d{1,3}(?:,\d{3})*|\d+) stars|stars count of (\d{1,3}(?:,\d{3})*|\d+)')

def extract_stars(text):
    m = star_pattern.search(text)
    if m:
        s = m.group(1) or m.group(2)
        return int(s.replace(',', ''))
    return 0

# For project name, I will try a few patterns.
name_patterns = [
    re.compile(r'The project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) is hosted on GitHub'),
    re.compile(r'The project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) on GitHub'),
    re.compile(r'The GitHub project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) currently'),
    re.compile(r'The GitHub project named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) currently'),
    re.compile(r'The project named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) is hosted'),
    re.compile(r'The project named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) on GitHub'),
    re.compile(r'hosted on GitHub under the name ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+),'),
    re.compile(r'GitHub repository named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+),')
]

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    stars = extract_stars(text)
    
    found_name = None
    for p in name_patterns:
        m = p.search(text)
        if m:
            found_name = m.group(1)
            break
            
    # Fallback/Debug if needed, but assuming generated text is consistent enough or we catch most.
    if found_name:
        project_stars_map[found_name] = stars

# 2. Set of latest packages
latest_keys = set()
for p in latest_pkgs:
    latest_keys.add((p['Name'], p['Version']))

# 3. Join
results = []
# Ensure uniqueness of package? The query asks for "packages". One package -> one latest version.
# So we want distinct packages.
processed_packages = set()

for m in mappings:
    pkg_name = m['Name']
    pkg_ver = m['Version']
    proj_name = m['ProjectName']
    
    if (pkg_name, pkg_ver) in latest_keys:
        if pkg_name not in processed_packages:
            if proj_name in project_stars_map:
                stars = project_stars_map[proj_name]
                results.append({
                    "Package": pkg_name,
                    "Version": pkg_ver,
                    "Stars": stars,
                    "Project": proj_name
                })
                processed_packages.add(pkg_name)

# 4. Sort
results.sort(key=lambda x: x['Stars'], reverse=True)

# 5. Top 5
top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-8680979322817014984': ['packageinfo'], 'var_function-call-8680979322817014253': ['project_info', 'project_packageversion'], 'var_function-call-17195691913539802633': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-17195691913539803528': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-17195691913539804423': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-1651778565595146207': [{'COUNT(*)': '661372'}], 'var_function-call-1651778565595145174': [{'count_star()': '597602'}], 'var_function-call-1651778565595148237': [{'count_star()': '770'}], 'var_function-call-18204407829612454580': 'file_storage/function-call-18204407829612454580.json', 'var_function-call-10062229100743089117': 'file_storage/function-call-10062229100743089117.json', 'var_function-call-10062229100743086290': 'file_storage/function-call-10062229100743086290.json'}

exec(code, env_args)
