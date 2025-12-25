code = """import json
import re

# Load project_info
file_path = locals()['var_function-call-16144669137365837437']
with open(file_path, 'r') as f:
    project_info_list = json.load(f)

# Regex to extract ProjectName and ForkCount
# Pattern for name: "The project ([^ ]+) is hosted" or "The project ([^ ]+) on GitHub" etc.
# But names can be anything. Usually "owner/repo".
# Pattern for forks: "and ([0-9,]+) forks" or "forks count of ([0-9,]+)" or "forked ([0-9,]+) times"

# Let's try to capture the project name more reliably. It seems to be the first word after "The project" or "The GitHub project named".
# Examples:
# "The project lberrocal/npm-packages-template is hosted..."
# "The GitHub project named linkshare/service-container has..."
# "The project on GitHub, named leonardparisi/easy-express-server, currently..."
# "The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and..."
# "The project leviticusmb/sysconsole is hosted..."

# Fork patterns:
# "and 5782 forks"
# "forks count of 988"
# "forked 12 times"
# "forks count of 0"
# "and 0 forks"

projects = []

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    
    # Extract Name
    name = None
    # Try different patterns for name
    # 1. "The project <name> is hosted" or "... on GitHub"
    m_name = re.search(r"The (?:GitHub )?project (?:named )?([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) (?:is hosted|on GitHub|has|currently)", text)
    if m_name:
        name = m_name.group(1)
    else:
        # 2. "The project on GitHub, named <name>,"
        m_name = re.search(r"The project on GitHub, named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+),", text)
        if m_name:
            name = m_name.group(1)
        else:
            # 3. "The project is hosted on GitHub under the name <name>,"
            m_name = re.search(r"under the name ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+),", text)
            if m_name:
                name = m_name.group(1)
    
    # Extract Forks
    forks = 0
    # Pattern 1: "and ([0-9,]+) forks"
    m_forks = re.search(r"and ([0-9,]+) forks", text)
    if m_forks:
        forks = int(m_forks.group(1).replace(',', ''))
    else:
        # Pattern 2: "forks count of ([0-9,]+)"
        m_forks = re.search(r"forks count of ([0-9,]+)", text)
        if m_forks:
            forks = int(m_forks.group(1).replace(',', ''))
        else:
            # Pattern 3: "forked ([0-9,]+) times"
            m_forks = re.search(r"forked ([0-9,]+) times", text)
            if m_forks:
                forks = int(m_forks.group(1).replace(',', ''))
    
    if name:
        projects.append({'ProjectName': name, 'ForkCount': forks})

# Sort by ForkCount desc
projects.sort(key=lambda x: x['ForkCount'], reverse=True)

print("__RESULT__:")
print(json.dumps(projects[:50])) # Print top 50 candidates"""

env_args = {'var_function-call-9353416136565816725': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-1492902969018891928': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-6616293602349405487': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-4575183336635639547': [{'COUNT(*)': '391228'}], 'var_function-call-12758722675786047331': [{'COUNT(*)': '176998'}], 'var_function-call-12156566359617442147': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-1970910957106405500': [{'count_star()': '770'}], 'var_function-call-16144669137365837437': 'file_storage/function-call-16144669137365837437.json'}

exec(code, env_args)
