code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-7648133642612730669'], 'r') as f:
    pkgs = json.load(f)
with open(locals()['var_function-call-7648133642612728362'], 'r') as f:
    maps = json.load(f)
with open(locals()['var_function-call-7648133642612730151'], 'r') as f:
    infos = json.load(f)

df_pkgs = pd.DataFrame(pkgs)
df_map = pd.DataFrame(maps)
df_info_raw = pd.DataFrame(infos)

# Debug: Print first text
first_text = df_info_raw['Project_Information'].iloc[0]
print(f"DEBUG: First text: {first_text}")

# Test Regex
regex1 = r'\b[a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+\b'
match1 = re.findall(regex1, first_text)
print(f"DEBUG: Regex1 result: {match1}")

regex2 = r'[a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+'
match2 = re.findall(regex2, first_text)
print(f"DEBUG: Regex2 result: {match2}")

regex3 = r'\S+/\S+'
match3 = re.findall(regex3, first_text)
print(f"DEBUG: Regex3 result: {match3}")

# Main Logic with Regex2 (safer)
df_valid = pd.merge(df_pkgs, df_map, on=['Name', 'Version'], how='inner')
valid_project_names = set(df_valid['ProjectName'].dropna().unique())

data = []
for text in df_info_raw['Project_Information']:
    # Fork Count
    fork_count = 0
    m1 = re.search(r'(\d+(?:,\d+)*)\s+forks', text)
    m2 = re.search(r'forks count of\s+(\d+(?:,\d+)*)', text)
    if m1:
        fork_count = int(m1.group(1).replace(',', ''))
    elif m2:
        fork_count = int(m2.group(1).replace(',', ''))
        
    # Project Name
    candidates = re.findall(regex2, text)
    found_name = None
    for cand in candidates:
        # cleanup
        clean_cand = cand.strip('.,')
        if clean_cand in valid_project_names:
            found_name = clean_cand
            break
            
    if found_name:
        data.append({'ProjectName': found_name, 'ForkCount': fork_count})

df_result = pd.DataFrame(data)
if not df_result.empty:
    df_result = df_result.sort_values(by='ForkCount', ascending=False).head(5)
    print("__RESULT__:")
    print(df_result.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-5815538726582626865': ['packageinfo'], 'var_function-call-5815538726582627588': ['project_info', 'project_packageversion'], 'var_function-call-11463183709253046167': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-11463183709253046192': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-11463183709253046217': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-5617372832707650483': [{'Count(*)': '176170'}], 'var_function-call-5617372832707653518': [{'count_star()': '591699'}], 'var_function-call-5617372832707652457': [{'count_star()': '770'}], 'var_function-call-7648133642612730669': 'file_storage/function-call-7648133642612730669.json', 'var_function-call-7648133642612728362': 'file_storage/function-call-7648133642612728362.json', 'var_function-call-7648133642612730151': 'file_storage/function-call-7648133642612730151.json', 'var_function-call-3383667491132360060': [], 'var_function-call-14346102787841553460': {'valid_projects_count': 5289, 'sample_valid_projects': ['walmartlabs/eslint-config-defaults', 'ditsmod/ditsmod', 'drrops/drrops-sdk', 'dword-design/base-config-css', 'double-great/stylelint-a11y'], 'extracted_names_count': 0, 'sample_extracted': [], 'overlap_count': 0, 'sample_overlap': []}}

exec(code, env_args)
