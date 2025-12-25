code = """import json
import re

# Load project_info
with open(locals()['var_function-call-584623543129131853'], 'r') as f:
    project_info = json.load(f)

projects = []
for entry in project_info:
    text = entry.get('Project_Information', '')
    
    # Extract Project Name
    # Patterns observed:
    # "The project owner/repo is hosted..."
    # "The project owner/repo on GitHub..."
    # "The project named owner/repo is hosted..."
    # "The project is hosted on GitHub under the name owner/repo..."
    # "The GitHub project named owner/repo..."
    # "The GitHub project owner/repo..."
    
    name_match = re.search(r'(?:project|repository)\s+(?:named\s+|is\s+hosted\s+on\s+GitHub\s+under\s+the\s+name\s+)?([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', text, re.IGNORECASE)
    
    # Extract Stars
    # "38,715 stars"
    # "stars count of 3761"
    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*)\s+stars', text)
    if not stars_match:
        stars_match = re.search(r'stars\s+count\s+of\s+(\d{1,3}(?:,\d{3})*)', text)
        
    if name_match and stars_match:
        name = name_match.group(1)
        stars_str = stars_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
            projects.append({'ProjectName': name, 'Stars': stars})
        except:
            pass

# Sort by stars descending
projects.sort(key=lambda x: x['Stars'], reverse=True)

# Return top 30 to ensure we find matching packages
top_projects = projects[:30]

print("__RESULT__:")
print(json.dumps(top_projects))"""

env_args = {'var_function-call-10108647606675870329': ['packageinfo'], 'var_function-call-10108647606675872212': ['project_info', 'project_packageversion'], 'var_function-call-1420295833218764681': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-1420295833218762508': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-1420295833218764431': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-1392887978617341216': [{'Count(*)': '661372'}], 'var_function-call-1392887978617342035': [{'count_star()': '597602'}], 'var_function-call-1392887978617342854': [{'count_star()': '770'}], 'var_function-call-584623543129131853': 'file_storage/function-call-584623543129131853.json'}

exec(code, env_args)
