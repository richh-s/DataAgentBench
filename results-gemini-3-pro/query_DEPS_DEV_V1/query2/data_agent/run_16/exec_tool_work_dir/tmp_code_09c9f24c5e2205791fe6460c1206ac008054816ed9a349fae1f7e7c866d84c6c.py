code = """import json
import re

file_path = locals()['var_function-call-1091766501772037012']
with open(file_path, 'r') as f:
    data = json.load(f)

extracted = []

for row in data:
    info = row.get('Project_Information', '')
    if not info:
        continue

    # Fork extraction (worked before)
    forks = 0
    fork_patterns = [
        r'and ([\d,]+) forks',
        r'forks count of ([\d,]+)',
        r'forked ([\d,]+) times'
    ]
    for pat in fork_patterns:
        m = re.search(pat, info)
        if m:
            num_str = m.group(1).replace(',', '')
            forks = int(num_str)
            break
            
    # Project Name extraction
    # Remove URL like strings first
    text = re.sub(r'https?://\S+', '', info)
    
    # Find tokens that look like 'owner/repo'
    # Valid github user/repo chars: alphanumeric, hyphen, dot (repo), underscore
    # Must have exactly one slash in the middle (usually).
    # We'll just look for a slash surrounded by valid chars.
    
    # regex: [a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+ 
    # But catch them in the wild.
    
    matches = re.findall(r'(?:\s|^)([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)(?:[\s,.]|$)', text)
    
    # If multiple matches, usually the first one is the project name.
    # We filter out obvious non-projects if necessary (e.g. 'project/repo' literal?)
    # But usually these descriptions are specific.
    
    project_name = None
    if matches:
        # Pick the first one
        project_name = matches[0]
        # Remove trailing dot if picked up (though the regex (?:[\s,.]) should handle the delimiter, 
        # but if the dot was part of the match group it would be an issue.
        # My regex group `([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)` allows dot inside.
        # If the sentence ends with "repo.", the dot might be captured if it thinks it's part of repo name.
        # Repos RARELY end in dot. So if it ends in dot, strip it.
        if project_name.endswith('.'):
            project_name = project_name[:-1]
            
    if project_name and forks >= 0:
        extracted.append({'ProjectName': project_name, 'Forks': forks})

# Sort
extracted.sort(key=lambda x: x['Forks'], reverse=True)

print("__RESULT__:")
print(json.dumps(extracted[:50]))"""

env_args = {'var_function-call-16421468372705516038': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-9171658350266870018': [{'COUNT(*)': '176998'}], 'var_function-call-13594546530643448558': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-13351802038019434835': [{'count_star()': '770'}], 'var_function-call-15880387836270630294': ['project_info', 'project_packageversion'], 'var_function-call-16111266674709275655': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-8021130935877446402': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-1091766501772037012': 'file_storage/function-call-1091766501772037012.json', 'var_function-call-3968375106778048591': [], 'var_function-call-13839069292138497907': [{'info': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'candidates': [], 'forks': 0}, {'info': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'candidates': [], 'forks': 5782}, {'info': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'candidates': [], 'forks': 118}, {'info': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'candidates': [], 'forks': 988}, {'info': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'candidates': [], 'forks': 636}]}

exec(code, env_args)
