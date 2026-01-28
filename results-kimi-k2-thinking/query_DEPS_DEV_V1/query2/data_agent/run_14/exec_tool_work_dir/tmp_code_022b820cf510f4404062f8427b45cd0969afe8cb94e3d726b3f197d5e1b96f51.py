code = """import json
import re

# Load data from the stored files
mit_packages = json.load(open('/tmp/tmp3x6wbsy7.json'))
versions = json.load(open('/tmp/tmp7_9z2x0f.json'))
projects = json.load(open('/tmp/tmpv3z_1v8v.json'))

print(f'Loaded: {len(mit_packages)} MIT packages, {len(versions)} versions, {len(projects)} projects')

# Build version lookup mapping
ver_lookup = {}
for v in versions:
    key = (v['System'], v['Name'], v['Version'])
    ver_lookup[key] = v

# Extract fork counts from project info
proj_forks = {}
for p in projects:
    info = p['Project_Information']
    match = re.search(r'(\d+)\s+forks', info, re.I)
    if match:
        proj_forks[p['Project_Information']] = int(match.group(1))

print(f'Extracted {len(proj_forks)} fork counts')

# Map packages to projects and get fork counts
project_forks = {}
for pkg in mit_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    ver_data = ver_lookup.get(key)
    if ver_data:
        proj_name = ver_data['ProjectName']
        if proj_name not in project_forks:
            # Find matching project info
            for proj_info, forks in proj_forks.items():
                if proj_name in proj_info:
                    project_forks[proj_name] = forks
                    break

# Get top 5 projects by fork count
top5 = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)[:5]

# Format result
result = []
for proj, forks in top5:
    result.append({'project': proj, 'forks': forks})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': [], 'var_functions.query_db:40': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:72': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'winup/dlcs-ng'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dom-packages/fp'}, {'ProjectName': 'lohfu/domp-is'}, {'ProjectName': 'lohfu/domp-is'}, {'ProjectName': 'dosyago/ws'}, {'ProjectName': 'dosyago/ws'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'shellscape/dot'}, {'ProjectName': 'march08/duik'}, {'ProjectName': 'march08/duik'}, {'ProjectName': 'march08/duik'}, {'ProjectName': 'march08/duik'}, {'ProjectName': 'march08/duik'}, {'ProjectName': 'march08/duik'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'devingen/devingen'}, {'ProjectName': 'anpham6/e-mc'}], 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
