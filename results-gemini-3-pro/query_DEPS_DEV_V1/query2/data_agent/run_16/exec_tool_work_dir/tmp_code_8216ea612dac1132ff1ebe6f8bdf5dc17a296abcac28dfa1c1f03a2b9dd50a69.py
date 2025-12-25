code = """import json
import re

# Load data
file_path = locals()['var_function-call-1091766501772037012']
with open(file_path, 'r') as f:
    data = json.load(f)

extracted = []

for row in data:
    info = row.get('Project_Information', '')
    if not info:
        continue
    
    # Extract Project Name
    # Patterns to try for name
    # "The project owner/repo ..."
    # "The GitHub project owner/repo ..."
    # "The project named owner/repo ..."
    # "under the name owner/repo"
    # "repository named owner/repo"
    
    # Simple heuristic: find "owner/repo" string.
    # It usually follows "project" or "named" or "name".
    # And it contains a slash.
    
    # Let's try to find a string with a slash that is not a URL (http)
    # Regex: \b[\w-]+/[\w-]+\b matches owner/repo
    # But check context.
    
    # Filter out URLs first to avoid extracting parts of URLs
    text_no_url = re.sub(r'https?://\S+', '', info)
    
    # Look for owner/repo
    # It seems to always follow "project" keywords closely or is the subject.
    # The examples:
    # "The project lberrocal/npm-packages-template is..."
    # "The GitHub project ledgerproject/keypairoom currently..."
    # "The project named leofelix077/bunchofnothing on..."
    # "The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and..."
    
    # Pattern: \b([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)
    # Note: repo names can have dots (e.g., leaflet.fullscreen)
    
    candidates = re.findall(r'\b([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)\b', text_no_url)
    
    # Filter candidates: Usually the first one is the project name if it's not some other ref.
    # But sometimes there might be multiple.
    # The sentence structure usually starts with "The project..."
    # So the first candidate found is likely the one.
    
    project_name = None
    if candidates:
        project_name = candidates[0]
        
    # Extract Fork Count
    # Patterns:
    # "and X forks"
    # "forks count of X"
    # "forked X times"
    # Remove commas from numbers
    
    forks = 0
    
    # Regex for forks
    # 1. "(\d+) forks"
    # 2. "forks count of (\d+)"
    # 3. "forked (\d+) times"
    
    # We must handle comma separated numbers e.g. "7,109"
    
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
            
    if project_name:
        extracted.append({'ProjectName': project_name, 'Forks': forks})

# Sort by Forks descending
extracted.sort(key=lambda x: x['Forks'], reverse=True)

# Return top 50
print("__RESULT__:")
print(json.dumps(extracted[:50]))"""

env_args = {'var_function-call-16421468372705516038': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-9171658350266870018': [{'COUNT(*)': '176998'}], 'var_function-call-13594546530643448558': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-13351802038019434835': [{'count_star()': '770'}], 'var_function-call-15880387836270630294': ['project_info', 'project_packageversion'], 'var_function-call-16111266674709275655': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-8021130935877446402': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-1091766501772037012': 'file_storage/function-call-1091766501772037012.json'}

exec(code, env_args)
