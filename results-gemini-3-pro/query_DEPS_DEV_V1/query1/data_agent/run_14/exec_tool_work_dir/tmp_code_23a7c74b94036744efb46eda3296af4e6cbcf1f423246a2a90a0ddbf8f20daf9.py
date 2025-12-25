code = """import json
import re
import pandas as pd

# 1. Load Project Info and Extract Stars/Name
project_info_path = locals()['var_function-call-1743245441723940041']
with open(project_info_path, 'r') as f:
    project_info_data = json.load(f)

project_stars_map = {}

def extract_stars_and_name(text):
    # Extract Name: Look for pattern "owner/repo"
    # Common prefixes: "project ", "name ", "named "
    # But names are unique in containing "/" (usually).
    # Exclude "GitHub/..." or common phrases if any.
    
    # Simple heuristic: find words with '/' inside, excluding URLs like "http://..."
    words = text.split()
    potential_names = []
    for w in words:
        clean_w = w.strip(".,;")
        if '/' in clean_w and 'http' not in clean_w and clean_w.count('/') == 1:
            potential_names.append(clean_w)
    
    project_name = None
    if potential_names:
        # Prioritize the one appearing earliest or after keywords like "project"
        # For now, take the first one that looks like owner/repo
        project_name = potential_names[0]
    
    # Extract Stars
    # Patterns: "X stars", "stars count of X", "total of X stars"
    stars = 0
    # Normalize
    text_norm = text.replace(',', '')
    
    # Regexes
    star_patterns = [
        r'(\d+)\s+stars',
        r'stars\s+count\s+of\s+(\d+)',
        r'total\s+of\s+(\d+)\s+stars'
    ]
    
    for pat in star_patterns:
        m = re.search(pat, text_norm)
        if m:
            stars = int(m.group(1))
            break
            
    return project_name, stars

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    p_name, p_stars = extract_stars_and_name(info)
    if p_name:
        project_stars_map[p_name] = p_stars

# 2. Load Package Info
package_info_path = locals()['var_function-call-17140001042633056540']
with open(package_info_path, 'r') as f:
    package_data = json.load(f)

df_pkg = pd.DataFrame(package_data)

# Process Versions to find Latest Release
def is_release(info_str):
    try:
        # It's a string, try to load json or check text
        # The string format in preview: "{\n  \"IsRelease\": true,\n...}"
        if '"IsRelease": true' in info_str:
            return True
        return False
    except:
        return False

df_pkg['IsRelease'] = df_pkg['VersionInfo'].apply(is_release)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')

# Filter logic:
# We want ONE version per Name.
# Preference: IsRelease=True, then Max Timestamp.
# If no IsRelease=True, Max Timestamp.
# Let's sort by Name, IsRelease (desc), UpstreamPublishedAt (desc)
df_pkg.sort_values(by=['Name', 'IsRelease', 'UpstreamPublishedAt'], ascending=[True, False, False], inplace=True)
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')

# 3. Load Project Package Map
map_path = locals()['var_function-call-17140001042633059611']
with open(map_path, 'r') as f:
    map_data = json.load(f)

df_map = pd.DataFrame(map_data)

# 4. Merge
# Join latest packages with map
df_merged = pd.merge(df_latest, df_map, on=['Name', 'Version'], how='inner')

# Map Stars
df_merged['Stars'] = df_merged['ProjectName'].map(project_stars_map).fillna(0).astype(int)

# Top 5
top_5 = df_merged.sort_values(by='Stars', ascending=False).head(5)

result = top_5[['Name', 'Version', 'Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3352328618415574598': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-3352328618415574047': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-3352328618415573496': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-16037315343165375606': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-401165894375835740': ['project_info', 'project_packageversion'], 'var_function-call-18263567307965433816': [{'COUNT(*)': '661372'}], 'var_function-call-18263567307965432179': [{'count_star()': '597602'}], 'var_function-call-18263567307965434638': [{'count_star()': '770'}], 'var_function-call-1743245441723940041': 'file_storage/function-call-1743245441723940041.json', 'var_function-call-17140001042633056540': 'file_storage/function-call-17140001042633056540.json', 'var_function-call-17140001042633059611': 'file_storage/function-call-17140001042633059611.json'}

exec(code, env_args)
