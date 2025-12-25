code = """import json
import re

# Load the project_info data
with open(locals()['var_function-call-14983993188463768296'], 'r') as f:
    project_data = json.load(f)

extracted_projects = []

for entry in project_data:
    info = entry.get('Project_Information', '')
    if not info:
        continue
        
    # Extract Stars
    stars = 0
    # Pattern 1: "38715 stars" or "2,534 stars"
    m_stars = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s+stars', info)
    if not m_stars:
        # Pattern 2: "stars count of 3761"
        m_stars = re.search(r'stars count of\s+(\d{1,3}(?:,\d{3})*|\d+)', info)
    
    if m_stars:
        stars_str = m_stars.group(1).replace(',', '')
        stars = int(stars_str)
    
    # Extract Project Name
    # Strategies:
    # 1. "The project X/Y"
    # 2. "The GitHub project X/Y"
    # 3. "The project named X/Y"
    # 4. "The project is hosted on GitHub under the name X/Y"
    
    name = None
    
    # Try to find the name pattern: user/repo
    # It usually appears early in the string
    
    # Pattern A: "The project <name>..." or "The GitHub project <name>..."
    m_name = re.search(r'The (?:GitHub )?project (?:named )?([a-zA-Z0-9_\-.]+/[a-zA-Z0-9_\-.]+)', info)
    if m_name:
        name = m_name.group(1)
    else:
        # Pattern B: "under the name <name>"
        m_name = re.search(r'under the name ([a-zA-Z0-9_\-.]+/[a-zA-Z0-9_\-.]+)', info)
        if m_name:
            name = m_name.group(1)
            
    if name and stars > 0:
        extracted_projects.append({'ProjectName': name, 'Stars': stars})

# Sort by stars descending
extracted_projects.sort(key=lambda x: x['Stars'], reverse=True)

# Keep top 50 for now
top_projects = extracted_projects[:50]

print("__RESULT__:")
print(json.dumps(top_projects))"""

env_args = {'var_function-call-13435969520773442202': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-2142675263081200051': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-2142675263081197938': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-4762447333160345576': [{'Count(*)': '661372'}], 'var_function-call-4762447333160342703': [{'count_star()': '770'}], 'var_function-call-14983993188463768296': 'file_storage/function-call-14983993188463768296.json'}

exec(code, env_args)
